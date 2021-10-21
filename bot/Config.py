import requests
from bs4 import BeautifulSoup
import datetime as dt
from datetime import date


# scraper.py, функция которая возвращает список! предстоящих игр Зенита
def match_day():
    url = 'https://www.sports.ru/zenit/calendar/'
    page = requests.get(url)  # записываем в переменную page html код страницы
    filteredNews = [] # объявили несколько списков
    allNews = []
    actual_games = []
    old_games = []
    actual_games.clear()  #очистить список, т.к. в него вроде как много говна с предыдущих прогонов записывается
    soup = BeautifulSoup(page.text, "html.parser") #парсим страницу в формате хтмл
    allNews = soup.findAll('td', class_="name-td alLeft bordR") #вычленяем их хтмл кода страницы нужный нам участок с играми зенита
    for data in allNews:
        filteredNews.append(data.text)
    filteredNews.remove('Дата')
        #print(filteredNews)
    for data in filteredNews:
        data2 = data.strip('\n')
        data2 = data2[:10] # дата в формате дд.мм.гг
        data3 = dt.datetime.strptime(data2, '%d.%m.%Y') # перевернутая дата в формате гг-мм-дд
        current_date = str(date.today())
        current_date2 = current_date.split("-")
        current_date2.reverse()
        current_date3 = ".".join(current_date2)
        current_date4 = dt.datetime.strptime(current_date3, '%d.%m.%Y')
        if data3 < current_date4:
            old_games.append(f'Зенит играл: {data2}')
        else:
            actual_games.append(f'Зенит будет играть: {data2}')
    return '\n' .join(actual_games)

# Функция алерт возвращает 1 следующую игру зенита
def alert():
    url = 'https://www.sports.ru/zenit/calendar/'
    page = requests.get(url)  # записываем в переменную page html код страницы
    filteredNews = [] # объявили несколько списков
    allNews = []
    actual_games = []
    old_games = []
    #actual_games.clear()  #очистить список, т.к. в него вроде как много говна с предыдущих прогонов записывается
    soup = BeautifulSoup(page.text, "html.parser") #парсим страницу в формате хтмл
    allNews = soup.findAll('td', class_="name-td alLeft bordR") #вычленяем их хтмл кода страницы нужный нам участок с играми зенита
    for data in allNews:
        filteredNews.append(data.text)
    filteredNews.remove('Дата')
        #print(filteredNews)
    for data in filteredNews:
        data2 = data.strip('\n')
        data2 = data2[:10]
        data3 = dt.datetime.strptime(data2, '%d.%m.%Y')
        current_date = str(date.today())
        current_date2 = current_date.split("-")
        current_date2.reverse()
        current_date3 = ".".join(current_date2)
        current_date4 = dt.datetime.strptime(current_date3, '%d.%m.%Y')
        if data3 < current_date4:
            old_games.append(f'Зенит играл: {data2}')
        else:
            actual_games.append(f'Ближайшая игра Зенита состоится: {data2}')
    return (actual_games[0])

#функция напоминалка возвращает дату и время в день игры. Возвращенные значения передаются в бот сенд меседж. Эта функция выполлняется только в том случае если функция матч дэйт выдаст True
def napominalka():
    url = 'https://www.sports.ru/zenit/calendar/'
    page = requests.get(url)  # записываем в переменную page html код страницы
    filteredNews = [] # объявили несколько списков
    allNews = []
    new_games = []
    old_games = []
    new_games.clear()  #очистить список, т.к. в него вроде как много говна с предыдущих прогонов записывается
    soup = BeautifulSoup(page.text, "html.parser") #парсим страницу в формате хтмл
    allNews = soup.findAll('td', class_="name-td alLeft bordR") #вычленяем их хтмл кода страницы нужный нам участок с играми зенита
    for data in allNews:
        filteredNews.append(data.text)
    filteredNews.remove('Дата')
        #print(filteredNews)
    for data in filteredNews:
        n = str()
        data2 = data.strip('\n')
        time = data2[11:16]
        data2 = data2[:10]
        data3 = dt.datetime.strptime(data2, '%d.%m.%Y') # даты спарсеные с сайта
        current_date = str(date.today())
        current_date2 = current_date.split("-")
        current_date2.reverse()
        current_date3 = ".".join(current_date2)
        current_date4 = dt.datetime.strptime(current_date3, '%d.%m.%Y') # дата текущего дня в верном формате
        if data3 < current_date4:
            old_games.append(f'Зенит играл: {data2}')
        else:
            new_games.append(f' {data2} в {time}')
    if data3 == current_date4:
        return f'Зенит играет сегодня {new_games[0]}'
    else:
        print (f'Зенит играет не сегодня')
        pass
      

#Функция которая проверит настал день игры или нет
def match_date():
    url = 'https://www.sports.ru/zenit/calendar/'
    page = requests.get(url)  # записываем в переменную page html код страницы
    clear_date = [] # объявили несколько списков
    parse_page = []
    soup = BeautifulSoup(page.text, "html.parser") #парсим страницу в формате хтмл
    parse_page = soup.findAll('td', class_="name-td alLeft bordR") #вычленяем их хтмл кода страницы нужный нам участок с играми зенита
    for data in parse_page:
        clear_date.append(data.text)
    clear_date.remove('Дата')
        #print(filteredNews)
    for data in clear_date:
        data2 = data.strip('\n')
        data2 = data2[:10]
        data3 = dt.datetime.strptime(data2, '%d.%m.%Y') # даты спарсеные с сайта
        current_date = str(date.today())
        current_date2 = current_date.split("-")
        current_date2.reverse()
        current_date3 = ".".join(current_date2)
        current_date4 = dt.datetime.strptime(current_date3, '%d.%m.%Y') # дата текущего дня в верном формате
        if data3 == current_date4:
            return True
        else:
            return False
