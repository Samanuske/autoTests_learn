import time
print("Импортировано время...")
import math
import os
print("Импортирована библиотека math...")

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
try:  # команда для выполнения, в случае ошибки будет выполнено то что в финале finally
  # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
  driver = webdriver.Chrome()

  # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
  #time.sleep(5)

  # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
  driver.get("http://suninjuly.github.io/file_input.html")
  #time.sleep(5)

  # Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
  # Ищем поле для ввода текста
  #textarea = driver.find_element_by_css_selector(".textarea")
  #time.sleep(5)


  
  
# Напишем текст ответа в найденное поле
  print("Ищем поле для ввода Имя...")
  textarea = driver.find_element(By.NAME, "firstname")
  print("Кладем в поле для ввода Alex...")
  textarea.send_keys('Alex')

  print("Ищем поле для ввода Фамилия...")
  textarea = driver.find_element(By.NAME, "lastname")
  print("Кладем в поле для ввода Kirk...")
  textarea.send_keys('Kirk')

  print("Ищем поле для ввода Почты...")
  textarea = driver.find_element(By.NAME, "email")
  print("Кладем в поле для ввода alex.K@mail.ru...")
  textarea.send_keys('alex.K@mail.ru')

#грузим файл
  print('Ищем кнопку загрузки файл....')
  element = driver.find_element(By.ID, 'file')
  current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
  file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
  print('Грузим файл....')
  element.send_keys(file_path)
  print('Файл загружен!!!')

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
