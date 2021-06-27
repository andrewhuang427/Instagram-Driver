from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class InstagramWebDriver:
    def __init__(self, username="", password=""):
        chromeDriver = ChromeDriverManager()
        self.driver = webdriver.Chrome(chromeDriver.install())
        self.url = "https://www.instagram.com/"
        self.username = username
        self.password = password

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def login(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(8)

        xPathToUsernameInput = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
        xPathToPasswordInput = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
        xPathToSubmitButton = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"
        xPathToDoNotSaveCredentialsButton = "/html/body/div[1]/section/main/div/div/div/div/button"
        xPathToDoNotTurnOnNotificationsButton = "/html/body/div[4]/div/div/div/div[3]/button[2]"

        # pass username into username input
        try:
            usernameInput = self.driver.find_element_by_xpath(
                xPathToUsernameInput)
            usernameInput.send_keys(self.username)
        except NoSuchElementException:
            print("Username Input not found\n")

        # pass password into password input
        try:
            passwordInput = self.driver.find_element_by_xpath(
                xPathToPasswordInput)
            passwordInput.send_keys(self.password)
        except NoSuchElementException:
            print("Password Input not found\n")

        # click on login button
        try:
            loginButton = self.driver.find_element_by_xpath(
                xPathToSubmitButton)
            loginButton.click()
        except NoSuchElementException:
            print("Login button not found\n")

        # click on do not save credentials
        try:
            doNotSaveButton = self.driver.find_element_by_xpath(
                xPathToDoNotSaveCredentialsButton)
            doNotSaveButton.click()
        except NoSuchElementException:
            print("Do not save credentials button not found\n")

        # click on do not save credentials
        try:
            doNotSendNotificationsButton = self.driver.find_element_by_xpath(
                xPathToDoNotTurnOnNotificationsButton)
            doNotSendNotificationsButton.click()
        except NoSuchElementException:
            print("Do not save notifications button not found\n")

        print("Login Successful\n")

    # def getFollowers(self, instagramHandle):
    #     url = self.url + str(instagramHandle)
    #     self.driver.get(url)

    #     xPathToFollowersButton = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a"

    #     try:
    #         followersButton = self.driver.find_element_by_xpath(
    #             xPathToFollowersButton)
    #         followersButton.click()
    #     except NoSuchElementException:
    #         print("Followers button was not found\n")

    #     sleep(5)
    #     pageSource = self.driver.page_source
    #     soup = BeautifulSoup(pageSource, "html.parser")
    #     with open("scraped.html", "w") as file:
    #         file.write(str(soup))

    def sendDM(self, userHandle, message):

        print("Sending dm to " + str(userHandle))

        url = "https://www.instagram.com/direct/inbox/"
        self.driver.get(url)

        self.driver.implicitly_wait(5)

        try:
            xPathToNewMessageButton = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button"
            newMessageButton = self.driver.find_element_by_xpath(
                xPathToNewMessageButton)
            newMessageButton.click()

            xPathToUsernameInput = "/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input"
            usernameInput = self.driver.find_element_by_xpath(
                xPathToUsernameInput)
            usernameInput.send_keys(userHandle)

            sleep(2)

            xPathToUserSelectButton = "/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div"
            selectUserButton = self.driver.find_element_by_xpath(
                xPathToUserSelectButton)
            selectUserButton.click()

            xPathToNextButton = "/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div"
            nextButton = self.driver.find_element_by_xpath(xPathToNextButton)
            nextButton.click()

            xPathToTextInput = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"
            messageBox = self.driver.find_element_by_xpath(xPathToTextInput)
            messageBox.send_keys(message)

            sleep(10)

            xPathToSendButton = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button"
            sendButton = self.driver.find_element_by_xpath(xPathToSendButton)
            sendButton.click()

            print("Message sent successfully to " + str(userHandle) + "\n")

        except NoSuchElementException:
            print("Missing element. Message not able to be sent")

    def disconnect(self):
        print("See ya later!")
        self.driver.implicitly_wait(5)
        self.driver.close()
