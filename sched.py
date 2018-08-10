import tornado.ioloop
import tornado.web
from tornado.web import asynchronous
from tornado import gen
import kube_deploy as kd
from datetime import datetime, timedelta
import motor.motor_tornado
import sys


@gen.coroutine
def getUserData(db):
    try:
        doc = yield db.users.find({},{"_id": 0 ,"username": 1, "cpulimit": 1, "memlimit": 1, "podlimit": 1, "state": 1, "expirationdate": 1}).to_list(length=100)
        userdata = [[l["username"],l["cpulimit"],l["memlimit"],l["podlimit"],l["state"],str(l["expirationdate"]-datetime.now())] for l in doc]
    except:
        userdata = []
    return userdata

@gen.coroutine
def printUserData(db):
    doc = db.users.find({},{"_id": 0 ,"username": 1, "cpulimit": 1, "memlimit": 1, "podlimit": 1, "state": 1, "expirationdate": 1}).to_list(length=100)
    userdata = [[l["username"],l["cpulimit"],l["memlimit"],l["podlimit"],l["state"],str(l["expirationdate"]-datetime.now())] for l in doc]

    print(userdata)


if __name__=="__main__":
    print(sys.argv[1])

    db = motor.motor_tornado.MotorClient().ResourceAllocation

    printUserData(db)
