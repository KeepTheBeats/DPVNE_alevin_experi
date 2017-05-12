#coding:utf-8

import re
import sys

if __name__=="__main__":
    b=open("data\\"+sys.argv[1]+".txt","w")
    
    i=10
    while(i<101):
        if(sys.argv[1]=="nr"):
            a=open("data\\results_10_200_undi\\"+str(i)+"\\DPVNE-AdvSubgraph_out.txt","r")
        else:
            a=open("data\\results_ps\\"+str(i)+"\\DPVNE-AdvSubgraph_out.txt","r")

        l1=a.readline()
        l2=a.readline()
        rl1 = re.split("_",l1)
        rl2 = re.split("_",l2)
        rl135 = re.split("\n",rl1[35])
        rl235 = re.split("\n",rl2[35])

        #for test 
        #print(len(rl1))
        #print(len(rl2))
        #print(rl1[34])
        #print(rl1[35])
        #print(rl2[35])

        b.writelines(str(i)+" VNRs\n")
        j = 0
        while(j<len(rl1)):
            if(j!=35):
                b.writelines(rl1[j]+" : "+rl2[j]+"\n")
            else:
                b.writelines(rl135[0]+" : "+rl235[0]+"\n")
            j=j+1
        b.writelines("\n\n")
        a.close()
        i=i+10

    b.close()
