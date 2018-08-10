import kube_deploy as kd
from datetime import datetime, timedelta
import sys
from pymongo import MongoClient



if __name__=="__main__":
    print(sys.argv[1])
    client = MongoClient('localhost', 27017)
    db = client.ResourceAllocation
    doc = db.users.find_one()
    print(doc)
    printUserData(db)
