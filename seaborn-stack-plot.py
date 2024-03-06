import numpy as np
import matplotlib.pyplot as plt

# Sample sales data
sales_data = np.array([
    [2500, 1800, 3200, 1500],  # Salesperson 1
    [3000, 2100, 2500, 2000],  # Salesperson 2
    [2800, 2300, 2900, 1800],  # Salesperson 3
])

# Calculate total sales for each product category
product_totals = np.sum(sales_data, axis=0)

# Calculate percentages of each salesperson's contribution to product category sales
percentages = sales_data / product_totals[np.newaxis, :] * 100

# Create a 100% stacked plot
fig, ax = plt.subplots()
product_categories = ["Earphones", "Screen Protector", "Smartphone", "Glasses"] 

# Stack bars for each salesperson, assigning meaningful labels
ax.stackplot(product_categories, percentages, labels=["Salesperson 1", "Salesperson 2", "Salesperson 3"])

# Add a legend and informative labels
ax.legend(loc='upper left')
ax.set_xlabel("Product Categories")
ax.set_ylabel("Percentage of Sales Contribution")
ax.set_title("Salesperson Contribution to Product Categories (100% Stacked)")

# Display the plot
plt.show()
