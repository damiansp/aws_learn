import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from   pyathena import connect
import seaborn as sns

%matplotlib inline
%config InlineBackend.figure_format = 'retina'


BUCKET = 'my-bucket-name'
region = 'us-east-1' # e.g.
db = 'dsoaws'
table = 'amazon_reviews_parquet'
s3_staging_dir = f's3::/{BUCKET}/athena/staging'
conn = connect(region=region, s3_staging_dir=s3_staging_dir)
query = (
    f'SELECT DISTINCT product_category from {db}.{table} '
    f'ORDER BY product_category')
pd.read_sql(query, conn)
