import requests
import json
from bs4 import BeautifulSoup

profile_id = 1351542139 # айди профиля получаю от юзера
profile_url = f"https://api.opendota.com/api/players/{profile_id}/matches"
r2 = requests.get(profile_url)
profile_data = json.loads(r2.text)
last_match_id = ((profile_data[0])['match_id'])
last_match_hero_id = ((profile_data[0])['hero_id']) # получаю айди матча и айди героя на котором играл


last_match_url = "https://api.opendota.com/api/matches/7117759871"
r1 = requests.get(last_match_url)
last_match_data = json.loads(r1.text)

list_of_players = last_match_data['players'] # это массив из статы 10 игроков
test_player_array = list_of_players[5]
print(test_player_array['hero_id'])
