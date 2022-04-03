SELECT
  CAST(DATE_PART('month', TO_DATE(review_date, 'YYYY-MM-DD')) AS INTEGER)
    AS month,
  AVG(star_rating::FLOAT) AS avg_rating
FROM redshift.amazon_reviews_tsv_2015
GROUP BY month
ORDER BY month;
