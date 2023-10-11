import os
import numpy as np
import pandas as pd

baseDir = '/home/bulk826/Desktop/Stanford/CS230/project'
a = pd.read_csv(baseDir+'/train_info.csv') 

print(a)
all_names = list(a['filename']) 
all_dates = list(a['date'])
print(all_dates)

data_path = "/home/bulk826/Downloads"
batch = 'train_7'
target = 'full7'
train2_names = os.listdir(data_path+'/'+batch)
#print(train2_names)

with open(baseDir+'/N2.txt', 'w+') as f1:
    print('# Names of all pictures', end = '\n', file = f1)

with open(baseDir+'/D2.txt', 'w+') as f2:
    print('# Year of all pictures', end = '\n', file = f2)

D = []

for i in range(len(train2_names)):
    print(i)
    idi = all_names.index(train2_names[i])
    n = train2_names[i]
    d = all_dates[idi]
    
    try:
        d = int(d)
        with open(baseDir+'/N2.txt', 'a+') as f1:
            print(n+' '+str(d), end = '\n', file = f1)
        with open(baseDir+'/D2.txt', 'a+') as f2:
            print(d, end = '\n', file = f2)
        
        #print(d)
        if d < 1300:
            os.system('mkdir '+data_path+'/'+target+'/train/1000_1200')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1000_1200')
        elif (d >= 1300 ) and (d < 1400):
            os.system('mkdir '+data_path+'/'+target+'/train/1300')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1300')
        elif (d >= 1400 ) and (d < 1500):
            os.system('mkdir '+data_path+'/'+target+'/train/1400')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1400')
        elif (d >= 1500 ) and (d < 1600):
            os.system('mkdir '+data_path+'/'+target+'/train/1500')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1500')
        elif (d >= 1600 ) and (d < 1700):
            os.system('mkdir '+data_path+'/'+target+'/train/1600')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1600')
        elif (d >= 1700 ) and (d < 1800):
            os.system('mkdir '+data_path+'/'+target+'/train/1700')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1700')
        elif (d >= 1800 ) and (d < 1900):
            os.system('mkdir '+data_path+'/'+target+'/train/1800')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1800')
        elif (d >= 1900 ) and (d < 2000):
            os.system('mkdir '+data_path+'/'+target+'/train/1900')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/1900')
        else:
            os.system('mkdir '+data_path+'/'+target+'/train/2000')
            os.system('mv '+data_path+'/'+batch+'/{} '.format(n)+data_path+'/'+target+'/train/2000')
    except:
        continue
    
    
        
    

#f1.close()
#f2.close()