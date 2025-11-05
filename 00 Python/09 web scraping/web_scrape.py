from bs4 import BeautifulSoup
import requests


def main():

    url = "https://www.trebesin.cz"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    all_p = soup.find_all("p")

    # for p in all_p:
    #     print(p.text)

    # gym = soup.find(id="favimagehover-title4")
    # print(gym)

    # .select používá CSS selectory ., #, atd.
    # select vrací všechny prvky v listu
    gym2 = soup.select("#favimagehover-title4")
    print(gym2[0].text)

    # alternativně
    # gym2 = soup.select_one("#favimagehover-title4")
    # print(gym2.text)

    # select_one a select jsou alternativy k find a find_all

if __name__ == "__main__":
    main()
