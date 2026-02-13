import matplotlib.pyplot as plt
products = ["Laptop","Mobile","Tablet","Headphones"]
sales = [150,200,100,80]
plt.bar(products,sales)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title(" Sales per Product")
plt.show()