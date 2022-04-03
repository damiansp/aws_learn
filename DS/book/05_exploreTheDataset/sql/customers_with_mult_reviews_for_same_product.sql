SELECT customer_id,
  product_category,
  product_title,
  ROUND(AVG(star_rating::FLOAT), 4) AS avg_rating,
  COUNT(*) AS n_review
FROM redshift.amazon_reviews_tsv_2015
GROUP BY customer_id, product_category, product_title
HAVING COUNT(*) > 1
ORDER BY n_review DESC
LIMIT 5;
