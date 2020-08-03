# Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the raw / uncleaned dataset
dataset = pd.read_csv('movie_metadata.csv')
data = dataset.loc[:, ['director_facebook_likes', 'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes','cast_total_facebook_likes','movie_facebook_likes','gross','num_critic_for_reviews','num_voted_users','budget','imdb_score']]

sns.pairplot(data)
plt.savefig('pairplot.png')