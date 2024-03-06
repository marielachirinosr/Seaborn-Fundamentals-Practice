import numpy as np
import matplotlib.pyplot as plt

# Generate sample product ratings
product_ratings = {
    "Quality": np.random.normal(4, 0.8, 50),
    "Durability": np.random.normal(3.5, 0.7, 50),
    "Value for Money": np.random.normal(3.8, 1, 50),
}

# Combine ratings into a NumPy array
combined_ratings = np.column_stack([product_ratings["Quality"], product_ratings["Durability"], product_ratings["Value for Money"]])

# Calculate overall scores 
overall_scores = np.mean(combined_ratings, axis=1)

# Create scatter plot with overall scores determining marker color
plt.scatter(combined_ratings[:, 0], combined_ratings[:, 1], c=overall_scores, cmap='viridis') 

# Add informative colorbar
plt.colorbar(label='Overall Score') 

# Add meaningful labels and title
plt.xlabel('Quality Rating')
plt.ylabel('Durability Rating')
plt.title('Product Ratings with Overall Scores Encoded in Marker Color')

# Show the scatter plot
plt.show()
