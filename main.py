# a = 4
# if a % 2:
#     print("нечет")
# else:
#     print("чет")

# b = "Арбуз"
# print(b[len(b)-1])


# 2323
# s1 = "ананас"
# s2 = "Апельсин"
# if s1[0] == s2[0]:
#     print("совпадают")
# else:
#     print("не соврадают")

# word = "Конь"
# if word[len(word)-1] == 'ь':
#     print(word[len(word)-2])
# else:
#     print(word[len(word)-1])

# num = 124
# print(num // 100 + num % 10)

# n1 = 32
# n2 = 3234
# if  n1 // 10 ** ( len(str(n1))-1) == n2 // 10 ** (len(str(n2)) - 1):
#     print("совпадают")
# else:
#     print("не совпадают")

# num1 = 3
# num2 = 2
# if num1 % num2 == 0:
#     print("делится без остатка")

# k = 3
# if k % 2 == 0:
#     print("число кратно 2")

# t1 = 2
# t2 = 4
# t3 = 6
# if t3 - t2 == t2 - t1:
#     print(True)
# else: 
#     print(False)

# u = 123
# if len(str(u)) == 3:
#     print(int(str(u)[0]) + int(str(u)[1]) + int(str(u)[2]))

# k1 = 13
# k2 = 13
# k3 = 13
# res = 1
# if k1 == k2 or k1 == k3:
#     res += 1
# if k2 == k3:
#     res += 1
# print(res)

# number = 225
# if int(str(number)[0]) == int(str(number)[1]):
#     print("1 и 2 цифры данного числа равны")

# a = 34
# user_number = 0
# count = 0
# while user_number != a:
#     count += 1
#     user_number = float(input())
#     if user_number > a:
#         print("Больше")
#     else:
#         print("Меньше")
# print(count)

# a = 1
# res = 1
# while a > 0:
#     res *= a
#     a = int(input())
# print(res)

# res = 1
# n = int(input())
# while n != 0:
#     res *= n
#     b = n - 1
#     n -= 1
# print(res)

# a = input()
# count = 0
# recount = int(len(a))
# while count < int(len(a)):
#     if a[count] == a[recount - 1]:
#         print("Палиндром")
#         break
#     count += 1
#     recount -= 1

# a = int(input())
# res = 0
# while a != 0:
#     res *= 10
#     b = a % 10
#     res += b
#     a = a // 10
#     if a == res:
#         print("Палиндром")

# word = input()
# res = ""
# for i in range(len(word) - 1, -1, -1):
#     res += word[i]
# print(res)




# text = " Арбуз арбуз   арбуз арбуз "
# words = 1
# text = text.strip()
# for i in range(len(text)):
    
#     if text[i]==' ':
#         if text[i+1] != ' ':
#             words += 1
# print(words)



# for i in range(100, 1000):
#     a = (i // 100) ** 3
#     b = ((i // 10) % 10) ** 3
#     c = (i % 10) ** 3
#     if a + b + c == i:
#         print(i)



# string = "Арбузик Арбуз Дыня"
# count = ""
# res = ""
# for i in string: 
#     if i != ' ':
#         count += i
#         if len(count) >= len(res):
#             res = count
#     else:
#         count = ""
# print(res)



# string = input()
# for i in range(len(string)):
#     string = string.replace(str(i), '')
# print(string)



# string = "kjwe wejfi fweij fw"
# string = string.replace(' ', '')
# print(string)



# email = "obuhovsemen@gmail.com"
# a = email.count('@')
# b = email.count('.')
# c = email.count(' ')
# if a != 1 or b != 1 or c != 0:
#     print(False)
# else:
#     print(True)



# s = "abcbca"
# sub = "ab"
# interval = ""
# count = 0
# for i in s:
#     interval += i
#     if interval == sub:
#         interval = ""
#         count += 1
# print(count)



# a = "Шалаш"
# a = a.lower()
# if a == a[::-1]:
#     print('Палиндром')



# b = "Арбузики"
# center = int(len(b) / 2)
# print(b[:center])
# print(b[center:])



# c = "slovo"
# if len(c) > 2:
#     c = c.replace(c[1:len(c) - 1], '') 
# print(c)



# a = [1,-2,3,-4]
# res = 0
# for i in a:
#     if i > 0:
#         res += i
# print(res)



# a = [1, 2, 'qwd', 'qwd', 'qdq', 1, 'awd']
# integer = input()
# res = 0
# for i in a:
#     if i == int(integer):
#         res += 1
# print(res)



# a = [1,3,6,7,9]
# b = [0,2,4,6,8]
# res = 0
# for i in a:
#     for j in b:
#         if i == j:
#             res = i
#             break
#     if res != 0:
#         break
# print(res)





# a = [1,3,5,6,10]
# res = []
# for i in range(len(a)):
#     if i != len(a) - 1:
#         res.append(a[i - 1] + a[i + 1])
# res.append(a[0] + a[len(a) - 2])
# print(res)



# a = [1,2,3,2,4,4,5,5]
# count = []
# res = []
# for i in range(len(a)):
#     for j in a:
#         if a[i] == j:
#             count.append(a[i])
#         if len(count) > 1 and a[i] not in res:
#             res.append(count[0])
#     else:
#         count.clear()
# print(res)

# string = "aaabbbcca"
# index = string[0]
# count = 0
# for i in string:
#     while index != i:
#         count+=1

# print(count)



# size = int(input())
# a = []
# for i in range(size):
#     a.append(int(input()))

# n = int(input())
# res = []
# for i,item in enumerate(a):
#     if item == n:
#         res += [a.index(n, i)]
# print(res)



# a = [1,2,3,4,5,6,7]
# res = []
# size = int(input())
# n = 0
# for i in a:
#     res += (a[n:n+size])
#     if res != []:
#         print(res)
#         n += size
#         res = []
#     else:
#         break



# size = int(input())
# k = int(input())
# a = []
# b = []
# n = 0
# for i in range(size):
#     k **= 2
#     b.append(k)
#     a.append(b)

# for i in a:
#     for j in i:
#         if j > n:
#             n = j
# print(a)
# print(n)



# size = int(input())
# a = []
# b = []
# count = 0

# for i in range(size):
#     for j in range(size):
#         b.append(int(input())) 
#     a.append(b)
#     b = []



# for i, item in enumerate(a):
#     for j, item2 in enumerate(item):
#         if i != j and a[i][j] == a[j][i]:
#             count += 1
#         if a[i][j] != a[j][i]:
#             count = 0
# if count != 0:
#     print(True)
# else:
#     print(False)



# a = [1,2,3,1,2,3,4,1,6,71,513,51315,351134]
# n = 0
# count = 0
# res = 0
# for i in a:
#     if i > n:
#         count += 1
#     else:
#         count = 1
#     n = i
#     if count > res:
#         res = count
# print(res)



# s = ["few", "fe", "f"]

# res = list(map(len, s))
# print(res)



# s = ["ab","bc","ca"]
# sub = 'a'

# res = list(filter(lambda x: sub in x,s))
# print(res)



# s = ["Шалаш", "лал", "плот"]

# res = list(filter(lambda x: x.lower() == x[::-1].lower(), s))
# print(res)


# s = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]

# res = list(map(lambda x: sum(list(filter(lambda y: y % 2 == 0, x))), s))
# print(res)



# s1 = [1,2,3,4,5]
# s2 = [5,6,7,8,9]

# print(set(s1).union(s2))



# str = "qweqweqeweweqweweqwqeqw"
# print(len(set(str)))



# str = "Арбуз мандарин Банан Банан"
# res = set(str.lower().split())
# print(res)



# s = [[1,2,3,1],
#      [4,5,5,6],
#      [7,9,8,7]]
# res = list(map(set, s))
# print(res)



# s = [{1,2,3},
#      {3,4,5},
#      {5,3,8}]



# slovar = {
#     "name": "egor",
#     "age": 17,
#     "phone": "9-999-999-99-99"
# }
# res = list()
# for i in slovar.values():
#     res += [i]
# print(res)



# date = "2025-12-31"
# datelist = date.split('-')

# slovar = {
#    "year": datelist[0],
#    "month": datelist[1],
#    "day": datelist[2]
# }

# print(slovar)



# string = "арбуз арбуз дыня арбуз дыня"
# stringlist = string.split()
# res = dict()
# for i in stringlist:
#     res[i] = stringlist.count(i)
# print(res)



# slovar = {
#      "list1": [1,2,3,4,5,1,2,3],
#      "list2": [3,4,5,6,7,3,4,5,6],
#      "list3": [1,2,3,4,5,6,7,8,9,22]
# }
# res = dict()
# res2 = set()
# for key, value in slovar.items():
#     count = set(value)
#     res2 |= count
#     res[key] = len(count)
# print(res)
# print(res2) 



# s = [1,2,3,4,5]

# def summ(s):
#     res = 0
#     for i in s:
#         res += i
#     return res 

# print(summ(s))



# def union(*s):
#     res = s[0] 
#     for i in s:
#         res &= i
#     return res

# res = union({1,2,3},{3,4,5,6})
# print(res)



# s = [1,2,3,4,5,6]

# def condition(x, y):
#     res = list(filter(y, s))
#     return res
# f = lambda x: x > 4
# res = condition(s, f)
# print(res)



# def f(x):
#     if x <= -2:
#         return 1 - (x + 2)**2
#     if -2 < x <= 2:
#         return -(x/2)
#     if x > 2:
#         return (x-2)**2 + 1
# n = int(input())
# res = f(n)
# print(res)

# slovar = {
#         3: 6
# }

# def factorial(x):
#     res = 1
#     if x in slovar.values():
#         return x
#     else: 
#         while x:
#             res *= x
#             x -= 1
#         slovar[x] = res
#     return res


# res = factorial(3)
# print(res)



# s = [[],[[]],[[[]]]]

# def depth(s):
#     count = 1
#     check = s
#     for i in check:
#         if type(i) == list:
#             count += 1
#             check = i
#     return count

# res = depth(s)
# print(res)



###################################### 11 ######################################


# def vvod(file):
#     with open(file + '.txt', "w") as info:
#         text = ' '
#         while text != '':
#             text = input()
#             info.write(text + "\n")

# vvod("vvod")



# def count(file):
#     with open(file + '.txt', "r") as info:
#         st_count = 0
#         sl_count = 0
#         string = list()
#         for i in info:
#             st_count += 1
#             string += i.split()
#         sl_count = len(string)
#     res = {
#         "строки": st_count,
#         "слова": sl_count
#     }
#     return res

# res = count("count")
# print(res)



# def files(file1, file2):
#     with open(file1 +'.txt', "r") as info:
#         res1 = set()
#         for i in info:
#             res1.add(str(i).strip())

#     with open(file2 + '.txt', "r") as info:
#         res2 = set()
#         for i in info:
#             res2.add(str(i).strip())
#     result = list(res1 & res2)

#     return result

# res = files("file1", "file2")
# print(res)


# def diff(file1, file2):
#     with open(file1 +'.txt', "r") as info:
#         res1 = set()
#         for i in info:
#             res1.add(str(i).strip())

#     with open(file2 + '.txt', "r") as info:
#         res2 = set()
#         for i in info:
#             res2.add(str(i).strip())

#     result = {
#         "Уникальные из первого": res1 - res2,
#         "Уникальные из второго": res2 - res1
#     }
#     return result

# res = diff("file1", "file2")
# print(res)



# def sort(file, newfile):
#     slovar = dict()
#     slovar2 = dict()
#     with open(file +'.txt', "r") as info:
#         with open(newfile +'.txt', "w") as info2:
#             for line in info:              
#                 slovar[line[0]] = line
#                 slovar2 = slovar

# slovar1 = {
#     "2":"B",
#     "3":"C",
#     "1":"A",
# }
# slovar2 = dict()

# count = 1
# for key, value in slovar1.items():
#     for key2, value2 in slovar1.items():
#         if int(key) == count:
#             slovar2[count] = value
#         # count += 1
#         print(slovar2, count)
        
                
# #             for value in slovar2.values():
# #                 info2.write(value.strip() + "\n")
# #     return slovar


# # res = sort("pereputano", "sortirovano")
# # print(res)


###################################### 13 ######################################

# table = [
#     ["","","","","","","",""],
#     ["","","","","","","",""],
#     ["","","","","","","",""],
#     ["","","","","","","",""],
#     ["","","","","","","",""],
#     ["","","","","","","",""],
#     ["","","","","","","",""],
#     ["","","","","","","",""],
# ]

# class Figura:
#     def __init__(self, x_value, y_value, side_value = "white"):
#         self.x = x_value
#         self.y = y_value
#         self.side = side_value
#     alive = True
#     def __attack__(self, enemy):
#         if self.x and self.y == enemy.x and enemy.y:
#             enemy.alive = False


# class pawn(Figura):
#     def __init__(self, x_value, y_value, side_value = "white"):
#         super().__init__(x_value, y_value, side_value)
#     symbol = "♟"
#     max_x = 1
#     max_y = 2

#     def step(self, new_x, new_y):
#         if self.y >= 3:
#             self.max_y = 1
#         if table[(8-new_y)-1][new_x-1] == '' and new_y > self.y:
#             self.x = new_x
#             self.y = new_y
#             # self.__attack__(enemy)
#             table[self.x][self.y] 
#             return f"x => {self.x}, y => {self.y}"
#             \
#         elif new_x == self.x and new_y == self.y:
#             return False 
#         else:
#             return False
#             # if self.side == enemy.side and self.x and self.y == enemy.x and enemy.y:
#             #                 return "Вы не можете атаковать союзную фигуру!"
#     # def create_queen(self):
#     #     if self.y == 8 and self.side == "white" or self.y == 1 and self.side == "black":
#     #         self.alive = False
#     #         queen_new.x = self.x
#     #         queen_new.y = self.y
#     #         return "Ферзь"

# # class Queen(Figura):
# #     def __init__(self, x_value, y_value, side_value="white"):
# #         super().__init__(x_value, y_value, side_value)
# #     max_x = 8
# #     max_y = 8  
# #     def step(self, new_x, new_y):
# #         if new_x - self.x <= self.max_x and new_y - self.y <= self.max_y:
# #             self.x = new_x
# #             self.y = new_y
# #             # self.__attack__(enemy)
# #             return f"x => {self.x}, y => {self.y}"
# #         elif new_x == self.x and new_y == self.y:
# #             return False 
# #         else:
# #             return False

# while(True):
#     for i in table:
#         print(i)
#     pawn1 = pawn(int(input()),int(input()))


###################################### 14 ######################################

# Импортируем модуль
# import char


# Semen = char.Character(5)
# goblin = char.Character(5)

# print(goblin.hitPoint)
# print(Semen.atkPhys(goblin))


# Импортируем модули из пакета
# from for_pack import armstrong ,str_reverse ,word_count

# armstrong.armstrong_num()
# str_reverse.str_reverse("Арбуз")
# word_count.word_count("fwek fjwei fj")


from figures import Rectangle, Triangle, contain


rect1 = Rectangle.Rectangle(10,5)
tria1 = Triangle.Triangle(3, 4, 5)
# tria1 = Triangle.Triangle(13, 14, 15)

print(contain.contain(rect1,tria1))

print(rect1.get_outer_rect())
print(tria1.get_outer_rect())