import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'x': [1, 2, 3, 4, 5],
        'y': [2, 3, 5, 7, 11],
        'variable': ['A', 'A', 'B', 'B', 'A']}

# Create a DataFrame
df = pd.DataFrame(data)

# Create scatter plot with different colors for each variable
plt.scatter(df[df['variable'] == 'A']['x'], df[df['variable'] == 'A']['y'], color='red', label='Variable A')
plt.scatter(df[df['variable'] == 'B']['x'], df[df['variable'] == 'B']['y'], color='blue', label='Variable B')

# Add labels, legend, and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Scatter Plot with Different Colors for Each Variable')

# Show plot
plt.show()