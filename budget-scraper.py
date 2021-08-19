
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Bank of America accounts
def boaselenium():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.bankofamerica.com/")

    username = browser.find_element_by_name("onlineId1").send_keys(<YOUR USERNAME>)
    time.sleep(2)
    password = browser.find_element_by_name("passcode1")
    password.send_keys(<YOUR PASSWORD>)
    password.send_keys(Keys.RETURN)

    # first credit card
    browser.find_element_by_link_text('Customized Cash Rewards Visa Signature - ****').click()
    boa_rewards_html = browser.page_source

    browser.back()

    # attached Bofa checking account
    browser.find_element_by_link_text('Adv Plus Banking - ****').click()
    boa_checking_html = browser.page_source
    
    return (boa_checking_html)

 # Chase accounts 
 def chaseselenium():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.chase.com/")

    username = browser.find_element_by_name("UserID").send_keys(<YOUR USERNAME>)
    time.sleep(2)
    password = browser.find_element_by_name("password")
    password.send_keys(<YOUR PASSWORD>)
    password.send_keys(Keys.RETURN)

    # first chase card
    browser.find_element_by_link_text('Sapphire - ****').click()
    chase_sapphire_html = browser.page_source

    browser.back()

    # second chase card
    browser.find_element_by_link_text('Freedom - ****').click()
    chase_freedom_html = browser.page_source
    
    return (chase_freedom_html)