#https://my-devblog.tistory.com/27

import requests
import json

#Start API
def startAPI(base_url,number) :
    headers = {'X-Auth-Token': 'fcd88ba49487f6c2dca8b3918aa0867b','Content-Type': 'application/json;'} 
    data = {'problem':number} 
    url = base_url+"/start"
    res = requests.request("POST", url, data=json.dumps(data), headers=headers)
    #print(str(res.status_code) + " | " + res.text)

    resDic = res.json();
    return resDic["auth_key"];

#Locations API
def locationsAPI(base_url,auth_key):
    headers = {'Authorization': auth_key,'Content-Type': 'application/json;'} 
    url = base_url+"/locations"
    res = requests.request("GET",url,headers=headers) 
    #print(str(res.status_code) + " | " + res.text)

    locDic=res.json()
    return locDic['locations'];

#Trucks API
def trucksAPI(base_url,auth_key):
    headers = {'Authorization': auth_key,'Content-Type': 'application/json;'} 
    url = base_url+"/trucks"
    res = requests.request("GET",url,headers=headers) 

    trkDic=res.json()
    return trkDic['trucks'];

#Score API
def scoreAPI(base_url,auth_key):
    headers = {'Authorization': auth_key,'Content-Type': 'application/json;'} 
    url = base_url+"/score"
    res = requests.request("GET",url,headers=headers) 

    score = res.json()
    return score['score'];

#Simulate API
def simulateAPI(base_url,auth_key,commands):
    headers = {'Authorization': auth_key,'Content-Type': 'application/json;'} 
    url = base_url+"/simulate"
    data = {"commands": commands}
    res = requests.request("PUT",url,headers=headers,data=json.dumps(data)) 
    print(str(res.status_code) + " | " + res.text)
