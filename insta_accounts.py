from instagrapi import Client
from time import sleep


class InstaAccounts:
    def __init__(self,login,password) -> None:
        self.login = login
        self.password = password
        
    def login_and_post(self):
        account = Client()
        
        try:
            account.login(self.login,self.password)
            sleep(5)
            user_info = account.account_info()
            print('Consegui logar na conta:',user_info.username)
            
        except Exception as e:
            print('Retire a dupla verificação!')
            

        


            
if __name__ =='__main__':
    login = InstaAccounts('username','password!')
    login.login_and_post()