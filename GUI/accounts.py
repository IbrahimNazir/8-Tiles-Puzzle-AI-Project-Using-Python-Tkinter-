import os.path


class Account:

    accountslist = []
    def __init__(self):
        # creates the default account
        if not os.path.exists("accountsfile.txt"):
            with open("accountsfile.txt", "a+") as accountsfile:
                accountsfile.write("ibrahimnazir72@gmail.com;xxx;Ibrahim;Nazir\n")
                accountsfile.seek(0)
        Account.accountList()

    # this will create the list of accounts created
    @staticmethod
    def accountList():
        with open("accountsfile.txt", "r+") as accountsfile:
            lines = accountsfile.readlines()
            Account.accountslist = []
            for account in lines:
                account = account.strip()
                x = account.split(";")
                Account.accountslist.append(x)

    @staticmethod
    def signUp(firstname="", lastname="", email="", password=""):
        if not Account.authenticate(email,password)["error"]:
            return {'error':True, 'response':"account already present"}

        if firstname == "" or lastname == "" or email == "" or password == "":
            return {"error": True, "response": "please fill complete details"}
        with open("accountsfile.txt", "a+") as accountsfile:
            accountsfile.write(f"{email};{password};{firstname};{lastname}\n")
            accountsfile.seek(0)
            Account.accountslist.append([email, password, firstname, lastname])
        return {"error": False, "response": "account created successfully"}


    # checks the email and password if exists

    @staticmethod
    def authenticate(email, password):
        for account in Account.accountslist:
            if account[0] == f"{email}" and account[1] == f"{password}":
                return {'error': False,"response": account}
        return {'error': True, 'response':'Account no found'}

