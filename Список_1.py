from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    element1 = browser.find_elements_by_id_name("num1")
    x = get.element1
    element2 = browser.find_elements_by_id_name("num2")
    y = get.element2
    z=x+y
   

    browser.find_element_by_id_namy("dropdown").click()
    
    browser.find_element_by_css_seletor("[value=z]").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
