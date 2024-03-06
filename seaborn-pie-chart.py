import matplotlib.pyplot as plt 
import numpy as np 


# Values for each category
data_values = [42, 30, 18, 10]
category_labels = ["Dogs", "Cats", "Birds", "Fish"]  

# Define colors for pie chart slices
slice_colors = ['#F7CAC9', '#A2D5F2', '#9EE09E', '#C5E0B4'] 

# Create the pie chart with labels, slice colors, and edge settings
plt.pie(data_values, labels=category_labels, colors=slice_colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

# Add Title and Tight Layout
plt.title("Pet Preferences in Our Neighborhood")
plt.tight_layout() 

plt.show()
