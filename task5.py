import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
data = pd.read_csv('D:\cleaned.csv')

# Setting up the visual style
sns.set(style="whitegrid")

# Accident Distribution by Road Surface Type and Weather Conditions
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Road Surface Type
sns.countplot(data=data, x='Road_surface_type', hue='Accident_severity', palette='viridis', ax=axes[0])
axes[0].set_title('Accidents by Road Surface Type and Severity')
axes[0].set_xlabel('Road Surface Type')
axes[0].set_ylabel('Number of Accidents')

# Weather Conditions
sns.countplot(data=data, x='Weather_conditions', hue='Accident_severity', palette='viridis', ax=axes[1])
axes[1].set_title('Accidents by Weather Conditions and Severity')
axes[1].set_xlabel('Weather Conditions')
axes[1].set_ylabel('Number of Accidents')

plt.tight_layout()
plt.show()