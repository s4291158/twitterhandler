from threading import Timer
from api.hashtag import *
from TwitterSearch import *
from twitterhandler.settings import TWITTER


class BigBoyTimer(object):
    def __init__(self, interval):
        self._timer = None
        self.interval = interval
        self.is_running = False
        self.since_id = 0

        self.ts = TwitterSearch(
            consumer_key=TWITTER["consumer_key"],
            consumer_secret=TWITTER["consumer_secret"],
            access_token=TWITTER["access_token_key"],
            access_token_secret=TWITTER["access_token_secret"]
        )

    def _run(self):
        self.is_running = False
        self.start()
        self.since_id = search(self.ts, since_id=self.since_id)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

    def toggle(self):
        if self.is_running:
            self.stop()
        else:
            self.start()
