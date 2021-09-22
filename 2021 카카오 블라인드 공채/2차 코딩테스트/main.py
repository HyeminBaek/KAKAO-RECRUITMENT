import requests
import json
import heapq
import random
import APIsetting

#problem requirements
#1. 불균형한 수요공급 최대한 맞춰주기
#2. 대여소에 취소되는 대여 요청 수를 최대한 줄여야 한다. 단, 트럭은 적게 움직이는 편이 좋다.
#3. 사용자가 요청을 보낸 시점에 자전거 대여소에 자전거가 부족하면 사용자가 보낸 요청은 자동으로 취소된다.
#4. 대여소에는 자전거를 무한대 보관할 수 있다
#5. 트럭이 100m를 이동하는 데에는 6초가 걸린다.
#6. 각 트럭은 자전거를 최대 20대 수용할 수 있다.

#basic setting
base_url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
scenario =1;

auth_key = APIsetting.startAPI(base_url,scenario)
#locations = APIsetting.locationsAPI(base_url,auth_key=auth_key)
#trucks = APIsetting.trucksAPI(base_url,auth_key=auth_key)

#print(locations)
#print(trucks)

with open("problem1_day-1.json") as d1:
    json_data = json.load(d1)

#print(json_data)

#algorithm start
#[자전거를 대여할 자전거 대여소 ID, 자전거를 반납할 자전거 대여소 ID, 자전거를 탈 시간(분 단위)]
# 0: 6초간 아무것도 하지 않음
# 1: 위로 한 칸 이동
# 2: 오른쪽으로 한 칸 이동
# 3: 아래로 한 칸 이동
# 4: 왼쪽으로 한 칸 이동
# 5: 자전거 상차
# 6: 자전거 하차

map = {0:[4,0],1:[3,0],2:[2,0],3:[1,0],4:[0,0],
        5:[4,1],6:[3,1],7:[2,1],8:[1,1],9:[0,1],
        10:[4,2],11:[3,2],12:[2,2],13:[1,2],14:[0,2],
        15:[4,3],16:[3,3],17:[2,3],18:[1,3],19:[0,3],
        20:[4,4],21:[3,4],22:[2,4],23:[1,4],24:[0,4]
    }

if(scenario==1):
    numOfTrucks = size = 5;
else:
    numOfTrucks=10
    size =60

dir = [1,5,-1,-5]
#{'id': 3, 'loaded_bikes_count': 0, 'location_id': 0}
#한 번 움직일 때 6초//10번
for i in range(720):
    commands=[]
    locations = APIsetting.locationsAPI(base_url,auth_key=auth_key)
    trucks = APIsetting.trucksAPI(base_url,auth_key=auth_key)
    for j in range(numOfTrucks):
        cmd = []
        curLocId = trucks[j]['location_id']
        curNumBk = trucks[j]['loaded_bikes_count']

        while(len(cmd)<10):
            #현재 위치의 자전거가 4개보다 많다면 싣는다
            if(locations[curLocId]['located_bikes_count']>4):
                # left = 20-curNumBk
                # print(locations[curLocId]['located_bikes_count']-4)
                # for i in range(min(left,locations[curLocId]['located_bikes_count']-4)):
                #     if(len(cmd)==10): break;
                curNumBk+=1;
                cmd.append(5);
            #적고, 현재 트럭에 자전거가 실려있다면 내린다
            elif(curNumBk>0):
                #cur = trucks[j]['loaded_bikes_count']
                #for i in range(min(4-locations[curLocId]['located_bikes_count'],cur)):
                #    if(len(cmd)==10): break;
                curNumBk-=1;
                cmd.append(6);
            #전부 해당 안 된다면 이동
            else:
                nextDir = random.randint(0,3)
                nextLoc=curLocId+dir[nextDir]
                
                if(0<=nextLoc<=24):
                    cmd.append(nextDir+1)
        #print(cmd)
        commands.append({"truck_id": j, "command": cmd})

    APIsetting.simulateAPI(base_url,auth_key=auth_key,commands=commands)

print(APIsetting.scoreAPI(base_url,auth_key))
