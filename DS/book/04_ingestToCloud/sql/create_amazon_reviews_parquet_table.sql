CREATE TABLE IF NOT EXISTS dsoaws.amazon_reviews_parquet
WITH (
  format='PARQUET',
  external_location='s3://cbtn-dev-data-analytics/aws_datasci_learning/book/data/amazon-reviews-pds/parquet',
  partitioned_by=ARRAY['product_category']
) AS
SELECT marketplace,
  customer_id,
  review_id,
  product_id,
  product_parent,
  product_title,
  star_rating,
  helpful_votes,
  total_votes,
  vine,
  verified_purchase,
  review_headline,
  review_body,
  CAST(YEAR(DATE(review_date)) AS INTEGER) AS year,
  DATE(review_date) AS review_date,
  product_category
FROM dsoaws.amazon_reviews_tsv;


/* Load Parquet Partitions */
MSCK REPAIR TABLE dsoaws.amazon_reviews_parquet;


/* Verify */
SELECT *
FROM dsoaws.amazon_reviews_parquet
WHERE product_category = 'Digital_Video_Download'
LIMIT 10;
