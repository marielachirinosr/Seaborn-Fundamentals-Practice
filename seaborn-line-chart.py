import matplotlib.pyplot as plt
import numpy as np

# Sample data for innings and scoring rate
innings = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
scoring_rate = [4.5, 5, 5.5, 6, 6.2, 7, 7.5, 8, 8.2, 8.5]

# Create two subplots for side-by-side arrangement
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6)) 

# Plot scoring rate for the first chart
ax1.plot(innings, scoring_rate, label='Scoring Rate')

# Customize ticks and labels for the first chart
ax1.set_xticks([x for x in np.arange(2, 21, 2)])
ax1.set_yticks([x for x in np.arange(4, 9, 0.5)])
ax1.set_title("Overall Scoring Rate")
ax1.set_xlabel("Innings")
ax1.set_ylabel("Scoring Rate")
ax1.legend()

# Sample data for innings and scoring rate for two different teams
team1_scoring_rate = [4.5, 5, 5.5, 6, 6.2, 7, 7.5, 8, 8.2, 8.5]
team2_scoring_rate = [4, 4.8, 5.2, 6.5, 7, 7.2, 7.8, 8.5, 8.8, 9]

# Plot scoring rate for each team in the second chart
ax2.plot(innings, team1_scoring_rate, label='Team 1 Scoring Rate')
ax2.plot(innings, team2_scoring_rate, label='Team 2 Scoring Rate')

# Customize ticks and labels for the second chart
ax2.set_xticks([x for x in np.arange(2, 21, 2)])
ax2.set_yticks([x for x in np.arange(4, 10, 0.5)])
ax2.set_title("Team-wise Scoring Rates")
ax2.set_xlabel("Innings")
ax2.set_ylabel("Scoring Rate")
ax2.legend()

# Adjust layout to prevent overlapping elements
plt.tight_layout()

plt.show()
