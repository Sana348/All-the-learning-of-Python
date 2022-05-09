#!/usr/bin/env python
# coding: utf-8

# In[1]:


student = 'Sam'


# In[ ]:





# In[2]:


student


# In[3]:


student = 'matt'


# In[4]:


student


# In[5]:


student = 'bob'


# In[6]:


student


# In[7]:


a1 = 10
a1


# In[8]:


type(a1)


# In[9]:


a1 = 3.14
a1


# 

# 

# In[10]:


type(a1)


# 

# In[11]:


a1 = True
a1


# In[12]:


type(a1)


# In[13]:


a1 = 'hello world'
a1


# In[14]:


type(a1)


# In[15]:


a1 = 3+4j
a1


# In[16]:


type(a1)


# In[17]:


#airthmetic operators


# In[18]:


a=10
b=20


# In[19]:


a,b


# In[20]:


a+b


# In[21]:


a-b


# In[22]:


a*b


# In[23]:


a/b


# In[24]:


#Relational operators 


# In[25]:


#<,>,==,!=


# In[26]:


a=50
b=100


# In[27]:


a>b


# In[28]:


a<b


# In[29]:


a==b


# In[30]:


a!=b


# In[31]:


#Logical operators & |


# In[32]:


a= True
b= False


# In[33]:


b & b


# In[34]:


a | b


# In[35]:


b | a


# In[36]:


a | a


# In[37]:


b | b


# In[38]:


#keywords, identifiers, literal, operators


# In[39]:


2+2


# In[40]:


print("hello world")


# In[41]:


a = "hello world"


# In[42]:


a


# In[43]:


a = 3.14


# In[44]:


a


# In[45]:


str1 = 'this is my first string'


# In[46]:


str1


# In[47]:


str2 = "this is my second string"


# In[48]:


str2


# In[49]:


str3 = '''this is string 
has lots of
lines in it'''


# In[50]:


str3


# In[51]:


my_string = "This is sparta"


# In[52]:


my_string


# In[53]:


my_string[0]


# In[54]:


my_string[5:11]


# In[55]:


my_string = 'this is sparta'
my_string 


# In[56]:


len(my_string)


# In[57]:


my_string.lower()


# In[58]:


my_string.upper()


# In[59]:


my_string.replace('s','a')


# In[60]:


str_new = 'sparta sparta 300 300 300 300 s'
str_new

str_new.count('sparta')
# In[61]:


str_new.count('sparta')


# In[62]:


str_new.count('300')


# In[63]:


str_new.count('s')


# In[64]:


my_string = 'Hello world is awesome '


# In[65]:


my_string.find('i')


# In[66]:


str_final = 'President Oabama is the best president of united state '


# In[67]:


str_final.split('e')


# In[68]:


tup1 = (1,True,3.14,5+7j)


# In[69]:


tup1


# In[70]:


type (tup1)


# In[71]:


tup1 [0]


# In[72]:


tup1[-1]


# In[73]:


tup1[0:2]


# In[ ]:





# In[74]:


tup1 =(1,2,3)
tup2 =(4,5,6)


# tup1,tup2

# In[75]:


tup1,tup2


# In[76]:


tup1 + tup2


# In[77]:


tup2 + tup1


# In[78]:


tup1*5 + tup2


# In[79]:


tup1 =(10,20,30,40,50,60)


# In[80]:


min(tup1)


# In[81]:


max (tup1)


# In[82]:


l1 =[1,'sparta',3.14,True]


# In[83]:


l1


# In[84]:


type(l1)


# In[85]:


l1[1]


# In[86]:


l1[2:5]


# In[ ]:





# In[87]:


l1


# In[88]:


l1[0]=100


# In[89]:


l1


# In[90]:


l1.append(-87.99)
l1


# In[91]:


l1.pop()


# In[92]:


l1


# In[93]:


l1 = [432,12,90,21,True,False]


# In[94]:


l1


# In[95]:


l1.reverse()


# In[96]:


l1


# In[97]:


l1.insert(3,"hello")


# l1

# In[98]:


l1


# In[99]:


l1 = ['a','f','f','d','b','z']


# 

# In[100]:


l1.sort()


# In[101]:


l1


# In[102]:


l2 = ['apple','mango','banana']


# In[103]:


l1 + l2


# In[104]:


l2 *5


# In[105]:


d1 = {'apple':50, 'mango':100, 'guava':200, 'banana':500}


# In[106]:


d1


# In[107]:


type(d1)


# In[108]:


d1.keys()


# In[109]:


d1.values()


# In[110]:


d1['orange'] = 5
d1


# In[111]:


d1['banana'] = 1
d1


# In[112]:


d1


# In[113]:


d2 = {'watermelon':1000, 'grapes':50, 'muskmelon' :850}


# In[114]:


d2


# In[115]:


d1.update(d2)


# In[116]:


d1


# In[117]:


d1.pop('banana')


# In[118]:


d1


# In[119]:


s1 = {1, 3.14 , 'sparta'}


# In[120]:


s1


# In[121]:


s1.add(False)
s1


# In[122]:


s1.update(['hello', 76548, 5+7j])
s1


# In[123]:


s1.remove('hello')


# In[124]:


s1


# In[125]:


s1 ={1,2,3,4,5,6}
s2 ={7,8,9,10}


# In[126]:


s1.union(s2)


# In[127]:


s3 = {5,6,7,8,,9}
s1.intersection(s3)


# In[128]:


a=10


# In[129]:


b=20


# In[130]:


if a>b:
    print('b is greater than A')


# In[131]:


if a>b:
    print('A is greater than B')
else:
    print('B is greater than A')


# In[132]:


a=10
b=20 
c=30


# In[133]:


if (a>b) & (a>c):
    print ('A is the greatest')
elif (b>a) & (b>c):
    print('B is the greatest')
else:
    print('C is the greatest')


# In[134]:


#if with tuple 


# In[135]:


tup1 = ('a','b','c')


# In[136]:


if 'z' in tup1:
      print('value a is present in tup1')
else:
      print('value z is not present in tup1')


# In[137]:


#if with list 


# In[138]:


l1 =['a','b','c']


# In[139]:


if l1[1]=='b':
    l1[1]='z'


# In[140]:


l1


# In[141]:


#if with dict


# In[142]:


d1 ={'k1':10, 'k2':20, 'k3':30}


# In[143]:


d1


# In[144]:


if d1['k3']==30:
    d1['k3']=d1['k3']+100


# In[145]:


d1


# In[146]:


i=1
while i<=10:
    print(i)
    i=i+1


# In[147]:


i=1
n=2
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1


# In[148]:


#while with list


# In[149]:


l1 =[1,2,3,4,5,]


# In[150]:


i=0


# In[151]:


while i<len(l1):
    l1[i]=l1[i]=100
    i=i+1


# In[152]:


l1


# In[153]:


l1 =['mango','apple','grapes','orange']


# In[154]:


for i in l1:
    print(i)


# In[155]:


def hello():
    print('hello world')


# In[156]:


hello()


# In[157]:


def add_10(x):
    return x+10


# In[158]:


add_10(9)


# In[159]:


add_10(9)


# In[160]:


def odd_even(x):
    if x%2==0:
        print(x,'is even')
    else:
        print(x,'is odd')
    


# In[161]:


odd_even(5)


# In[162]:


odd_even(10)


# In[163]:


g=lambda x: x*x*x


# In[164]:


g(3)


# In[165]:


#lambda with filter


# In[166]:


l1 =[1,2,3,4,5,6,7,8,9,10]
final_list=list(filter(lambda x:(x%2!=0),l1))


# In[167]:


final_list


# In[168]:


#lambda with map


# In[169]:


l1=[1,2,3,4,5,6,7,8,9,10]


# In[170]:


list_final_new=list(map(lambda x: x*2,l1))


# In[171]:


list_final_new


# In[172]:


from functools import reduce


# In[173]:


sum=reduce(lambda x,y: x+y,l1)


# In[174]:


sum


# In[175]:


class phone:
    def make_call(self):
        print ('i am making call')
    def play_game(self):
        print('i am playing game')


# In[176]:


p1 = phone()


# In[177]:


p1.make_call()


# In[178]:


p1.play_game()


# In[179]:


class phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print('make call')
    def play_game(self):
        print('play game')


# In[180]:


p2 = phone()


# In[181]:


p2.set_color('blue')


# In[182]:


p2.set_cost(5000)


# In[183]:


p2.show_color()


# In[184]:


p2.show_cost()


# In[185]:


p2.play_game()


# In[186]:


class employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def show_employee_details(self):
        print('name of employee is',self.name)
        print('age of employee is',self.age)
        print('salary of employee is',self.salary)
        print('gender of employee is',self.gender)


# In[187]:


e1 = employee('sana',20,10000000,'female')


# In[188]:


e1.show_employee_details()


# In[189]:


class vehicle:
    def __init__(self,milege,cost):
        self.milege = milege
        self.cost = cost
        
        
    def show_vehicle_details(self):
        print ('milege of vehicle is',self.milege)
        print ('cost of vehicle is',self.cost)
        print ('i am a vehicle')


# In[190]:


v1 = vehicle(300,500)


# In[191]:


v1.show_vehicle_details()


# In[192]:


class car(vehicle):
    def show_car_details(self):
        print ('i am a car')


# In[193]:


c1 = car(250,800)


# In[194]:


c1.show_vehicle_details()


# In[195]:


c1.show_car_details()


# In[196]:


class car(vehicle):
    def __init__(self,milege,cost,tyres,hp):
        super().__init__(milege,cost)
        self.tyres = tyres
        self.hp = hp
        
    def show_car_details(self):
        print('numbers od tyres in a car:',self.tyres)
        print('hourse power of a car is',self.hp)
        print ('i am a car')


# In[197]:


c1 = car(600,100000000,8,999)


# In[198]:


c1.show_car_details()


# In[199]:


class parent1:
    def assign_string_one(self,str1):
        self.str = str1
    def show_string_one(self):
            return self.str1


# In[200]:


class parent2:
    def assign_string_two(self,str2):
        self.str = str2
    def show_string_two(self):
            return self.str2


# In[201]:


class child(parent1,parent2):
    def assign_string_three(self,str3):
        self.str3 = str3
    def show_string_three(self):
        return self.str3


# In[202]:


my_child = child()


# In[203]:


my_child.assign_string_one('i am string of parent 1')


# In[204]:


my_child.assign_string_two('i am string of parent 2')


# In[205]:


my_child.assign_string_three('i am string of child')


# In[206]:


my_child.show_string_one()


# In[ ]:


my_child.show_string_two()


# In[ ]:


my_child.show_string_three()


# In[ ]:


class parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        return self.name


# In[ ]:


class child(parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        return self.age

        


# In[ ]:


class grandchild(child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender


# In[ ]:


gc = grandchild()


# In[ ]:


gc.get_name('avi')


# In[ ]:


gc.get_age(20)


# In[ ]:


gc.get_gender('male')


# In[ ]:


gc.show_name()


# In[207]:


gc.show_age()


# In[ ]:


gc.show_gender()


# In[ ]:


import numpy as np


# In[ ]:


l1 = [1,2,3,4,5]


# In[ ]:


n1=np.array(l1)


# In[ ]:


n1


# In[208]:


type(n1)


# In[ ]:


n2=np.array([[1,2,3,4],[4,3,2,1]])


# In[ ]:


n2


# In[ ]:


type(n2)


# In[209]:


n3 = np.zeros((2,3))


# In[ ]:


n3


# In[ ]:


type(n3)


# In[ ]:


n4 = np.zeros((10,10))


# In[ ]:


n4


# In[ ]:


n5 = np.full((3,3),55)


# In[210]:


n5


# In[ ]:


n6 = np.arange(50,101)


# In[ ]:


n6


# In[ ]:


n7 = np.arange(50,500,10)


# In[ ]:


n7


# In[211]:


n8 = np.random.randint(100,200,10)


# In[ ]:


n8


# In[ ]:


n8


# In[ ]:


n9 = np.array([[1,2,3,4],[4,3,2,1]])


# In[ ]:


n9


# In[212]:


n9.shape=(4,2)


# In[ ]:


n9


# In[ ]:


n9.shape = (8,1)


# In[ ]:


n9


# In[ ]:


# vstack,hstack,column_stack


# In[213]:


n11=np.array([10,20,30,40,50,60,])


# In[ ]:


n22 = np.array([60,70,80,90])


# In[ ]:


np.intersect1d(n11,n22)


# In[ ]:


np.setdiff1d(n11,n22)


# In[ ]:


np.setdiff1d(n22,n11)


# In[214]:


# additionm of numpy arrays np.sum(x,y), axis-0,axis-1


# In[215]:


n1=np.array([10,20,30])


# In[ ]:


n1


# In[ ]:


n1+1


# In[ ]:


n1*10


# In[ ]:


n1-1


# In[216]:


n1/5


# In[ ]:


n1=np.random.randint(1,50,10)


# In[ ]:


n1


# In[ ]:


np.mean(n1)


# In[ ]:


np.median(n1)


# In[217]:


np.std(n1)


# In[ ]:


np.save('myarray',n1)


# In[ ]:


new_n1=np.load('myarray.npy')


# In[ ]:


new_n1


# In[ ]:


import pandas as pd


# In[ ]:


s1=pd.Series([1,2,3,4,5])


# In[218]:


s1


# In[219]:


type(s1)


# In[220]:


s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])


# In[ ]:


s1


# In[ ]:


pd.Series({'k1':10,'k2':20,'k3':30})


# In[ ]:


s5=pd.Series({'k1':10,'k2':20,'k3':30},index=['k3','k1','k2','k4'])


# In[221]:


s5


# In[ ]:


l1 = [1,2,3,4,5,6,7,8,9]


# In[ ]:


s1=pd.Series(l1)


# In[ ]:


s1


# In[ ]:


s1[4]


# In[222]:


s1[:5]


# In[ ]:


s1[-5:]


# In[ ]:


s1 +10


# In[ ]:


s1 - 100


# In[223]:


s1*5


# In[ ]:


s1/ 10


# In[ ]:


s2 = pd.Series([10,20,30,40,50,60,70,80,90])


# In[ ]:


s1+s2


# In[ ]:


pd.DataFrame({'name':['ani','bob','mat'],'marks':[75,12,82]})


# In[224]:


iris = pd.read_csv('iris.csv')


# In[ ]:


iris=pd.read_csv('iris.csv')


# In[ ]:


#read,head,tail,shape methods,describe,iloc,loc


# In[ ]:


import numpy as np


# In[ ]:


from matplotlib import pyplot as plt


# In[225]:


x = np.arange(1,11)


# In[ ]:


x


# In[ ]:


y = 3*x


# In[ ]:


y


# In[ ]:


plt.plot(x,y,color= 'r',linestyle=':',linewidth=5)
plt.title('x vs y')
plt.xlabel('this is x axis')
plt.ylabel('this is y axis')

plt.show()


# In[226]:


x


# In[ ]:


y1 = 2*x


# In[ ]:


y2 = 3*x


# In[ ]:


plt.plot(x,y1, color = 'r',linestyle=':')
plt.plot(x,y2, color = 'y',linewidth= 4)
plt.title('two lines in a plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(True)
plt.show()


# In[ ]:


plt.subplot(2,1,1)
plt.plot(x,y1, color = 'r',linestyle=':')
plt.subplot(2,1,2)
plt.plot(x,y2, color = 'y',linewidth= 4)
plt.title('two lines in a plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.grid(True)
plt.show()


# In[ ]:


student = {'bob':87,'julia':45,'annie':100,'matt':67}


# In[227]:


names=list(student.keys())


# In[ ]:


names


# In[ ]:


values = list(student.values())


# In[ ]:


values


# In[228]:


plt.barh(names,values,color='g')
plt.title('distribution of student marks')
plt.xlabel('names of students')
plt.ylabel('marks of students')
plt.show()


# In[ ]:


import numpy as np


# In[ ]:


x=[2,3,4,3,9,7,6,3,5,5,1]
y=[2,4,2,5,7,8,9,6,3,4,6]


# In[ ]:


plt.scatter(x,y,marker = '*',c='r',s=110)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




