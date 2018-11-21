class Admin:
    list_of_users=[];
    list_of_emails=[];
    list_of_passwords=[];

    def __init__(self,userid,username,email,password):
        self.userid=userid
        self.username=username
        self.email=email
        self.password=password
        self.list_of_users.append(self)
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

u1=Admin(2018184,"Piyush Srivastava","piyush18184@iiitd.ac.in"  ,"piyush"  )
u1=Admin(2018184,"Vivek Prakash    ","vivek18179@iiitd.ac.in"   ,"vivek"   )
u1=Admin(2018184,"Jitendra Yadav   ","jitendra18203@iiitd.ac.in","jitendra")



