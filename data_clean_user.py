import json
import pandas as pd
# data_file = open("yelp_academic_dataset_user.json",'rb')
# data = []
# for line in data_file:
#     data.append(json.loads(line))
# user_df = pd.DataFrame(data)
# data_file.close()
#
#
# user_df.drop(columns=['name', 'yelping_since', 'useful', 'funny', 'cool', 'friends', 'compliment_more', 'compliment_profile', 'compliment_cute', 'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool', 'compliment_funny', 'compliment_writer', 'compliment_photos', 'compliment_hot', 'average_stars'], inplace=True)
#
#
#
# user_df.to_json("yelp_academic_dataset_user_modified.json", orient='records', lines=True)



with open('yelp_academic_dataset_user_modified.json', 'rb',buffering=1) as infile, open('yelp_academic_dataset_user_two_modified.json', 'w') as outfile:
    # read the input file as JSON
    for line in infile:
        # parse the line as JSON
        obj = json.loads(line)
        #outfile.write(json.dumps(obj) + '\n')
        # get the elite string and split it into a list of years
        elite = obj['elite']
        # print(elite)
        years = elite.split(',')
        # #print(years)
        # # count the number of years in the list
        count = len(years)
        #print(count)

        # add the count to the object
        obj['elite'] = count

        # write the updated object to the output file
        outfile.write(json.dumps(obj) + '\n')