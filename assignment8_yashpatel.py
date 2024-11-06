import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris Dataset
iris_df = pd.read_csv('iris.csv')

# Scatter Plot of Sepal Length vs Sepal Width
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris_df, x='sepal_length', y='sepal_width', hue='species', palette='viridis')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(title='Species')
plt.show()

# Box Plot of Petal Length by Species
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris_df, x='species', y='petal_length', palette='viridis')
plt.title('Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# Pair Plot of All Features
sns.pairplot(iris_df, hue='species', palette='viridis')
plt.suptitle('Pair Plot of All Features', y=1.02)
plt.show()