#coding=utf-8

import math
def square_fun(shape, formula):
    def cal_areas(*args):
        if len(args)==1 and shape=="circular":
            r=args[0]
        elif len(args)==2 and (shape=="triangle" or shape=="rectangle"):
            w=args[0]
            h=args[1]
        else:
            raise ValueError("the input is not correct!")
        return eval(formula) #运算面积的计算公式
    return (shape, cal_areas)

def formula(formulas_filename):
    with open(formulas_filename, encoding='utf-8') as formulas_file:
        for line in formulas_file: 
            shape ,formula = line.split(None,2)
            yield square_fun(shape,formula)#闭合生成器 返回形状和其对应的面积计算公式

def cal_area(shape, *args, rules_filename='areas.txt'): 
    for shape_tx, cal_areas in formula(rules_filename):
        if shape_tx == shape:
            return cal_areas(*args) #计算公式输入参数得出面积大小

print(cal_area('circular',4))#圆
print(cal_area('triangle',4,4))#三角形
print(cal_area('rectangle',4,4))#矩形