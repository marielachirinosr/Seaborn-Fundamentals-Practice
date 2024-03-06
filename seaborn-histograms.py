import numpy as np
import matplotlib.pyplot as plt

# Experiment data (replace with your actual data)
experiment_data = np.array([189, 185, 195, 149, 189, 147, 154,
                           174, 169, 195, 159, 192, 155, 191, 134, 144, 137, 139,
                           153, 157, 140, 144, 172, 157, 181,
                           182, 166, 167, 140, 130, 150, 190, 171, 189, 142, 153, 159, 161, 169, 165, 133, 188])

# Calculate median and standard deviation
median = np.median(experiment_data)
standard_deviation = np.std(experiment_data)

# Print calculated values (optional)
print(f"Median: {median:.2f}")
print(f"Standard Deviation: {standard_deviation:.2f}")

# Plot the distribution of the data with 10 bins, left-aligned, blue color, and red edges
plt.hist(experiment_data, bins=22, align='left', color='orange')

# Add informative axis labels and title
plt.xlabel("Experiment Data Values")
plt.ylabel("Frequency")
plt.title("Distribution of Experiment Data")

# Display the histogram
plt.show()
