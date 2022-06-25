import time
print("Импортировано время...")
import math
print("Импортирована библиотека math...")

def calc(x):    
  return str(math.log(abs(12*math.sin(int(x)))))
    

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
#time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/math.html")
#time.sleep(5)

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
#textarea = driver.find_element_by_css_selector(".textarea")
#time.sleep(5)


#ищем значение Х и считаем его по фомле вызывая метод calc
print("Ищем значение Х...")
x_element = driver.find_element_by_css_selector("[id='input_value']")
x = x_element.text
print("Считаем значение по формуле, присваиваем ее y: ")
y = calc(x)
print(y)
# Напишем текст ответа в найденное поле
print("Ищем поле для ввода...")
textarea = driver.find_element_by_css_selector("[id='answer']")
print("Кладем в поле для ввода вычисленное значение y...")
textarea.send_keys(y)

#ищем элемент checkbox и ставим флак методом клик
print("Ищем чекбокс")
option1 = driver.find_element_by_css_selector("[id='robotCheckbox']")
print("Ставим флаг в чекбоксе...")
option1.click()

print("Ищем radiobutton")
option1 = driver.find_element_by_css_selector("[id='robotsRule']")
print("Выбираем пункт Роботы рулят...")
option1.click()

#time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
print("ищем кнопку подтверждения...")
submit_button = driver.find_element_by_css_selector("[type='submit']")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
print("нажимем подтвердить!")
submit_button.click()
print("ждем 20 секунд, потом закрываем браузер!!!")
time.sleep(20)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
