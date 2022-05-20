db.create_dataset(
    Name='amazon-reviews-parquet',
    Input={
        'S3InputDefinition': {
            'Bucket': 'amazon-reviews-pds',
            'Key': 'parquet/'}})

