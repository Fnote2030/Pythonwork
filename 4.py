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
        self.login_attempts = Login()#login_attempts属性
    def describe_user(self):
        print(f"用户的姓名是<{self.last_name.title()}{self.first_name.title()}>,性别为<{self.sex}>,今年<{self.age}>岁。")
    def greet_user(self):
        if self.age > 18:
            if self.sex == "男" or self.sex == "male":
                print(f"{self.last_name}先生你好！")
            elif self.sex == "女" or self.sex == "female":
                print(f"{self.last_name}女士你好！")
        else:
            print("小朋友你好！")

#9-3实例
u1 = User("小明", "张", "男", 20)
u1.describe_user()
u1.greet_user()
u2 = User("小红", "李", "女", 22)
u2.describe_user()
u2.greet_user()
u3 = User("小美", "张", "女", 16)
u3.describe_user()
u3.greet_user()
print("-"*50)
#9-5实例
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
        print(f"此管理员的权限有{self.privileges}")

privileges = ["can add post","can delelte post","can ban user"]
admin1=Admin("小明", "张", "男", 20, privileges[:])
admin1.show_privileges()