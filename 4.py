#coding=gbk
'''
        ## 9-3 & 9-3 ##
'''
class Login():
    def __init__(self, login_attempts=0):
        self.login_attempts = login_attempts
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    def print_login_attempts(self):
        print(self.login_attempts)

class User():
    def __init__(self, first_name, last_name,sex,age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = Login()#login_attempts����
    def describe_user(self):
        print(f"�û���������<{self.last_name.title()}{self.first_name.title()}>,�Ա�Ϊ<{self.sex}>,����<{self.age}>�ꡣ")
    def greet_user(self):
        if self.age > 18:
            if self.sex == "��" or self.sex == "male":
                print(f"{self.last_name}������ã�")
            elif self.sex == "Ů" or self.sex == "female":
                print(f"{self.last_name}Ůʿ��ã�")
        else:
            print("С������ã�")

#9-3ʵ��
u1 = User("С��", "��", "��", 20)
u1.describe_user()
u1.greet_user()
u2 = User("С��", "��", "Ů", 22)
u2.describe_user()
u2.greet_user()
u3 = User("С��", "��", "Ů", 16)
u3.describe_user()
u3.greet_user()
print("-"*50)
#9-5ʵ��
for i in range(3):
    u1.login_attempts.increment_login_attempts()
    u1.login_attempts.print_login_attempts()
u1.login_attempts.reset_login_attempts()
u1.login_attempts.print_login_attempts()


'''
        ## 9-7 ##
'''
class Admin(User):
    def __init__(self, first_name, last_name, sex, age, privileges):
        super().__init__(first_name, last_name, sex, age)
        self.privileges = privileges
    def show_privileges(self):
        print(f"�˹���Ա��Ȩ����{self.privileges}")

privileges = ["can add post","can delelte post","can ban user"]
admin1=Admin("С��", "��", "��", 20, privileges[:])
admin1.show_privileges()