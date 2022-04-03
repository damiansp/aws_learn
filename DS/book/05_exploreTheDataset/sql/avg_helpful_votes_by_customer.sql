SELECT customer_id,
  AVG(helpful_votes) AS avg_helpful,
  COUNT(*) AS n_reviews,
  COUNT(DISTINCT product_category) AS n_categories,
  ROUND(AVG(star_rating::FLOAT), 1) AS avg_rating
FROM redshift.amazon_reviews_tsv_2015
GROUP BY customer_id
HAVING COUNT(*) > 99
ORDER BY avg_helpful DESC
LIMIT 10;
