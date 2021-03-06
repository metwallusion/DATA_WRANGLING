#!/usr/bin/env python
# coding: utf-8

# # <span style="color:black"><center><u>Data Wrangling</u></center></span>
# ### <span style="color:black"><u>Objectives:<i>(The traffic light from data perspective)</i></u></span>
# #### &emsp;1.<span style="color:solid red"><b> Gathering</b></span>
# #### &emsp;2.<span style="color:solid orange"><b> Assessing</b></span>
# #### &emsp;3.<span style="color:solid green"><b> Cleaning</b></span>
# ---
# <hr style="border:1px solid black"> </hr>
# 
# ### Step 1: <span style="color:red"><u>Gathering</u></span>
# ---
# <i><b>&emsp;The first step in the process is gathering the data which serves the analysis. In this project, there is 3 different source of data gathered. And are as the following:</b></i>
# 1. The <b>twitter archive</b> which is in <b>csv format</b> and downloadable from udacity as it was sent by the twitter team. Therefore, it contains the data about <b><u>@WeRateDogs</u></b>.
# ---
# 2. The <b>image prediction</b> neural network data outcome in a <b>tsv file</b> which can be downloaded by the request library or from udacity. 
# ---
# 3. The <b>twitter api</b> data which can be gathered by the tweepy lib. but there must be a developer account on twitter api. Also it is downloadable from udacity as a <b>txt file</b>.
# ---
# <hr style="border:1px solid black"></hr>
# 
# ### Step 2: <span style="color:solid orange"><u>Assessing</u></span>
# ---
# <i><b>&emsp;Assessing the data is the process of observing the data programatically using python and visually using g-sheets. The target is to discover the quality and tidiness issues. The following problems are the outcome of the assessing and reassessing process the data has been observed and reobserved multiple times.</b></i>
# ### Quality Issues
# 
# ###### - Dataset 1
#  Dropping the rows with values in retweeted_status_id before dropping the column (UPDATE) 
# 1. The timestamp column should be datetime format.
# 2. The dog (name,doggo,floofer,pupper,puppo) columns have Nones instead of NaNs.
# 3. The source html format in source column since the source can be extracted.
# 4. "A Retweet is a re-posting of a Tweet.". So its columns can be dropped since it's not the interest.
# 5. In reply is also to be dropped.
# 6. The name column in 1747 index is 'officially' which doesn't match.
# 7. Some of the numerator ratings inside text columns are in decimal @index 45.
# 8. The text column is including the rating and the review with respect to the link.
# 9. Sometimes denominator ratings are not out of 10.
# 10. The NaNs in expanded urls. Since expanded urls = tweet URLs which is essential.
# 11. Some dogs are classified into multiple stage.
# 12. Drop the tweets that are NaNs.
# 13. Remove all of the '.*only rate dogs' of the tweet column as shown in index 25.
# 
# ###### - Dataset 2
# 1. Drop the img_num as for example each img_num category have different links and are showing different results.
# 2. Combining p1,p2,p3 and p1_conf,p2_conf,p3_conf ,p1_dog,p2_dog,p3_dog into 2 columns only (dog name & probability).Drop the unwanted columns p1,....p3_dog as we already got the dog_name and dog_prob.
# 3. Drop the NaN if all of the p (p1,p2,p3) that are false since the false combined indicating that this row does not belong to any dog.
# 
# ###### - Dataset 3
# 1. Problem in naming the id column should match the other 2 dataset should be tweet_id instead of id.
# 2. Any column except tweet_id, favourite_count, retweeted_count can be dropped.
# 
# ### Tidiness Issues
# 
# ###### - Dataset 1
# 1. (Already combined) columns (doggo,floofer,pupper,puppo) to dog_stat .Drop the unwanted columns (doggo,floofer,pupper,puppo).
# 
# ###### - Combining the data based on tweet_id.
# 1. Combining all of the data into 1 dataset.
# 
# <hr style="border:1px solid black"> </hr>
# 
# ### Step 3: <span style="color:solid green"><u>Cleaning</u></span>
# ---
# <i><b>&emsp;The last step in the process is cleaning and visualize it based on step 2 which was based on step 1. The amount of cleanliness will show better results in visualization. The cleaning steps are as following: </i></b>
# 
# ---
# 
# 1. <b>Define</b> the problem based on each observation.
# ---
# 2. <b>Code</b> programatically. 
# ---
# 3. <b>Test</b> the final product.
# ---
# <hr style="border:1px solid black"> </hr>
