import matplotlib.pyplot as plt

# Step 1: Define data
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]

# Step 2: Create line plot
plt.plot(months, revenue)

# Step 3: Add title and labels
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

# Step 4: Show plot
plt.show()
