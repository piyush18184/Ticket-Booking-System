class AdministrationDetails():
    list_of_admins=[];
    list_of_emails=[];
    list_of_passwords=[];
    list_of_coupons=["WOW","SUMMER","HAPPYME"];

    def __init__(self,userid,username,email,password):
        self.userid=userid
        self.username=username
        self.email=email
        self.password=password
        self.list_of_admins.append(self)
        self.list_of_emails.append(email)
        self.list_of_passwords.append(password)

    def GetUserID(self):
        return self.userid
    def GetUserName(self):
        return self.username
    def GetUserEmail(self):
        return self.email
    def GetUserPassword(self):
        return self.password

v1=AdministrationDetails(2018184,"Piyush Srivastava","piy2610@gmail.com","piyush")


