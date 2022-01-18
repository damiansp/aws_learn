UNLOAD (
  'SELECT
    marketplace,
    customer_id,
    review_id,
    product_id,
    product_parent,
    product_title, 
    product_category,
    star_rating,
    helpful_votes,
    total_votes,
    vine,
    verified_purchase,
    review_headline,
    review_body,
    review_date,
    year
  FROM redshift.amazon_reviews_tsv_2015')
TO 's3://mybucket/amazon-reviews-pds/parquet-from-redshift/2015'
IAM_ROLE '<MY_ROLE>'
PARQUET PARALLEL ON
PARTITION BY (product_category)
