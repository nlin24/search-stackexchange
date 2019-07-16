
#https://api.stackexchange.com/2.2/search?pagesize=5&fromdate=1559347200&order=desc&sort=creation&intitle=ilo&site=stackoverflow
import sys, requests, json
from datetime import datetime

def main(topic, site):
    t = str(topic)
    s = str(site)
    monthago = int(datetime.today().timestamp()) - 2629800 # 2629800 seconds in a month
    
    query = "https://api.stackexchange.com/2.2/search?pagesize=5&fromdate="+ str(monthago) + "&order=desc&sort=creation&intitle=" + t + "&site=" + s
    r = requests.get(query)
    if r.status_code != 200:
        raise Exception("Query errored out!") 
    else:
        data = r.json()
        for i in range(len(data["items"])):
            print("[" + str(i) + "] " + data["items"][i]["title"] + " @ " + data["items"][i]["link"])

if __name__ == "__main__":
    sys.exit(main("ilo","stackoverflow"))
