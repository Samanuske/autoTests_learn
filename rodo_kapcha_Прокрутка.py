import time
print("Импортировано время...")
import math
print("Импортирована библиотека math...")

def calc(x):    
  return str(math.log(abs(12*math.sin(int(x)))))
    

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
try:  # команда для выполнения, в случае ошибки будет выполнено то что в финале finally
  # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
  driver = webdriver.Chrome()

  # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
  #time.sleep(5)

  # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
  driver.get("http://SunInJuly.github.io/execute_script.html")
  #time.sleep(5)

  # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
  # Ищем поле для ввода текста
  #textarea = driver.find_element_by_css_selector(".textarea")
  #time.sleep(5)


  #ищем значение Х и считаем его по фомле вызывая метод calc
  print("Ищем значение Х...")

  x_element = driver.find_element(By.ID, "input_value") #ищем элемент в котором надо узнать значение атрибута valuex для расчета в формуле
  print('1')
  x_valuex = x_element.text # берем значение атрибута valuex
  print(x_valuex)
  x = int(x_valuex) # можно было сразу использовать x без x_valuex 
  print("Считаем значение по формуле, присваиваем ее y: ")
  print(x)
  y = calc(x)
  print(y)
# Напишем текст ответа в найденное поле
  print("Ищем поле для ввода...")
  textarea = driver.find_element(By.ID, "answer")
  print("Кладем в поле для ввода вычисленное значение y...")
  textarea.send_keys(y)

#ищем элемент чекбокс и ставим флак методом клик
  print("Ищем чекбокс")
  option1 = driver.find_element(By.ID, "robotCheckbox")
  driver.execute_script("return arguments[0].scrollIntoView(true);", option1)

  print("Ставим флаг в Роботы рулят...")
  option1.click()

#ищем элемент radiobutton и ставим флак методом клик
  print("Ищем radiobutton")
  option2 = driver.find_element(By.ID, "robotsRule")
  driver.execute_script("return arguments[0].scrollIntoView(true);", option2)

  print("Ставим флаг в Роботы рулят...")
  option2.click()


#time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
  print("ищем кнопку подтверждения...")
  submit_button = driver.find_element(By.CSS_SELECTOR, 'body > div.container > form > button')
  driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
  print("нажимаем подтвердить!")
  submit_button.click()
  print("ждем 20 секунд, потом закрываем браузер!!!")
  time.sleep(20)

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:   # в случае чего браузер закрывается, если все нормально, то просто закроет браузер
# После выполнения всех действий мы не должны забыть закрыть окно браузера  
  driver.quit()
