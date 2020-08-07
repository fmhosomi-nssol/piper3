#!/usr/bin/env python3

#########################################################
# This is the database processing file. (aka. Models)
# It contains the DB connections, queries and functions.
# Uses principles of Models, Views, Controllers (MVC).
#########################################################

# Import modules required for app
import os
import json
import redis

# Check if running in Pivotal Web Services with MongoDB service bound
if 'VCAP_SERVICES' in os.environ:
    VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
    REDISCRED = VCAP_SERVICES["rediscloud"][0]["credentials"]
    r = redis.Redis(host=REDISCRED['hostname'], port=REDISCRED['port'], password=REDISCRED['password'])

# Otherwise, assume running locally with local MongoDB instance    
else:
    r = redis.Redis(host="127.0.0.1", port='6379')

def redis():
    return r
