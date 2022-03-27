SELECT product_category, year, ROUND(AVG(star_rating), 4) AS avg_rating
FROM dsoaws.amazon_reviews_parquet
WHERE product IN ('Books', 'Digital_Ebook_Purchase', 'Wireless', 'Home')
GROUP BY product_category, year
ORDER BY year, avg_rating DESC;
