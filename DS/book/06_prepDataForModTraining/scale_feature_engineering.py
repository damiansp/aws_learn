from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.sklearn.processing import SKLearnProcessor


SKLEARN_VERSION = '1.2.3'
processor = SKLearnProcessor(
    framework_version=SKLEARN_VERSION,
    role=role,
    instance_type='ml.c5.4xlarge',
    instance_count=2)
processor.run(
    code='preprocess-scikit-text-to-bert.py',
    inputs=[
        ProcessingInput(
            input_name='raw-input-data',
            source=raw_input_data_s3_ui,
            destination='/opt/ml/processing/input/data/',
            s3_data_distribution_type='ShardedByS3Key')],
    outputs=[
        ProcessingOutput(
            output_name=f'bert-{subset}',
            s3_upload_mode='EndOfJob',
            source=f'/opt/ml/processing/output/bert/{subset}')
        for subset in ['train', 'validation', 'test']],
    arguments=[
        '--train-split-percentage', str(train_split_percentage),
        '--validation-split-percentage', str(validation_split_percentage),
        '--test-split-percentage', str(test_split_percentage),
        '--max-seq-lenth', str(max_seq_len)],
    logs=True,
    wait=False)

output_config = processing_job_description['ProcessingOutputConfig']
for output in output_config['Outputs']:
    if output['OutputName'] == 'bert-train':
        processed_train_data_s3_uri = output['S3Output']['S3Uri']
    elif output['OutputName'] == 'bert-validation':
        processed_validation_data_s3_uri = output['S3Output']['S3Uri']
    elif output['OutputName'] == 'bert-test':
        processed_test_data_s3_uri = output['S3Output']['S3Uri']

