import pandas as pd
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier


active_user_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_user.json").reset_index(drop=True)
restaurant_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_business.json").reset_index(drop=True)
review_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_review.json").reset_index(drop=True)
tip_df = pd.read_json("./rev_Yelp/yelp_academic_dataset_tip.json").reset_index(drop=True)

active_user_df['elite'] = active_user_df['elite'].str.split(',').str.len()


def gen_prange(n):
    return np.arange(n + 1) / n


def convert_column_by_percentage(column_data, percentage, score=None):
    '''
    Args
        column_data: pandas Series
            input feature
        percentage: list
            list of percentage for assigning different scores.
            note that the list should be in the assending order and have only positive value ranging from 0.0 to 1.0.
        score: list (Optional)
            list of scores corresponding to the percentage list,
            if not given, will automatically use [0 ... len(percentage)]
    '''
    if score is None:
        score = np.arange(len(percentage))
    assert len(percentage) == len(score), print("The length of the defined range is not equal to that of the scores")
    column_sorted = np.sort(column_data)
    output = column_data.values.copy()
    last_value = column_data.min() - 1
    for p, s in zip(percentage, score):
        indice = int((column_sorted.size - 1) * p)
        value = column_sorted[indice]
        idx = (column_data <= value) & (column_data > last_value)
        output[idx.values] = s
        last_value = value
    return output


def convert_column_by_absolute(column_data, absolute_values, score=None):
    '''
    Args
        column_data: pandas Series
            input feature
        absolute_values: list
            absolute value range for assigning different scores.
            note that the list should be in the assending order.
        score: list (Optional)
            list of scores corresponding to the percentage list,
            if not given, will automatically use [0 ... len(percentage)]
    '''
    if score is None:
        score = np.arange(len(absolute_values))
    assert len(absolute_values) == len(score), print(
        "The length of the defined range is not equal to that of the scores")
    column_sorted = np.sort(column_data)
    output = column_data.values.copy()
    last_value = column_data.min() - 1
    for av, s in zip(absolute_values, score):
        idx = (column_data <= av) & (column_data > last_value)
        output[idx.values] = s
        last_value = av
    return output


def assign_score(to_df, from_src, by_feature, split_list, with_type, score=None):
    assert with_type != 'absolute' or with_type != 'percentage', print("Neither `absolute` or `percentage`")
    output = None
    if with_type == 'percentage':
        output = convert_column_by_percentage(active_user_df[by_feature], split_list)
    elif with_type == 'absolute':
        output = convert_column_by_absolute(active_user_df[by_feature], split_list)
    user_score_df[by_feature] = output.tolist()


user_score_df = pd.DataFrame(active_user_df['user_id'])
user_score_df = user_score_df.reset_index(drop=True)

trg_features = ['review_count', 'fans', 'elite']
trg_split_range = [gen_prange(5), gen_prange(10), [0, 1, 2, 4, 6, 8, 17]]
trg_split_type = ['percentage', 'percentage', 'absolute']

for i in range(len(trg_features)):
    assign_score(to_df=user_score_df, from_src=active_user_df, by_feature=trg_features[i],
                 split_list=trg_split_range[i], with_type=trg_split_type[i])

review_score_df = pd.DataFrame(review_df.iloc[:, 1:4])
review_score_df = review_score_df.join(user_score_df.set_index('user_id'), on='user_id')

review_restaurant_df = review_score_df.drop(columns="user_id")
review_restaurant_df = review_restaurant_df.groupby('business_id', as_index=False).mean()

restaurant_score_df = pd.DataFrame(restaurant_df['business_id'])
restaurant_score_df = restaurant_score_df.join(review_restaurant_df.set_index('business_id'), on='business_id')


# apply weight method
def my_combine_function(arr):
    return (arr[1] * 0.25) + (arr[2] * 0.25) + (arr[3] * 0.5)


# using addition to get final score
restaurant_score_df['final_score'] = restaurant_score_df[['stars', 'review_count', 'fans', 'elite']].apply(
    my_combine_function, axis=1)
# merge tip and bussiness
merged_df = pd.merge(restaurant_df, tip_df[['business_id', 'compliment_count']], on='business_id', how='left')
restaurant_df['compliment_count'] = merged_df['compliment_count']
restaurant_df = restaurant_df.merge(restaurant_score_df[['business_id', 'stars']], on='business_id', how='left')


restaurant_df['compliment_count'] = restaurant_df['compliment_count'].fillna(0)


# merge final score and bussiness
merged_df1 = pd.merge(restaurant_df, restaurant_score_df[['business_id', 'final_score']], on='business_id',
                      how='left')
restaurant_df['final_score'] = merged_df1['final_score']

# k-means

columns_to_cluster = ['stars_y', 'review_count', 'compliment_count','final_score']
imputed_data = restaurant_df[columns_to_cluster].fillna(0)
min_values = imputed_data[columns_to_cluster].min()
max_values = imputed_data[columns_to_cluster].max()
normalized_data = (imputed_data[columns_to_cluster] - min_values) / (max_values - min_values)
print(max(normalized_data['stars_y']))

#data_to_cluster = restaurant_df[columns_to_cluster]
kmeans = KMeans(n_clusters=20)
kmeans.fit(normalized_data)
# importances = kmeans.cluster_centers_.mean(axis=0)
#
# df_importances = pd.DataFrame({'feature': columns_to_cluster, 'importance': importances})
#
# # Use px.bar to create a bar chart of the feature importances
# bar_chart = px.bar(df_importances, x='feature', y='importance', title='Feature Importances')
# bar_chart.show()
normalized_data['cluster_label'] = kmeans.labels_
# # Visualize the results using a scatter plot
#
scatter_matrix = px.scatter_matrix(normalized_data, dimensions=columns_to_cluster, color='cluster_label')
scatter_matrix.show()

