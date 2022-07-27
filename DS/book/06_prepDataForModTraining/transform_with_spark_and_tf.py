from sagemaker.spark.processing import PySparkProcessor


processor = PySparkProcessor(
    base_job_name='spark-amazon-reviews-processor',
    role=role,
    framework_version='3.2.1',  # Spark version
    instance_count=2,
    instance_type='ml.r5.xlarge',
    max_runtime_in_seconds=7200)
root_path = f's3://{bucket}/{prefix}/output/bert'
train_data_bert_output = f'{root_path}-train'
validation_data_bert_output = f'{root_path}-validation'
test_data_bert_output = f'{root_path}-test'

processor.run(
    submit_app='proprocessor-spark-text-to-bert.py',
    arguments=[
        's3_input_data', s3_input_data,
        's3_output_train_data', train_data_bert_output,
        's3_output_validation_data', validation_data_bert_output,
        's3_output_test_data', test_data_bert_output,
        'train_split_percentage', str(train_split_percentage),
        'validation_split_percentage', str(validation_split_percentage),
        'test_split_percentage', str(test_split_percentage),
        'max_seq_length', str(max_seq_length)],
    outputs=[
        ProcessingOutput(
            s3_upload_mode='EndOfJob',
            output_name='bert-train',
            source='/opt/ml/processing/output/bert/train'),
        ProcessingOutput(
            s3_upload_mode='EndOfJob',
            output_name='bert-validation',
            source='/opt/ml/processing/output/bert/validation'),
        ProcessingOutput(
            s3_upload_mode='EndOfJob',
            output_name='bert-test',
            source='/opt/ml/processing/output/bert/test')],
    logs=True,
    wait=False)
