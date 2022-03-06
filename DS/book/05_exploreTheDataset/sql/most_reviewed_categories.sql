SELECT product_category, COUNT(star_rating) AS n_ratings
FROM dsoaws.amazon_reviews_parquet
GROUP BY product_category
ORDER BY n_ratings DESC;
