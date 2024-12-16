import requests
from unique_random import generate_unique_random_number

# url="http://nxmtxb.duckdns.org:5000/chat"
url="http://127.0.0.1:5000/chat"
unique_rand=generate_unique_random_number(1,1000)
data={
    "message":"hi",
    "user_id":f"{str(unique_rand)}"
}
headers={
    "Content-Type":"application/json"
}

while True:
    response=requests.post(url,json=data,headers=headers)
    if response.status_code==200 or response.status_code==201:
        res=response.json()
        if "message" in res:
            print("\nJarvis:",res["message"])
        else:
            print("No message in response.")
    else:
        print(f"Failed to send request. Status code : {response.status_code}")
    
    value=input("You: ")
    if "exit" in value:
        break
    data["message"]=value


