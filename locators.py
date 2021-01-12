from selenium.webdriver.common.by import By

class SeleniumLocator:
    class Twitter:
        USERNAME_BOX = (By.NAME, "session[username_or_email]")
        PASSWORD_BOX = (By.NAME, "session[password]")
        LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[3]/div")
        POST_TEXT_BOX = (By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div")
