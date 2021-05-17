#coding=utf-8
import re

romanNumeralMap = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                   ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                   ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
# 定义有效的正则表达式来检查罗马数字是否合格
romanNumeralPattern = r"^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"

def roman_to_num(romans): # 罗马数字转阿拉伯数字的函数
    ##非纯数字
    if isinstance(romans,int) == True or isinstance(romans,float) == True:
        raise ValueError("输入的是数字！")
    ##是小于4000的罗马数字字符串
    if not re.search(romanNumeralPattern, romans):  
        raise ValueError("输入的不是罗马数字字符串！")
        
    result = 0
    index = 0
    ##大的数字在左边
    for numeral, integer in romanNumeralMap:
        while romans[index:index+len(numeral)] == numeral: 
            result += integer
            index += len(numeral)
    return result