import requests


response =    requests.get(f"https://api.github.com/repos/kubernetes/kubernetes/pulls")   

complete_response = response.json()


for i in complete_response:
    print(i["id"])