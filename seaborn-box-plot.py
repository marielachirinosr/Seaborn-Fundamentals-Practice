import matplotlib.pyplot as plt

# Sample exam scores for three subjects
exam_scores = {
    "Mathematics": [85, 78, 92, 80, 75, 90, 82],
    "Physics": [70, 82, 75, 88, 65, 95, 78],
    "Chemistry": [68, 80, 72, 85, 70, 92, 84],
}

# Extract exam scores into separate lists for box plot creation
math_scores = exam_scores["Mathematics"]
physics_scores = exam_scores["Physics"]
chemistry_scores = exam_scores["Chemistry"]

# Create the box plot with different colors and customizations
plt.boxplot(
    [math_scores, physics_scores, chemistry_scores],
    notch=True,  
    vert=True,  
    patch_artist=True, 
    widths=0.5,  
    labels=["Math", "Physics", "Chemistry"],  
    showmeans=True,  
    medianprops={"linewidth": 2, "color": "blue"},  
    boxprops={"facecolor": "lightblue", "edgecolor": "green"},  
    capprops={"linewidth": 2, "color": "red"},  
    whiskerprops={"linewidth": 2, "color": "red"},  
    flierprops={"marker": "o", "markerfacecolor": "yellow", "markeredgewidth": 1, "markeredgecolor": "black"},  
)

# Add informative labels and title
plt.xlabel("Subjects")
plt.ylabel("Exam Scores")
plt.title("Exam Score Distribution Across Subjects")

# Display the box plot
plt.show()
