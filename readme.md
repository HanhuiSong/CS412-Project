## For yelp_academic_dataset_review.json
   Run data_clean_review.py in root folder, resulting in a new file "yelp_academic_dataset_review_modified.json". All commented line can be ignored.

## For yelp_academic_dataset_user.json
  First uncomment the first part of data_clean_user.py (from "data_file = ..." to "... user_df.to_json(...)"), then comment the second part (from "with open() ..." to "... outfile.write(...)")</br>
  
  Run the modified file we get "yelp_academic_dataset_user_modified.json", which only delete the noisy data. 
  
  To make data more clear, we want to change the "elite" attritubes from list of years to its count. We can run the unmodified "data_clean_user.py" to achieve that, which will resulting a new file named "yelp_academic_dataset_user_two_modified.json"
