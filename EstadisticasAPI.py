import requests

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":"Venezuela"}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "9dadda6754msh2b5903a9c34495cp108ba5jsn3696139a67e9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

dic = response.json()
print(dic)