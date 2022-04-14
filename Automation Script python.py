import pandas as pd
import numpy as np

pth= input("Enter the file path in csv without quotation marks\n")
df = pd.read_csv(pth)
arr = df.to_numpy()
on = False
i = 0
t=0
for row in arr:
    if i+1>= len(arr):
        break
    X = row[7]
    if isinstance(X,type(np.nan))==True:
        pass 
    elif X[:3]=="PSP":
        on = True

    elif X[:3]=="Bre" :
        on = False
        t=0

    if on ==True:
        row[8]= t
        t+=1

    print(t)

for row in arr:
    if i+1>= len(arr):
        break

    D48=arr[i][3]
    D49=arr[i+1][3]
    I49=arr[i+1][8]
    I48=arr[i][8]
    C48=arr[i][2]
    C49=arr[i+1][2]
    K48=(C48+C49)/2*(I49-I48)
    G48=arr[i][6]
    
    j = (D48+D49)/2*(I49-I48)
    k = (C48+C49)/2*(I49-I48)
    l = K48*G48
    
    print(K48,G48)
    if k <0:
        k=0
    if l<0:
        l=0
   #print(D48,D49,I49,I48,C48,C49,K48,G48)
    #print(f"j:{j},k:{k},l:{l}")
    X = row[7]
    if isinstance(X,type(np.nan))==True:
        print("passed")
    elif X[:3]=="PSP":
        print("psp detected")
        on = True

    elif X[:3]=="Bre" :
        print("break detected")
        on = False

    
    if on ==True:
        print("on true")
        row[9] = j
        row[10] = k
        print(l)
        row[11] = l
    i+=1

for row in arr:
    X = row[7]
    if isinstance(X,type(np.nan))==True:
        pass
    elif X[:3]=="PSP":
        row[8]=np.nan
        row[9]=np.nan
        row[10]=np.nan
        row[11]=np.nan
    elif X[:3]=="Bre" :
        print("break detected")
        on = False


final_df = pd.DataFrame(arr,columns=df.columns)
with pd.ExcelWriter("output.xlsx") as writer:
    final_df.to_excel(writer,index=False)  

input("Done")