from sklearn.model_selection import train_test_split


TEST_FRAC = 0.05
VALID_FRAC = 0.05
HOLDOUT = TEST_FRAC + VALID_FRAC

df_train, df_holdout = train_test_split(
    df_balanced, test_size=HOLDOUT, stratify=df_balanced.star_rating)
df_valid, df_test = train_test_split(
    df_holdout, test_size=TEST_FRAC / HOLDOUT, stratify=df_holdout.star_rating)
