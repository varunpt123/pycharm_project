# a=int(input('Enter a number'))
# print(type(a))
# if a%2==0:
#     print('a is even')
# else:
#     print('a is odd')



# def demo():
#     a=int(input('Enter a number'))
#     b=int(input('Enter another number'))
#     print((a+b)/2)
# demo()


# def demo(a,b):
#     print((a+b)/2)
# demo(10,40)


# def demo(a,b,c):
#     if a>=b and a>=c:
#         print('a is largest value')
#     elif b>=a and b>=c:
#         print('b is largest value')
#     else:
#         print('c is largest value')
#
# demo(400,60,300)



# for i in range(25,51):
#     if i % 2 == 0:
#      print(i)


# total = 0
# for i in range(1,11):
#     total+=i
# print(total)



# total = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         total += i
# print(total)



# i=1
# while i<=10:
#     print(i)
#     i+=1






# i=10
# while i>=1:
#     print(i)
#     i-=1





# for i in range(10,31):
#     if i % 2 == 0:
#         print(i,'Even number')
#     elif i >= 26:
#         break
#         print('stop')





# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#     def display(self):
#         print(self.name, self.position, self.salary)
#
#
#
# obj1 = Employee('Akhil','HR',10000)
# obj1.display()
# obj2 = Employee('Adnan','staff',5000)
# obj2.display()





# class Student:
#     company="futura"
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#     def display(self):
#         print(self.name, self.age, self.score,Student.company)
#
# std1 = Student('Nihal', 20, 68)
# std1.display()
# std2 =Student('asif', 19, 56)
# std2.display()




# class company:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#
#     def parent_method(self):
#         print("parent method")
#
# class Student(company):
#     def __init__(self, std_name, class_name,name,location):
#         self.std_name = std_name
#         self.class_name = class_name
#         super().__init__(name,location)
#     def display(self):
#         print( self.std_name, self.class_name,self.name, self.location)
#
#
# obj2 = Student('Adil',"mca",'futura','calicut')
# obj2.display()
# obj2.parent_method()



# class Library:
#     def __init__(self, book_name, author, price):
#         self.book_name = book_name
#         self.author = author
#         self.price = price
# class Student(Library):
#     def __init__(self, name, std_class, std_id, book_name, author, price):
#         self.name = name
#         self.std_class = std_class
#         self.std_id = std_id
#         super().__init__(book_name,author,price)
#     def display(self):
#         print(self.name, self.std_class, self.std_id, self.book_name, self.author, self.price)
#
# obj1 = Student('nihal','mca',21,'harry potter','mt',500)
# obj1.display()




# class Student:
#     def demo(self):
#         print('hello')
# class Subject(Student):
#     def demo(self):
#         print('hai')
#         super().demo()
#
# obj1 = Subject()
# obj1.demo()



#
# a="a"
# b="b"
# c=a+b
# print(c)

# class Shopping:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __add__(self,other):
#         print(self.price+other.price)
# biriyani=Shopping("Biryani",500)
# mandhi=Shopping("Mandhi",500)
#
# biriyani+mandhi










# class Shopping:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __mul__(self, other):
#         print(self.price * other.price)
# biriyani=Shopping('Biriyani',5)
# mandhi=Shopping('Mandhi',5)
#
# biriyani*mandhi








# class Student:
#     def __init__(self, name, age, score):
#         self__name = name
#         self.age = age
#         self.score = score
# class subject(Student):
#     def __init__(self, book_no, book_name, name, age, score):
#         self.book_no = book_no
#         self.book_name = book_name
#         super().__init__(name,age,score)
#     def display(self):
#         print(self.book_no,self.book_name,self.name,self.age,self.score)
#
# obj2 = subject(13,'Harrypotter','mt',19,48)
# obj2.display()






# list1=[1,2,3,4,5,6,7,8,30]
# even_num=[]
# for i in list1:
#     if i%2==0:
#         even_num.append(i)
# print(even_num)

# even=[i for i in list1 if i%2==0]
# print(even)

# even=[i+2 for i in list1 if i%2==0]
# print(even)

# even=[i+10 for i in list1 if i%2==0]
# print(even)
# even=[i*2 for i in list1 if i%2==0]
# print(even)

#set comprehesn

# setdemo={1,5,4,7,6,4,8,1}
# set1={1*2 for i in setdemo}
# print(set1)




# dicdemo={'anu':25,'abhi':30,'akhil':28}
# dic2={k.upper():v for(k,v) in dicdemo.items()}
# print(dic2)




#palindrome

# list2=['malayalam','english','mom','hindi','abbba']
# list1=[i for i in list2 if i==i[::-1]]
# print(list1)




#4 generator comprhsn
# input_list = [1,2,3,4,5,6,7,7]
# # # # #
# output_gen = (i for i in input_list if i % 2 == 0)
# print(output_gen)
# for var in output_gen:
#     print(var)



#Search()

import re
# txt = 'The rain in spain'
# x = re.search('in',txt)
# # print(x)
# if x:
#     print('Yes! We have a match!')
# else:
#     print('No match')





#findall()
# txt = 'The rain in spain'
# x = re.findall('ai',txt)
# print(x)



#split()

# txt = 'The rain Spain'
# x = re.split('in',txt)
# print(x)



# sub()

# txt = 'The rain in spain'
# x = re.sub('a','9',txt)
# print(x)





# span, string, group
# txt = 'The rain in spain rain'
# x = re.search('rain',txt)
# print(x)
# print(x.span())
# print(x.string)
# print(x.group())





#Add 5 to each element in list
# list1=[2,3,4]
# even=[i+5 for i in list1]
# print(even)




#Unique set comprehenssion in vowels
# vowels = 'aeiouAEIOU'
# word = 'communication'
# s={i for i in word if i in vowels}
# print(s)




#Duplicate elements
# list1 = [1,2,2,3,4,4,5]
# list2 = list(set(list1))
# print(list2)




