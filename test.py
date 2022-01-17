import pickle
import numpy as np

# F1=open(r'newprocess_datacopy.pkl','rb')
# newcontent=pickle.load(F1)
# print(len(newcontent))
#
# F2=open(r'process_datacopy.pkl','rb')
# content=pickle.load(F2)
# print(len(content))

# print(content==newcontent)
F0=open(r'process_datacopy0.pkl','rb')
content0=pickle.load(F0)
print(len(content0))
F1=open(r'process_datacopy1.pkl','rb')
content1=pickle.load(F1)
F2=open(r'process_datacopy2.pkl','rb')
content2=pickle.load(F2)
F3=open(r'process_datacopy3.pkl','rb')
content3=pickle.load(F3)
F4=open(r'process_datacopy4.pkl','rb')
content4=pickle.load(F4)
F5=open(r'process_datacopy5.pkl','rb')
content5=pickle.load(F5)
F6=open(r'process_datacopy6.pkl','rb')
content6=pickle.load(F6)
F7=open(r'process_datacopy7.pkl','rb')
content7=pickle.load(F7)

content=content0+content1+content2+content3+content4+content5+content6+content7
#
open('process_datacopy.pkl', "wb").write(pickle.dumps(content))
# for i in range(8):
#     shuzi=i*15000
#     if i==7:
#         open('process_datacopy%d.pkl' % i, "wb").write(pickle.dumps(content[shuzi:]))
#         break
#     open('process_datacopy%d.pkl'%i, "wb").write(pickle.dumps(content[shuzi:shuzi+15000]))

# ho=open("partofdict.txt","w")
# lst=[]
# for i in range(20):
#     for j in content[i]:
#         lst.append(j)
#         lst.append("\n\n")
#         lst.append(content[i][j])
#         lst.append("\n\n")
#     lst.append("\n\n")
# print(lst)
# ho.writelines(lst)
# for i in content.keys():
#     print(i,":",content[i])
# print(content[0]["newtree"])
# print(content[0]["new"])