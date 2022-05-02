import pandas as pd
from sagemaker import clarifyimport seaborn as sns


sns.countplot(data=df, x='star_rating', hue='product_category')

df = pd.read_csv('./amazon_customer_reviews_dataset.csv')
bias_report_outpath = f's3://{BUCKET}/clarify'
clarify_processor = clarify.SagemakerClarifyProcessor(
    role=ROLE,
    instance_count=1,
    instance_type='ml.c5.2xlarge',
    sagemaker_sesion=sess)
data_config = clarify.DataConfig(
    s3_data_input_path=data_s3_uri,
    s3_output_path=bias_report_output_path,
    label='star_rating',
    headers=list(df),
    dataset_type='text/csv')
data_bias_config = clarify.BiasConfig(
    label_values_or_threshold=[4, 5],
    facet_name='product_category',
    facet_values_or_trheshold=['Gift Card'],
    group_name=product_category)
clarify_preprocessor.run_pre_training_bias(
    data_config=data_config,
    data_bias_config=data_bias_config,
    methods='all',
    wait=True)

