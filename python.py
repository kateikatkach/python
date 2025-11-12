import math

# #1
# import math
# x=int(input())
# y=3*x**2+math.sin(x+2)
# print(y)


#2
# import math
# x=int(input())
# a=int(input())
# y=a*x**2+math.cos(2*x+1)
# print(y)

#3
# x,a,b=map(int,input().split())
# y=a*x+b*math.sin(2*x+2)
# print(y)


# #4
# x,a=map(int,input().split())
# y=a*x**3+math.cos(3*x+1)
# print(y)


#5
# x,a=map(int,input().split())
# y=x**2/a+math.cos(2*x-1)
# print(y)

#6
# x,a=map(int,input().split())
# y=x/a+2*x**2
# print(y)

#7
# x=int(input())
# y=3*x**2-2*x+1
# print(y)

# 8
# x=int(input())
# y=0.5*x**2-3*x+1
# print(y)


#9
# x,a=map(int,input().split())
# y=1/(x**2+1)-a
# print(y)

#10
# x,a=map(int,input().split())
# y=a/(x**2+1)-math.cos(2*x-1)
# print(y)

#11
# x=int(input())
# y=x**3-2*x**2+4
# print(y)


#12
# x,a,b=map(int,input().split())
# y=a*x**2+b*x**3-8
# print(y)


#13
# x,a,b=map(int,input().split())
# y=a*(math.sqrt(x**2+4))-b
# print(y)

#14
# x=int(input())
# y=math.cos(2*x-1)+math.sin(x)
# print(y)

# 15
# x,a,b=map(int,input().split())
# y=a*math.sqrt(x)+b*x**2
# print(y)

# БЛОК2
#1
# a,b,c=map(int,input().split())
# V=a*b*c
# S=2*(a*b+b*c+a*c)
# print(V,S)


# 2
# R=int(input())
# L=2*math.pi*R
# S=math.pi*R**2
# print(L,S)

#3
# a, b = map(int, input().split())
# c = math.sqrt(a ** 2 + b ** 2)
# P = a + b + c
# print(c, P)


#4
# R1,R2=map(int,input().split())
# S1=math.pi*R1**2
# S2=math.pi*R2**2
# S3=S1-S2
# print(S3)

#5
# x1,y1,x2,y2=map(int,input().split())
# st1=x2-x1
# st2=y2-y1
# S=st1*st2
# P=2*(st1+st2)
# print(S,P)

#6
# x1,y1,x2,y2=map(int,input().split())
# f=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(f)

# #7
# def rast(a1, a2, b1, b2):
#     liner = math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2)
#     return liner
#
#
# x1, y1, x2, y2, x3, y3 = map(int, input().split())
# st1 = rast(x1, x2, y1, y2)
# st2 = rast(x2, x3, y2, y3)
# st3 = rast(x1, x3, y1, y3)
# polper = (st1 + st2 + st3) / 2
# Per = st1 + st2 + st3
# S = math.sqrt(polper * (polper - st1) * (polper - st2) * (polper - st3))
# print(Per, S)

#8
# tempF = int(input())
# tempC = (tempF - 32) * 5 / 9
# print(tempC)


#9
# for i in range(50):
#     x, a, y, b = map(int, input().split())
#     choc = 1 * a
#     iris = 1 * b
#     raz = choc / iris
#     print(choc, iris, raz)


#10
# a1, a2, b1, b2, c1, c2 = map(int, input().split())
# d = a1 * b2 - a2 * b1
# x = (c1 * b2 - c2 * b1) / d
# y = (a1 * c2 - a2 * c1) / d
# print(x, y)

#11
# alf = int(input())
# alfrad = alf * math.pi / 180
# print(alfrad)


#12
# v1, v2, pyt, t = map(int, input().split())
# s2 = t * (v1 + v2)
# obS = pyt + s2
# print(obS)

# 13
# a, b, c = map(int, input().split())
# ac = abs(c - a)
# bc = abs(c - b)
# sums = ac + bc
# print(ac, bc, sums)


#14
# a, b = map(int, input().split())
# a2 = a ** 2
# b2 = b ** 2
# sums = a2 + b2
# razn = a2 - b2
# proiz = a2 * b2
# dels = a2 / b2
# print(sums, razn, proiz, dels)

#15
# vtech, vkater, t1, t2 = map(int, input().split())
# s1 = vkater * t1
# s2 = (vkater - vtech) * t2
# S = s1 + s2
# print(S)


#БЛОК 3
#1
# a, x = map(int, input().split())
# if x > 0:
#     y = a * x ** 2 + 1
# else:
#     y = a * x - 1
# print(y)


#2
# a, x = map(int, input().split())
# if x >= 1:
#     y = a * x + 1
# else:
#     x ** 2 - 1
# print(y)


#3
# a, x = map(int, input().split())
# if x < 0:
#     y = 3 * a ** 2
# else:
#     y = 4 * a * x - 1
# print(y)


# #4
# a, x = map(int, input().split())
# if x > 4:
#     y = 2 * a ** 2
# else:
#     y = 3 * x - 1
# print(y)


#5
# a, x = map(int, input().split())
# if x > 2:
#     y = 2 * a * x - 2
# else:
#     y = 3 * a ** 2 - 2 * x
# print(y)


#6
# a, x = map(int, input().split())
# if x > 1:
#     y = 2 * a * x ** 2 - 1
# else:
#     y = x
# print(y)

#7
# a, x = map(int, input().split())
# if x > 2:
#     y = x ** 2
# else:
#     y = 2 * a - 1
# print(y)

#8
# x = int(input())
# if x > 2:
#     y = math.cos(2 * x - 1)
# else:
#     y = math.sin(3 * x + 1)
# print(y)

#9
# x = int(input())
# if x > 2:
#     y = 2 * x ** 3 - 2 * x - 1
# else:
#     y = 3 * x ** 2 - 2 * x + 1
# print(y)

#10
# a, x = map(int, input().split())
# if x > 1:
#     y = 2 * a * x ** 2 - 1
# else:
#     y = 1 / a
# print(y)


#11
# a, x = map(int, input().split())
# if x >= 0:
#     y = a * math.sqrt(x) + 1
# else:
#     y = a * x - 1
# print(y)


# #12
# a, x = map(int, input().split())
# if x >= 0:
#     y = math.sqrt(x) + a
# else:
#     y = a / x - 1
# print(y)

#13
# a, x = map(int, input().split())
# if x > 0:
#     y = 1 / x + a
# else:
#     y = x ** 2 - 1
# print(y)


#14
# x = int(input())
# if x > math.pi / 2:
#     y = math.cos(x)
# else:
#     y = math.sin(x)
# print(y)

#15
# x = int(input())
# if x > 2:
#     y = math.sqrt(x - 2)
# else:
#     y = (x - 2) ** 2 + 1
# print(y)

#БЛОК 4
#1
# k, n = map(int, input().split())
# while n > 0:
#     print(k)
#     n -= 1

#2
# a, b = map(int, input().split())
# cnt = 0
# for i in range(a, b + 1):
#     print(i)
#     cnt += 1
# print(cnt)

#3
# a, b = map(int, input().split())
# cnt = 0
# for i in range(b - 1, a, -1):
#     print(i)
#     cnt += 1
# print(cnt)

#4
# c = 20.4
# for i in range(1, 11):
#     print(i, '-', i * c)


#5
# a, b, h = map(int, input().split())
# for i in range(a, b, h):
#     print(i ** 2)


#6
# a, b, h = map(int, input().split())
# for i in range(a, b, h):
#     if i >= 0:
#         print(i)

#7

# a, b = map(int, input().split())
# sumc = 0
# for i in range(a, b + 1):
#     sumc += i
# print(sumc)


#8
# a, b = map(int, input().split())
# sumc = 1
# for i in range(a, b + 1):
#     sumc *= i
# print(sumc)

#9
# a, b = map(int, input().split())
# sumc = 0
# for i in range(a, b + 1):
#     sumc += i ** 2
# print(sumc)


# #10
# n = float(input())
# for weight in range(12, 22, 2):
#     weight /= 10
#     cost = n * weight
#     print(weight, '-', cost)

#11
# n = int(input())
# sq = 0
# for i in range(n):
#     sq += (2 * i + 1)
# print(sq)

#12
# n = int(input())
# a = float(input())
# i = 0
# while a ** i <= n:
#     print(a ** i)
#     i += 1

#13
# n = int(input())
# maxi = 1
# for i in range(1, n + 1):
#     if i ** 2 <= n:
#         maxi = i ** 2
# print(maxi)

#14
# n = int(input())
# maxk = 1
# for k in range(1, n + 1):
#     if 3 ** k < n:
#         maxk = k
# print(maxk)

#15
# n = int(input())
# a, b = map(float, input().split())
# lined = (b - a) / n
# print(lined)
# for i in range(0, int(b - a)):
#     print(a + lined * i)

#БЛОК 5
#1
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += 1 / (2 ** i)
# print(sumd)

#2
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += (math.cos(x)) ** n / n
# print(sumd)


#3
# n = int(input())
# sumd = 0
# for i in range(0, n + 1):
#     sumd += (-1) ** i * 3 ** i
# print(sumd)


#4
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += 1 / (math.sin(i))
# print(sumd)


#5
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += ((-1) ** (i + 1)) * i ** 3
# print(sumd)

#6
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += (-1) ** (i + 1) * math.cos(i)
# print(sumd)


#7
# import math

# n = int(input())
# x = float(input())
# sumd = 0
# if abs(x) < 1:
#     for i in range(1, n + 1):
#         sumd += ((-1) ** (i - 1) * x ** i) / i
# else:
#     print('Error')
# print(sumd)


#8
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += (-1) ** (i + 1) * math.factorial(i)
# print(sumd)

#9
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += math.sin(x ** i)
# print(sumd)

#10
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += 1 / math.factorial(i)
# print(sumd)


#11
# import math
#
# n = int(input())
# s = 0
# for i in range(n+1):
#     s += (n + i) ** 2
# print(s)


#12
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += math.factorial(i)
# print(sumd)

#13
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(n + 1):
#     sumd += (x ** i) / (math.factorial(i))
# print(sumd)

#14
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(0, n + 1):
#     sumd += (-1) ** i * x ** i
# print(sumd)


#15
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(n + 1):
#     p = 2 * i + 1
#     sy = (-1) ** i
#     sumd += sy * (x ** p) / p
# print(sumd)

#БЛОК 6
#1
# import math
#
# a = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     a.append(element)
# k, l = map(int, input().split())
# if not (1 <= k <= l <= n):
#     print('error')
# masa2 = a[k - 1:l]
# sumel = sum(masa2)
# countel = len(masa2)
# srarif = sumel / countel
# print(srarif)


#2
# import math
#
# a = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     a.append(element)
# k, l = map(int, input().split())
# if not (1 <= k <= l <= n):
#     print('error')
# masa2 = a[k - 1:l]
# sumel = sum(masa2)
# suma = sum(a)
# razn = suma - sumel
# print(razn)

#3
#1
# import math
#
# a = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     a.append(element)
# k, l = map(int, input().split())
# if not (1 <= k <= l <= n):
#     print('error')
# del a[k - 1:l]
# print(a)
# sumel = sum(a)
# countel = len(a)
# srarif = sumel / countel
# print(srarif)

#4
# a = [0, 1, 2, 3, 4, 5]
# chet = []
# nechet = []
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         chet.append(a[i])
#     else:
#         nechet.append(a[i])
# nechet.reverse()
# maxar = chet + nechet
# print(maxar)

#5
# a = [0, 1, 2, 3, 4, 5]
#
# for i in range(0, len(a), 2):
#     print(a[i], end=' ')
# for i in range(1, len(a), 2):
#     print(a[i], end=' ')

#6
# a = [0, 6, 2, 3, 4, 5]
# maxel = max(a)
# r = a.index(maxel)
# del a[0:r + 1]
# prod = 1
# for i in range(len(a)):
#     prod *= a[i]
# print(prod)

#7
# a = [3, 1, 2, 3, 4, 7]
# maxel = max(a)
# minel = min(a)
# r = a.index(maxel)
# l = a.index(minel)
# if r - l > 0:
#     masa = a[l:r + 1]
# else:
#     masa = a[r:l + 1]
# print(masa)
# suma = sum(masa)
# print(suma)

#8
# a = [3, 1, 2, 3, 4, 7]
# maxel = max(a)
# minel = min(a)
# r = a.index(maxel)
# l = a.index(minel)
# start = min(r, l)
# finish = max(l, r)
# for i in range(start + 1, finish):
#     a[i] = 0
# print(a)

#9
# a = [0, 1, 2, 3, 4, 5]
# n = int(input())
# chet = []
# nechet = []
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         a[i] = a[i] * n
# print(a)

#10
# a = [0, 1, 2, 3, 4, 5]
# for i in range(0, len(a)):
#     if a[i] % 2 != 0:
#         a[i] = a[i] * 0
# print(a)


#11
# a = [0, 1, 2, 3, 4, 5]
# chet = []
# for i in range(0, len(a)):
#     if i % 2 == 0:
#         chet.append(a[i])
# rez = min(chet)
# print(rez)

#12
# a = [0, 8, 5, 3, 4, 5]
# rez = []
# cnt = 0
# for i in range(0, len(a) - 1):
#     if a[i] > a[i + 1]:
#         rez.append(i)
#         cnt += 1
# print(rez)
# print(cnt)

#13
# a = [0, 8, 5, 3, 4, 5]
# rez = []
# maxsum = 0
# maxel1 = 0
# maxel2 = 0
# for i in range(0, len(a) - 1):
#     if a[i] + a[i + 1] > maxsum:
#         maxsum = a[i] + a[i + 1]
#         maxel1 = a[i]
#         maxel2 = a[i + 1]
# sd = []
# sd.append(maxel1)
# sd.append(maxel2)
# print(sd)

#14
# a = [0, 8, 5, 3, 4, 5]
# minind = a.index(min(a))
# maxind = a.index(max(a))
# a[minind], a[maxind] = a[maxind], a[minind]
# print(a)

#15
# n, a, b = map(int, input().split())
# rez = [a, b]
# for i in range(2, n):
#     nexel = sum(rez)
#     rez.append(nexel)
# print(rez)



#БЛОК 7
#1
# import math
#
# a = [5, 2, 9, 1, 7, 4, 8, 3, 6, 8, 9]
# necha = [x for x in a if x % 2 != 0]
# necha.sort(reverse=True)
# print(necha)


#2
# import math
#
# a = [5, -2, 9, 1, -7, 4, 8, 3, -6, 8, 9, -6, 4, 4, 2]
# pologa = [x for x in a if x >= 0]
# pologa.sort()
# print(pologa)


#3
# import math
#
# a = [5, -2, 9, 1, -7, 4, 8, 3, -6, 8, 9, -6, 4, 4, 2]
# pologa = [x for x in a if x >= 0]
# pologa.sort(reverse=True)
# print(pologa)


#4
# import math
#
# a = [5, 2, 9, 1, 7, 4, 8, 3, 6, 8, 9]
# cheta = [x for x in a if x % 2 == 0]
# cheta.sort()
# print(cheta)


#5
# import math
#
# k = int(input())
# a = [5, 2, 9, 1, 7, 4, 8, 3, 6, 8, 9]
# olda = [x for x in a if x > k]
# olda.sort(reverse=True)
# print(olda)


#6
# import math
#
# a = [10, 13, 5, 3, 4, 8, 90, 121, 52, 34, 6, 4, 1, 2, 67, 111]
# olda = [x for x in a if x > 10]
# olda.sort()
# print(olda)

#7
# import math
#
# a = [1, 12, 10, 4, 5, 0, 15, 25, 64, 35, 78, 78, 90, 52, 1000]
# olda = [x for x in a if x % 5 == 0]
# olda.sort(reverse=True)
# print(olda)


#8
# import math
#
# k = int(input())
# a = [1, 12, 10, 4, 5, 0, 15, 25, 64, 35, 78, 78, 90, 52, 1000]
# jolda = [x for x in a if x < k]
# jolda.sort()
# print(jolda)

#9
# import math
#
# a = [10, 13, 5, 3, 4, 8, 90, 121, 52, 34, 6, 4, 1, 2, 67, 111]
# olda = [x for x in a if x < 15]
# olda.sort(reverse=True)
# print(olda)


#10
# import math
#
# a = [1, 12, 10, 4, 5, 0, 15, 25, 64, 35, 78, 78, 90, 52, 1000]
# olda = [x for x in a if x % 3 == 0]
# olda.sort()
# print(olda)


#11
# import math
#
# k = int(input())
# a = [1, 12, 10, 4, 5, 0, 15, 25, 64, 35, 78, 78, 90, 52, 1000]
# olda = [x for x in a if x % k == 0]
# olda.sort(reverse=True)
# print(olda)


#12
# import math
#
# a = [1, -12, 10, 4, 5, 0, -15, 25, 64, -35, -78, 78, 90, -52, -1000]
# olda = [x for x in a if x < 0]
# olda.sort()
# print(olda)


#13
# import math
#
# olda = []
# a = [1, -12, 10, 4, 5, 0, -15, 25, 64, -35, -78, 78, 90, -52, -1000]
# for x in range(len(a)):
#     if x % 2 != 0:
#         olda.append(a[x])
# olda.sort(reverse=True)
# print(olda)


#14
# import math
#
# a = [1, 12, 10, 4, 5, 0, 15, 25, 64, 35, 78, 78, 90, 52, 1000]
# olda = [x for x in a if len(str(x)) == 2]
# olda.sort()
# print(olda)

#15
# import math
#
# olda = []
# a = [1, -12, 10, 4, 5, 0, -15, 25, 64, -35, -78, 78, 90, -52, -1000]
# for x in range(len(a)):
#     if x % 2 == 0:
#         olda.append(a[x])
# olda.sort()
# print(olda)


#БЛОК 8
#1
# row-строка
# col-столбец
# 1
# def findsd(matrix):  # фун-ция для нахождения первого столбца,содержащего только нечётные числа
#     if not matrix or not matrix[0]:  # это проверка на пустую матрицу и на пустые строки
#         return 0
#
#     for col in range(len(matrix[0])):  # тут проверяем, все ли элементы в столбце нечетные
#         if all(matrix[row][col] % 2 != 0 for row in range(len(matrix))):
#             return col + 1
#
#     return 0
#
#
# matrix = [
#     [1, 2, 3, 9],
#     [3, 4, 5, 7],
#     [5, 6, 7, 5]
# ]
# print(findsd(matrix))


#2
# def transformer(matrix):
#     for row in matrix:
#         if len(row) == 0:
#             continue
#         # для начала находим индексы минимального и максимального элемента в строке
#         min_index = row.index(min(row))
#         max_index = row.index(max(row))
#         # меняем местами минимальный и максимальный элемент
#         row[min_index], row[max_index] = row[max_index], row[min_index]
#
#     return matrix
#
#
# matrix = [
#     [3, 1, 4, 1, 5],
#     [9, 2, 6, 5, 3],
#     [5, 8, 9, 7, 9]
# ]
# print("Исходная матрица:")
# for row in matrix:
#     print(row)
# transformed = transformer(matrix)
# print("\nПреобразованная матрица:")
# for row in transformed:
#     print(row)


#БЛОК 8
#1
# # row-строка
# # col-столбец
# # 1
# def findsd(matrix):  # фун-ция для нахождения первого столбца,содержащего только нечётные числа
#     if not matrix or not matrix[0]:  # это проверка на пустую матрицу и на пустые строки
#         return 0
#
#     for col in range(len(matrix[0])):  # тут проверяем, все ли элементы в столбце нечетные
#         if all(matrix[row][col] % 2 != 0 for row in range(len(matrix))):
#             return col + 1
#
#     return 0
#
#
# matrix = [
#     [1, 2, 3, 9],
#     [3, 4, 5, 7],
#     [5, 6, 7, 5]
# ]
# print(findsd(matrix))


#2
# def transformer(matrix):
#     for row in matrix:
#         if len(row) == 0:
#             continue
#         # для начала находим индексы минимального и максимального элемента в строке
#         min_index = row.index(min(row))
#         max_index = row.index(max(row))
#         # меняем местами минимальный и максимальный элемент
#         row[min_index], row[max_index] = row[max_index], row[min_index]
#
#     return matrix
#
#
# matrix = [
#     [3, 1, 4, 1, 5],
#     [9, 2, 6, 5, 3],
#     [5, 8, 9, 7, 9]
# ]
# print("Исходная матрица:")
# for row in matrix:
#     print(row)
# transformed = transformer(matrix)
# print("\nПреобразованная матрица:")
# for row in transformed:
#     print(row)


# #3
# def transform(matrix):
#     if not matrix or not matrix[0]:
#         return matrix
#     #находим минимальный и максимальный элементы и их строки
#     flat_matrix = [(val, i) for i, row in enumerate(matrix) for val in row]
#
#     min_val, min_row = min(flat_matrix, key=lambda x: x[0])
#     max_val, max_row = max(flat_matrix, key=lambda x: x[0])
#
#     # Меняем строки местами
#     if min_row != max_row:
#         matrix[min_row], matrix[max_row] = matrix[max_row], matrix[min_row]
#
#     return matrix
#
# matrix = [
#     [3, 1, 4],
#     [9, 2, 6],
#     [5, 8, 7],
#     [0, 3, 2]
# ]
# transformed = transform(matrix)
# for row in transformed:
#     print(row)


#4
# def mir(matr):
#     k = len(matr)  # считаем кол-во строк
#     for i in range(k // 2):  # идём до середины массива
#         matr[i], matr[k - 1 - i] = matr[k - 1 - i], matr[i]  # меняем местами строчки
#
#
# matr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
# for row in matr:  # начальная матрица
#     print(row)
#
# mir(matr)  # матрица после изменений
# for row in matr:
#     print(row)

#5
# def remov(matr):
#     M = len(matr)
#     N = len(matr[0])
#     min_valh = matr[0][0]
#     min_row = 0
#     for i in range(M):
#         for j in range(N):
#             if matr[i][j] < min_valh:
#                 min_valh = matr[i][j]
#                 min_row = i
#
#     del matr[min_row]  # удаляем строку с минимальным элементом
#     return matr
#
#
# matr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
# for row in matr:  # начальная матрица
#     print(row)
# remov(matr)  # матрица после изменений
# for row in matr:
#     print(row)


#6
# def remov(matr):
#     M = len(matr)
#     N = len(matr[0])
#     max_valh = matr[0][0]
#     max_st = 0
#     for i in range(M):
#         for j in range(N):
#             if matr[i][j] > max_valh:
#                 max_valh = matr[i][j]
#                 max_st = j
#     for i in range(M):
#         del matr[i][max_st]#удаляем столбец
#     return matr
#
#
# matr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
# for row in matr:  # начальная матрица
#     print(row)
# remov(matr)  # матрица после изменений
# for row in matr:
#     print(row)


# #7
# def mir(matr):
#     k = len(matr)  # количество строк
#     n = len(matr[0])  # количество столбцов
#     for i in range(k):
#         for j in range(n // 2):
#             matr[i][j], matr[i][n - 1 - j] = matr[i][n - 1 - j], matr[i][j]
#
#
# matr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# for row in matr:  # начальная матрица
#     print(row)
#
# mir(matr)  # матрица после изменений
# for row in matr:
#     print(row)


#8
# def dublic(matr):
#     M = len(matr)
#     N = len(matr[0])
#     # находим максимальный элемент и его позицию
#     max_value = matr[0][0]
#     max_row = 0
#     for i in range(M):
#         for j in range(N):
#             if matr[i][j] > max_value:
#                 max_value = matr[i][j]
#                 max_row = i
#
#     # Дублируем строку с максимальным элементом
#     matr.insert(max_row + 1,
#                 matr[max_row][:])  # получаем строку с макс элем,дублируем её,вставляем на следующую позицию
#
#     return matr
#
#
# # Пример использования
# matr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
#
# print("Исходная матрица:")
# for row in matr:
#     print(row)
#
# dublic(matr)
# for row in matr:
#     print(row)


#9
# def srarifel(matrix):
#     M = len(matrix)  # количество строк
#     N = len(matrix[0])  # количество столбцов
#     result = []
#     for j in range(N):
#         # вычисляем сумму элементов столбца j
#         sumn = 0
#         for i in range(M):
#             sumn += matrix[i][j]
#         # вычисляем среднее арифметическое столбца
#         srarifg = sumn / M
#         # считаем количество элементов больше среднего
#         count = 0
#         for i in range(M):
#             if matrix[i][j] > srarifg:
#                 count += 1
#
#         result.append(count)
#
#     return result
#
#
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# result = srarifel(matrix)
#
# for j, count in enumerate(result):
#     print(f"Столбец {j}: {count}")




#1
# def f(text):
#     words = text.split()
#     if not words:
#         return 0
#     return min(len(word) for word in words)
#
# text = "длину самого короткого слова"
# result = f(text)
# print(f"Длина самого короткого слова: {result}")
#
#
# def countlet(s):
#     # Подсчитывает количество букв верхнего регистра в строке
#     return sum(1 for char in s if char.isupper())
#
#
# def main():
#     # а) Создание кортежа из строк, введенных пользователем
#     print("Введите строки (для завершения введите пустую строку):")
#     strings_list = []
#
#     while True:
#         user_input = input("> ")
#         if user_input == "":
#             break
#         strings_list.append(user_input)
#
#     # Преобразуем список в кортеж
#     strings_tuple = tuple(strings_list)
#
#     print(f"\nСозданный кортеж: {strings_tuple}")
#
#     # б) Преобразование кортежа в словарь
#     result_dict = {}
#
#     for string in strings_tuple:
#         uppercase_count = countles(string)
#         result_dict[string] = uppercase_count
#
#     print("\nРезультирующий словарь:")
#     for key, value in result_dict.items():
#         print(f"'{key}': {value}")
#
#     return strings_tuple, result_dict


#13
# def filter_non_strings_and_get_slice(tuple_data):
#     """
#     Функция для получения среза кортежа без строковых элементов
#     """
#     # Фильтруем элементы, оставляя только нестроковые
#     filtered_tuple = tuple(item for item in tuple_data if not isinstance(item, str))
#
#     # Запрашиваем у пользователя параметры среза
#     try:
#         start = int(input("Введите начальный индекс среза: ") or "0")
#         end = int(input("Введите конечный индекс среза: ") or str(len(filtered_tuple)))
#         step = int(input("Введите шаг среза: ") or "1")
#
#         # Получаем срез
#         result_slice = filtered_tuple[start:end:step]
#         return result_slice
#
#     except ValueError:
#         print("Ошибка: введите целые числа для индексов и шага")
#         return None
#
#
# def convert_to_positive_integers(strings_tuple):
#     """
#     Функция для преобразования кортежа строк в кортеж положительных целых чисел
#     """
#     result = []
#     for item in strings_tuple:
#         try:
#             num = int(item)
#             if num >= 0:  # Оставляем только неотрицательные числа
#                 result.append(num)
#         except ValueError:
#             # Пропускаем элементы, которые нельзя преобразовать в число
#             continue
#
#     return tuple(result)
#
#
# def main():
#     print("=== Часть А: Срез кортежа без строк ===")
#
#     # Пример кортежа для части А
#     sample_tuple_a = (1, "hello", 3.14, "world", 42, "python", 7, 8.9)
#     print(f"Исходный кортеж: {sample_tuple_a}")
#
#     # Получаем срез без строк
#     slice_result = filter_non_strings_and_get_slice(sample_tuple_a)
#     if slice_result is not None:
#         print(f"Срез без строковых элементов: {slice_result}")
#
#     print("\n=== Часть Б: Преобразование строк в положительные целые числа ===")
#
#     # Пример кортежа для части Б
#     sample_tuple_b = ("123", "-45", "67", "hello", "0", "-100", "42", "3.14")
#     print(f"Исходный кортеж строк: {sample_tuple_b}")
#
#     # Преобразуем в положительные целые числа
#     converted_tuple = convert_to_positive_integers(sample_tuple_b)
#     print(f"Кортеж положительных целых чисел: {converted_tuple}")
#
#     # Демонстрация с пользовательским вводом
#     print("\n=== Работа с пользовательским вводом ===")
#
#     # Ввод кортежа для части А
#     user_input_a = input("Введите элементы кортежа для части А через запятую: ")
#     if user_input_a:
#         user_tuple_a = tuple(item.strip() for item in user_input_a.split(','))
#         print(f"Ваш кортеж: {user_tuple_a}")
#         slice_result_user = filter_non_strings_and_get_slice(user_tuple_a)
#         if slice_result_user is not None:
#             print(f"Срез без строк: {slice_result_user}")
#
#     # Ввод кортежа для части Б
#     user_input_b = input("\nВведите строковые значения для части Б через запятую: ")
#     if user_input_b:
#         user_tuple_b = tuple(item.strip() for item in user_input_b.split(','))
#         print(f"Ваш кортеж строк: {user_tuple_b}")
#         converted_user = convert_to_positive_integers(user_tuple_b)
#         print(f"Положительные целые числа: {converted_user}")
#
#
# def compact_solution():
#     """Компактная версия решения"""
#
#     # Часть А: Срез без строк
#     tuple_a = (1, "text", 2, "more", 3, 4.5, "end")
#     print(f"Исходный кортеж А: {tuple_a}")
#
#     # Фильтруем нестроковые элементы
#     non_strings = tuple(x for x in tuple_a if type(x) != str)
#     print(f"Без строк: {non_strings}")
#
#     # Срез (пример)
#     slice_example = non_strings[0:len(non_strings):2]
#     print(f"Срез с шагом 2: {slice_example}")
#
#     # Часть Б: Преобразование в положительные целые
#     tuple_b = ("10", "-5", "25", "abc", "0", "-1", "100")
#     print(f"\nИсходный кортеж Б: {tuple_b}")
#
#     # Преобразуем и фильтруем
#     positive_ints = tuple(int(x) for x in tuple_b if x.lstrip('-').isdigit() and int(x) >= 0)
#     print(f"Положительные целые: {positive_ints}")
#
#
#     print("\n" + "=" * 50)
#     print("Компактная версия:")
#     compact_solution()



# 7
# # Заданные предложения
# sentence1 = "Пример первого предложения"
# sentence2 = "Пример второго предложения"
# sentence3 = "Пример третьего предложения"
#
# # Объединяем буквы из всех предложений в одно множество
# unique_letters = set(sentence1.replace(" ", "").lower()) | set(sentence2.replace(" ", "").lower()) | set(sentence3.replace(" ", "").lower())
#
# print("Уникальные буквы:", unique_letters)
# # Даны два множества A и B
# A = {1, 2, 3, 4}
# B = {5, 6, 7, 8}
#
# # Проверяем, пересекаются ли множества
# if A.isdisjoint(B):
#     print("Множества A и B непересекающиеся.")
# else:
#     print("Множества A и B имеют общие элементы.")



# 14
def missing_consonants(text):
    # Определяем множество согласных букв
    consonants = set("bcdfghjklmnpqrstvwxyz")

    # Приводим текст к нижнему регистру и создаем множество букв в тексте
    text_letters = set(text.lower())

    # Находим согласные, которые не встречаются в тексте
    missing = consonants - text_letters

    # Возвращаем отсортированный список отсутствующих согласных
    return sorted(missing)


# Пример использования
text = "Пример текста для анализа"
missing_consonants_list = missing_consonants(text)
print("Отсутствующие согласные буквы:", missing_consonants_list)
def are_sets_equal(set_a, set_b):
    return set_a == set_b

# Пример использования
set_a = {1, 2, 3, 4}
set_b = {4, 3, 2, 1}
set_c = {1, 2, 3}

print("Множества A и B равны:", are_sets_equal(set_a, set_b))  # True
print("Множества A и C равны:", are_sets_equal(set_a, set_c))  # False
