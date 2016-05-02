from TwitterSearch import *
from twitterhandler.settings import KEYWORDS
import pprint, time, requests

pp = pprint.PrettyPrinter(indent=2)


def get_rate_limit(ts):
    url = "https://api.twitter.com/1.1/application/rate_limit_status.json"
    auth = ts.get_auth()
    proxy = ts.get_proxy()
    r = requests.get(url, auth=auth, proxies={"https": proxy})
    resources = r.json()["resources"]
    search_limit = resources["search"]["/search/tweets"]["remaining"]
    print("rate_limit_remain: {0}".format(search_limit))


def search(ts, since_id=0):
    try:
        start = time.time()
        tso = TwitterSearchOrder()
        tso.set_keywords(KEYWORDS, True)
        if since_id:
            tso.set_since_id(since_id)
        tso.set_result_type("recent")

        get_rate_limit(ts)

        tweets_org = ts.search_tweets_iterable(tso)
        # print(tso.url)
        tweets = tweets_org.get_tweets()["statuses"]
        tweets_count = len(tweets)
        # print(len(tweets["statuses"]))
        if tweets_count > 0:
            since_id = tweets[0]["id"]

        for tweet_dict in tweets:
            tweet_id = tweet_dict["id"]
            tweet_text = tweet_dict["text"]
            # print("{0}: {1}".format(tweet_id, tweet_text))
        end = time.time()
        print("tweets: {0}, time taken: {1}".format(len(tweets), end - start))

    except TwitterSearchException as e:
        print(e)

    return since_id
