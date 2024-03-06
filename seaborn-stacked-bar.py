import matplotlib.pyplot as plt 
import numpy as np  

# Prepare data 
categories = ['Category 1', 'Category 2', 'Category 3']  
values_group1 = np.array([25, 35, 15, 40])  
values_group2 = np.array([18, 32, 22, 30])  
values_group3 = np.array([12, 19, 28, 15])  
values_group4 = np.array([10, 31, 17, 25])  

# Create a stacked bar chart 
plt.bar(categories, values_group1, color='red', label='Group 1')
plt.bar(categories, values_group2, bottom=values_group1, color='blue', label='Group 2')
plt.bar(categories, values_group3, bottom=values_group1 + values_group2, color='yellow', label='Group 3')

# Add descriptive labels and title:
plt.xlabel("Categories")
plt.ylabel("Total Values")  
plt.title("Total Values for Each Category Across Four Groups")  
plt.legend()  

# Display the chart
plt.show()
