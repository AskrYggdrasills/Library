Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dic
NameError: name 'dic' is not defined
>>> dic = ["a":1,"b":2,"c":3,]
SyntaxError: invalid syntax
>>> dic = ['a':1,'b':2,'c':3,]
SyntaxError: invalid syntax
>>> dic = {'a':1,'b':2,'c':3,}

>>> dic = {'a':1,'b':2,'c':3,}
>>> dic['b']
2
>>> dic
{'a': 1, 'b': 2, 'c': 3}
>>> ID_city = {4101="郑州",4103="洛阳"}
SyntaxError: invalid syntax
>>> ID_city = {"4101"=郑州,"4103"=洛阳}
SyntaxError: invalid syntax
>>> ID_city = {"4101"="郑州"}
SyntaxError: invalid syntax
>>> ID_city = {4101:"郑州",4103:"洛阳"}
>>> ID_city
{4101: '郑州', 4103: '洛阳'}
>>> print(ID_city[4101])
郑州
>>> ID = 411023200002146037
>>> city = {4101:"郑州市",4103:"洛阳市",4105:"安阳市",4107:"新乡市",4110:"许昌市",4112:"三门峡市",4114:"商丘市",4116:"周口市",4102:"开封市",4104:"平顶山市",4106:"鹤壁市",4108:"焦作市",4109:"濮阳市",4111:"漯河市",4113:"南阳市",4115:"信阳市",4117:"驻马店市"}
>>> print(city[ID[0:4]])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(city[ID[0:4]])
TypeError: 'int' object is not subscriptable
>>> print(city['ID[0:4]]')
	  
SyntaxError: invalid syntax
>>> print(city[ID[0:4]])
	  
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(city[ID[0:4]])
TypeError: 'int' object is not subscriptable
>>> city = {'4101':"郑州市"}
