SELECT product_category, MIN(year) AS first_review
FROM dsoaws.amazon_reviews_parquet
GROUP BY product_category
ORDER BY first_review;
