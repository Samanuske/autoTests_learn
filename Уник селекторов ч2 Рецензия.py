# тест заполнения только обязательных полей

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = driver.find_element_by_css_selector('div[class="first_block"]:nth-child(1)&gt; input')
    input1.send_keys("Ivan")
    
    input2 = driver.find_element_by_css_selector('div[class="first_block"]:nth-child(2)&gt; input')
    input2.send_keys("Taranov")

    input3 = driver.find_element_by_css_selector('div[class="first_block"]:nth-child(3)&gt; input')
    input3.send_keys("no_adress@mail.ru")
    
    

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
    print('test finish')
