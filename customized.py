import matplotlib.pyplot as plt
months = [1,2,3,4,5,6]
sales = [100,200,300,400,500,600]
plt.plot(months,sales)
plt.xlabel("months")
plt.ylabel("sales")
plt.title("monthly sales data")
plt.show()