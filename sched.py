import kube_deploy as kd
from datetime import datetime, timedelta
import sys
from pymongo import MongoClient



if __name__=="__main__":
    namespace = sys.argv[1]
    dbhost = sys.argv[2]
    print(sys.argv[1])
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

    if diff.seconds < 0:
        print("Time's up. Killing jobs.")
        kd.delete_cronjob(namespace)
        kd.namespace_cleanup(namespace)

        db.users.update_one(
        {'namespace':namespace},
        {
            "$set":{
            "jobs":jobs,
            "state":"inactive"
            }
        })
    else:
        print("There is still time. Keep runnning.")
