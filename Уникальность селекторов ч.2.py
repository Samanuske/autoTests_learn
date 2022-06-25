from selenium import webdriver
import time
#Заполняем только обязательные поля
try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    print("Ищем строку имя...")
    #проверяем, что поле обязательно - есть *
    input1 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.first_class > input")
    FN_lt = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.first_class > label")
    FN = FN_lt.text
    if ("First name*" == FN):
        print("Записываем имя в найденной строке")
        input1.send_keys("Ivan")
    print("Ищем строку фамилию...")
    input2 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.second_class > input")
    SN_lt = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.second_class > label")
    SN = SN_lt.text
    if ("Last name*" == SN):
        print("Записываем фамилию в найденной строке")
        input2.send_keys("Petrov")
    print("Ищем строку электронной почты...")
    input3 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.third_class > input") #заместо пробела в селекторе ставим точку - она заменится на пробел
    EM_lt = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.third_class > label")
    EM = EM_lt.text
    if ("Email*" == EM):
        print("Записываем электронную почту в найденной строке")
        input3.send_keys("test@mail.ru")
    print("Ищем строку телефон...")
    input4 = browser.find_element_by_css_selector("body > div.container > form > div.second_block > div.form-group.first_class > input")
    PH_lt = browser.find_element_by_css_selector("body > div.container > form > div.second_block > div.form-group.first_class > label")
    PH = PH_lt.text
    if ("Phone*" == PH):
        print("Записываем телефон в найденной строке")
        input4.send_keys("+793321234677")
    print("Ищем строку адреса...")
    input5 = browser.find_element_by_css_selector("body > div.container > form > div.second_block > div.form-group.second_class > input")
    AD_lt = browser.find_element_by_css_selector("body > div.container > form > div.second_block > div.form-group.first_class > label")
    AD = AD_lt.text
    if ("Addres*" == AD):
        print("Записываем адрес в найденной строке")
        input5.send_keys("г.Москва, ул.Преездная д.47")

    # Отправляем заполненную форму
    print("Ищем кнопку подтверждения...")
    button = browser.find_element_by_css_selector("button.btn")
    print("Нажимаем кнопку подтвердить")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
