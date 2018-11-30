from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



trigger = input("Enter a keyword to trigger the bot: ")
try:
    inclu = input("Must the keyword be on its own? (Y/N) ").lower()
except ValueError:
    print("We only accept y,n,Y or N")
    print("Set to default, Y")
    inclu = y
Autotext = input("Enter something for the bot to reply: ")
App = input("Enter the name of someone or a group for to bot to check: ")


watermark = "_BeepBoop I am a bot, this action was done automatically_"


driver = webdriver.Chrome(executable_path="Your Chromedriver path here")
elem = driver.get(r"https://web.whatsapp.com/")
input("Hit enter after you've scanned the QR code ")



while True:
    try:
        elem = driver.find_element_by_xpath("//span[@title='{}']".format(App)).click()
        elem = driver.find_elements_by_css_selector("._3zb-j.ZhF0n")
        new = elem[len(elem)-1]
        if new.text == trigger and new.text != Autotext and inclu == "y":
            elem = driver.find_element_by_xpath("//span[@title='{}']".format(App)).click()
            elem = driver.find_element_by_css_selector("._2S1VP.copyable-text.selectable-text")
            elem.send_keys(Autotext)
            elem.send_keys(Keys.RETURN)
        elif trigger in new.text and new.text != Autotext and inclu == "n":
            elem = driver.find_element_by_xpath("//span[@title='{}']".format(App)).click()
            elem = driver.find_element_by_css_selector("._2S1VP.copyable-text.selectable-text")
            elem.send_keys(Autotext)
            elem.send_keys(Keys.RETURN)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Ending program")
        driver.quit()
