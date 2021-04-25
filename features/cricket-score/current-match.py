from bs4 import BeautifulSoup
import requests


def get_current_match():
    data = str()
    r = requests.get("https://www.cricbuzz.com/")

    soup = BeautifulSoup(r.content,'html.parser')

    menu = soup.find(id="match_menu_container")
    matches = menu.find('li')
    for q in matches.find_all('div'):
        chl = q.findChild()
        if not chl:
            data+=q.text+"\n"

    return data

if __name__ == '__main__':
    print(get_current_match())


