import pandas as pd
from pyathena import connect


se_staging_dir = f's3://{BUCKET}/athena/staging'
conn = connect(region_name=region, s3_staging_dir=s3_staging_dir)
sql = (
    f'SELECT DISTINCT product_category '
    f'FROM {SCHEMA}.{TABLE} '
    f'ORDER BY product_category')
pd.read_sql(sql, conn)


df = pd.read_sql_query(
    f'SELECT APPROXIMATE COUNT(DISTINCT customer_id) '
    f'FROM {SCHEMA}.{TABLE} '
    f'GROUP BY product_category'.
    engine)

# much faster than
df = pd.read_sql_query(
    f'SELECT COUNT(DISTINCT customer_id) '
    f'FROM {SCHEMA}.{TABLE} '
    f'GROUP BY product_category'.
    engine)

