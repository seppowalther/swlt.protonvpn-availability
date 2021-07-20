import requests
from pythonping import ping

result1 = requests.get("https://api.protonmail.ch/vpn/logicals")
result2 = result1.json()
response = result2["LogicalServers"]
reachable = list()
nonreachable = list()

remainingservers = len(response)

for i in response:
    name = i['Name']
    entryip = i['Servers'][0]['EntryIP']
    pingresponse = ping(entryip, verbose=False, count=1)
    pingsuccess = pingresponse.success()
    print(name+" is reachable: "+str(pingsuccess)+" remaining servers to test: "+str(remainingservers))
    if pingsuccess == True:
        reachable.append(name)
    else:
        nonreachable.append(name)
    remainingservers = remainingservers - 1

print("Reachable servers:")
for i in reachable:
    print(i)

print ("Non-reachable servers:")
for i in nonreachable:
    print(i)