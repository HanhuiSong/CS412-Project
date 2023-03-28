import json
import pandas as pd
data_file = open("yelp_academic_dataset_review.json", 'rb')
data = []
for line in data_file:
    review = json.loads(line)
    review.pop('funny', None)
    review.pop('cool', None)
    review.pop('text', None)
    review.pop('date', None)
    data.append(review)
checkin_df = pd.DataFrame(data)
data_file.close()
# invalid_stars = (~checkin_df['stars'].apply(lambda x: isinstance(x, float) and x >= 0)).sum()
# invalid_useful = (~checkin_df['useful'].apply(lambda x: isinstance(x, int) and x >= 0)).sum()
#
# print(f"Found {invalid_stars} rows with non-numeric or negative values in the 'stars' column.")
# print(f"Found {invalid_useful} rows with non-numeric or negative values in the 'useful' column.")
checkin_df = checkin_df[(checkin_df['stars'].apply(lambda x: isinstance(x, float) and x >= 0)) & (checkin_df['useful'].apply(lambda x: isinstance(x, int) and x >= 0))]

# Write into new file with cleaned data

checkin_df.to_json("yelp_academic_dataset_review_modified.json", orient='records', lines=True)

# with open("yelp_academic_dataset_review_modified.json", 'w') as f:
#     for review in data:
#         json.dump(review, f)
#         f.write('\n')


# with open("yelp_academic_dataset_review_modified.json", "r") as f:
#     line_count = 0
#     for line in f:
#         line_count += 1
#
# print("Number of lines:", line_count)
#& ~checkin_df['stars'].isna()


