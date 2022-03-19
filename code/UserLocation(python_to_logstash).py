import requests
import json
import socket
import json
import sys
import time

HOST = 'localhost'
PORT = 1236

while(True):
    
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key=<>'

    data = {
        'considerIp': True, # 현 IP로 데이터 추출
    }

    result = json.loads(requests.post(url, data).text) # 해당 API에 요청을 보내며 데이터를 추출 후 json으로 load한다.

    lat = result["location"]["lat"] # 현재 위치의 위도 추출
    lon = result["location"]["lng"] # 현재 위치의 경도 추출

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        sys.exit(1)

    try:
        sock.connect((HOST, PORT))
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        sys.exit(2)

    msg = {                 
        "location" : {
            "lat" : lat,
            "lon" : lon
        }
    }

    sock.send(str(json.dumps(msg)).encode('utf-8') )

    time.sleep(1)   # 1초 주기로 위치 정보를 보내기 위해 사용된 sleep함수

    #sock.close()
    #sys.exit(0)
