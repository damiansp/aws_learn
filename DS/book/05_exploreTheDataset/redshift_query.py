df = pd.read_sql_query(
    '''
    SELECT product_category, COUNT(DISTINCT customer_id) as n_customers 
    FROM redshift.amazon_reviews_tsv_2015
    GROUP BY product_category
    ORDER BY n_customers DESC;''',
    engine)
df.head()

products_by_review_count_2015_query = (
    '''
    SELECT year, product_category, COUNT(star_rating) AS n_ratings
    FROM redshift.amazon_reviews_tsv_2015
    GROUP BY product_category, year
    ORDER BY n_ratings DESC;''')
