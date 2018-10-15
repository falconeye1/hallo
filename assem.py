#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:57:51 2018

@author: awad
"""
o=open("SRR7534266.fastq",'r')
z=list(o)
p=open('SRR7534266_1.fas','w')
q=open('SRR7534266_titles_1.txt','w')
r=open('SRR7534266_seq_1.txt','w')
s=open('SRR7534266_quality_1.txt','w')
qq=open('Tag_SRR7534266_titles_1.txt','w')
rr=open('Tag_SRR7534266_seq_1.txt','w')
ss=open('Tag_SRR7534266_quality_1.txt','w')
'''
lines_no = sum(1 for line in o) #139294512
'''
a,b,c=[],[],[]
n=0
m=[]
while n<=len(z):
    m.append(n)
    n=n+4
n=1
mm=[]
while n<=len(z):
    mm.append(n)
    n=n+4
n=2
mmm=[]
while n<=len(z):
    mmm.append(n)
    n=n+4
n=3
mmmm=[]
while n<=len(z):
    mmmm.append(n)
    n=n+4
n=0
while n<len(z)-1:
    d=z[n]
    if n in m:
        a.append(d)
        p.writelines(str(d))
        q.writelines(str(d))
        qq.writelines(str(n)+'\t'+str(d))
        n=n+1
    elif n in mm:
        b.append(str(d))
        p.writelines(str(d))
        r.writelines(str(d))
        rr.writelines(str(n)+'\t'+str(d))
        n=n+1
    elif n in mmmm:
        c.append(d)
        s.writelines(str(d))
        ss.writelines(str(n)+'\t'+str(d))
        n=n+1
    else:
        n=n+1
        print(n)
o.close()
p.close()
q.close()
r.close()
s.close()
qq.close()
rr.close()
ss.close()

