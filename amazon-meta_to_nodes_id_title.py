# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:35:34 2019

@author: John
"""

id=[];


title=[]

id_str = ""
asin_str = ""
title_str = ""


count=0

#C:\Users\Ada\Desktop\CUNY_SPS_DA\620_Data_Mining\project1

myfile = open(r"C:\Users\Ada\Desktop\CUNY_SPS_DA\620_Data_Mining\project1\amazon-meta.txt", encoding='utf-8' )

output_file = open(r"C:\Users\Ada\Desktop\CUNY_SPS_DA\620_Data_Mining\project1\amazon-small-meta.csv", encoding='utf-8',  mode = "w+")

output_file2 = open(r"C:\Users\Ada\Desktop\CUNY_SPS_DA\620_Data_Mining\project1\nodes.csv", encoding='utf-8',  mode = "w+")
    

line = myfile.readline() 
    
while line:

    count+=1

    id_str = "" #init value
    asin_str = ""
    title_str = "" #init value
    group_str = "" #init value
    categories_str = "" #init value
        

    if 'Id:' in line:

        numOfId = line[3:].strip()
        id_str = numOfId #id code as string
    
    
        #start after Id line: read in parallel
    
        line = myfile.readline()
    
     
        if 'ASIN:' in line:
        
            asin_str = line[5:].strip()
    
        line = myfile.readline()
        
        if 'title:' in line:
        
            name=line[8:].strip()
            name = name.replace(',',' ')
                        
            title_str = name

        line = myfile.readline()

        if 'group:' in line:
        
            name=line[8:].strip()
                        
            group_str = name

        
        line = myfile.readline() #read after salesrank
        
        line = myfile.readline() #read after similar
        
        line = myfile.readline() 
        

        if 'categories:' in line:
        
            name=line[14:].strip()
            name = name.replace(',',' ')                        
            categories_str = name

        output_file.writelines((id_str + "," + asin_str + "," + title_str + "," + group_str + "," + categories_str + "\n"))
        output_file2.writelines((id_str  + "," + title_str + "\n"))

    
    #skipping line by while loop
    line = myfile.readline()
    
output_file.close()
myfile.close()




