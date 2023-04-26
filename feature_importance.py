import pandas as pd
import matplotlib.pyplot as plt
from kmeans_interp.kmeans_feature_imp import KMeansInterp

active_user_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_user.json").reset_index(drop=True)
restaurant_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_business.json").reset_index(drop=True)
review_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_review.json").reset_index(drop=True)
tip_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_tip.json").reset_index(drop=True)

active_user_df['elite'] = active_user_df['elite'].str.split(',').str.len()

review_df = review_df.fillna(0)
review_df = review_df.drop(['review_id', 'user_id', 'business_id','text', 'date'],axis=1)
print(tip_df.columns)
print(review_df.head(1).to_string())
kms = KMeansInterp(
       n_clusters=10,
       ordered_feature_names=review_df.columns.tolist(),
       feature_importance_method='wcss_min', # or 'unsup2sup'
).fit(review_df.values)
print(kms.feature_importances_[0][:10])
feature_names = [x[0] for x in kms.feature_importances_[0]]
importance_scores = [x[1] for x in kms.feature_importances_[0]]

# Create a vertical bar chart
fig, ax = plt.subplots(figsize=(32, 16))
ax.bar(feature_names, importance_scores)

# Customize the plot
ax.set_title('Feature Importance')
ax.set_ylabel('Importance Score') # increase font size of y-axis label
ax.tick_params(axis='x', rotation=0, labelsize=40)

# Display the plot
plt.show()


