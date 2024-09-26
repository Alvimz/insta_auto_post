from instagrapi import Client
from time import sleep


class InstaAccountsAPI:
    def __init__(self,login,password) -> None:
        self.login = login
        self.password = password
        self.account = Client()
        
    def login(self):
        print('Estou tentando logar sem a dupla verificação!...')
        self.account.login(self.login,self.password)
        sleep(5)
        user_info = self.account.user_info()
        print('Consegui logar na conta:',user_info)
        
    def post(self):
        ...
    
        
            

        


            
if __name__ =='__main__':
    login = InstaAccountsAPI('username','password!')
    login.login()