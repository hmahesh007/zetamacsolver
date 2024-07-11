import time


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://arithmetic.zetamac.com/game?key=a7220a92")


while True:
    #print(question_element)
    question_element = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/span")
    question_element = question_element.text
    if " ÷ " in question_element:
        x2 = question_element.replace(" ÷ ","/")
    question_element = question_element
    if " – " in question_element:
        x2 = question_element.replace(" – ", "-")
    question_element = question_element
    if "×" in question_element:
        x2 = question_element.replace(" × ", " * ")
    if "+" in question_element:
        x2 = question_element.replace(" + ", "+")
    #print(x2)
    answer = str(int(eval(x2)))
    print(x2,answer)
    pyautogui.write(answer)
sleep(1200)
