import json
import requests
import time



blocks_address="https://beta-api.explorer.space/api/blocks/height/"
tx_address="https://beta-api.explorer.space/api/blocks//coins"

last_block=requests.get("https://xchscan.com/api/blocks?limit=1").json()["blocks"][0]["height"]
print("Height of blockchain: "+str(last_block))

data=[]
f=open("chia.json","w")
f.write("{\n")
i=816488
while i<1500000:

    try:
        response=requests.get(blocks_address+str(i),timeout=10)
    except:
        time.sleep(10)
        continue
    if response.status_code>=400:
        print("Status code: "+str(response.status_code))
        time.sleep(10)
        continue
    response=json.loads(response.text)

    try:
        response2=requests.get(tx_address[:-6]+str(i)+tx_address[-6:],timeout=10)
    except:
        time.sleep(10)
        continue
    if response2.status_code>=400:
        print("Status code: "+str(response2.status_code))
        time.sleep(10)
        continue
    response2=json.loads(response2.text)
    response["tx"]=response2["results"]

    f.write("\""+str(i)+"\":"+json.dumps(response)+",")
    print(str(i))
    i+=1


f.write("\n}")
f.close()



























