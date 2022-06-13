df = pd.read_csv(
    './data/amazon_reviews_us_Digital_Software_v1_00.tsv.gz',
    delimiter='\t',
    quoting=csv.QUOTE_NONE,
    compression='gzip')
df_grouped = df.groupby(['star_rating'])
df_balanced = df_grouped.apply(
    lambda x: x.sample(df_grouped.size().min()).reset_index(drop=True))
