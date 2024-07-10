import numpy as np
import os
import csv
avgErr=0

logfiles=["Video1_errorlog.csv","Video2_errorlog.csv","Video3_errorlog.csv"]
for log in logfiles:
    errE=0
    errT=0
    cnt=0
    f=open(log)
    csvR=csv.reader(f)
    _=next(csvR)
    for row in csvR:
        cnt+=1
        errE+=float(row[8])
        errT+=float(row[9])
    f.close()
    rmseE=np.sqrt(errE/cnt)
    rmseT=np.sqrt(errT/cnt)
    diff=rmseT-rmseE
    improve=round(diff*100/rmseT,2)
    avgErr+=improve
    print("For log {} RMSE-T {} RMSE-E {} Improvement {}".format(log,rmseT,rmseE,improve))
print("Overall Improvement ",avgErr/(len(logfiles)))
