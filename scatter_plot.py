import matplotlib.pyplot as plt
study_hours =[7,8,3,4,8]
marks = [85,89,66,67,56]
plt.scatter(study_hours,marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()