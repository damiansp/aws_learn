SELECT year, ROUND(AVG(star_rating), 4) AS mean_rating
FROM dsoaws.amazon_reviews_parquet
GROUP BY year
ORDER BY year;
