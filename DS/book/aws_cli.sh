AMAZON_BUCKET=s3://amazon-reviews-pds # public data source (product reviews)
aws s3 ls $AMAZON_BUCKET/tsv
aws s3 ls $AMAZON_BUCKET/parquet
