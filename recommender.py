import pandas as pd
from textblob import TextBlob

def sentiment_score(text):
    return TextBlob(text).sentiment.polarity

def recommend(city, cuisine, max_price):
    restaurants = pd.read_csv("restaurants.csv")
    reviews = pd.read_csv("reviews.csv")
 
    filtered = restaurants[
        (restaurants["city"] == city) &
        (restaurants["cuisine"] == cuisine) &
        (restaurants["price"] <= max_price)
    ]

    scores = []
    for _, row in filtered.iterrows():
        rest_reviews = reviews[reviews["restaurant_id"] == row["id"]]
        sentiment = rest_reviews["review"].apply(sentiment_score).mean()

        final_score = (
            0.6 * row["rating"] +
            0.4 * (sentiment * 5)   
        )

        scores.append((row["name"], round(final_score, 2)))
    return sorted(scores, key=lambda x: x[1], reverse=True)
