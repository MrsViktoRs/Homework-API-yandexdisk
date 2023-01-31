import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

res = requests.get(url)
data = res.json()
list_heros = ['Hulk', 'Captain America', 'Thanos']
dict_heros = {}
for hero in data:
    if hero['name'] in list_heros:
        dict_heros[hero['name']] = hero['powerstats']['intelligence']
for name, intel in dict_heros.items():
    if intel == max(dict_heros.values()):
        winner_hero = name
        winner_hero_intel = intel
print(f' Самый умный герой {winner_hero} \n Интелект = {winner_hero_intel}')

#------------------------------------Задание 2-------------------------------------
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self): # функция для параметров
        return {
            "Content-Type": "application/json",
            "Authorization": 'OAuth {}'.format(self.token)
        }

    def upload_link(self, disk_file_path): # получаю ссылку для загрузки
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        res = requests.get(url, headers=headers, params=params)
        return res.json()

    def upload_file(self, disk_file_path, file_name): # собственно загружаю
        res = self.upload_link(disk_file_path=disk_file_path)
        url = res.get('href')
        response = requests.put(url, data=open(file_name, 'rb'))


if __name__ == '__main__':
    path_file = ...# путь к файлу
    token = ...# тут наш токен
    uploader = YaUploader(token)