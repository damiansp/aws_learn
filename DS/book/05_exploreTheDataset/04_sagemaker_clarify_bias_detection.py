import pandas as pd
import seaborn as sns
from smclarify.bias import report


df = pd.read_csv('./amazon_customer_reviews_dataset.csv')
facet_col = report.FacetColun(name='product_category')
label_col = report.LabelColumn(
    name='star_rating', data=df.star_rating, positive_label_values=[4, 5])
group_var = df.product_category
report.bias_report(
    df,
    facet_col,
    label_col,
    stage_type=report.StageType.PRE_TRAINING,
    group_variable=group_car)


# Mitigate bias
group_by = ['product_category', 'star_rating']
df_grouped_by = df.groupby(group_by)[group_by]
df_balanced = df_grouped_by.apply(
    lambda x: x.sample(df_grouped_by.size().min()).reset_index(drop=True))
sns.countplot(data=df_balanced, x='star_rating', hue='product_category')
