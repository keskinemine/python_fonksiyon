from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver',chrome_options=self.browserProfile)
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        

        print(f"first count: {followerCount} ")

        action = webdriver.ActionChains(self.browser)
        
        while followerCount < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount} ")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        i = 0 
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
            i += 1
            if i == max:
                break 

        with open("followers.txt","w") as file:
            for item in followerList:
                file.write(item + "\n")

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_css_selector("button._5f5mN.-fzfL._6VtSN.yZn4P")
        if followButton.text != "":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_css_selector("button._5f5mN.-fzfL._6VtSN.yZn4P")
        if followButton.text == "":
            followButton.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
        else:
            print("zaten takip etmiyorsun!")

instagrm = Instagram(username, password)
instagrm.signIn()
instagrm.getFollowers(50)
# instagrm.followUser("kod_evreni")
# instagrm.unFollowUser("kod_evreni")



# list = ["kod_evreni", "...", "..."]

# for us in list:
#     instagrm.followUser(us)
#     time.sleep(3)
