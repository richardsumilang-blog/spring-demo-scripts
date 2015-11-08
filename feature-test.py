#!/usr/bin/env python

import os,sys,time,re,urllib,json


if __name__ == '__main__':
    fp = urllib.urlopen('http://feature.cfapps.io/env')
    json_str = fp.read()
    result = json.loads(json_str)
    ip= result['systemEnvironment']['CF_INSTANCE_IP']
    sp = result['configService:https://github.com/richardsumilang-blog/spring-demo-rest-config.git/feature.yml']
    print ip, sp
    fp.close()
