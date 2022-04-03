SELECT product_title,
  helpful_votes,
  LENGTH(review_body) AS review_len,
  SUBSTRING(review_body, 1, 100) AS body
FROM redshift.amazon_reviews_tsv_2015
ORDER BY helpful_votes DESC
LIMIT 10;
