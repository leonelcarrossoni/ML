from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.message = "Teste de Bot https://www.youtube.com/watch?v=fL308_-Kbt0"
        self.groups = ["Leonel","Igreja Universal"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def SendMessage(self):
        #<span dir="auto" title="Neto legal" class="_1wjpf _3NFp9 _3FXB1">Neto legal</span>
        #<span dir="auto" title="Amigos" class="_1wjpf _3NFp9 _3FXB1">Amigos</span>
        #<div tabindex="-1" class="_1Plpp">
        #<span data-icon="send" class="">
        #<span dir="auto" title="Igreja Universal" class="_1wjpf _3NFp9 _3FXB1">Igreja Universal</span>
        print('Teste')
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for group in self.groups:
            group = self.driver.find_element_by_xpath(f"//span[@title='{group}']")
            time.sleep(3)
            group.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)
            send_buttom = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            time.sleep(3)
            send_buttom.click()
            time.sleep(5)

bot = WhatsappBot()
bot.SendMessage()



