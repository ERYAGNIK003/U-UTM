import os 
import csv
import numpy as np


vids=["Video4","Video5","Video6","Video7","Video8"]
for vid in vids:
    f=open(vid+".csv")
    csvR=csv.reader(f)
    _=next(csvR)
    totalT=[]
    totalObjs=[]
    #Frame,Objects,Pre-processing Time,Inference Time,Post-processing Time
    for row in csvR:
        totalObjs.append(int(row[1]))
        totalT.append(float(row[2])+float(row[3])+float(row[4]))
    f.close()
    print("Video {} has average objects/frame {} time {}".
          format(vid,round(np.mean(totalObjs),0),round(np.mean(totalT),2)))





