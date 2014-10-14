#!/usr/bin/python
#Script created by VND - Visual Network Description (SDN version) 
#You can start floodlight controller with command: java -jar target/floodlight.jar

import httplib
import json
class StaticFlowPusher(object):
    def __init__(self, server):
        self.server = server
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
    def rest_call(self, data, action):
        path = '/wm/staticflowentrypusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
pusher = StaticFlowPusher('192.168.56.105')

flow_0 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"Flow_flow1",
    "cookie":"0",
    "priority":"20",
    "active":"true",
    "actions":"set-src-mac=00:00:00:00:00:01"
    }
pusher.set(flow_0)

flow_0 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"Flow_flow2",
    "cookie":"0",
    "priority":"50",
    "active":"true",
    "actions":"set-src-mac=00:00:00:00:00:01"
    }
pusher.set(flow_0)
