from gitignored_login_info import TaglinesOfTerror
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SeleniumLocator
import time

class SeleniumContext:
    #   SeleniumContext was taken from my other project,
    #       "Data Scraping and Browser Automation",
    #   and specifically from "webscraping_context_managers.py".
    #
    class BasicChromeDriver():
        def __init__( self, url):
            self.url = url

        def __enter__(self):
            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
            return self.driver

        def __exit__(self, exc_type, exc_value, exc_traceback):
            self.driver.quit()

    class BasicFirefoxDriver():
        def __init__( self, url):
            self.url = url

        def __enter__(self):
            self.driver = webdriver.Firefox()
            self.driver.get(self.url)
            return self.driver

        def __exit__(self, exc_type, exc_value, exc_traceback):
            self.driver.quit()


class ArtBot:
    def __init__( self):
        pass

class TwitterArtBot( ArtBot):
    def __init__( self):
        super().__init__()
        self.base_url = "https://twitter.com/"

    def set_login_identity( self, username, password):
        self.username = username
        self.password = password

    def text_post( self, post_text):
        with SeleniumContext.BasicFirefoxDriver( self.base_url) as self.driver:
            self._login()
            self._form_text_post( post_text)
            time.sleep(10)
                # I'm not ready to start posting yet.

    def _form_text_post(self, post_text):
        post_text_box = WebDriverWait(self.driver, 2).until( EC.presence_of_element_located(SeleniumLocator.Twitter.POST_TEXT_BOX))
        post_text_box.send_keys( post_text)

    def _login( self):
        username_box = WebDriverWait(self.driver, 2).until( EC.presence_of_element_located(SeleniumLocator.Twitter.USERNAME_BOX))
        username_box.send_keys( self.username)
        password_box = WebDriverWait(self.driver, 2).until( EC.presence_of_element_located(SeleniumLocator.Twitter.PASSWORD_BOX))
        password_box.send_keys( self.password)
        login_button = WebDriverWait(self.driver, 2).until( EC.presence_of_element_located(SeleniumLocator.Twitter.LOGIN_BUTTON))
        login_button.click()

if __name__=='__main__':
    account = TaglinesOfTerror()
    artbot  = TwitterArtBot()
    artbot.set_login_identity( account.username, account.password)
    artbot.text_post( "Blah blah blah, #hashtag #yayayaIAmLorde")
