ID = input("请输入身份证号(仅限河南):")

if len(ID) != 18:
    print("请输入正确的身份证号")
else:
    ID_city = ID[0]