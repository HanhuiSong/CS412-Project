import pandas as pd
import matplotlib.pyplot as plt
from kmeans_interp.kmeans_feature_imp import KMeansInterp

active_user_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_user.json").reset_index(drop=True)
restaurant_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_business.json").reset_index(drop=True)
review_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_review.json").reset_index(drop=True)
tip_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_tip.json").reset_index(drop=True)

active_user_df['elite'] = active_user_df['elite'].str.split(',').str.len()
# user
active_user_df = active_user_df.fillna(0)
active_user_df = active_user_df.drop(
    ['user_id', 'name', 'yelping_since', 'friends', 'compliment_hot', 'compliment_more',
     'compliment_profile', 'compliment_cute', 'compliment_list',
     'compliment_note', 'compliment_plain', 'compliment_cool',
     'compliment_funny', 'compliment_writer', 'compliment_photos'], axis=1)
# restaurant
restaurant_df = restaurant_df.fillna(0)
restaurant_df = restaurant_df.drop(['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'categories', 'attributes','hours'],
                                   axis=1)
# review
review_df = review_df.fillna(0)
review_df = review_df.drop(['review_id', 'user_id', 'business_id', 'text', 'date'], axis=1)

print(restaurant_df.columns)
print(restaurant_df.head(1).to_string())
kms = KMeansInterp(
    n_clusters=10,
    ordered_feature_names=review_df.columns.tolist(),
    feature_importance_method='wcss_min',  # or 'unsup2sup'
).fit(review_df.values)

feature_names = [x[0] for x in kms.feature_importances_[0]]
importance_scores = [x[1] for x in kms.feature_importances_[0]]

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(32, 48))

# First plot
ax1.bar(feature_names, importance_scores)
ax1.set_title('Review Feature Importance', fontsize=40)
ax1.set_ylabel('Importance Score', fontsize=40)
ax1.tick_params(axis='x', rotation=0, labelsize=40)
ax1.tick_params(axis='y', labelsize=40)

kms1 = KMeansInterp(
    n_clusters=10,
    ordered_feature_names=active_user_df.columns.tolist(),
    feature_importance_method='wcss_min',  # or 'unsup2sup'
).fit(active_user_df.values)

feature_names = [x[0] for x in kms1.feature_importances_[0]]
importance_scores = [x[1] for x in kms1.feature_importances_[0]]

# Second plot
ax2.bar(feature_names, importance_scores)
ax2.set_title('User Feature Importance', fontsize=40)
ax2.set_ylabel('Importance Score', fontsize=40)
ax2.tick_params(axis='x', rotation=0, labelsize=40)
ax2.tick_params(axis='y', labelsize=40)

kms2 = KMeansInterp(
       n_clusters=10,
       ordered_feature_names=restaurant_df.columns.tolist(),
       feature_importance_method='wcss_min',  # or 'unsup2sup'
).fit(restaurant_df.values)

feature_names = [x[0] for x in kms2.feature_importances_[0]]
importance_scores = [x[1] for x in kms2.feature_importances_[0]]

# Third plot
ax3.bar(feature_names, importance_scores)
ax3.set_title('Business Feature Importance', fontsize=40)
ax3.set_ylabel('Importance Score', fontsize=40)
ax3.tick_params(axis='x', rotation=0, labelsize=40)
ax3.tick_params(axis='y', labelsize=40)

plt.tight_layout()
# Display the plot
plt.show()
