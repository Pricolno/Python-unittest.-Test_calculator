import unittest
from simple_calculator import Calculator
from random import randint
from time import clock

INF = 1e20
eps = 1e-20
cnt = 0

class TestCalculator(unittest.TestCase):
    def setUp(self):
        global cnt
        cnt +=1
        print('Test',cnt,': ', clock())
        self.calculator = Calculator(randint(-1000, 1000))


    def test_add(self):
        self.assertEqual(self.calculator.value + 6, self.calculator.add(1, 2, 3).value)
        self.assertEqual(self.calculator.value + 3 * INF, self.calculator.add(INF, INF, INF).value) # maxTest
        self.assertRaises(TypeError, self.calculator.add, 'asda')          # typeErorTest
        self.assertRaises(TypeError, self.calculator.add, '1212 1212')          # typeErorWithNumberInStringTest
        self.assertEqual(self.calculator.value - 500, self.calculator.add(-500).value) # negativeTest
        self.assertEqual(self.calculator.value + eps + eps, self.calculator.add(eps, eps).value) # minTest


    def test_multiply(self):
        self.assertEqual(self.calculator.value * 900, self.calculator.multiply(5, 2, 90).value)
        self.assertEqual(self.calculator.value * INF * INF, self.calculator.multiply(INF, INF).value) # maxTest
        self.assertEqual(self.calculator.value * 0 * 5, self.calculator.multiply(0, 5).value) # zeroTest
        self.assertEqual(self.calculator.value * -500, self.calculator.multiply(-500).value) # negativeTest
        self.assertRaises(TypeError, self.calculator.multiply, 'asda')  # typeErorTest
        self.assertRaises(TypeError, self.calculator.multiply, '1212 1212')  # typeErorWithNumberInStringTest
        self.assertEqual(self.calculator.value * -500 * -500, self.calculator.multiply(-500, -500).value)  # negativeAndNegativeTest
        self.assertEqual(self.calculator.value * eps * eps, self.calculator.multiply(eps, eps).value)  # minTest


    def test_divide(self):
        self.assertAlmostEqual( self.calculator.value/9, self.calculator.divide(3, 3).value)
        self.assertAlmostEqual(self.calculator.value/INF /INF, self.calculator.divide(INF, INF).value) #maxTest
        self.assertAlmostEqual(self.calculator.value/eps /eps, self.calculator.divide(eps, eps).value) #minTest
        self.assertAlmostEqual(self.calculator.value/-5/ 100, self.calculator.divide(-5, 100).value) #negativeTest
        self.assertRaises(TypeError, self.calculator.divide, 'asda')  # typeErorTest
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 0)  # typeErorTest
        self.assertRaises(TypeError, self.calculator.divide, '1212 1212')  # typeErorWithNumberInStringTest


    def test_power(self):
        if self.calculator.value > 0:
            self.assertAlmostEqual(self.calculator.value ** 0, self.calculator.power(0).value)    # zeroTest
            self.assertAlmostEqual(self.calculator.value ** 2, self.calculator.power(2).value)
            self.assertAlmostEqual(self.calculator.value ** 5, self.calculator.power(5).value)
            self.assertAlmostEqual(self.calculator.value ** 200, self.calculator.power(200).value)  # maxTest
            self.assertAlmostEqual(self.calculator.value ** -200, self.calculator.power(-200).value)  # maxTest
        self.assertRaises(TypeError, self.calculator.power, 'asda')  # typeErorTest
        self.assertRaises(TypeError, self.calculator.power, '1212 1212')  # typeErorWithNumberInStringTest
        self.calculator.value = -200
        self.assertAlmostEqual(self.calculator.value, self.calculator.power(10).value)  # baseNegativeTest return vales_last , becouse pow(10) is not exist


    def test_root(self):
        print(self.calculator.value)
        if self.calculator.value > 0:
            self.assertAlmostEqual(self.calculator.value ** (1/2), self.calculator.root(2).value)
            self.assertAlmostEqual(self.calculator.value, self.calculator.root(0).value) #  zeroTest, return vales_last , becouse root(0) is not exist
            self.assertAlmostEqual(self.calculator.value ** (1/5), self.calculator.root(5).value)
            self.assertAlmostEqual(self.calculator.value ** (1/200), self.calculator.root(200).value)  # maxTest
        self.assertRaises(TypeError, self.calculator.root, 'asda')  # typeErorTest
        self.assertRaises(TypeError, self.calculator.root, '1212 1212')  # typeErorWithNumberInStringTest
        self.calculator.value = -200
        self.assertAlmostEqual(self.calculator.value, self.calculator.root(10).value) # baseNegativeTest return vales_last , becouse root(10) is not exist

    def test_subtract(self):
        self.assertAlmostEqual(self.calculator.value - 6, self.calculator.subtract(1, 2, 3).value)
        self.assertAlmostEqual(self.calculator.value - 3 * INF, self.calculator.subtract(INF, INF, INF).value)  # maxTest
        self.assertRaises(TypeError, self.calculator.subtract, 'asda')  # typeErorTest
        self.assertRaises(TypeError, self.calculator.subtract, '1212 1212')  # typeErorWithNumberInStringTest
        self.assertAlmostEqual(self.calculator.value + 500, self.calculator.subtract(-500).value)  # negativeTest
        self.assertAlmostEqual(self.calculator.value - eps - eps, self.calculator.subtract(eps, eps).value)  # minTest



if __name__ == '__main__':
    # time_start = clock()
    #print('klk;llk')
    unittest.main(exit=False)  # Не работает, почему то всёравно обрывает программу, но без __main__ всё работает, я не понимаю почему так
    # time_finish = clock()
    # print('ggg')
    # print('\nВремя начала: ', time_start)
    # print('Время конца: ', time_finish)





