from pydeequ.analyzers import *
from pydeequ.checks import *
from pydeequ.verification import *
from sagemaker.spark.processing import PySparkProcessor


s3_input_data = f's3://{BUCKET}/amazon-reviews-pds/tsv'
s3_output_analyze_data = f's3://{BUCKET}/{PREF}/output'
processor = PySparkProcessor(
    base_job_name='spark-amazon-reviews-analyzer',
    role=role,
    framework_version='2.4',
    instance_count=10,
    instance_type='ml.r5.8xlarge',
    max_runtime_in_seconds=300)
processor.run(
    submit_app='preprocess-deequ-pyspark.py',
    submit_jars=['deequ-1.0.3-rc2.jar'],
    arguments=[
        's3_input_data', s3_input_data,
        's3_output_analyze_data', s3_output_analyze_data]
    logs=True,
    wait=False)
dataset = spark.read.csv(
    s3_input_data, header=True, schema=schema, sep='\t', quote='')
anlaysis_res = (
    AnalysisRunner(spark)
    .onData(datset)
    .addAnalyzer(Size())
    .addAnalyzer(Completeness('review_id'))
    .addAnalyzer(ApproxCOuntDistinct('review_id'))
    .addAnalyzer(Mean('star_rating'))
    .addAnalyzer(Compliance('top star_rating', 'star_rating >= 4.0'))
    .addAnalyzer(Correlation('total_votes', 'star_rating'))
    .addAnalyzer(Correlation('total_votes', 'helpful_votes'))
    .run())
verification_res = (
    VerificationSuite(spark)
    .onData(dataset)
    .addCheck(
        Check(spark, CheckLevel.Error, 'Review Check')
        .hasSize(lambda x: x >= 150_000_000)
        .hasMin('star_rating', lambda x: x == 1.)
        .hasMax('star_rating', lambda x: x == 5.)
        .isComplete('review_id')
        .isComplete('marketplace')
        .isContainedIn('marketplae', ['US', 'UK', 'DE', 'JP', 'FR']))
    .run())
