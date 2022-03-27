SELECT star_rating AS rating, COUNT(*) AS n_reviews
FROM dsoaws.amazon_reviews_parquet
GROUP BY rating
ORDER BY rating DESC;
