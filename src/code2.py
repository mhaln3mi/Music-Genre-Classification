# feature engineering
#1- Using KNN to replace the missing value 
imputer = KNNImputer(n_neighbors=5)
data = df.DataFrame(imputer.fit_transform(df),columns = df.columns)
#Check the missing value 
df.isna().any()
#2-Center and scale (i.e., standardize) all numeric features.
# define standard scaler
scaler = StandardScaler()
# transform data
df = scaler.fit_transform(df)
df
# 3-Dropping columns we don't need 
del df["Track Name"]
