ID = input("请输入身份证号(仅限河南):")
city = {"4101":"郑州市","4103":"洛阳市","4105":"安阳市","4107":"新乡市","4110":"许昌市","4112":"三门峡市","4114":"商丘市","4116":"周口市","4102":"开封市","4104":"平顶山市","4106":"鹤壁市","4108":"焦作市","4109":"濮阳市","4111":"漯河市","4113":"南阳市","4115":"信阳市","4117":"驻马店市"}
gender = {"1":"男","3":"男","5":"男","7":"男","9":"男","0":"女","2":"女","4":"女","6":"女","8":"女"}

print("省份: 河南省",city[ID[0:4]])
print("生日: %s年%s月%s日" %(ID[6:10], ID[10:12], ID[12:14]))
print("性别:",gender[ID[-2]])

