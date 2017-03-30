import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

data = r'data\titanic-data.csv' 

df = pd.read_csv(data)

print df.head()

dead_male = df.loc[(df['Sex'] == 'male') & (df['Survived'] == 0)]
dead_male_group = dead_male.groupby(['Pclass']).count()['Survived']
print dead_male_group

survive_male = df.loc[(df['Sex'] == 'male') & (df['Survived'] == 1)]
survive_male_group = survive_male.groupby(['Pclass']).count()['Survived']
print survive_male_group


dead_female = df.loc[(df['Sex'] == 'female') & (df['Survived'] == 0)]
dead_female_group = dead_female.groupby(['Pclass']).count()['Survived']
print dead_female_group

survive_female = df.loc[(df['Sex'] == 'female') & (df['Survived'] == 1)]
survive_female_group = survive_female.groupby(['Pclass']).count()['Survived']
print survive_female_group

#print df.count()['Survived']

# data to plot
n_groups = 3
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
dead_male_plot = plt.bar(index, dead_male_group, bar_width,
                 alpha=opacity - .2,
                 color='r',
                 hatch='x',
                 label='Dead - Male')

survive_male_plot = plt.bar(index, survive_male_group, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Survived - Male')



dead_female_plot = plt.bar(index + bar_width, dead_female_group, bar_width,
                 alpha=opacity- .2,
                 color='r',
                 hatch='x',
                 label='Dead - Female')

survive_female_plot = plt.bar(index + bar_width, survive_female_group, bar_width,
                 alpha=opacity,
                 color='#ffb6c1',
                 label='Survived - Female') 

 
plt.xlabel('Class')
plt.ylabel('Survivors')
plt.title('Titanic Survivors by Class')
plt.xticks(index + bar_width, ('Upper', 'Middle', 'Lower'))
plt.legend()
 
plt.tight_layout()
plt.show()