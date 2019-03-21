import os, sys, requests, time, json, prometheus_client
from prometheus_client import start_http_server, Metric, REGISTRY


class JsonCollector(object):
    def __init__(self):
        pass

    def collect(self):
        pewdiepie = 'pewdiepie'
        tseries = 'tseries'
        youtube_key = 'YOUR_API_KEY'
        endpoint = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='
        youtube_host = os.environ.get('YOUTUBE_HOST', endpoint)
        status = 'running'
        url = youtube_host + pewdiepie + '&key=' + youtube_key
        r = requests.get(url, verify=False)
        try:
            #create pewdiepie metric
            metric = Metric('subscriber_count', 'Current number of subs', 'gauge')
            metric.add_sample('subscriber_count', value=((r.json()["items"][0]["statistics"]["subscriberCount"])), labels={'Channel': 'PewDiePie'})
            # yield metric
        except:
            pass

        url = youtube_host + tseries + '&key=' + youtube_key
        r = requests.get(url, verify=False)
        try:
            #create tseries metric
            # metric = Metric('tseries_subs', 'Current number of non-bros', 'gauge')
            metric.add_sample('subscriber_count', value=((r.json()["items"][0]["statistics"]["subscriberCount"])), labels={'Channel': 'Tseries'})
            yield metric
        except:
            pass

if __name__ == "__main__":
	#start the webserver on the required port
    start_http_server(6969)
    REGISTRY.register(JsonCollector())
    while True: time.sleep(20)
