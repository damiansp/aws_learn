CREATE EXTERNAL TABLE IF NOT EXISTS dsoaws.amazon_reviews_tsv(
  marketplace       STRING,
  customer_id       STRING,
  review_id         STRING,
  product_id        STRING,
  product_parent    STRING,
  product_title     STRING,
  product_category  STRING,
  star_rating       INT,
  helpful_votes     INT,
  total_votes       INT,
  vine              STRING,
  verified_purchase STRING,
  review_headline   STRING,
  review_body       STRING,
  review_date       STRING
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
LOCATION 's3://cbtn-dev-data-analytics/aws_datasci_learning/book/data/amazon-reviews-pds/tsv'
TBLPROPERTIES ('compressionType' = 'gzip', 'skip.header.line.count' = '1');
