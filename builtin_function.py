'''Pre-Defined functions'''

'''sorted()'''
# a=[21,22,23,24]
# a.sort()
# print(a)    #  [21,22,23,24]
# a.sort(reverse=True)
# print(a)      #  [24,23,22,21]                            

# '''all()-if any of the function has empty string or None or 0 or False,it will shows the o/p as False'''
# print(all([True,1]))  #  True
# print(all([True,1,'']))   #  False
# print(all([True,1,0,None]))   #  False
# print(all([True,1,0,False]))   #  False
# print(all([True,1,'hii']))   #  True
# print(all([True,1,'hii',' ']))   #  True

# '''any()-if any of the function is true,it will show the o/p as True'''
# print(any([True,0,None,False]))    #  True                                       
# print(any([1,0,None,False]))       #  True
# print(any(['',0,None,False]))      #  False
# print(any([' ',0,None,False]))     #  True
# print(any(['hii',0,None,False]))   #  True     
# print(any([0,None,'']))            #  False     


# '''bool()-if any of the function has True or string,it will shows the o/p as True'''
# # print(bool(True))     #  True
# # print(bool(False))    #  False
# # print(bool(1))        #  True
# # print(bool(0))        #  False
# # print(bool(None))     #  False
# # print(bool('hii'))    #  True
# # print(bool(''))       #  False

# '''eval()-it will take  int and float values,if the total value is int it will show the o/p as int,or if the total value
#           is float it will show the o/p as float'''
# # print(eval('5+6+2-1'))   # 12
# # print(eval('8+4.5-9'))   # 3.5

# '''sum()'''
# # print(sum([1,2,3,4]))  #  10
# # print(sum([5.6,4,7]))  # 16.6

# '''prod()'''
# # import math
# # print(math.prod([1,4,5,7]))  #  140
# # print(math.prod([2.5,8,6]))  #  120.0

# '''reversed()-tuple'''
# # for x in reversed((1,2,3,4)):
#     # print(x)         #  4321 in vertical order
#     # print(x,end='')  # 4321 in horizontal order

# '''reversed()-list'''
# # for y in reversed([10,20,30,40]):
# #     print(y)  #  40302010 in vertical order

# '''enumerate()-it will directly shoe the index number'''
# # a=['python','java','c']
# # b=enumerate(a)
# # print(type(b))   #  enumerate
# # print(list(b))   #  [(0, 'python'), (1, 'java'), (2, 'c')]
# # print(tuple(b))  # ((0, 'python'), (1, 'java'), (2, 'c'))
# # print(dict(b))    # {0: 'python', 1: 'java', 2: 'c'}

# '''enumerate()-we can specify index number which number we want'''
# a=['python','java','c']
# # b=enumerate(a,4)
# # print(dict(b))  # {4: 'python', 5: 'java', 6: 'c'}