SELECT product_category, star_rating, COUNT(*) AS n_reviews
FROM dsoaws.amazon_reviews_parquet
GROUP BY product_category, star_rating
ORDER BY product_category, star_rating DESC;
