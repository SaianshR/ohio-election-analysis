import pandas as pd
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import random

"""Calculates the lift ratio from a given Pandas Dataframe for specified columns/features within the dataset

Keyword arguments:
index -- (list) object containing the items/things of interest to calculate the lift ratio on
data -- (Pandas DataFrame) object with data that has feature/column names that are contained in the 'index' argument
Return: Pandas DataFrame that displays the lift ratios for the given features
"""
def lift_ratio(index : list, data : pd.DataFrame):
    lift_dict = pd.DataFrame(index=index, columns=index)
    total_shape = data.shape[0]
    for i in range(len(index)):
        for j in range(len(index)):
            brand_1 = index[i]
            brand_2 = index[j]
            count_1 = 0
            count_2 = 0
            count_3 = 0
            
            for txt in data.comments.values:
                if brand_1 in txt and brand_2 in txt:
                    count_3 = count_3 + 1
                elif brand_1 in txt and brand_2 not in txt:
                    count_1 = count_1 + 1 
                elif brand_1 not in txt and brand_2 in txt:
                    count_2 = count_2 + 1
            
            if(brand_1==brand_2):
                lift_dict[brand_1][brand_2] = 0

            else:
                pa = count_1/total_shape
                pb = count_2/total_shape
                pab = count_3/total_shape
                ans = (pa*pb)/pab
                
                lift_dict[brand_1][brand_2] = round(1/ans,3)
    return lift_dict.apply(pd.to_numeric).style.background_gradient(axis=0,cmap='Blues')



"""Display a multi-dimensional scaling graph

Keyword arguments:
mdslifts -- (Pandas DataFrame) object that contains the lift values for features 
points -- (list) that contains the desired feature names found in the 'mdslifts' (Pandas DataFrame)
Return: Displays a multi-dimensional scaling graph of the given dataframe's features
"""
def multi_dimensional_scaling(mdslifts : pd.DataFrame, points : list):
    mdslifts.reset_index(drop=True, inplace=True)
    mds = MDS(random_state=0)
    mdslifts = mds.fit_transform(mdslifts)

    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(len(points))]

    size = [64 for i in range(len(points))] ##41FB29
    fig = plt.figure(2, (10,4))
    plt.scatter(mdslifts[:,0], mdslifts[:,1], s=size, c=colors)
    count = 0
    for x, y in zip(mdslifts[:,0], mdslifts[:,1]):
        label = "{0}".format(points[count])
        count += 1
        plt.annotate(label, # this is the text
                    (x,y), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha=('center') # horizontal alignment
        )
    plt.title('mds')
    return plt.show()

"""Applies scalar modification to lift value dataframe to reshape for MDS plot

Keyword arguments:
df -- (Pandas Dataframe)
threshold_1 -- (float) value determine which lift value to modify
threshold_2 -- (float) value determine which lift value to modify
scale_1 -- (float) value to modify lift value
scale_2 -- (float) value to modify lift value
Return: Dataframe with the rescaled/modified lift values
"""
# NOTE: Can improve this code by making it able to accept multiple arguments ex. using **args with nested loop of comparison
# What I mean is take the "If value > threshold: ..." and make it its own function to accept any number of keywords.
def lift_adjustment(df : pd.DataFrame, threshold_1 : float, threshold_2 : float, threshold_3 : float, scale_1 : float, scale_2 : float, scale_3 : float):
    col_names = [x for x in df.columns]
    new_arr = []
    for row in df.values:
        new_val = []
        for value in row:
            if value > threshold_1:
                value = value * scale_1
            if value > threshold_2:
                value = value * scale_2
            if value > threshold_3:
                value = value * scale_3
            new_val.append(value)
        new_arr.append(new_val)
    complete_df = pd.DataFrame(new_arr, columns=col_names)
    return complete_df