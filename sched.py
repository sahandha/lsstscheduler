from datetime import datetime, timedelta
import sys
from pymongo import MongoClient
import requests


if __name__=="__main__":
    username  = sys.argv[1]
    namespace = sys.argv[2]
    dbhost    = sys.argv[3]

    client = MongoClient("{}.resourceallocation.svc.cluster.local".format(dbhost), 27017)
    db = client.ResourceAllocation
    doc = db.users.find_one({"namespace":namespace})

    expdate = doc["expirationdate"]

    now = datetime.now()

    diff = expdate - now
    print("expiration: ", expdate)
    print("Now: ", now)
    print("difference: ", diff)
    print("difference in seconds: ", diff.seconds)

    if diff.total_seconds() < 0:
        print("Time's up. Killing jobs.")
        requests.get("https://lsstlabs.ncsa.illinois.edu/lsstsim/deactivateuser", params={"user":username},verify=False)
    else:
        print("There is still time. Keep runnning.")
