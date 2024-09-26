#import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class AccountsInstaSelenium:
    def __init__(self,name,password) -> None:
        self.name = name
        self.password = password
        self.insta = webdriver.Edge()
        
    def login(self):
        
        self.insta.get('https://www.instagram.com/accounts/login/')
        sleep(4)
        
        button_username = self.insta.find_element(By.XPATH,"//input[@aria-label='Telefone, nome de usuário ou email']")
        button_username.send_keys(self.name)
        button_username.send_keys(Keys.ENTER)
        sleep(2)
        button_password = self.insta.find_element(By.XPATH,"//input[@aria-label='Senha']")
        button_password.send_keys(self.password)
        button_password.send_keys(Keys.ENTER)
        sleep(5)
        button_join = self.insta.find_element(By.XPATH,"//div[contains(@class, 'x9f619')]")
        button_join.click()
        sleep(3)

            
        
    def wait_verification_upload(self):
        try_tentative = 0
        while True:
            try:
                button_post = self.insta.find_element(By.XPATH,"(//div[contains(@class, 'x9f619') and contains(@class, 'x3nfvp2') and contains(@class, 'xr9ek0c')])[8]")
                sleep(1)
                button_post.click()
                sleep(3)
                
                return False
            except:
                try_tentative+=1
                print('Ainda não encontrei o botão de publicar! tentativa:',try_tentative)
                sleep(2)
    
    def upload_image(self,diretory):
        while True:
            try:
                WebDriverWait(self.insta, 1).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='button' and text()='Selecionar do computador']")))
                print('Botão de enviar encontrado!')
                upload_img = self.insta.find_element(By.XPATH,"//input[@type='file']") 
                upload_img.send_keys(diretory)
                sleep(4)
                button_avance = self.insta.find_element(By.XPATH,"//div[@role='button' and @tabindex='0' and text()='Avançar']")
                button_avance.click()
                sleep(3)
                button_avance_again = self.insta.find_element(By.XPATH,"//div[@role='button' and text()='Avançar']")
                button_avance_again.click()
                sleep(5)
                return False
            except:
                print('Procurando o botão de enviar...')
                sleep(1)    
            
    def image_data(self,msg:str):
        while True:
            try:
                box_msg = self.insta.find_element(By.XPATH,"//div[@aria-placeholder='Escreva uma legenda...']")
                sleep(2)
                print('Enviando legenda da imagem!')
                box_msg.send_keys(msg)
                sleep(1)
                return False
            except:
                print('Tentando enviar a foto...')
                sleep(2)
        
        
    def share(self):
        print('Preparando para enviar a foto!')
        share_button = self.insta.find_element(By.XPATH,"//div[@role='button' and @tabindex='0' and text()='Compartilhar']")
        print('Enviando a foto!')
        sleep(2)
        share_button.click()
        sleep(10)
    
if __name__ == '__main__':
    account = AccountsInstaSelenium('username','password!')
    account.login()
    account.wait_verification_upload()
    account.upload_image(r"D:\teste_automacao.png")
    account.image_data('Isto é um teste!')
    account.share()
    