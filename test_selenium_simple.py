import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# chromedriver_directory= "P:/ChromeDriver"
# не надо, включи ссылку 
# python3 -m pytest -v --driver Chrome --driver-path P:/ChromeDriver/chromedriver.exe  test_selenium_simple.py
# driver = webdriver.Chrome()
# def test_search_example(selenium):

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   driver.maximize_window()
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   yield driver

   driver.quit()


def test_show_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys('yrikmolnenosec@mail.ru')
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys('1234')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # driver.find_element(By.PARTIAL_LINK_TEXT, 'Мои').click()
   # Проверяем, что мы оказались на главной странице пользователя
   # assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   driver.implicitly_wait(3)
   images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
   for i in range(len(names)):
      # assert images[i].get_attribute('src') != ''
      # assert names[i].text != ''
      # assert descriptions[i].text != ''
      assert ', ' in descriptions[i].text
      # parts = descriptions[i].text.split(", ")
      # assert len(parts[0]) > 0
      # assert len(parts[1]) > 0


def test_show_my_pets2(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys('yrikmolnenosec@mail.ru')
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys('1234')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   driver.find_element(By.PARTIAL_LINK_TEXT, 'Мои').click()
   # Проверяем, что мы оказались на главной странице пользователя
   # assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   # descriptions = driver.find_elements(By.TAG_NAME, 'td')
   descriptions = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
   for i in range(len(descriptions)):
      assert descriptions[i].text != ''
