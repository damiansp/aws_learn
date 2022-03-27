SELECT CARDINALITY(SPLIT(review_body, ' ')) as n_words
FROM dsoaws.amazon_reviews_parquet;
