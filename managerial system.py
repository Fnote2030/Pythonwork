print(">>>>> 欢迎来到学生学籍管理系统 <<<<<")
print("")
print("    (输入'help'显示所有命令信息)")
print("")

#存储学生信息的列表
infolist = []

#载入学生的信息
def loadlist():
    flag = 1
    try:
        f =open('contact.dat')
        f.close()
    except FileNotFoundError:
        print(">>>>>> 没有储存学生信息的文件 <<<<<<")
        print("")
        flag = 0
    except PermissionError:
        print("你没有权限访问该文件！")
    if flag:
        file = open('contact.dat','r+')
        file.seek(0)
        name = file.readline().replace("\n","")
        while name:
            number = file.readline().replace("\n","")
            classes = file.readline().replace("\n","")
            sex = file.readline().replace("\n","")
            infolist.append({"name":name,"number":number,"class":classes,"sex":sex})
            name = file.readline().replace("\n","")
        file.close()
        print(">>>>>>>>> 载入学生信息成功 <<<<<<<<<")
        print("")
        

#同步学生的信息到本地
def savelist():
    file = open('contact.dat','w+')   
    file.seek(0)
    for i in range(0,len(infolist),1):
        file.write(infolist[i]["name"]+"\n")
        file.write(infolist[i]["number"]+"\n")
        file.write(infolist[i]["class"]+"\n")
        file.write(infolist[i]["sex"]+"\n")
    file.close()
    print("\n>> 学生学籍信息成功保存到本地文件 <<\n")


#分析输入字符串的类型  返回值：0 #混合（不符合格式） 1  #纯数字  2 #纯非数字
def inputtype(put):
    flag = 1
    if put.isdigit():
        return 1  #纯数字
    else:
        for i in range(0,len(put),1):
            if put[i].isdigit():
                flag = 0
                break
        if flag:
            return 2 #纯非数字
        else:
            return 0 #混合


#返回实际的格式长度   
#len(string.encode('GBK'))字符串的长度(一个中文字符长度算2)
#len(string)              字符串的长度(每个字符长度都是1)
#多一个中文字符，实际格式化输出长度减一
def pad_len(string, length):
    #想要设置的长度 - 中文字符数量
    return length - ( len(string.encode('GBK')) - len(string) )


#打印列表中队列下标为i的记录
def print_info(i,sel):
    if sel:
        print("%-6d" % (i+1),end="")
    print("{0:<{len0}}{1:<14}{2:<12}{3:<4}".format(infolist[i]["name"],infolist[i]["number"],infolist[i]["class"],infolist[i]["sex"],len0=pad_len(infolist[i]["name"],12)))


#打印查询到的记录集合的所有信息  返回记录大小
def print2_info(goallist):
    if not goallist:
        print("没有查询到！")
        return 0
    print("序号  姓名        学号          班级        性别")
    i = 0
    for i in range(0,len(goallist),1):
        print("%-6d" % (i+1),end="")
        print_info(goallist[i],0) #打印查询到的记录
    return i+1 #返回记录的的大小


#返回指定关键字的列表下表集合，str为关键字，sel==1关键字为名字，sel==2关键字为学号
def getlist(str1,sel):
    goallist = []
    if sel == 1:  #根据姓名查找
        for i in range(0,len(infolist),1):
            if infolist[i]["name"] == str1:
                goallist.append(i)
    if sel == 2:  #根据学号查找
        for i in range(0,len(infolist),1):
            if infolist[i]["number"] == str1:
                goallist.append(i)
                break   #学号没有重复的
    return goallist


#输入一条合法的记录，然后返回  sel == 1 添加  sel == 2 更改
def addlist(i,sel):     
    #1、输入合法的名字
    name = "" 
    while 1:
        name = input("请输入学生的姓名：") 
        if sel == 2:
            break  #不用检查名字是否存在
        #名字不能出现数字
        if not inputtype(name) == 2:
            print("名字带有数字！")
            continue
        goallist = getlist(name,1)  #查找
        #有相同的名字
        if goallist:  
            print("输入的姓名已经存在！")
            print2_info(goallist) #打印
            #获得正确的命令
            s = ""
            while 1:
                s = input("要继续以该名字存储吗？(yes/no)：")
                if s == "y" or s == "n" or s == "yes" or s == "no":
                    break
                else:
                    print("命令输入错误！")
            #是否重新输入（姓名可以重复）
            if "n" == s or "no" == s:
                continue  #重新输入姓名
        break

    #2、输入合法的学号
    number = ""
    while 1:
        number = input("请输入学生的学号：")
        #（1）、不全都是数字
        if not number.isdigit():
            print("不全都是数字！")
            continue
        #（2）、学号重复i
        goallist = getlist(number,2)
        if goallist:
            if sel == 2 and i in goallist:
                break  #修改的学号是原来的不算重复
            print("输入的学号已经存在！")
            continue
        break

    #3、输入合法的班级
    classes = "" 
    while 1:
        classes = input("请输入学生的班级：")
        #不是全是数字
        if not classes.isdigit():
            print("不全是数字！")
            continue
        break

    #4、输入合法的性别
    sex = ""
    while 1:
        sex = input("请输入学生的性别：")
        #非男女的标记
        if not (sex == "男" or sex == "女"):
            print("输入非‘男’或者‘女’！")
            continue
        break
    
    info = {"name":name,"number":number,"class":classes,"sex":sex}
    return info



#操作列表的某个元素  1 - 删除  2 - 修改
def handlelist(i,sel): 
    shows = ["删除","修改"]
    show = shows[sel-1]
    info = {}   #存储新的记录的字典
    #修改
    if sel == 2:
        info = addlist(i,2)  #2修改，1添加 在位置i
    s = ""
    #获得正确的命令
    while 1:
        s = input(f"确定{show}吗？(yes/no)：")   
        if s == "y" or s == "n" or s == "yes" or s == "no":
            break
        else:
            print("命令输入错误！")
    #是否执行
    if "n" == s or "no" == s:
        print(f"取消{show}！")
    else:
        if sel == 1:
            infolist.remove(infolist[i])
        if sel == 2: #修改
            infolist[i]["name"] = info["name"] 
            infolist[i]["number"] = info["number"] 
            infolist[i]["class"] = info["class"] 
            infolist[i]["sex"] = info["sex"] 
        print(f"{show}成功！")


#根据什么查询到要修改的记录 返回1 名字查询  返回 2 学号查询
def getsel1_2(str1):
    while 1:
        print(f">>> 1.根据姓名{str1} 2.根据学号{str1} <<<")
        sel = (input("请选择（1/2）："))
        if sel.isdigit():
            sel = int(sel)
        else:
            print("输入非数字！")
            continue
        if not (sel == 1 or sel == 2):
            print("输入错误！")
            continue
        else:
            return sel        


#载入学生信息
loadlist()

while 1:
    command = input("输入命令:")
    ###################### 添加信息 ######################
    if command == "add":
    #存进列表
        info = addlist(1,0)
        infolist.append(info)
        print("学生学籍信息添加成功！")
        continue


    ###################### 删除信息 ######################
    elif command == "remove":
        #1、判断列表是否为空
        if not infolist:
            print("列表为空！")
            continue
        #2、删除信息,根据什么删除记录
        put = input("请输入学号或者姓名：")
        puttype  = inputtype(put)
        
        if not puttype:
            print("输入格式错误！")

        elif puttype == 1:  #根据学号
            goallist = getlist(put,2) #返回下标列表 没有重复的所以只有一个元素
            #有该记录
            if goallist:
                #打印
                print2_info(goallist)
                #删除记录
                handlelist(goallist[0],1)
            #没有该记录
            else:
                print("没有该学号的记录！")

        else:  #根据姓名
            goallist = getlist(put,1)  #返回该学生名字的记录下标
            #存在
            if goallist:
                i = print2_info(goallist) #打印 & 返回记录的大小
                ml = 0
                while 1:
                    ml = input("请输入要删除的序号：")
                    #获得数字序列
                    if ml.isdigit():
                        ml = int(ml)
                    else:
                        print("输入非数字！")
                        continue
                    #是否是存在的序号
                    if ml < (i+1) and ml > 0:
                        break
                    else:
                        print("输入的序号不存在！")
                ml -= 1
                #删除下标为goallist[ml]的记录
                handlelist(goallist[ml],1)
            #不存在
            else:
                print("没有该姓名的记录！")
        continue


    ###################### 查找信息 ######################
    elif command == "find":
        #1、判断列表是否为空
        if not infolist:
            print("列表为空！")
            continue
        #2.根据什么查找
        put = input("请输入学号或者姓名：")
        puttype  = inputtype(put)

        if not puttype:
            print("输入格式错误！")

        elif puttype == 1:
            #根据学号查找
            goallist = getlist(put,2) #查找
            print2_info(goallist)

        else:
            #根据姓名查找
            goallist = getlist(put,1) #查找
            print2_info(goallist)
        continue


    ###################### 修改信息 ######################
    elif command == "modify":
        #1、判断列表是否为空
        if not infolist:
            print("列表为空！")
            continue
        #2.修改信息,根据什么查询到要修改的记录
        put = input("请输入学号或者姓名：")
        puttype  = inputtype(put)   #什么类型的输入

        if not puttype:
            print("输入格式错误！")

        elif puttype == 1:  #根据学号
            goallist = getlist(put,2) #返回下标列表 没有重复的所以只有一个元素
            #有该记录
            if goallist:
                #打印
                print2_info(goallist)
                #修改记录
                handlelist(goallist[0],2)
            #没有该记录
            else:
                print("没有该学号的记录！")    

        else:   #根据姓名
            goallist = getlist(put,1)  #返回该学生名字的记录下标列表
            #存在
            if goallist:
                i = print2_info(goallist) #打印 返回记录的大小
                ml = 0
                while 1:
                    ml = input("请输入要修改的序号：")
                    #获得数字序列
                    if ml.isdigit():
                        ml = int(ml)
                    else:
                        print("输入非数字！")
                        continue
                    #序号是否存在
                    if ml < (i+1) and ml > 0:
                        break
                    else:
                        print("输入的序号不存在！")
                ml -= 1
                #修改下标为goallist[ml]的记录
                handlelist(goallist[ml],2)
            #不存在
            else:
                print("没有该姓名的记录！")
        continue


    ###################### 展示所有信息 ######################
    elif command == "show all":
        #1、列表是否为空
        if not infolist:
            print("列表为空！")
            continue
        #2、输出信息
        print(">>>>>>>>>>>>>>>> 所有学生的信息 <<<<<<<<<<<<<<<<")
        print("序号  姓名        学号          班级        性别")
        for i in range(0,len(infolist),1): 
            print_info(i,1) #打印
        continue


    ###################### 输出命令信息 ######################
    elif command == "help":
        print("quit     退出程序")
        print("add      添加学生的学籍信息")
        print("remove   删除学生的学籍信息")
        print("find     查找学生的学籍信息")
        print("modify   修改学生的学籍信息")
        print("save     保存学生的学籍信息到本地")
        print("show all 展示所有学生的学籍信息")
        continue


    ###################### 退出程序 ######################
    elif command == "quit":
        savelist()
        print("<<<<<<<<<<<<  退出程序  >>>>>>>>>>>>\n")
        break


    ###################### 保存信息 ######################
    elif command == "save":
        savelist()
        continue
    else:
        print("没有此命令！")

