import twitter
import yweather

from pprint import pprint

api = twitter.Api(
    consumer_key="<consumer-key>",
    consumer_secret="<consumer-key>",
    access_token_key="<access-key>",
    access_token_secret="<access-key>"
)


def get_where_on_earth_id(country = None):
    if country:
        client = yweather.Client()
        woeid = client.fetch_woeid(country)
        return woeid


def get_trends(country = None):
    woeid = get_where_on_earth_id(country)
    print(woeid)
    if country :
        try:
            trends = api.GetTrendsWoeid(woeid, exclude=None)
            pprint(trends)
        except Exception as e:
            print(e[0][0]["message"])
    else:
        try:
            trends = api.GetTrendsCurrent()
            pprint(trends)
        except Exception as e:
            print(e[0][0]["message"])


if __name__ == "__main__":
    # edit this according to country of your choice
    country_name = None
    get_trends(country_name)

