from instagrapi import Client
from time import sleep


class InstaAccountsAPI:
    def __init__(self,login,password) -> None:
        self.login = login
        self.password = password
        self.account = Client()
        
    def login_and_post(self,msg):
        print('Estou tentando logar sem a dupla verificação!...')
        self.account.login(self.login,self.password)
        sleep(2)
        print('Consegui logar na conta...')
        
        self.account.photo_upload(r"D:\Download\testefotoreal.jpeg",msg)
        print('Imagem postada com sucesso!')
        

        
        
            

        


            
if __name__ =='__main__':
    login = InstaAccountsAPI('name','password')
    login.login_and_post('Isto é um teste, por favor não interaja!')
