# Importing necessary library
import pandas as pd
# Read the dataset from a CSV file
importance_df = pd.read_csv('/project/kc20230915001/src/survival_results/C-index_and_feautre_importances_est_5year.csv')
# Group by 'feature' and aggregate the 'Importance' with mean and count
feature_group = importance_df.groupby('feature').agg({'Importance':['mean','count']
                                                     }).reset_index()
feature_group.columns = ['Feature', 'Importance_mean', 'Importance_Count']
# Sort the features based on the mean importance in descending order
sorted_features = feature_group.sort_values('Importance_mean', ascending=False)

# Display the top 10 features with the highest mean importance
top_features = sorted_features.head(10)

top_features.to_csv('top_feautres_est_5year.csv', index=False)
print(top_features)

