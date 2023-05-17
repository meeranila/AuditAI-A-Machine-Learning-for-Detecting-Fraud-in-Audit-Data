# -*- coding: utf-8 -*-
"""ASSIGNMENT 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1duXU2ZC9MJwxw8HHu9var59Sel6CWNZF
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #simple data visualization
# %matplotlib inline
import seaborn as sns #some advanced data visualizations
import warnings
warnings.filterwarnings('ignore') # to get rid of warnings
plt.style.use('seaborn-white') #defining desired style of viz

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('/content/penguins_size.csv')
original = df.copy()

print('Dataset has', df.shape[0] , 'rows and', df.shape[1], 'columns')

df.info()

df.describe()

df.isnull().sum()

df.head(10)

plt.rcParams['figure.figsize'] = (10,7)

df['species'].value_counts(normalize = True).plot(kind = 'bar', color = 'seagreen', linewidth = 1, edgecolor = 'k')
plt.title('Penguin Species')
plt.xlabel('Species')
plt.ylabel('% (100s)')
plt.xticks(rotation = 360)
plt.show()

df['island'].value_counts(normalize = True).plot(kind = 'bar', color = 'seagreen', linewidth = 1, edgecolor = 'k')
plt.title('Islands where Penguins live')
plt.xlabel('Island')
plt.ylabel('% (100s)')
plt.xticks(rotation = 360)
plt.show()

df['sex'].value_counts(normalize = True).plot(kind = 'bar', color = 'seagreen', linewidth = 1, edgecolor = 'k')
plt.title('Penguins - Sex')
plt.xlabel('Sex')
plt.ylabel('% (100s)')
plt.xticks(rotation = 360)
plt.show()

def ecdf(x):
    n = len(x)
    a = np.sort(x)
    b = np.arange(1, 1 + n) / n
    plt.subplot(211)
    plt.plot(a, b, marker = '.', linestyle = 'None', c = 'seagreen')
    mean_x = np.mean(x)
    plt.axvline(mean_x, c = 'k', label = 'Mean')
    plt.title('ECDF')
    plt.legend()
    plt.show()
    plt.subplot(212)
    sns.distplot(x, color = 'r')
    plt.title('Probability Density Function')
    plt.show()

ecdf(df['culmen_length_mm'])

ecdf(df['culmen_depth_mm'])

ecdf(df['flipper_length_mm'])

ecdf(df['body_mass_g'])

def box(f):
    sns.boxplot(y = f, x = 'species', hue = 'sex',data = df)
    plt.title(f)
    plt.show()

box('culmen_length_mm')

box('culmen_depth_mm')

box('flipper_length_mm')

box('body_mass_g')

sns.pairplot(df, hue = 'species')
plt.show()

new_df = original.copy()

new_df['culmen_length_mm'].fillna(np.mean(original['culmen_length_mm']), inplace = True)
new_df['culmen_depth_mm'].fillna(np.mean(original['culmen_depth_mm']), inplace = True)
new_df['flipper_length_mm'].fillna(np.mean(original['flipper_length_mm']), inplace = True)
new_df['body_mass_g'].fillna(np.mean(original['body_mass_g']), inplace = True)
new_df['sex'].fillna(original['sex'].mode()[0], inplace = True)

new_df.isnull().sum()

print('Skewness of numeric variables')
print('-' * 35)

for i in new_df.select_dtypes(['int64', 'float64']).columns.tolist():
    print(i, ' : ',new_df[i].skew())