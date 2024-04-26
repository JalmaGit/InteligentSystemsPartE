import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': ['X', 'Y', 'X', 'Z', 'Y']}
df = pd.DataFrame(data)

df.hist()

# Remove rows with 'X' in column 'B'
df = df[df['B'] != 'X']

df.hist()
plt.show()