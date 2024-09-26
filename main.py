from insta_accounts_api import InstaAccountsAPI
from insta_accounts_selenium import InstaAccountSelenium


if __name__ == '__main__':
    try:
        account_api = InstaAccountsAPI('login','password')
        account_api.login_and_post()
    except:
        account_selenium = InstaAccountSelenium('login','password')
        account_selenium.login()
        account_selenium.wait_verification_upload()
        account_selenium.upload_image(r"D:\teste_automacao.png")
        account_selenium.image_data('Isto é um teste! Por favor, não interaja!')
        account_selenium.share()
        
        
        