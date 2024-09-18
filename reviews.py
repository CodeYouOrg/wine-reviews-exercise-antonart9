import pandas as pd 
import numpy as np 
reviews = pd.read_csv("data\winemag-data-130k-v2.csv.zip", compression='zip', index_col=0)

countries_count = reviews.groupby('country').description.count() # country count

mean_points = reviews.sort_values(['points']).groupby('country').points.mean() # average score 

reviews = pd.merge(countries_count, 
                              mean_points.round(1), on='country') # raw merge

reviews_by_country = reviews.sort_values('description', ascending=False).rename(columns={'description':'count'}).reset_index() # renaming and resetting the index

#print(reviews_by_country) # preview 

reviews_by_country.to_csv('data/reviews-per-country.csv', index=False)

