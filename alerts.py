# This Python file uses the following encoding: utf-8

import urllib.request
import json

class alerts:
    def __init__(self):
        pass
    def getActualData(self):
        contents = urllib.request.urlopen("https://api.alerts.in.ua/v1/alerts/active.json?token=").read()
        json_data_str = contents.decode("utf-8") if isinstance(contents, bytes) else contents
        data = json.loads(json_data_str)

        location_oblast_uids = [alert["location_oblast_uid"] for alert in data["alerts"] if alert["alert_type"] == "air_raid"]

        # print(set(location_oblast_uids))
        return set(location_oblast_uids)







