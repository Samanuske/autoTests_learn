from selenium import webdriver
import time
import math

link_open = "http://suninjuly.github.io/find_link_text"
link = "http://suninjuly.github.io/simple_form_find_task.html"
a = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    print("Открываем браузер по ссылке...")
    browser.get(link_open)
    print("Брауезр успешно открыт")
    print("Ищем текстовый элемент согласно формуле")
    inpute = browser.find_element_by_link_text(a)
    print("Нажимаем на найденную ссылку ")
    inpute.click()

    #browser.get(link)

    print("Ищем строку имя...")
    input1 = browser.find_element_by_tag_name("[name='first_name']")
    print("Записываем имя в найденной строке")
    input1.send_keys("Ivan")
    print("Ищем строку фамилию...")
    input2 = browser.find_element_by_name('last_name')
    print("Записываем фамилию в найденной строке")
    input2.send_keys("Petrov")
    print("Ищем строку город...")
    input3 = browser.find_element_by_class_name('form-control.city') #заместо пробела в селекторе ставим точку - она заменится на пробел
    print("Записываем город в найденной строке")
    input3.send_keys("Smolensk")
    print("Ищем строку страна...")
    input4 = browser.find_element_by_id('country')
    print("Записываем страну в найденной строке")
    input4.send_keys("Russia")
    print("Ищем кнопку подтвердить...")
    button = browser.find_element_by_css_selector("button.btn")
    print("Нажимаем кнопку подтвердить")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
