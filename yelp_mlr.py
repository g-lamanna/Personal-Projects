import pandas as pd 
from matplotlib import pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

business = pd.read_json("$PATH_TO_JSON_FILE",lines=True)
user = pd.read_json("$PATH_TO_JSON_FILE",lines=True)
review = pd.read_json("$PATH_TO_JSON_FILE",lines=True)
tip = pd.read_json("$PATH_TO_JSON_FILE",lines=True)
checkin = pd.read_json("$PATH_TO_JSON_FILE",lines=True)
photo = pd.read_json("$PATH_TO_JSON_FILE",lines=True)

df = pd.merge(business,review,how="left",on="business_id")
df = pd.merge(df, user, how='left', on='business_id')
df = pd.merge(df, checkin, how='left', on='business_id')
df = pd.merge(df, tip, how='left', on='business_id')
df = pd.merge(df, photo, how='left', on='business_id')


pitt_df = df[df["city"]=="Pittsburgh"]

#print(pitt_df.columns)
#print(pitt_df.isna().any())

# print(pitt_df.columns)

features_to_remove = ['address','attributes','business_id','categories','city','hours','is_open','latitude','longitude','name','neighborhood','postal_code','state','time']
df.drop(labels=features_to_remove, axis=1, inplace=True)

pitt_df = pitt_df.fillna({"weekday_checkins":0,
                "weekend_checkins":0,
                "average_tip_length":0,
                "number_tips":0,
                "average_caption_length":0,
                "number_pics":0})

#print(pitt_df.isna().any())

#print(pitt_df['stars'].max())

#Current Cols
'''['alcohol?', 'good_for_kids', 'has_bike_parking', 'has_wifi',
       'price_range', 'review_count', 'stars', 'take_reservations',
       'takes_credit_cards', 'average_review_age', 'average_review_length',
       'average_review_sentiment', 'number_funny_votes', 'number_cool_votes',
       'number_useful_votes', 'average_number_friends', 'average_days_on_yelp',
       'average_number_fans', 'average_review_count',
       'average_number_years_elite', 'weekday_checkins', 'weekend_checkins',
       'average_tip_length', 'number_tips', 'average_caption_length',
       'number_pics']
'''

# x = pitt_df["average_caption_length"]
# y = pitt_df["stars"]

# plt.scatter(x,y,alpha=.5)

# plt.xlabel("number_tips")
# plt.ylabel("Rating")
# plt.title("Rating due to sentiment")

# plt.show()

features = pitt_df[['alcohol?', 'good_for_kids', 'has_bike_parking', 'has_wifi',
       'price_range', 'review_count', 'take_reservations',
       'takes_credit_cards', 'average_review_age', 'average_review_length',
       'average_review_sentiment', 'number_funny_votes', 'number_cool_votes',
       'number_useful_votes', 'average_number_friends', 'average_days_on_yelp',
       'average_number_fans', 'average_review_count',
       'average_number_years_elite', 'weekday_checkins', 'weekend_checkins',
       'average_tip_length', 'number_tips', 'average_caption_length',
       'number_pics']]
rating = pitt_df[["stars"]]

X_train, X_test, y_train, y_test = train_test_split(features,rating,train_size=0.8,test_size = 0.2,random_state=1)

mlr = LinearRegression()
mlr.fit(X_train,y_train)

test_predictor = [[1,1,1,1,1,1,10,2,3,10,10,1200,0.9,3,6,5,50,3,50,1800,12,123,0.5,0,0]]
predict_y = mlr.predict(test_predictor)
mlr.score(X_train,y_train)


