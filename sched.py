import tornado.ioloop
import tornado.web
from tornado.web import asynchronous

import kube_deploy as kd
from datetime import datetime, timedelta
import motor.motor_tornado
import sys



if __name__=="__main__":
    print(sys.argv[1])

    db = motor.motor_tornado.MotorClient().ResourceAllocation

    doc = db.users.find({},{"_id": 0 ,"username": 1, "cpulimit": 1, "memlimit": 1, "podlimit": 1, "state": 1, "expirationdate": 1}).to_list(length=100)
    userdata = [[l["username"],l["cpulimit"],l["memlimit"],l["podlimit"],l["state"],str(l["expirationdate"]-datetime.now())] for l in doc]

    print(userdata)

    print("server running at localhost:8888 ...")
    ("press ctrl+c to close.")
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
