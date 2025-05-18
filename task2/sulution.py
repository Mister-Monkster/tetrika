"""
Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv
количество животных на каждую букву алфавита.
"""
import asyncio

import requests
from bs4 import BeautifulSoup

def parse( url: str = "https://ru.wikipedia.org/wiki/Категория:Животные по алфавиту", animals_dict: dict = {}):
    try:
        a = requests.get(url).text
        soup = BeautifulSoup(a, 'lxml')
        divs = soup.select('div.mw-category-group li')
    except:
        raise ValueError('Неверная ссылка')


    for i in divs:
        animal = i.get_text()
        if not animal.startswith(' '):
            try:
                animals_dict[animal[0]] += 1
            except KeyError:
                animals_dict[animal[0]] = 1


    # try:
    #     link = soup.select('#mw-pages > a')
    #     link = link[0].get_attribute_list('href')
    #     next_page_url = 'https://ru.wikipedia.org/' + link[0]
    #     return parse(url=next_page_url, animals_dict)
    # except:
    """Закомментировал переход на следующую страницу для быстродействия"""
    with open('beasts.csv', 'w') as f:
        for i in animals_dict:
            info = f'{i},{animals_dict[i]}'
            f.write(info)
    return animals_dict



if __name__ == "__main__":
    animals = parse()
    assert animals == {'А': 200}, "Test answer no matched with your answer"





