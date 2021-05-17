#coding=utf-8
from f181110377 import roman_to_num
import unittest

class valueTestCase(unittest.TestCase):
    """测试罗马数字 是否正确的转换成 阿拉伯数字"""
    def setUp(self):
        self.test_romans_nums = (('IV',4),('V',5),('III',3),
                                 ('VI',6),('CCL',250),('ML',1050),
                                 ('MD',1500),('CCCLXXXIX',389),('CXXIII',123),
                                 ('XIV',14),('DCCCLXXXVIII',888),('DXCIII',5931))
    def test_roman_to_num(self):
        for test_roman_num in self.test_romans_nums:
            num = roman_to_num(test_roman_num[0]) 
            self.assertEqual(num,test_roman_num[1])

    def test_notroman(self):
        self.assertRaises(ValueError, roman_to_num,"12CMID")
        self.assertRaises(ValueError, roman_to_num, "13IDSW")
        self.assertRaises(ValueError, roman_to_num, "IIV")
        self.assertRaises(ValueError, roman_to_num, "MMMM")

    def test_isnum(self):
        self.assertRaises(ValueError, roman_to_num, 1234)
        self.assertRaises(ValueError, roman_to_num, 34.89)

unittest.main()

