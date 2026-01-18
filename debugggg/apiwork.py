import random

import requests


count_vacancies = random.randint(0,13)
print(count_vacancies)
def send_req(page):
   headers = {
      "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 YaBrowser/25.10.0.0 Safari/537.36"
   }
   url = f"https://api.hh.ru/vacancies?page=4&per_page={page}&only_with_salary=true"
   search_url = "https://api.hh.ru/suggests/android"
   response = requests.get(url,headers)
   req = response.json()
   #print(type(req))
   #req = req["items"]
   return req



if __name__ == '__main__':
   for i in range(13):
      result = send_req(i)
      #print()
   reqs = result["items"]
   #print(reqs)
   for j in range(len(reqs)):
      print(reqs[j]['name'],"|\t Ссылка:", reqs[j]['alternate_url'])
#todo форматирование текста добавь и поиск по кейвордам
#todo Я за чаем покекав

