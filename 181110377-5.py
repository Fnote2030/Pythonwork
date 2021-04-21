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
        return eval(formula) #��������ļ��㹫ʽ
    return (shape, cal_areas)

def formula(formulas_filename):
    with open(formulas_filename, encoding='utf-8') as formulas_file:
        for line in formulas_file: 
            shape ,formula = line.split(None,2)
            yield square_fun(shape,formula)#�պ������� ������״�����Ӧ��������㹫ʽ

def cal_area(shape, *args, rules_filename='areas.txt'): 
    for shape_tx, cal_areas in formula(rules_filename):
        if shape_tx == shape:
            return cal_areas(*args) #���㹫ʽ��������ó������С

print(cal_area('circular',4))#Բ
print(cal_area('triangle',4,4))#������
print(cal_area('rectangle',4,4))#����