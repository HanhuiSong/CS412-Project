# Ranking Restaurant Services using Cluster Analysis of Yelp Dataset
## Members
  Hanhui Song (hanhuis2@illinois.edu) MCS student Department of Computer Science </br>
  Mingyi Lai (mingyi4@illinois.edu) MS student Department of Industrial and System Engineering</br>
  Shun-Hsiang Hsu (hsus2@illinois.edu) Ph.D. student Department of Civil and Environmental Engineering
## INTRODUCTION
  This project aims to use cluster analysis of the Yelp dataset to
obtain the preferred services of the active users and rank restaurant
services for providing recommendations. To that end, our clustering
methods will take only the numerical and categorical data (e.g. the
review count and category of a restaurant) in the Yelp dataset as
the inputs to analyze the relationship between the active users and
their reviews for ranking restaurant services. Based on the results,
customized rules for different users will be developed to provide
recommendations.

## DATASET
The Yelp dataset consists of reviews, businesses, users, tips, and
check-in data with a total size of 9 GB, including about 700k reviews,
1M+ users, and 150k+ restaurants. In addition to the categorical and
numerical data, the text data of review contents are also included.

## METHODS
This project will first discuss which columns might be important
to rank services and conduct data cleaning to the selected columns
(e.g., handling missing data). With the columns, different clustering
methods will be developed and compared to obtain the relationship
between the active users and their reviews. Then, the recommendations
based on the relationships will be presented. For feasibility,
our objective and research scope are similar to the previous research
[1], where K-means and DBSCAN were adopted to infer electricity
behavior.

## SCHEDULES
• Before the midpoint (3/21), data preprocessing and preliminary
clustering results using baseline approaches (K-means
and DBSCAN) should be completed.</br>
• [3/21-4/4] Review and develop new methods for comparison.</br>
• [4/4-4/18] Rank restaurant services for providing recommendation.</br>
• [4/18-5/2] Write final report.</br>

## REFERENCES
[1] Liping Zhang, Song Deng, and Shiyue Li. 2017. Analysis of power consumer
behavior based on the complementation of K-means and DBSCAN. In 2017 IEEE
Conference on Energy Internet and Energy System Integration (EI2). IEEE, 1–5.

