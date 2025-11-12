from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
password = getenv("PASSWORD")

def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        # page.click('span[class="login pl-2"]')
        page.click('span.login.pl-2')

        # page.fill('input[id="username"]', "souhrada")
        page.fill('input#username', login)

        page.fill('input#password', password)

        page.click('button#loginbtn')




        input("Zmáčkni jakoukoliv klávesu pro zavření prohlížeče")
        browser.close()


if __name__ == "__main__":
    main()