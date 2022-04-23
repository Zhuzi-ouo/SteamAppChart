import requests
from bs4 import BeautifulSoup
import json
def chart(AppName):
    with open(r"Package/steamAppID.json", "r", encoding = "utf8") as file:
        AppID = json.load(file)
    if(AppName in AppID):
        response=requests.get(f"http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid={AppID[AppName]}").json()
        soup=response["response"]
        chart.count=soup["player_count"]
        chart.search="True"
    else:
        chart.search="False"