import matplotlib.pyplot as plt


x =[0.5,1,2,3,4]
y = [0,7,0,7,0]

plt.plot(x,y)
plt.show()

w = [1,2,3,4,5,6]
z = [2,3,4,5,6,7]


plt.bar(w,z)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()



plt.title("Transport")
plt.pie(x, labels=["Train","Car","Bus","Airplane","Ship"])
plt.show()