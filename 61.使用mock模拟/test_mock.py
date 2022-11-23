使用mock可以模拟一个类中的方法。比如模拟requests



# from mock_.product_impl import Product
# https://docs.python.org/zh-cn/3/library/unittest.mock.html
import unittest

# clas
# @patch('mock_.product_impl.Product.get_product_status_by_id')
# def test_succuse(mock_get_product_status_by_id):
#
# # Mock方法，指定一个返回值 mock_get_product_status_by_id.
#     return_value = {"id": 1, "name": "苹果", "num": 23}
#     product = Product()
#     assert product.buy_product(1).get("status") == 0
#

import requests
# requests.exceptions.MissingSchema: Invalid URL 'http': No scheme supplied. Perhaps you meant http://http?
# 可以解决避免requests请求出错的问题
class A():
    def a(self):
        requests.get("http")
    #
from unittest.mock import patch
@patch.object(A,"a")
def test(aaa):
    input_={}
    A.a(input_)
    aaa.assert_called_with(input_)


test()


# requests.get("http")


from unittest.mock import patch
#
# foo ={}
# @patch.dict(foo,{"a":99})
# def test():
#     assert foo == {"a":99}
#
# print(test())

# 为内置函数打补丁

# @patch("__main__.ord")
# def test(mock_ord):
#     mock_ord.return_value =99
#     print(ord("c"))
# test()
# print(ord("c"))

# 使用 Mock 的常见场景：
#
#1. 模拟函数调用
#2.记录在对象上的方法调用
# 两种mock的方法
#第二种增加了mock的函数和mock文件，并在mock文件中，增加了mock的基类，后面具体的mock生效的子类继承基类后。就直接返回IE过操作后的结果。达到了mock的目的
class Test(unittest.TestCase):

    @patch.object(Mock_class, "mock_function")
    def test_(self,mock_function):
        print(inspect.currentframe().f_code.co_name)
        _input = ""
        _input.update(_function)
        mock_function(_input).side_effect = self.mock_function

    def mock_mock_function(self, req, context=None):
        return  m_mock.MockCreate()

