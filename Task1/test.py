import matplotlib.pyplot as plt

# Data for the first scatter plot
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

# Data for the second scatter plot
x2 = [1, 2, 3, 4, 5]
y2 = [3, 5, 7, 11, 13]

# Create a figure and two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the first scatter plot
ax1.scatter(x1, y1, color='blue', label='First Scatter Plot')
ax1.set_title('First Scatter Plot')
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y Axis')

# Plot the second scatter plot
ax2.scatter(x2, y2, color='red', label='Second Scatter Plot')
ax2.set_title('Second Scatter Plot')
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y Axis')

# Add legend to each subplot
ax1.legend()
ax2.legend()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
