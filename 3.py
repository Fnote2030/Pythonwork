################# 8-12 #################
def showinfo(*batching):
    print("你的三明治添加的食材有>>")
    print("    ",end="")
    for bch in batching:
        print(bch,end="-")
    print()

showinfo("火腿","奶酪","面包屑","鸡蛋")
showinfo("火腿","花生","奶酪","面包屑","鸡蛋")
showinfo("火腿","苹果","蔬菜","奶酪","面包屑","鸡蛋")
print("-"*60)


################# 8-14 #################
def make_car(*manufacturer_model, **information):
    info = {}
    info["manufacturer"] = manufacturer_model[0]
    info["model"] = manufacturer_model[1]
    for key in information.keys():
        info[key] = information[key]
    return info

car = make_car("subaru","outback",color="blue",tow_package=True)
print(car)
