import pandas as pd
import numpy as np


class DataLoader():#inorder to load our data set to our project we refer this class
    #..........This Contains Varibles Like.....
    #path_video      -->
    #path_labels     -->
    #path_train      -->
    #path_validation -->
    #path_test       -->
    def __init__(self,path_video,path_labels,path_train=None,path_validation=None,path_test=None):
        self.path_video=path_video
        self.path_labels=path_labels
        self.path_train=path_train
        self.path_validation=path_validation
        self.path_test=path_test

        self.get_labels(self.path_labels)
    
    def get_labels(self,path_labels):#used to get names of our labels and create dictionary for easy access through key-value pair

        self.lables_df=pd.read_csv(path_labels,names=["labels"])#we create dataframe inorder to obtain only column with path_labels

        self.labels=[str(labels[0]) for labels in self.lables_df.values] #we etarct label names into list for easy access

        self.n_labels=len(self.labels) # we get the count of lables present in our data set

        self.label_to_int=dict(zip(self.labels,range(self.n_labels))) # we create dictionary with key as labels and values as its corresponding integers

        self.int_to_label=dict(enumerate(self.labels)) # we create dictionary with key as integer and corresponding  values as labels

        


        
