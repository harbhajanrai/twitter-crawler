import twitter

api = twitter.Api(
    consumer_key="<consumer-key>",
    consumer_secret="<consumer-key>",
    access_token_key="<access-key>",
    access_token_secret="<access-key>"
)


print("Trending #hashtags across the world")

trends = api.GetTrendsCurrent()

for trend in trends:
    print(trend.name)