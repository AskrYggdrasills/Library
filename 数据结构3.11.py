# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class SequenceList:       #定义顺序表self.SeqList，并初始化
    def __init__(self):
        self.SeqList=[]
        
    def CreateSequenceList(self):    #创建顺序表
        e=input("请输入 一个元素")
        while e!="#":
            self.SeqList.append(int(e))
            e=input("请输入 一个元素")
            
    def printf(self):#输出顺序表
        print("该顺序表的所有元素为：")
        '''
        for i in range(len(self.SeqList)):
            print(self.SeqList[i],end=" ") 
        通过列表长度输出
        '''
        for e in self.SeqList:
            print(e,end=" ")    #列表内循环输出
    def nums(self):
        print("当前列表内元素为：")
        for i in self.SeqList:
            print(i,end=" ")
    def find(self):#输入要查找元素的元素e，输出e的位置。若e不存在，则输出false
        e=int(input("请输入要查找的值："))
        for j in range(len(self.SeqList)):
            if self.SeqList[j] == e:
                print("该元素在第%d位"%(j+1))
            elif j == len(self.SeqList)-1 and self.SeqList[j] != e:
                print("false")
    def delect1(self):#输入一个数据并删除
        x=int(input("请输入要删除的数据："))
        if x in self.SeqList:
            self.SeqList.remove(x) 
        else:
            print("False")
        list1.nums()
        
    def delect2(self):  #输入位置，删除该位置数据
        i=int(input("请输入一个位置（位置从0开始）："))
        if i < 0 or i >=len(self.SeqList): #判断位置的值
            print("TypeError")
        else:
            for j in range(i,len(self.SeqList)-1):
                self.SeqList[j]=self.SeqList[j+1]
            del self.SeqList[len(self.SeqList)-1]
        list1.nums()
    
    def Insert(self): #插入数据 insert语句
        i=int(input("请输入要插入的位置（位置从0开始）："))
        x=int(input("请输入要插入的值："))
        """
        if i < 0 or i >=len(self.SeqList): #判断位置的值
            print("TypeError")
        else:
            self.SeqList.append(0)
            for j in range(len(self.SeqList)-1,i,-1):
                self.SeqList[j]=self.SeqList[j-1]
            self.SeqList[i]=x
            list1.nums()
        """
        if i < 0: #判断位置的值
            print("TypeError")
        else:
            self.SeqList.insert(i,x)
        list1.nums()

        
list1=SequenceList()     
list1.CreateSequenceList()
list1.printf()
#list1.find()
#list1.Insert()
#list1.delect2()
list1.Insert()
#list1.delect1()