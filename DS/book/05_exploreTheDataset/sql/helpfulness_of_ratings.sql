SELECT star_rating, AVG(helpful_votes) AS avg_helpful_votes
FROM dsoaws.amazon_reviews_parquet
GROUP BY star_rating
ORDER BY star_rating DESC;
