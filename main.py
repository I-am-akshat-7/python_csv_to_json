# import all the modules
import pandas as pd
import json
import os




def csv_to_json(f1, f2):
    
    
    if f2 in os.listdir():  # checks if the output file already exists in the directory
        
        print("file already exists ")
        raise FileExistsError
        
        
        
    else:
        f2 = open(f2, 'w')
        
        df = pd.read_csv(f1)  # reading the csv file 
        
        
        l = df.columns.tolist()
        l1 = []

        

        
        for i in range(len(l)):


            l1.append(df[l[i]].tolist())



        d = dict(zip(l, l1))  # using zip to concatenate lists into dict


        json.dump(d, f2)

        return d # returns the csv file into a dictionary



    
