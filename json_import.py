import json

class JsonImport:
    def __init__(self) -> None:
        
        self.accounts = list()
        
    def add_account(self,login,password):
        account = {
            'login':login,
            'senha':password
        }
        return self.accounts.append(account)
    
    def save_json(self,filename):
        with open(filename,'w') as json_file:
            json.dump(self.accounts,json_file,indent=4)
            
if __name__ == '__main__':
    test = JsonImport()
    test.add_account('conta_1','senha_aqui')
    test.add_account('conta_4','cornin')
    print('contas adicionadas com sucesso!')
    test.save_json('contas_premiadas!')
        
        