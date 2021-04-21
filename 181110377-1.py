############# 3-4嘉宾名单 #############
namelist = ["张三","李四","王五"]
for i in range(len(namelist)):
    print(f"邀请{namelist[i]}共进晚餐")
print("")


############# 3-5修改嘉宾的名单 #############
absentname = "李四"
newname = "小明"
for i in range(len(namelist)):
    if namelist[i] == absentname:
        namelist.remove(absentname)
        break
namelist.insert(i,newname)

print(f"{absentname}无法赴约")
for i in range(len(namelist)):
    print(f"邀请{namelist[i]}共进晚餐")
print("")


############# 3-6添加嘉宾 #############
print("我找到了一个更大的餐桌")
namelist.insert(0,"熊哥")
namelist.insert(len(namelist)//2,"文森")
namelist.append("赵云")
for i in range(len(namelist)):
    print(f"邀请{namelist[i]}共进晚餐")
print("")


############# 3-7缩减名单 #############
print("因特殊原因，只能邀请两个嘉宾共进晚餐")
for i in range(len(namelist)-1,1,-1):
    name = namelist.pop()
    print(f"亲爱的{name}，实在是抱歉，因特殊原因无法邀请您共进晚餐。")
for i in range(len(namelist)):
    print(f"邀请{namelist[i]}共进晚餐")
for i in range(len(namelist)-1,-1,-1):
    del(namelist[i])
print(f"邀请共进晚餐的名单>>{namelist}")
print("")


############# 4-1比萨 #############
pisalist =["烤盘披萨","厚型披萨","薄脆型披萨"]
for i in range(len(pisalist)):
    print(pisalist[i])
for i in range(len(pisalist)):
    print(f"我喜欢{pisalist[i]}")
print("")


############# 4-11你的披萨和我的披萨 #############
friend_pizzas = pisalist[:]
pisalist.append("外带焙烤式披萨")
friend_pizzas.append("至尊水果披萨")

print("My favorite pizzas are:")
for i in range(len(pisalist)):
    print(pisalist[i])
print("My friend's favorite pizzas are:")
for i in range(len(friend_pizzas)):
    print(friend_pizzas[i])
