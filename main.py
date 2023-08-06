import requests
import lxml
from bs4 import BeautifulSoup
import csv
from time import sleep

# переменная с юзер агентом
headers =  {
        "accept":"*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

# пустой список для названия и автора фильма с сылкой
data = []

for p in range(1,5): # общий цикл для выполнения парсера страниц на сайте
    print(p) # выводит количество спарсеных страниц
    url = f"https://litnet.com/ru/top/detektivy?alias=detektivy&page={p}" # переменная р для прохорда парсера по страницам
    req = requests.get(url, headers) # запрос на сервер
    sleep(3) # делает остановку парсинга на 3 секунды
    soup = BeautifulSoup(req.text, 'lxml')
    books = soup.find_all('div', class_='row book-item') # нахождение по фильтру блока общего


    for item in books: # обход тегов с классами
            title_autor = item.find('p', class_='author-wr').find('a').text
            link = item.find('h4', class_='book-title').find('a').get('href')
            tmp = { "название":title_autor, "ссылка":link} # словарь для добавления в список с найдкными тегами в переменной
            data.append(tmp) # добавление в список
            csv_text = ["название", "ссылка"] # заголовок для файла на сохранении

    # запись в файл csv
    with open('text.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames = csv_text, delimiter=";")
            writer.writeheader()
            writer.writerows(data)
        
print(len(data)) # выводит колиство записанных в список пройденых значений


































