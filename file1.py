import numpy as np
import re
import json
count_Words={}
def createDictionary(l):
    for i in range(0,len(l)):

        if l[i].lower() not in count_Words:
            count_Words[l[i].lower()]=1
        else:
            count_Words[l[i].lower()]+=1
            



all_strings=[]
if __name__=="__main__":
    with open('output.txt','r',encoding='utf-8') as f:
        
        for x in f.readlines():
            arr=x.split(',')
            
            for i in range(0,len(arr)):
                line_String=arr[i].split(' ')

                for j in range(0,len(line_String)):
                    if re.match(r'^[a-zA-Z]{3,}$',line_String[j]):
                        
                        all_strings.append(line_String[j])


    createDictionary(all_strings)
    #print(count_Words)

    f=open('finally_dictionary.json','w')
    f.write(json.dumps(count_Words))
    print("Ended")