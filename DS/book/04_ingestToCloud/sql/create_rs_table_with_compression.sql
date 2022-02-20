CREATE TABLE IF NOT EXISTS redshift.amazon_reviews_tsv_2015 (
  marketplace       VARCHAR(2)     ENCODE zstd,
  customer_id       VARCHAR(8)     ENCODE zstd,
  review_id         VARCHAR(14)    ENCODE zstd,
  product_id        VARCHAR(10)    ENCODE zstd DISTKEY,
  product_parent    VARCHAR(9)     ENCODE zstd,
  product_category  VARCHAR(24)    ENCODE raw,
  star_rating       INT            ENCODE az64,
  helpful_votes     INT            ENCODE zstd,
  total_votes       INT            ENCODE zstd,
  vine              VARCHAR(1)     ENCODE zstd,  
  verified_purchase VARCHAR(1)     ENCODE zstd,
  review_headline   VARCHAR(128)   ENCODE zstd,
  review_body       VARCHAR(65535) ENCODE zstd,
  review_date       VARCHAR(10)    ENCODE bytedict,
  year              INT            ENCODE az64
) SORTKEY (product_category);


/* Check compression efficacy */
ANALYZE COMPRESSION redshift.amazon_reviews_tsv_2015;
