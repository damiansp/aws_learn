SELECT product_category, AVG(star_rating) AS mean_star_rating
FROM dsoaws.amazon_reviews_parquet
GROUP BY product_category
ORDER BY mean_star_rating DESC;
