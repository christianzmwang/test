
import numpy as np
from statistics import mean
import math

# Gravitational constant
g = 9.81 

# Mass of brio train in kg
m = 0.086

# f due to g for each incline 
f = [round(m * g * math.sin(math.radians(i)), 5) for i in range(0, 31, 5)][::-1]

# Function to group sublists in list
def group(lst, size):
  return [lst[i:i+size] for i in range(0, len(lst), size)]

with open("IA/data.txt") as file:
  content = file.read()

lst = list( map(float, content.split() ) ) 

array_data_split = group(group(lst, 5), 2) 
ads_mean = [ round(mean(k), 2) for i, l in enumerate(array_data_split) for k in l]
ads_mean_grouped = group(ads_mean, 2)

ads_mean_v = list(map(lambda x: round( (1/x)  , 5), ads_mean ) )
ads_mean_v_grouped = group(ads_mean_v, 2)


array_data_joined = np.array(group(lst, 10))
adj_mean = np.fromiter(map(lambda x: mean(x), array_data_joined), float )

