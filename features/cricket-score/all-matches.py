from bs4 import BeautifulSoup
import requests


def get_all_match():
    data = str()
    r = requests.get("https://www.cricbuzz.com/")

    soup = BeautifulSoup(r.content,'html.parser')

    menu = soup.find(id="match_menu_container")
    matches = menu.find_all('li')
    for i in matches:
        for q in i.find_all('div'):
            chl = q.findChild()
            if not chl:
                data+= q.text+"\n"
        data+="\n"

    return data

if __name__ == "__main__":
    print(get_all_match())
