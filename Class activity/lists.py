from operator import concat


Friends = ["Micheal", "Raheem", "Jadon", "Raphael", "Zuraiz", "Alan", "Jasper", "Abubakr", "Faham", "Omer"]
print(Friends)
print(Friends[5])
print(Friends[0])
print(Friends[4])
print(Friends[7])
print(Friends[0:4])
print(Friends[-1])
print(Friends[-2])
pre = Friends[0], Friends[-1]
print(pre)
Friends[8] = "Joshua"
print(Friends)
Friends[0:1] = "Hamad", "Lee"
print(Friends)
Friends.insert(0, "Faham")
print(Friends)
Friends.insert(6, "Umer")
Friends.insert(-1, "Osman")
print(Friends)
Friends.remove("Alan")
print(Friends)
Friends.pop(0)
letters = ["A", "B", "C", "D"]
print(Friends+letters)
num = [6, 5, 8, 5, 9, 0, 3]
num.sort()
print(num)
num.reverse()
print(num)



