# for clarification, not all of this code is mine

# other contributions are made by:
# absolllute/wegfan - for the encryption/decryption code for the save file
# harm - encryption/decryption code for the level

# everything else is made by me

import pygame
import sys
import os
import math
from pygame.locals import *
import base64
import gzip
import struct
import traceback
import zlib
from xml.dom import minidom
sub = os.path.dirname(os.path.abspath(__file__))
sub2 = []
sub3 = ""
for i in range(len(sub)):
    if sub[i] == "\\":
        sub2.append(sub3)
        sub3 = ""
    else:
        sub3 += sub[i]
mFilePath = ""
for i in range(3):
    for j in range(len(sub2[i])):
        mFilePath += sub2[i][j]
    mFilePath += "\\"
mFilePath += "AppData\\Local\\GeometryDash\\CCLocalLevels.dat"
class poly:
    def __init__(self, c):
        self.c = c
    def f(self, x):
        final = 0
        for i in range(len(self.c)):
            final += pow(x,len(self.c)-i-1)*self.c[i]
        return final
def dPoly(x):
    final = []
    for i in range(len(x.c)-1):
        final.append(x.c[i]*(len(x.c)-i-1))
    return poly(final)
def polyMult(p1,p2):
    final = []
    finalDeg = len(p1.c)+len(p2.c)-1
    for i in range(finalDeg):
        final.append(0)
    for i in range(len(p1.c)):
        for j in range(len(p2.c)):
            final[i+j] += p1.c[i]*p2.c[j]
    return poly(final)
def add(p1,p2):
    final = []
    if len(p1.c) == len(p2.c):
        for i in range(len(p1.c)):
            final.append(p1.c[i]+p2.c[i])
    else:
        if len(p1.c) > len(p2.c):
            for i in range(len(p1.c)):
                if len(p2.c) < len(p1.c)-i:
                    final.append(p1.c[i])
                else:
                    final.append(p1.c[i]+p2.c[i-len(p1.c)+len(p2.c)])
        else:
            for i in range(len(p2.c)):
                if(len(p1.c) < len(p2.c)-i):
                    final.append(p2.c[i])
                else:
                    final.append(p2.c[i]+p1.c[i-len(p2.c)+len(p1.c)])
    return poly(final)
class full:
    def __init__(self, l, pt):
        self.l = l
        self.pt = pt
    def f(self, x):
        cot = []
        cut = []
        for i in range(len(self.l)):
            if self.l[i][0] == 0:
                cot.append(True)
                sub = self.l[i][1].f(x)
                if self.l[i][2] == 1:
                    sub = math.sqrt(sub)
                elif self.l[i][2] == 2:
                    sub = math.sin(sub)
                elif self.l[i][2] == 3:
                    sub = math.cos(sub)
                if self.l[i][3]:
                    sub = -sub
                cut.append(sub)
            else:
                cot.append(False)
                cut.append(0)
        run = False
        for i in range(len(cot)):
            if not cot[i]:
                run = True
        while(run):
            fin = []
            for i in range(len(cot)):
                if not cot[i]:
                    sub = True
                    if self.l[i][0] == 1:
                        for j in range(len(self.l[i][1])):
                            for k in range(len(self.l[i][1][j])):
                                if not cot[self.l[i][1][j][k]]:
                                    sub = False
                        if sub:
                            sub2 = 0
                            for j in range(len(self.l[i][1])):
                                sub3 = 1
                                for k in range(len(self.l[i][1][j])):
                                    sub3*=cut[self.l[i][1][j][k]]
                                sub2+=sub3
                            if self.l[i][2] == 1:
                                sub2 = math.sqrt(sub2)
                            elif self.l[i][2] == 2:
                                sub2 = math.sin(sub2)
                            elif self.l[i][2] == 3:
                                sub2 = math.cos(sub2)
                            if self.l[i][3]:
                                sub2 = -sub2
                            cut[i] = sub2
                    elif self.l[i][0] == 2:
                        for j in range(len(self.l[i][1])):
                            if not cot[self.l[i][1][j]]:
                                sub = False
                        if sub:
                            if abs(cut[self.l[i][1][1]]) > 0:
                                sub2 = cut[self.l[i][1][0]]/cut[self.l[i][1][1]]
                            else:
                                sub2 = 0
                            if self.l[i][2] == 1:
                                sub2 = math.sqrt(sub2)
                            elif self.l[i][2] == 2:
                                sub2 = math.sin(sub2)
                            elif self.l[i][2] == 3:
                                sub2 = math.cos(sub2)
                            if self.l[i][3]:
                                sub2 = -sub2
                            cut[i] = sub2
                    cot[i] = sub
            run = False
            for i in range(len(cot)):
                if not cot[i]:
                    run = True
        final = 0
        for i in range(len(self.pt)):
            sub = 1
            for j in range(len(self.pt[i])):
                sub *= cut[self.pt[i][j]]
            final += sub
        return final
def depWeb(x):
    final = []
    sub2 = []
    for i in range(len(x.pt)):
        for j in range(len(x.pt[i])):
            sub = True
            count = 0
            while sub and count < len(sub2):
                if sub2[count] == x.pt[i][j]:
                    sub = False
                count += 1
            if sub:
                sub2.append(x.pt[i][j])
    final.append(sub2)
    run = True
    while run:
        sub2 = []
        for i in range(len(final[-1])):
            if x.l[final[-1][i]][0] == 1:
                for j in range(len(x.l[final[-1][i]][1])):
                    for k in range(len(x.l[final[-1][i]][1][j])):
                        sub = True
                        count = 0
                        while sub and count < len(sub2):
                            if sub2[count] == x.l[final[-1][i]][1][j][k]:
                                sub = False
                            count += 1
                        if sub:
                            sub2.append(x.l[final[-1][i]][1][j][k])
            elif x.l[final[-1][i]][0] == 2:
                for j in range(len(x.l[final[-1][i]][1])):
                    sub = True
                    count = 0
                    while sub and count < len(sub2):
                        if sub2[count] == x.l[final[-1][i]][1][j]:
                            sub = False
                        count += 1
                    if sub:
                        sub2.append(x.l[final[-1][i]][1][j])
        if len(sub2) == 0:
            run = False
        else:
            final.append(sub2)
    needed = []
    for i in range(len(x.l)):
        needed.append(False)
    for i in range(len(final)):
        for j in range(len(final[i])):
            needed[final[i][j]] = True
    return needed
def singleDep(x,s):
    final = []
    for i in range(len(x.l)):
        if x.l[i][0] == 1:
            for j in range(len(x.l[i][1])):
                for k in range(len(x.l[i][1][j])):
                    if x.l[i][1][j][k] == s:
                        final.append(i)
        elif x.l[i][0] == 2:
            for k in range(len(x.l[i][1])):
                if x.l[i][1][k] == s:
                    final.append(i)
    tFinal = []
    for i in range(len(final)):
        sub = True
        for j in range(len(tFinal)):
            if tFinal[j] == final[i]:
                sub = False
        if sub:
            tFinal.append(final[i])
    return tFinal
def optFull(ix):
    sl = []
    for i in range(len(ix.l)):
        sl.append([])
        for j in range(len(ix.l[i])):
            if not j == 1:
                sl[i].append(ix.l[i][j])
            else:
                if ix.l[i][0] == 0:
                    sub = []
                    for k in range(len(ix.l[i][j].c)):
                        sub.append(ix.l[i][j].c[k])
                    sl[i].append(poly(sub))
                elif ix.l[i][0] == 1:
                    sub = []
                    for k in range(len(ix.l[i][1])):
                        sub.append([])
                        for m in range(len(ix.l[i][1][k])):
                            sub[k].append(ix.l[i][1][k][m])
                    sl[i].append(sub)
                elif ix.l[i][0] == 2:
                    sub = []
                    for k in range(len(ix.l[i][1])):
                        sub.append(ix.l[i][1][k])
                    sl[i].append(sub)
    spt = []
    for i in range(len(ix.pt)):
        spt.append(ix.pt[i])
    x = full(sl,spt)
    keepList = depWeb(x)
    zeros = []
    for i in range(len(x.l)):
        if x.l[i][0] == 0:
            if len(x.l[i][1].c) == 0:
                zeros.append(i)
            elif len(x.l[i][1].c) == 1 and x.l[i][1].c[0] == 0:
                zeros.append(i)
    for i in range(len(zeros)):
        keepList[zeros[i]] = False
        depZero = singleDep(x,zeros[i])
        for j in range(len(depZero)):
            sub = []
            if x.l[depZero[j]][0] == 1:
                for k in range(len(x.l[depZero[j]][1])):
                    sub2 = True
                    for m in range(len(x.l[depZero[j]][1][k])):
                        if x.l[depZero[j]][1][k][m] == zeros[i]:
                           sub2 = False
                    if sub2:
                        sub.append(x.l[depZero[j]][1][k])
            elif x.l[depZero[j]][0] == 2:
                if x.l[depZero[j]][1][0] == zeros[i] or x.l[depZero[j]][1][1] == zeros[i]:
                    keepList[depZero[j]] = False
            x.l[depZero[j]][1] = sub
    shift = []
    dec = 0
    for i in range(len(x.l)):
        if not keepList[i]:
            dec += 1
        shift.append(dec)
    for i in range(len(x.l)-1,-1,-1):
        if x.l[i][0] == 1:
            for j in range(len(x.l[i][1])):
                for k in range(len(x.l[i][1][j])):
                    x.l[i][1][j][k] -= shift[x.l[i][1][j][k]]
        elif x.l[i][0] == 2:
            x.l[i][1][0] -= shift[x.l[i][1][0]]
            x.l[i][1][1] -= shift[x.l[i][1][1]]
        if not keepList[i]:
            x.l[i:i+1] = []
    for i in range(len(x.pt)-1,-1,-1):
        for j in range(len(x.pt[i])-1,-1,-1):
            if not keepList[x.pt[i][j]]:
                x.pt[i][j:j+1] = []
                if len(x.pt[i]) == 0:
                    x.pt[i:i+1] = []
    for j in range(len(x.pt)):
        for k in range(len(x.pt[j])):
            x.pt[j][k] -= shift[x.pt[j][k]]
    copyPoly = []
    sourcePoly = []
    for i in range(len(x.l)):
        if x.l[i][0] == 0:
            sub = -1
            for j in range(len(sourcePoly)):
                if len(x.l[sourcePoly[j]][1].c) == len(x.l[i][1].c) and x.l[sourcePoly[j]][2] == x.l[i][2] and x.l[sourcePoly[j]][3] == x.l[i][3]:
                    for k in range(len(x.l[i][1].c)):
                        if x.l[i][1].c[k] == x.l[sourcePoly[j]][1].c[k]:
                            sub = j
            if sub == -1:
                sourcePoly.append(i)
            else:
                copyPoly.append([i,sourcePoly[sub]])
    for i in range(len(copyPoly)):
        dep = singleDep(x,copyPoly[i][0])
        for j in range(len(dep)):
            if x.l[dep[j]][0] == 1:
                for k in range(len(x.l[dep[j]][1])):
                    for m in range(len(x.l[dep[j]][1][k])):
                        if x.l[dep[j]][1][k][m] == copyPoly[i][0]:
                            x.l[dep[j]][1][k][m] = copyPoly[i][1]
            elif x.l[dep[j]][0] == 2:
                if x.l[dep[j]][1][0] == copyPoly[i][0]:
                    x.l[dep[j]][1][0] = copyPoly[i][1]
                if x.l[dep[j]][1][1] == copyPoly[i][0]:
                    x.l[dep[j]][1][1] = copyPoly[i][1]
    for j in range(len(x.pt)):
        for k in range(len(x.pt[j])):
            for i in range(len(copyPoly)):
                if x.pt[j][k] == copyPoly[i][0]:
                    x.pt[j][k] = copyPoly[i][1]
    singles = []
    for i in range(len(x.l)):
        if x.l[i][0] == 1 and x.l[i][2] == 0 and x.l[i][3] == False:
            if len(x.l[i][1]) == 1 and len(x.l[i][1][0]) == 1:
                singles.append(i)
    for i in range(len(singles)):
        dep = singleDep(x,singles[i])
        for j in range(len(dep)):
            if x.l[dep[j]][0] == 1:
                for k in range(len(x.l[dep[j]][1])):
                    for m in range(len(x.l[dep[j]][1][k])):
                        if x.l[dep[j]][1][k][m] == singles[i]:
                            x.l[dep[j]][1][k][m] = x.l[singles[i]][1][0][0]
            elif x.l[dep[j]][0] == 2:
                if x.l[dep[j]][1][0] == singles[i]:
                    x.l[dep[j]][1][0] = x.l[singles[i]][1][0][0]
                if x.l[dep[j]][1][1] == singles[i]:
                    x.l[dep[j]][1][1] = x.l[singles[i]][1][0][0]
    for j in range(len(x.pt)):
        for k in range(len(x.pt[j])):
            for i in range(len(singles)):
                if x.pt[j][k] == singles[i]:
                    x.pt[j][k] = x.l[singles[i]][1][0][0]
    keepList = depWeb(x)
    shift = []
    dec = 0
    for i in range(len(x.l)):
        if not keepList[i]:
            dec += 1
        shift.append(dec)
    for i in range(len(x.l)-1,-1,-1):
        if x.l[i][0] == 1:
            for j in range(len(x.l[i][1])):
                for k in range(len(x.l[i][1][j])):
                    x.l[i][1][j][k] -= shift[x.l[i][1][j][k]]
        elif x.l[i][0] == 2:
            x.l[i][1][0] -= shift[x.l[i][1][0]]
            x.l[i][1][1] -= shift[x.l[i][1][1]]
        if not keepList[i]:
            x.l[i:i+1] = []
    for i in range(len(x.pt)-1,-1,-1):
        for j in range(len(x.pt[i])-1,-1,-1):
            if not keepList[x.pt[i][j]]:
                x.pt[i][j:j+1] = []
                if len(x.pt[i]) == 0:
                    x.pt[i:i+1] = []
    for j in range(len(x.pt)):
        for k in range(len(x.pt[j])):
            x.pt[j][k] -= shift[x.pt[j][k]]
    return x
def dFull(x):
    final = []
    pd = []
    cd = []
    for i in range(len(x.l)):
        final.append(x.l[i])
        pd.append(0)
        cd.append(None)
    for i in range(len(x.l)):
        if x.l[i][0] == 0:
            final.append([0,dPoly(x.l[i][1]),0,False])
            pd[i] = len(final)-1
            if x.l[i][2] == 0:
                cd[i] = len(final)-1
    for i in range(len(x.l)):
        if x.l[i][0] == 0:
            if x.l[i][2] == 1:
                sub = polyMult(x.l[i][1],poly([4]))
                final.append([0,sub,1,x.l[i][3]])
                final.append([2,[pd[i],len(final)-1],0,False])
                cd[i]=len(final)-1
            elif x.l[i][2] == 2:
                final.append([0,x.l[i][1],3,x.l[i][3]])
                final.append([1,[[pd[i],len(final)-1]],0,False])
                cd[i]=len(final)-1
            elif x.l[i][2] == 3:
                final.append([0,x.l[i][1],2,(not x.l[i][3])])
                final.append([1,[[pd[i],len(final)-1]],0,False])
                cd[i]=len(final)-1
    run = False
    for i in range(len(cd)):
        if cd[i] == None:
            run = True
    while run:
        for i in range(len(x.l)):
            if x.l[i][0] == 1:
                sub3 = True
                for j in range(len(x.l[i][1])):
                    for k in range(len(x.l[i][1][j])):
                        if cd[x.l[i][1][j][k]] == None:
                            sub3 = False
                if sub3:
                    sub = []
                    for j in range(len(x.l[i][1])):
                        for k in range(len(x.l[i][1][j])):
                            sub2 = []
                            for m in range(len(x.l[i][1][j])):
                                if k == m:
                                    sub2.append(cd[x.l[i][1][j][m]])
                                else:
                                    sub2.append(x.l[i][1][j][m])
                            sub.append(sub2)
                    final.append([1,sub,0,False])
                    if x.l[i][2] == 0:
                        final[-1][3] = x.l[i][3]
                    elif x.l[i][2] == 1:
                        final.append([0,poly([2]),0,x.l[i][3]])
                        final.append([1,[[i,len(final)-1]],0,False])
                        final.append([2,[len(final)-3,len(final)-1],0,False])
                    elif x.l[i][2] == 2:
                        final.append([1,x.l[i][1],3,x.l[i][3]])
                        final.append([1,[[len(final)-2,len(final)-1]],0,False])
                    elif x.l[i][2] == 3:
                        final.append([1,x.l[i][1],2,(not x.l[i][3])])
                        final.append([1,[[len(final)-2,len(final)-1]],0,False])
                    cd[i] = len(final)-1
            elif x.l[i][0] == 2:
                if (not cd[x.l[i][1][0]] == None) and (not cd[x.l[i][1][1]] == None):
                    final.append([1,[[x.l[i][1][1],cd[x.l[i][1][0]]]],0,False])
                    final.append([1,[[x.l[i][1][0],cd[x.l[i][1][1]]]],0,True])
                    final.append([1,[[len(final)-2],[len(final)-1]],0,False])
                    final.append([1,[[x.l[i][1][1],x.l[i][1][1]]],0,False])
                    final.append([2,[len(final)-2,len(final)-1],0,False])
                    if x.l[i][2] == 0:
                        final[-1][3] = x.l[i][3]
                    elif x.l[i][2] == 1:
                        final.append([0,poly([2]),0,x.l[i][3]])
                        final.append([1,[[i,len(final)-1]],0,False])
                        final.append([2,[len(final)-3,len(final)-1],0,False])
                    elif x.l[i][2] == 2:
                        final.append([1,x.l[i][1],3,x.l[i][3]])
                        final.append([1,[[len(final)-2,len(final)-1]],0,False])
                    elif x.l[i][2] == 3:
                        final.append([1,x.l[i][1],2,(not x.l[i][3])])
                        final.append([1,[[len(final)-2,len(final)-1]],0,False])
                    cd[i] = len(final)-1
        run = False
        for i in range(len(cd)):
            if cd[i] == None:
                run = True
    pt = []
    for i in range(len(x.pt)):
        for j in range(len(x.pt[i])):
            sub = []
            for k in range(len(x.pt[i])):
                if j == k:
                    sub.append(cd[x.pt[i][j]])
                else:
                    sub.append(x.pt[i][k])
            pt.append(sub)
    return full(final,pt)
def comp(x,y):
    final = []
    pt = []
    for i in range(len(y.l)):
        final.append(y.l[i])
    final.append([1,y.pt,0,False])
    fy = len(final)-1
    cot = []
    cut = []
    for i in range(len(x.l)):
        cot.append(False)
        cut.append(0)
    for i in range(len(x.l)):
        if x.l[i][0] == 0:
            sub = []
            for j in range(len(x.l[i][1].c)):
                final.append([0,poly([x.l[i][1].c[j]]),0,False])
                sub2 = [len(final)-1]
                for k in range(len(x.l[i][1].c)-j-1):
                    sub2.append(fy)
                sub.append(sub2)
            final.append([1,sub,x.l[i][2],x.l[i][3]])
            cot[i] = True
            cut[i] = len(final)-1
    run = False
    for i in range(len(cot)):
        if not cot[i]:
            run = True
    while run:
        for i in range(len(x.l)):
            if not cot[i]:
                if x.l[i][0] == 1:
                    sub = True
                    for j in range(len(x.l[i][1])):
                        for k in range(len(x.l[i][1][j])):
                            if not cot[x.l[i][1][j][k]]:
                                sub = False
                    cot[i] = sub
                    if sub:
                        sub2 = []
                        for j in range(len(x.l[i][1])):
                            sub3 = []
                            for k in range(len(x.l[i][1][j])):
                                sub3.append(cut[x.l[i][1][j][k]])
                            sub2.append(sub3)
                        final.append([1,sub2,x.l[i][2],x.l[i][3]])
                        cut[i] = len(final)-1
                elif x.l[i][0] == 2:
                    sub = True
                    for j in range(len(x.l[i][1])):
                        if not cot[x.l[i][1][j]]:
                            sub = False
                    cot[i] = sub
                    if sub:
                        sub2 = []
                        for j in range(len(x.l[i][1])):
                            sub2.append(cut[x.l[i][1][j]])
                        final.append([2,sub2,x.l[i][2],x.l[i][3]])
                        cut[i] = len(final)-1
        run = False
        for i in range(len(cot)):
            if not cot[i]:
                run = True
    pt = []
    for i in range(len(x.pt)):
        pt.append([])
        for j in range(len(x.pt[i])):
            pt[i].append(cut[x.pt[i][j]])
    return optFull(full(final,pt))
class para:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def f(self, x):
        return [self.x.f(x),self.y.f(x)]
def strToDec(l):
    returnVal = 0
    decPointPlace = len(l)
    negative = 0
    if l[0] == "-":
        negative = 1
    for i in range(len(l)):
        if l[i] == ".":
            decPointPlace = i
    for i in range(len(l)):
        if i < decPointPlace:
            if l[i] == '1':
                returnVal = returnVal + 1 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '2':
                returnVal = returnVal + 2 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '3':
                returnVal = returnVal + 3 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '4':
                returnVal = returnVal + 4 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '5':
                returnVal = returnVal + 5 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '6':
                returnVal = returnVal + 6 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '7':
                returnVal = returnVal + 7 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '8':
                returnVal = returnVal + 8 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '9':
                returnVal = returnVal + 9 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
        if i > decPointPlace:
            if l[i] == '1':
                returnVal = returnVal + 1 / pow(10,i-decPointPlace)
            elif l[i] == '2':
                returnVal = returnVal + 2 / pow(10,i-decPointPlace)
            elif l[i] == '3':
                returnVal = returnVal + 3 / pow(10,i-decPointPlace)
            elif l[i] == '4':
                returnVal = returnVal + 4 / pow(10,i-decPointPlace)
            elif l[i] == '5':
                returnVal = returnVal + 5 / pow(10,i-decPointPlace)
            elif l[i] == '6':
                returnVal = returnVal + 6 / pow(10,i-decPointPlace)
            elif l[i] == '7':
                returnVal = returnVal + 7 / pow(10,i-decPointPlace)
            elif l[i] == '8':
                returnVal = returnVal + 8 / pow(10,i-decPointPlace)
            elif l[i] == '9':
                returnVal = returnVal + 9 / pow(10,i-decPointPlace)
    if negative == 1:
        returnVal = returnVal * -1
    return returnVal
def pascal(r,n):
    return math.factorial(r)/(math.factorial(n)*math.factorial(r-n))
def bez(sc,cpl,ec):
    co = [sc]
    for i in range(len(cpl)):
        co.append(cpl[i])
    co.append(ec)
    pol = [[],[]]
    for i in range(len(co)):
        t = 0
        for j in range(len(co)-i):
            t += co[j][0]*pascal(len(co)-i-1,j)*pow(-1,j+1+i)
        pol[0].append(pascal(len(co)-1,i)*t*pow(-1,len(co)))
    for i in range(len(co)):
        t = 0
        for j in range(len(co)-i):
            t += co[j][1]*pascal(len(co)-i-1,j)*pow(-1,j+1+i)
        pol[1].append(pascal(len(co)-1,i)*t*pow(-1,len(co)))
    return para(full([[0,poly(pol[0]),0,False]],[[0]]),full([[0,poly(pol[1]),0,False]],[[0]]))
def spiral(x,y,br,fr,dof,da):
    return para(full([[0,poly([x]),0,False],[0,poly([fr-br,br]),0,False],[0,poly([da*math.pi/180,dof*math.pi/180]),3,False]],[[0],[1,2]]),full([[0,poly([y]),0,False],[0,poly([fr-br,br]),0,False],[0,poly([da*math.pi/180,dof*math.pi/180]),2,False]],[[0],[1,2]]))
def translateCurve(x,t,v):
    final = []
    sxl = []
    for i in range(len(x.x.l)):
        sxl.append(x.x.l[i])
    xpt = []
    for i in range(len(x.x.pt)):
        xpt.append([])
        for k in range(len(x.x.pt[i])):
            xpt[i].append(x.x.pt[i][k])
    syl = []
    for i in range(len(x.y.l)):
        syl.append(x.y.l[i])
    ypt = []
    for i in range(len(x.y.pt)):
        ypt.append([])
        for k in range(len(x.y.pt[i])):
            ypt[i].append(x.y.pt[i][k])
    final = para(full(sxl,xpt),full(syl,ypt))
    for j in range(len(t)):
        if t[j] == 0:
            final.x.l.append([0,poly([v[j][0]]),0,False])
            final.x.pt.append([len(final.x.l)-1])
            final.y.l.append([0,poly([v[j][1]]),0,False])
            final.y.pt.append([len(final.y.l)-1])
        elif t[j] == 1:
            sub = []
            for i in range(len(final.x.l)):
                sub.append(final.x.l[i])
            sub.append([1,final.x.pt,0,False])
            xe = len(sub)-1
            for i in range(len(final.y.l)):
                if final.y.l[i][0] == 0:
                    sub.append(final.y.l[i])
                elif final.y.l[i][0] == 1:
                    sub2 = []
                    for k in range(len(final.y.l[i][1])):
                        sub2.append([])
                        for n in range(len(final.y.l[i][1][k])):
                            sub2[k].append(final.y.l[i][1][k][n]+xe+1)
                    sub.append([1,sub2,final.y.l[i][2],final.y.l[i][3]])
                elif final.y.l[i][0] == 2:
                    sub2 = []
                    for k in range(len(final.y.l[i][1])):
                        sub2.append(final.y.l[i][1][k]+xe+1)
                    sub.append([2,sub2,final.y.l[i][2],final.y.l[i][3]])
            sub2 = []
            for i in range(len(final.y.pt)):
                sub2.append([])
                for k in range(len(final.y.pt[i])):
                    sub2[i].append(final.y.pt[i][k]+xe+1)
            sub.append([1,sub2,0,False])
            ye = len(sub)-1
            sub.append([0,poly([math.cos(v[j][0]*math.pi/180)]),0,False])
            xl = []
            for i in range(len(sub)):
                xl.append(sub[i])
            xl.append([0,poly([-math.sin(v[j][0]*math.pi/180)]),0,False])
            yl = []
            for i in range(len(sub)):
                yl.append(sub[i])
            yl.append([0,poly([math.sin(v[j][0]*math.pi/180)]),0,False])
            xpt = [[xe,len(xl)-2],[ye,len(xl)-1]]
            ypt = [[ye,len(yl)-2],[xe,len(yl)-1]]
            final = para(full(xl,xpt),full(yl,ypt))
        elif t[j] == 2:
            final.x.l.append([0,poly([v[j][0]]),0,False])
            for i in range(len(final.x.pt)):
                final.x.pt[i].append(len(final.x.l)-1)
            final.y.l.append([0,poly([v[j][1]]),0,False])
            for i in range(len(final.y.pt)):
                final.y.pt[i].append(len(final.y.l)-1)
    return para(optFull(final.x),optFull(final.y))
def compCurve(x,y):
    return para(x.x,y.y)
def horShift(p,x):
    f = p.c
    final = []
    for i in range(len(f)):
        final.append(0)
    for i in range(len(f)):
        sub = poly([f[i]])
        for j in range(len(f)-i-1):
            sub = polyMult(sub,poly([1,-x]))
        for j in range(len(sub.c)):
            final[i+j] += sub.c[j]
    return poly(final)
def slic(p,r):
    f = p.c
    ns = r[1]-r[0]
    final=poly([])
    for i in range(len(f)):
        final.c.append(f[i])
    final = horShift(final,-r[0])
    for i in range(len(f)):
        final.c[i]*=pow(ns,len(f)-1-i)
    return final
def slicePara(x,r):
    val = 0
    final = []
    sxl = []
    for i in range(len(x.x.l)):
        sxl.append([])
        for j in range(len(x.x.l[i])):
            sxl[i].append(x.x.l[i][j])
    xpt = []
    for i in range(len(x.x.pt)):
        xpt.append([])
        for k in range(len(x.x.pt[i])):
            xpt[i].append(x.x.pt[i][k])
    syl = []
    for i in range(len(x.y.l)):
        syl.append([])
        for j in range(len(x.y.l[i])):
            syl[i].append(x.y.l[i][j])
    ypt = []
    for i in range(len(x.y.pt)):
        ypt.append([])
        for k in range(len(x.y.pt[i])):
            ypt[i].append(x.y.pt[i][k])
    final = para(full(sxl,xpt),full(syl,ypt))
    for i in range(len(final.x.l)):
        if final.x.l[i][0] == 0:
            final.x.l[i][1] = slic(final.x.l[i][1],r)
    for i in range(len(final.y.l)):
        if final.y.l[i][0] == 0:
            final.y.l[i][1] = slic(final.y.l[i][1],r)
    return para(optFull(final.x),optFull(final.y))
def wrap(x,ia,t):
    sub = ia.l
    sub.append([1,ia.pt,0,False])
    sub.append([0,poly([t[0]]),0,False])
    sub.append([0,poly([t[1]]),0,False])
    a = full(sub,[[len(sub)-3,len(sub)-2],[len(sub)-1]])    
    sub = []
    dx = dFull(x.x)
    for i in range(len(dx.l)):
        sub.append(dx.l[i])
    sub.append([1,x.x.pt,0,False])
    xi = len(sub)-1
    sub.append([1,dx.pt,0,False])
    dxi = len(sub)-1
    dy = dFull(x.y)
    for i in range(len(dy.l)):
        if dy.l[i][0] == 0:
            sub.append(dy.l[i])
        elif dy.l[i][0] == 1:
            sub2 = []
            for j in range(len(dy.l[i][1])):
                sub2.append([])
                for k in range(len(dy.l[i][1][j])):
                    sub2[j].append(dy.l[i][1][j][k]+dxi+1)
            sub.append([1,sub2,dy.l[i][2],dy.l[i][3]])
        elif dy.l[i][0] == 2:
            sub2 = []
            for j in range(len(dy.l[i][1])):
                sub2.append(dy.l[i][1][j]+dxi+1)
            sub.append([2,sub2,dy.l[i][2],dy.l[i][3]])
    sub2 = []
    for i in range(len(x.y.pt)):
        sub2.append([])
        for j in range(len(x.y.pt[i])):
            sub2[i].append(x.y.pt[i][j]+dxi+1)
    sub.append([1,sub2,0,False])
    yi = len(sub)-1
    sub2 = []
    for i in range(len(dy.pt)):
        sub2.append([])
        for j in range(len(dy.pt[i])):
            sub2[i].append(dy.pt[i][j]+dxi+1)
    sub.append([1,sub2,0,False])
    dyi = len(sub)-1
    sub.append([1,[[dxi,dxi],[dyi,dyi]],1,False])
    den = len(sub)-1
    xl = []
    yl = []
    for i in range(len(sub)):
        xl.append(sub[i])
        yl.append(sub[i])
    si = len(sub)-1
    for i in range(len(a.l)):
        if a.l[i][0] == 0:
            xl.append(a.l[i])
            yl.append(a.l[i])
        elif a.l[i][0] == 1:
            sub2 = []
            for j in range(len(a.l[i][1])):
                sub2.append([])
                for k in range(len(a.l[i][1][j])):
                    sub2[j].append(a.l[i][1][j][k]+si+1)
            xl.append([1,sub2,a.l[i][2],a.l[i][3]])
            yl.append([1,sub2,a.l[i][2],a.l[i][3]])
        elif a.l[i][0] == 2:
            sub2 = []
            for j in range(len(a.l[i][1])):
                sub2.append(a.l[i][1][j]+si+1)
            xl.append([2,sub2,a.l[i][2],a.l[i][3]])
            yl.append([2,sub2,a.l[i][2],a.l[i][3]])
    sub2 = []
    for i in range(len(a.pt)):
        sub2.append([])
        for j in range(len(a.pt[i])):
            sub2[i].append(a.pt[i][j]+si+1)
    xl.append([1,sub2,0,False])
    yl.append([1,sub2,0,True])
    xl.append([1,[[len(xl)-1,dyi]],0,False])
    xl.append([2,[len(xl)-1,den],0,False])
    xpt=[[xi],[len(xl)-1]]
    yl.append([1,[[len(yl)-1,dxi]],0,False])
    yl.append([2,[len(yl)-1,den],0,False])
    ypt=[[yi],[len(yl)-1]]
    return para(optFull(full(xl,xpt)),optFull(full(yl,ypt)))
def dis(a,b,c,d):
    return math.sqrt(pow(a-c,2)+pow(b-d,2))
def da(x1,y1,x2,y2):
    final = 0
    if abs(x2-x1) > 0:
        final = math.atan((y2-y1)/(x2-x1))/math.pi*180
    else:
        if (y2-y1) > 0:
            final = 90
        else:
            final = -90
    if (x2-x1) < 0:
        final += 180
    elif (x2-x1) > 0 and (y2-y1) < 0:
        final += 360
    return final
def tangent(b,bp,s,sp):
    final = para(s.x,s.y)
    spf = s.f(sp)
    bpf = b.f(bp)
    final = translateCurve(final,[0],[[-spf[0],-spf[1]]])
    ds = [dFull(s.x),dFull(s.y)]
    db = [dFull(b.x),dFull(b.y)]
    sa = da(0,0,ds[0].f(sp),ds[1].f(sp))
    ba = da(0,0,db[0].f(bp),db[1].f(bp))
    final = translateCurve(final,[1,0],[[ba-sa],[bpf[0],bpf[1]]])
    return para(optFull(final.x),optFull(final.y))
def singleWarp(b,s,w,h,o):
    subx = []
    for i in range(len(s.x.l)):
        subx.append(s.x.l[i])
    subx.append([0,poly([o[0]]),0,False]);
    subx2 = []
    for i in range(len(s.x.pt)):
        subx2.append(s.x.pt[i])
    subx2.append([len(subx)-1])
    subx.append([1,subx2,0,False])
    subx.append([0,poly([w]),0,False])
    subx.append([2,[len(subx)-2,len(subx)-1],0,False])
    sx = full(subx,[[len(subx)-1]])
    suby = []
    for i in range(len(s.y.l)):
        suby.append(s.y.l[i])
    suby.append([0,poly([o[1]]),0,False])
    suby2 = []
    for i in range(len(s.y.pt)):
        suby2.append(s.y.pt[i])
    suby2.append([len(suby)-1])
    suby.append([1,suby2,0,False])
    suby.append([0,poly([h]),0,False])
    suby.append([2,[len(suby)-2,len(suby)-1],0,False])
    sy = full(suby,[[len(suby)-1]])
    xc = comp(b.x,sx)
    yc = comp(b.y,sx)
    dxc = comp(dFull(b.x),sx)
    dyc = comp(dFull(b.y),sx)
    xl=[]
    yl=[]
    for i in range(len(sy.l)):
        xl.append(sy.l[i])
        yl.append(sy.l[i])
    xl.append([1,sy.pt,0,False])
    yl.append([1,sy.pt,0,False])
    syi = len(xl)-1
    for i in range(len(xc.l)):
        if xc.l[i][0] == 0:
            xl.append(xc.l[i])
        elif xc.l[i][0] == 1:
            sub2 = []
            for k in range(len(xc.l[i][1])):
                sub2.append([])
                for n in range(len(xc.l[i][1][k])):
                    sub2[k].append(xc.l[i][1][k][n]+syi+1)
            xl.append([1,sub2,xc.l[i][2],xc.l[i][3]])
        elif xc.l[i][0] == 2:
            sub2=[]
            for k in range(len(xc.l[i][1])):
                sub2.append(xc.l[i][1][k]+syi+1)
            xl.append([2,sub2,xc.l[i][2],xc.l[i][3]])
    sub2=[]
    for i in range(len(xc.pt)):
        sub2.append([])
        for k in range(len(xc.pt[i])):
            sub2[i].append(xc.pt[i][k]+syi+1)
    xl.append([1,sub2,0,False])
    xci=len(xl)-1
    for i in range(len(dyc.l)):
        if dyc.l[i][0] == 0:
            xl.append(dyc.l[i])
        elif dyc.l[i][0] == 1:
            xl2 = []
            for k in range(len(dyc.l[i][1])):
                xl2.append([])
                for n in range(len(dyc.l[i][1][k])):
                    xl2[k].append(dyc.l[i][1][k][n]+xci+1)
            xl.append([1,xl2,dyc.l[i][2],dyc.l[i][3]])
        elif dyc.l[i][0] == 2:
            xl2=[]
            for k in range(len(dyc.l[i][1])):
                xl2.append(dyc.l[i][1][k]+xci+1)
            xl.append([2,xl2,dyc.l[i][2],dyc.l[i][3]])
    xl2 = []
    for i in range(len(dyc.pt)):
        xl2.append([])
        for k in range(len(dyc.pt[i])):
            xl2[i].append(dyc.pt[i][k]+xci+1)
    xl.append([1,xl2,0,False])
    dyci = len(xl)-1
    xpt = [[xci],[syi,dyci]]
    for i in range(len(yc.l)):
        if yc.l[i][0] == 0:
            yl.append(yc.l[i])
        elif yc.l[i][0] == 1:
            sub2 = []
            for k in range(len(yc.l[i][1])):
                sub2.append([])
                for n in range(len(yc.l[i][1][k])):
                    sub2[k].append(yc.l[i][1][k][n]+syi+1)
            yl.append([1,sub2,yc.l[i][2],yc.l[i][3]])
        elif yc.l[i][0] == 2:
            sub2 = []
            for k in range(len(yc.l[i][1])):
                sub2.append(yc.l[i][1][k]+syi+1)
            yl.append([2,sub2,yc.l[i][2],yc.l[i][3]])
    sub2 = []
    for i in range(len(yc.pt)):
        sub2.append([])
        for k in range(len(yc.pt[i])):
            sub2[i].append(yc.pt[i][k]+syi+1)
    yl.append([1,sub2,0,False])
    yci=len(yl)-1
    for i in range(len(dxc.l)):
        if dxc.l[i][0] == 0:
            yl.append(dxc.l[i])
        elif dxc.l[i][0] == 1:
            yl2=[]
            for k in range(len(dxc.l[i][1])):
                yl2.append([])
                for n in range(len(dxc.l[i][1][k])):
                    yl2[k].append(dxc.l[i][1][k][n]+yci+1)
            yl.append([1,yl2,dxc.l[i][2],dxc.l[i][3]])
        elif dxc.l[i][0] == 2:
            yl2 = []
            for k in range(len(dxc.l[i][1])):
                yl2.append(dxc.l[i][1][k]+yci+1)
            yl.append([2,yl2,dxc.l[i][2],dxc.l[i][3]])
    yl2 = []
    for i in range(len(dxc.pt)):
        yl2.append([])
        for k in range(len(dxc.pt[i])):
            yl2[i].append(dxc.pt[i][k]+yci+1)
    yl.append([1,yl2,0,True])
    dxci=len(yl)-1
    ypt = [[yci],[syi,dxci]]
    return para(optFull(full(xl,xpt)),optFull(full(yl,ypt)))
def addFull(x,n):
    final = []
    pt = []
    last = -1
    for i in range(len(x)):
        for j in range(len(x[i].l)):
            if x[i].l[j][0] == 0:
                final.append(x[i].l[j])
            elif x[i].l[j][0] == 1:
                sub = []
                for k in range(len(x[i].l[j][1])):
                    sub.append([])
                    for m in range(len(x[i].l[j][1][k])):
                        sub[k].append(x[i].l[j][1][k][m]+last+1)
                final.append([1,sub,x[i].l[j][2],x[i].l[j][3]])
            elif x[i].l[j][0] == 2:
                sub = []
                for k in range(len(x[i].l[j][1])):
                    sub.append(x[i].l[j][1][k]+last+1)
                final.append([2,sub,x[i].l[j][2],x[i].l[j][3]])
        sub = []
        for k in range(len(x[i].pt)):
            sub.append([])
            for m in range(len(x[i].pt[k])):
                sub[k].append(x[i].pt[k][m]+last+1)
        final.append([1,sub,0,n[i]])
        pt.append([len(final)-1])
        last = len(final)-1
    return optFull(full(final,pt))
def multFull(x):
    final = []
    pt = []
    last = -1
    for i in range(len(x)):
        for j in range(len(x[i].l)):
            if x[i].l[j][0] == 0:
                final.append(x[i].l[j])
            elif x[i].l[j][0] == 1:
                sub = []
                for k in range(len(x[i].l[j][1])):
                    sub.append([])
                    for m in range(len(x[i].l[j][1][k])):
                        sub[k].append(x[i].l[j][1][k][m]+last+1)
                final.append([1,sub,x[i].l[j][2],x[i].l[j][3]])
            elif x[i].l[j][0] == 2:
                sub = []
                for k in range(len(x[i].l[j][1])):
                    sub.append(x[i].l[j][1][k]+last+1)
                final.append([2,sub,x[i].l[j][2],x[i].l[j][3]])
        sub = []
        for k in range(len(x[i].pt)):
            sub.append([])
            for m in range(len(x[i].pt[k])):
                sub[k].append(x[i].pt[k][m]+last+1)
        final.append([1,sub,0,False])
        pt.append(len(final)-1)
        last = len(final)-1
    return optFull(full(final,[pt]))
def doubleWarp(b1,b2,s,w,h,o):
    subx = []
    for i in range(len(s.x.l)):
        subx.append(s.x.l[i])
    subx.append([0,poly([o[0]]),0,False])
    subx2 = []
    for i in range(len(s.x.pt)):
        subx2.append(s.x.pt[i])
    subx2.append([len(subx)-1])
    subx.append([1,subx2,0,False])
    subx.append([0,poly([w]),0,False])
    subx.append([2,[len(subx)-2,len(subx)-1],0,False])
    sx = full(subx,[[len(subx)-1]])
    suby = []
    for i in range(len(s.y.l)):
        suby.append(s.y.l[i])
    suby.append([0,poly([o[1]]),0,False])
    suby2 = []
    for i in range(len(s.y.pt)):
        suby2.append(s.y.pt[i])
    suby2.append([len(suby)-1])
    suby.append([1,suby2,0,False])
    suby.append([0,poly([h]),0,False])
    suby.append([2,[len(suby)-2,len(suby)-1],0,False])
    sy = full(suby,[[len(suby)-1]])
    xc1 = comp(b1.x,sx)
    yc1 = comp(b1.y,sx)
    xc2 = comp(b2.x,sx)
    yc2 = comp(b2.y,sx)
    xd = addFull([xc1,xc2],[True,False])
    yd = addFull([yc1,yc2],[True,False])
    xc3 = multFull([xd,sy])
    yc3 = multFull([yd,sy])
    xc4 = addFull([xc1,xc3],[False,False])
    yc4 = addFull([yc1,yc3],[False,False])
    return para(xc4,yc4)
def quadWarp(sa,na,ea,wa,s,w,h,o):
    subx = []
    for i in range(len(s.x.l)):
        subx.append(s.x.l[i])
    subx.append([0,poly([o[0]]),0,False]);
    subx2 = []
    for i in range(len(s.x.pt)):
        subx2.append(s.x.pt[i])
    subx2.append([len(subx)-1])
    subx.append([1,subx2,0,False])
    subx.append([0,poly([w]),0,False])
    subx.append([2,[len(subx)-2,len(subx)-1],0,False])
    sx = full(subx,[[len(subx)-1]])
    suby = []
    for i in range(len(s.y.l)):
        suby.append(s.y.l[i])
    suby.append([0,poly([o[1]]),0,False])
    suby2 = []
    for i in range(len(s.y.pt)):
        suby2.append(s.y.pt[i])
    suby2.append([len(suby)-1])
    suby.append([1,suby2,0,False])
    suby.append([0,poly([h]),0,False])
    suby.append([2,[len(suby)-2,len(suby)-1],0,False])
    sy = full(suby,[[len(suby)-1]])
    pax=comp(sa.x,sx)
    pay=comp(sa.y,sx)
    pbx=comp(na.x,sx)
    pby=comp(na.y,sx)
    hdx=addFull([multFull([addFull([pax,pbx],[True,False]),sy]),pax],[False,False])
    hdy=addFull([multFull([addFull([pay,pby],[True,False]),sy]),pay],[False,False])
    bpx=addFull([multFull([full([[0,poly([na.f(0)[0]-sa.f(0)[0]]),0,False]],[[0]]),sy]),full([[0,poly([sa.f(0)[0]]),0,False]],[[0]])],[False,False])
    bpy=addFull([multFull([full([[0,poly([na.f(0)[1]-sa.f(0)[1]]),0,False]],[[0]]),sy]),full([[0,poly([sa.f(0)[1]]),0,False]],[[0]])],[False,False])
    epx=addFull([multFull([full([[0,poly([na.f(1)[0]-sa.f(1)[0]]),0,False]],[[0]]),sy]),full([[0,poly([sa.f(1)[0]]),0,False]],[[0]])],[False,False])
    epy=addFull([multFull([full([[0,poly([na.f(1)[1]-sa.f(1)[1]]),0,False]],[[0]]),sy]),full([[0,poly([sa.f(1)[1]]),0,False]],[[0]])],[False,False])
    pcx=comp(ea.x,sy)
    pcy=comp(ea.y,sy)
    pdx=comp(wa.x,sy)
    pdy=comp(wa.y,sy)
    fx=addFull([hdx,pcx,bpx,multFull([addFull([pdx,pcx,bpx,epx],[False,True,False,True]),sx])],[False,False,True,False])
    fy=addFull([hdy,pcy,bpy,multFull([addFull([pdy,pcy,bpy,epy],[False,True,False,True]),sx])],[False,False,True,False])
    final=para(fx,fy)
    return para(optFull(final.x),optFull(final.y))
def leg(n,l,c):
    a = []
    for i in range(n):
        a.append([])
    for i in range(n):
        if i == l:
           a[0].append([[i]])
        elif i == l-1:
             a[0].append([[-(i+2)]])
        else:
            a[0].append(False)
    for m in range(n-1):
        for i in range(n-(m+1)):
            sub2 = []
            sub = []
            if not a[m][i] == False:
                for j in range(len(a[m][i])):
                    for k in range(len(a[m][i][j])):
                        sub.append(a[m][i][j][k])
                    sub.append(i)
                    sub2.append(sub)
                    sub = []
            sub = []
            if not a[m][i+1] == False:
                for j in range(len(a[m][i+1])):
                    for k in range(len(a[m][i+1][j])):
                        sub.append(a[m][i+1][j][k])
                    sub.append(-(i+m+3))
                    sub2.append(sub)
                    sub = []
            if a[m][i] == False and a[m][i+1] == False:
                sub2 = False
            a[m+1].append(sub2)
    cL = a[n-1][0]
    gFinal = poly([])
    for i in range(n+1):
        gFinal.c.append(0)
    for j in range(len(cL)):
        prod=poly([1])
        for i in range(len(cL[j])):
            sub = poly([])
            if cL[j][i]< -1:
                sub.c = [-1,-cL[j][i]]
            else:
                sub.c = [1,-cL[j][i]]
            prod=polyMult(prod,sub)
        for i in range(len(prod.c)):
            gFinal.c[i]+=prod.c[i]
    gFinal = horShift(gFinal,-l)
    f = c/math.factorial(n)
    for i in range(len(gFinal.c)):
        gFinal.c[i] *= f
    return gFinal
def customLeg(p,d,l,t):
    points = []
    if t == 0:
        for i in range(d-1):
            points.append(p[0])
        for i in range(len(p)):
            points.append(p[i])
        for i in range(d-1):
            points.append(p[len(p)-1])
    elif t == 1:
        for i in range(len(p)):
            points.append(p[i])
        for i in range(d):
            points.append(points[i])
    pol = [0]
    for i in range(d):
        pol.append(0)
    for i in range(d+1):
        a = leg(d,d-i,points[i+l])
        for m in range(d+1):
            pol[m] += a.c[m]
    return poly(pol)
def findClosest(x,p,dx):
    r = [0,1]
    cp = 0.5
    dc = False
    for i in range(50):
        lp = x.f(cp-pow(2,-(i+1)))
        mp = x.f(cp)
        rp = x.f(cp+pow(2,-(i+1)))
        ld = dis(lp[0],lp[1],p[0],p[1])
        md = dis(mp[0],mp[1],p[0],p[1])
        rd = dis(rp[0],rp[1],p[0],p[1])
        if ld < rd and ld < md:
            cp -= pow(2,-(i+1))
        elif rd < ld and rd < md:
            cp += pow(2,-(i+1))
        if cp < 0:
            cp = 0
        if cp > 1:
            cp = 1
    final = cp
    if final < 0:
        final = 0
    if final > 1:
        final = 1
    fp = x.f(final)
    y = dis(fp[0],fp[1],p[0],p[1])
    dfp = dx.f(final)
    ad = round(da(p[0],p[1],fp[0],fp[1])-da(0,0,dfp[0],dfp[1]))
    if ad > 180:
        ad -= 360
    elif ad < -180:
        ad += 360
    return [final,y,ad]
def findFlips(f):
    p = 0
    sub = 0
    final = []
    df = para(dFull(f.x),dFull(f.y))
    while p < 1:
        dp = df.f(p)
        dx = dp[0]
        dy = dp[1]
        if p == 0:
            sub = da(0,0,dx,dy)
        p += 1/math.sqrt(pow(dx,2)+pow(dy,2))
        sampAn = da(0,0,dx,dy)
        if abs(sub-sampAn) > 180:
            final.append(p)
            sub = sampAn
    return final
def posToList(f,s,df):
    p = 0
    final = []
    finalPos = []
    if df.f(0)[0] == 0 and df.f(0)[1] == 0:
        final.append(f.f(p))
        sp = [0,0]
        for j in range(11):
            t = j/10
            ft = f.f(t)
            f0 = f.f(0)
            d = abs(dis(ft[0],ft[1],f0[0],f0[1])-s)
            if j == 0:
                sp[1] = d
            else:
                if d < sp[1]:
                    sp = [j/10,d]
        for j in range(15):
            td = [0,s]
            for k in range(-10,11,1):
                t = max(0,sp[0]+k/pow(10,j+2))
                ft = f.f(t)
                f0 = f.f(0)
                d = abs(dis(ft[0],ft[1],f0[0],f0[1])-s)
                if d < td[1]:
                    td=[t,d]
            sp=td
        p = sp[0]
    while p < 1:
        fp = f.f(p)
        dfp = df.f(p)
        final.append(fp)
        finalPos.append(p)
        p += s/math.sqrt(pow(dfp[0],2)+pow(dfp[1],2))
    if len(finalPos) >= 2:
        finalPos[-1] = (finalPos[-2]+1)/2
        final[-1] = f.f(finalPos[-1])
    finalP = f.f(1)
    final.append(finalP)
    finalPos.append(1)
    return [final,finalPos]
def pointSlope(x1,y1,x2,y2):
    returnValues = []
    if not y2-y1 == 0 and not x2-x1 == 0:
        returnValues = [(y2-y1)/(x2-x1),-((y2-y1)/(x2-x1))*x1+y1]
    if y2-y1 == 0:
        returnValues = ["y",y1]
    if x2-x1 == 0:
        returnValues = ["x",x1]
    if y2-y1 == 0 and x2-x1 == 0:
        returnValues = []
    return returnValues
def inter(const1,m,a,const2,n,b):
    returnValues = [0,0]
    if const1 == False and const2 == False:
        if not n-m == 0:
            returnValues[0] = (a-b)/(n-m)
            returnValues[1] = (a-b)/(n-m)*m+a
    if const1 == True and const2 == False:
        if m == "x":
            returnValues[0] = a
            returnValues[1] = n*a+b
        if m == "y":
            returnValues[0] = (a-b)/n
            returnValues[1] = a
    if const1 == False and const2 == True:
        if n == "x":
            returnValues[0] = b
            returnValues[1] = m*b+a
        if n == "y":
            returnValues[0] = (b-a)/m
            returnValues[1] = b
    if const1 == True and const2 == True:
        returnValues=[b,a]
    if m == n:
        returnValues = []
    return returnValues
def detectInter(l1,l2,t):
    exportValues = []
    for i in range(len(l1)-1):
        for j in range(len(l2)-1):
            valid = True
            if l1[i][0] == l1[i+1][0] and l1[i][1] == l1[i+1][1]:
                valid = False
            if l2[j][0] == l2[j+1][0] and l2[j][1] == l2[j+1][1]:
                valid = False
            if valid == True:
                p1 = 0
                p2 = 0
                s1 = pointSlope(l1[i][0],l1[i][1],l1[i+1][0],l1[i+1][1])
                s2 = pointSlope(l2[j][0],l2[j][1],l2[j+1][0],l2[j+1][1])
                c1 = False
                if l1[i][0]-l1[i+1][0] == 0 or l1[i][1]-l1[i+1][1] == 0:
                    c1 = True
                c2 = False
                if l2[j][0]-l2[j+1][0] == 0 or l2[j][1]-l2[j+1][1] == 0:
                    c2 = True
                if not inter(c1,s1[0],s1[1],c2,s2[0],s2[1]) == []:
                    inte = inter(c1,s1[0],s1[1],c2,s2[0],s2[1])
                    if l1[i][0]-l1[i+1][0] == 0:
                        p1 = (inte[1]-l1[i][1])/(l1[i+1][1]-l1[i][1])
                    else:
                        p1 = (inte[0]-l1[i][0])/(l1[i+1][0]-l1[i][0])
                    if l2[j][0]-l2[j+1][0] == 0:
                        p2 = (inte[1]-l2[j][1])/(l2[j+1][1]-l2[j][1])
                    else:
                        p2 = (inte[0]-l2[j][0])/(l2[j+1][0]-l2[j][0])
                else:
                    p1 = 1.1
                if p1>=0 and p1<=1 and p2>=0 and p2<=1:
                    if t == "lp":
                        exportValues.append([i,p1,j,p2])
                    if t == "ai":
                        exportValues.append(inte)
    return exportValues
def findInter(f1,f2,df1,df2):
    r1 = posToList(f1,1,df1)
    r2 = posToList(f2,1,df2)
    estimates = detectInter(r1[0],r2[0],"lp")
    estimateXVal = []
    for i in range(len(estimates)):
        estimateXVal.append([r1[1][estimates[i][0]]+(r1[1][estimates[i][0]+1]-r1[1][estimates[i][0]])*estimates[i][1],r2[1][estimates[i][2]]+(r2[1][estimates[i][2]+1]-r2[1][estimates[i][2]])*estimates[i][3]])
    final = []
    for z in range(len(estimates)):
        subFinal = []
        for x in range(2):
            subFinal.append(estimateXVal[z][x])
        finalIndex = [0,0]
        subStartPoint = 0
        if len(estimates) > 1:
            if z == 0:
                subStartPoint=min(abs(estimateXVal[0][0]-estimateXVal[1][0]),abs(estimateXVal[0][1]-estimateXVal[1][1]))
            elif z == len(estimates)-1:
                subStartPoint=min(abs(estimateXVal[-1][0]-estimateXVal[-2][0]),abs(estimateXVal[-1][1]-estimateXVal[-2][1]))
            else:
                subStartPoint=min(min(abs(estimateXVal[z-1][0]-estimateXVal[z][0]),abs(estimateXVal[z-1][1]-estimateXVal[z][1])),min(abs(estimateXVal[z+1][0]-estimateXVal[z][0]),abs(estimateXVal[z+1][1]-estimateXVal[z][1])))
            startPoint = abs(math.floor(math.log(subStartPoint)/math.log(10)))+1
        else:
            startPoint = 1
        for i in range(10):
            sampleDist = 100
            for j in range(21):
                for k in range(21):
                    p1 = subFinal[0]+(j-10)/pow(10,i+startPoint)
                    if p1 < 0:
                        p1 = 0
                    if p1 > 1:
                        p1 = 1
                    p2 = subFinal[1]+(k-10)/pow(10,i+startPoint)
                    if p2 < 0:
                        p2 = 0
                    if p2 > 1:
                        p2 = 1
                    sp1 = f1.f(p1)
                    sp2 = f2.f(p2)
                    if dis(sp1[0],sp1[1],sp2[0],sp2[1]) < sampleDist:
                        finalIndex = [j-10,k-10]
                        sampleDist = dis(sp1[0],sp1[1],sp2[0],sp2[1])
            subFinal[0]+=finalIndex[0]/pow(10,i+startPoint)
            subFinal[1]+=finalIndex[1]/pow(10,i+startPoint)
        final.append(subFinal)
    return final
def objLine(l,s):
    d = dis(l[0],l[1],l[2],l[3])
    angle = da(l[0],l[1],l[2],l[3])
    final = []
    if(d>s):
        xu=(l[2]-l[0])/d
        yu=(l[3]-l[1])/d
        start=[l[0]+xu*s/2,l[1]+yu*s/2]
        end=[l[2]-xu*s/2,l[3]-yu*s/2]
        mOb=math.ceil(dis(start[0],start[1],end[0],end[1])/s)
        if mOb > 10:
            mOb = -1
        if mOb > 0:
            sx=(end[0]-start[0])/mOb
            sy=(end[1]-start[1])/mOb
        else:
            sx=0
            sy=0
        for i in range(mOb+1):
            final.append([917,start[0]+sx*i,start[1]+sy*i,-angle,s/7.5])
    if(d<=s):
        xu=(l[3]-l[1])/d
        yu=(l[2]-l[0])/d
        start=[(l[0]+l[2])/2+xu*s/2-xu*d/2,(l[1]+l[3])/2-yu*s/2+yu*d/2]
        end=[(l[0]+l[2])/2-xu*s/2+xu*d/2,(l[1]+l[3])/2+yu*s/2-yu*d/2]
        mOb=math.floor(s/d)
        if mOb > 10:
            mOb = -1
        if mOb > 0:
            sx=(end[0]-start[0])/mOb
            sy=(end[1]-start[1])/mOb
        else:
            sx=0
            sy=0
        for i in range(mOb+1):
            final.append([917,start[0]+sx*i,start[1]+sy*i,-angle,d/7.5])
    return final
def direction(dpl,ddpl,amt):
    final = 0
    nex = 0
    for i in range(len(dpl)):
        for j in range(amt):
            d = dpl[i].f(j/amt)
            x = d[0]
            y = d[1]
            dd = ddpl[i].f(j/amt)
            dx = dd[0]
            dy = dd[1]
            if((pow(x,2)+pow(y,2))>0):
                final += (x*dy-y*dx)/(pow(x,2)+pow(y,2))/amt
        if i < len(dpl)-1:
            tp = dpl[i+1].f(0)
            z1x = False
            if abs(tp[0]) > 0:
                if math.log(abs(tp[0]),10) < -10:
                    z1x = True
            else:
                z1x = True
            z1y = False
            if abs(tp[1]) > 0:
                if math.log(abs(tp[1]),10) < -10:
                    z1y = True
            else:
                z1y = True
            if z1x and z1y:
                tp = dpl[i+1].f(0.000001)
            a1 = da(0,0,tp[0],tp[1])
            z2x = False
            tp2 = dpl[i].f(1)
            if abs(tp2[0]) > 0:
                if math.log(abs(tp2[0]),10) < -10:
                    z2x = True
            else:
                z2x = True
            z2y = False
            if abs(tp2[1]) > 0:
                if math.log(abs(tp2[1]),10) < -10:
                    z2y = True
            else:
                z2y = True
            if z2x and z2y:
                tp2 = dpl[i].f(0.999999)
            a2 = da(0,0,tp2[0],tp2[1])
            nex = (a1-a2)*math.pi/180
            if abs(a1-a2) == 180:
                if da(0,0,dpl[i+1].f(0.000001)[0],dpl[i+1].f(0.000001)[1])-da(0,0,dpl[i].f(0.999999)[0],dpl[i].f(0.999999)[1]) > 0:
                    nex = math.pi
                else:
                    nex = -math.pi
            if nex > math.pi:
                nex -= (2*math.pi)
            elif nex < -math.pi:
                nex += (2*math.pi)
            final += nex
    i = -1
    tp = dpl[i+1].f(0)
    z1x = False
    if abs(tp[0]) > 0:
        if math.log(abs(tp[0]),10) < -10:
            z1x = True
    else:
        z1x = True
    z1y = False
    if abs(tp[1]) > 0:
        if math.log(abs(tp[1]),10) < -10:
            z1y = True
    else:
        z1y = True
    if z1x and z1y:
        tp = dpl[i+1].f(0.000001)
    a1 = da(0,0,tp[0],tp[1])
    tp2 = dpl[i].f(1)
    z2x = False
    if abs(tp2[0]) > 0:
        if math.log(abs(tp2[0]),10) < -10:
            z2x = True
    else:
        z2x = True
    z2y = False
    if abs(tp2[1]) > 0:
        if math.log(abs(tp2[1]),10) < -10:
            z2y = True
    else:
        z2y = True
    if z2x and z2y:
        tp2 = dpl[i].f(0.999999)
    a2 = da(0,0,tp2[0],tp2[1])
    if abs(a1-a2) == 180:
        if da(0,0,dpl[i+1].f(0.000001)[0],dpl[i+1].f(0.000001)[1])-da(0,0,dpl[i].f(0.999999)[0],dpl[i].f(0.999999)[1]) > 0:
            nex = math.pi
        else:
            nex = -math.pi
    nex = (a1-a2)*math.pi/180
    if nex > math.pi:
        nex -= 2*math.pi
    elif nex < -math.pi:
        nex += 2*math.pi
    final += nex
    if round(final/(2*math.pi)) == 0:
        osudbvoa
    return round(final/(2*math.pi))
def inPrism(ipl,p,d,df):
    final = 0
    lDist = 100
    for i in range(len(ipl)):
        sDist = findClosest(ipl[i],p,df[i])[1]
        if sDist < lDist:
            lDist = sDist
        for j in range(100):
            sp = ipl[i].f(j/100)
            dsp = df[i].f(j/100)
            sp[0] -= p[0]
            sp[1] -= p[1]
            if pow(sp[0],2)+pow(sp[1],2) > 0:
                final += (sp[0]*dsp[1]-sp[1]*dsp[0])/(pow(sp[0],2)+pow(sp[1],2))/100
    if round(final/(math.pi*2))*d >= 1:
        return True
    else:
        if lDist < pow(10,-6):
            return True
        else:
            return False
def oInPrism(ipl,p,d,df):
    final = 0
    for i in range(len(ipl)):
        for j in range(100):
            sp = ipl[i].f(j/100)
            dsp = df[i].f(j/100)
            sp[0] -= p[0]
            sp[1] -= p[1]
            if pow(sp[0],2)+pow(sp[1],2) > 0:
                final += (sp[0]*dsp[1]-sp[1]*dsp[0])/(pow(sp[0],2)+pow(sp[1],2))/100
    if round(final/(math.pi*2))*d >= 1:
        return True
    else:
        return False
def ninPrism(ipl,p,d,df):
    final = 0
    lDist = 100
    for i in range(len(ipl)):
        sDist = findClosest(ipl[i],p,df[i])[1]
        if sDist < lDist:
            lDist = sDist
        for j in range(100):
            sp = ipl[i].f(j/100)
            dsp = df[i].f(j/100)
            sp[0] -= p[0]
            sp[1] -= p[1]
            if pow(sp[0],2)+pow(sp[1],2) > 0:
                final += (sp[0]*dsp[1]-sp[1]*dsp[0])/(pow(sp[0],2)+pow(sp[1],2))/100
    if round(final/(math.pi*2))*d >= 1:
        if lDist < pow(10,-6):
            return True
        else:
            return False
    else:
        return True
def insertIn(v,l,ind):
    final = []
    for i in range(ind):
        final.append(l[i])
    final.append(v)
    for i in range(ind,len(l)):
        final.append(l[i])
    return final
def antiFillPrism(p,t,d,df):
    lines = []
    for i in range(len(p)):
        lines.append(posToList(p[i],1,df[i])[0])
    sizes = [240]
    for i in range(math.ceil(math.log(t/240,0.5))+1):
        sizes.append(240/pow(2,i+1))
    final = []
    bo = [p[0].f(0),p[0].f(0)]
    for i in range(len(p)):
        for j in range(100):
            po = p[i].f(j/100)
            if po[0] < bo[0][0]:
                bo[0][0] = po[0]
            if po[1] < bo[0][1]:
                bo[0][1] = po[1]
            if po[0] > bo[1][0]:
                bo[1][0] = po[0]
            if po[1] > bo[1][1]:
                bo[1][1] = po[1]
    run = True
    while run:
        ab = [[0,0],[0,0]]
        ab[0][0] = math.floor(bo[0][0]/sizes[0])*sizes[0]
        ab[0][1] = math.floor(bo[0][1]/sizes[0])*sizes[0]
        ab[1][0] = math.ceil(bo[1][0]/sizes[0])*sizes[0]
        ab[1][1] = math.ceil(bo[1][1]/sizes[0])*sizes[0]
        sp = []
        i = ab[0][0]
        while i <= ab[1][0]:
            j = ab[0][1]
            while j <= ab[1][1]:
                sp.append([i,j,ninPrism(p,[i,j],d,df)])
                j += sizes[0]
            i += sizes[0]
        if len(sp) > 4:
            for j in range(len(sp)):
                if sp[j][2] == True:
                    run = False
            if run:
                sizes[0:1] = []
        else:
            sizes[0:1] = []
    confirmed = []
    samp = ""
    for x in range(len(sizes)):
        s = sizes[x]
        pointPos = []
        if x == 0:
            pointPos = sp
        else:
            pointPos = final[x-1][0]
        pc = []
        if x > 0:
            pc = final[x-1][1]
        points = []
        for i in range(len(pointPos)):
            points.append(pointPos[i][2])
        newBlocks = []
        for i in range(len(points)):
            sub = [points[i],-1,-1,-1,pointPos[i]]
            j = i-1
            run = True
            if j < 0:
                run = False
            while run:
                if pointPos[i][0] == pointPos[j][0] and pointPos[i][1] == pointPos[j][1]+s:
                    newBlocks[j][1] = points[i]
                if pointPos[i][0] == pointPos[j][0]+s and pointPos[i][1] == pointPos[j][1]:
                    newBlocks[j][2] = points[i]
                if pointPos[i][0] == pointPos[j][0]+s and pointPos[i][1] == pointPos[j][1]+s:
                    newBlocks[j][3] = points[i]
                if pointPos[i][0]-pointPos[j][0] > s:
                    run = False
                j-=1
                if j < 0:
                    run = False
            newBlocks.append(sub)
        for i in range(len(newBlocks)-1,-1,-1):
            if newBlocks[i][1] == -1 or newBlocks[i][2] == -1 or newBlocks[i][3] == -1:
                newBlocks[i:i+1] = []
        classBlocks = []
        for i in range(len(pc)):
            classBlocks.append([pc[i][0],pc[i][1],3,[True,True,True,True]])
            classBlocks.append([pc[i][0]+s,pc[i][1],3,[True,True,True,True]])
            classBlocks.append([pc[i][0]+s,pc[i][1]+s,3,[True,True,True,True]])
            classBlocks.append([pc[i][0],pc[i][1]+s,3,[True,True,True,True]])
        for i in range(len(newBlocks)):
            sub = 0
            if newBlocks[i][0] and newBlocks[i][1] and newBlocks[i][2] and newBlocks[i][3]:
                sub5 = True
                for j in range(len(p)):
                    sub2 = [[newBlocks[i][4][0],newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]]]
                    sub4 = detectInter(sub2,lines[j],"ai")
                    if len(sub4) > 0:
                        sub5 = False
                if sub5:
                    sub = 1
                else:
                    sub = 0
            elif not newBlocks[i][0] and not newBlocks[i][1] and not newBlocks[i][2] and not newBlocks[i][3]:
                sub5 = True
                for j in range(len(p)):
                    sub2 = [[newBlocks[i][4][0],newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]]]
                    sub4 = detectInter(sub2,lines[j],"ai")
                    if len(sub4) > 0:
                        sub5 = False
                if sub5:
                    sub = 2
                else:
                    sub = 0
            classBlocks.append([newBlocks[i][4][0],newBlocks[i][4][1],sub,newBlocks[i]])
            if sub == 1:
                confirmed.append([newBlocks[i][4][0],newBlocks[i][4][1],s])
        sortedBlocks = [classBlocks[0]]
        for i in range(1,len(classBlocks)):
            count = i-1
            run = True
            while run:
                if classBlocks[i][0] > sortedBlocks[count][0]:
                    sortedBlocks = insertIn(classBlocks[i],sortedBlocks,count+1)
                    run = False
                if classBlocks[i][0] == sortedBlocks[count][0]:
                    if classBlocks[i][1] > sortedBlocks[count][1]:
                        sortedBlocks = insertIn(classBlocks[i],sortedBlocks,count+1)
                        run = False
                if count == 0 and run:
                    sortedBlocks = insertIn(classBlocks[i],sortedBlocks,0)
                    run = False
                count -= 1
        classBlocks = sortedBlocks
        for i in range(len(classBlocks)):
            adjCheck = [-1,-1,-1,-1,-1]
            if i < len(classBlocks)-1:
                if classBlocks[i+1][0] == classBlocks[i][0] and classBlocks[i+1][1] == classBlocks[i][1]+s:
                   adjCheck[0] = classBlocks[i+1][2]
                run = True
                count = i+1
                while run:
                    if classBlocks[count][0]-classBlocks[i][0] > s:
                        run = False
                    if classBlocks[count][0]-classBlocks[i][0] == s:
                        if classBlocks[count][1] == classBlocks[i][1]:
                            adjCheck[1] = classBlocks[count][2]
                        if classBlocks[count][1] == classBlocks[i][1]+s:
                            adjCheck[4] = classBlocks[count][2]
                            run = False
                        if classBlocks[count][1] > classBlocks[i][1]:
                            run = False
                    count += 1
                    if count == len(classBlocks):
                       run = False
            if i > 0:
                if classBlocks[i-1][0] == classBlocks[i][0] and classBlocks[i-1][1] == classBlocks[i][1]-s:
                    adjCheck[2] = classBlocks[i-1][2]
                run = True
                count = i-1
                while run:
                    if classBlocks[count][0]-classBlocks[i][0] < -s:
                        run = False
                    if classBlocks[count][0]-classBlocks[i][0] == -s:
                        if classBlocks[count][1] == classBlocks[i][1]:
                            adjCheck[3] = classBlocks[count][2]
                            run = False
                        if classBlocks[count][1]<classBlocks[i][1]:
                           run=False
                    count -= 1
                    if count == -1:
                       run = False
            classBlocks[i].append(adjCheck)
        newPoints = []
        for i in range(len(classBlocks)):
            newPoints.append([classBlocks[i][0],classBlocks[i][1],classBlocks[i][3][0]])
            if classBlocks[i][2] == 0:
                if classBlocks[i][4][1] == -1:
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1],True])
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s/2,True])
                if classBlocks[i][4][1] == 2:
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s/2,False])
                if classBlocks[i][4][1] == 1 or classBlocks[i][4][1] == 3:
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s/2,True])
                if classBlocks[i][4][0] == -1:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s,True])
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s,True])
                if classBlocks[i][4][0] == 2:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s,False])
                if classBlocks[i][4][0] == 1 or classBlocks[i][4][0] == 3:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s,True])
                if (classBlocks[i][4][0] == -1 or classBlocks[i][4][0] == 1 or classBlocks[i][4][0] == 3) and (classBlocks[i][4][1] == -1 or classBlocks[i][4][1] == 1 or classBlocks[i][4][1] == 3) and (classBlocks[i][4][4] == -1 or classBlocks[i][4][4] == 1 or classBlocks[i][4][4] == 3):
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s,True])
                if classBlocks[i][4][2] == 2:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1],False])
                elif classBlocks[i][4][2] == 1 or classBlocks[i][4][2] == 3 or classBlocks[i][4][2] == -1:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1],True])
                else:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1],-1])
                if classBlocks[i][4][3] == 2:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s/2,False])
                elif classBlocks[i][4][3] == 1 or classBlocks[i][4][3] == 3 or classBlocks[i][4][3] == -1:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s/2,True])
                else:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s/2,-1])
                newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s/2,-1])
        for i in range(len(newPoints)):
            if newPoints[i][2] == -1:
                newPoints[i][2] = ninPrism(p,[newPoints[i][0],newPoints[i][1]],d,df)
        sortedPoints = [newPoints[0]]
        for i in range(1,len(newPoints)):
            count = i-1
            run = True
            while run:
                if newPoints[i][0] > sortedPoints[count][0]:
                    sortedPoints = insertIn(newPoints[i],sortedPoints,count+1)
                    run = False
                if newPoints[i][0] == sortedPoints[count][0]:
                    if newPoints[i][1] > sortedPoints[count][1]:
                        sortedPoints = insertIn(newPoints[i],sortedPoints,count+1)
                        run = False
                if count == 0:
                   run = False
                count -= 1
        for i in range(len(sortedPoints)-1,0,-1):
            if sortedPoints[i][0] == sortedPoints[i-1][0] and sortedPoints[i][1] == sortedPoints[i-1][1]:
                sortedPoints[i-1:i] = []
        ac = []
        for i in range(len(classBlocks)):
            if classBlocks[i][2] == 3 or classBlocks[i][2] == 1:
                if not ((classBlocks[i][4][0] == 3 or classBlocks[i][4][0] == 1) and (classBlocks[i][4][1] == 3 or classBlocks[i][4][1] == 1) and (classBlocks[i][4][2] == 3 or classBlocks[i][4][2] == 1) and (classBlocks[i][4][3] == 3 or classBlocks[i][4][3] == 1)):
                    ac.append([classBlocks[i][0],classBlocks[i][1]])
                sub = True
                for j in range(4):
                    if not ((classBlocks[i][4][j] == 3 or classBlocks[i][4][j] == 1) and (classBlocks[i][4][(j+1)%4] == 3 or classBlocks[i][4][(j+1)%4] == 1) and (classBlocks[i][4][(j+2)%4] == 3 or classBlocks[i][4][(j+2)%4] == 1) and classBlocks[i][4][(j+3)%4] == -1):
                        sub = False
                for j in range(4):
                    if not ((classBlocks[i][4][j] == 3 or classBlocks[i][4][j] == 1) and (classBlocks[i][4][(j+1)%4] == 3 or classBlocks[i][4][(j+1)%4] == 1) and classBlocks[i][4][(j+2)%4] == -1 and classBlocks[i][4][(j+3)%4] == -1):
                        sub = False
                if sub:
                    ac.append([classBlocks[i][0],classBlocks[i][1]])
        final.append([sortedPoints,ac])
    return confirmed
def fillPrism(p,t,d,df):
    lines = []
    for i in range(len(p)):
        lines.append(posToList(p[i],1,df[i])[0])
    sizes = [240]
    for i in range(math.ceil(math.log(t/240,0.5))+1):
        sizes.append(240/pow(2,i+1))
    final = []
    bo = [p[0].f(0),p[0].f(0)]
    for i in range(len(p)):
        for j in range(100):
            po = p[i].f(j/100)
            if po[0] < bo[0][0]:
                bo[0][0] = po[0]
            if po[1] < bo[0][1]:
                bo[0][1] = po[1]
            if po[0] > bo[1][0]:
                bo[1][0] = po[0]
            if po[1] > bo[1][1]:
                bo[1][1] = po[1]
    run = True
    while run:
        ab = [[0,0],[0,0]]
        ab[0][0] = math.floor(bo[0][0]/sizes[0])*sizes[0]
        ab[0][1] = math.floor(bo[0][1]/sizes[0])*sizes[0]
        ab[1][0] = math.ceil(bo[1][0]/sizes[0])*sizes[0]
        ab[1][1] = math.ceil(bo[1][1]/sizes[0])*sizes[0]
        sp = []
        i = ab[0][0]
        while i <= ab[1][0]:
            j = ab[0][1]
            while j <= ab[1][1]:
                sp.append([i,j,inPrism(p,[i,j],d,df)])
                j += sizes[0]
            i += sizes[0]
        if len(sp) > 4:
            for j in range(len(sp)):
                if sp[j][2] == True:
                    run = False
            if run:
                sizes[0:1] = []
        else:
            sizes[0:1] = []
    confirmed = []
    for x in range(len(sizes)):
        s = sizes[x]
        pointPos = []
        if x == 0:
            pointPos = sp
        else:
            pointPos = final[x-1][0]
        pc = []
        if x > 0:
            pc = final[x-1][1]
        points = []
        for i in range(len(pointPos)):
            points.append(pointPos[i][2])
        newBlocks = []
        for i in range(len(points)):
            sub = [points[i],-1,-1,-1,pointPos[i]]
            j = i-1
            run = True
            if j < 0:
                run = False
            while run:
                if pointPos[i][0] == pointPos[j][0] and pointPos[i][1] == pointPos[j][1]+s:
                    newBlocks[j][1] = points[i]
                if pointPos[i][0] == pointPos[j][0]+s and pointPos[i][1] == pointPos[j][1]:
                    newBlocks[j][2] = points[i]
                if pointPos[i][0] == pointPos[j][0]+s and pointPos[i][1] == pointPos[j][1]+s:
                    newBlocks[j][3] = points[i]
                if pointPos[i][0]-pointPos[j][0] > s:
                    run = False
                j-=1
                if j < 0:
                    run = False
            newBlocks.append(sub)
        for i in range(len(newBlocks)-1,-1,-1):
            if newBlocks[i][1] == -1 or newBlocks[i][2] == -1 or newBlocks[i][3] == -1:
                newBlocks[i:i+1] = []
        classBlocks = []
        for i in range(len(pc)):
            classBlocks.append([pc[i][0],pc[i][1],3,[True,True,True,True]])
            classBlocks.append([pc[i][0]+s,pc[i][1],3,[True,True,True,True]])
            classBlocks.append([pc[i][0]+s,pc[i][1]+s,3,[True,True,True,True]])
            classBlocks.append([pc[i][0],pc[i][1]+s,3,[True,True,True,True]])
        for i in range(len(newBlocks)):
            sub = 0
            if newBlocks[i][0] and newBlocks[i][1] and newBlocks[i][2] and newBlocks[i][3]:
                sub5 = True
                for j in range(len(p)):
                    sub2 = [[newBlocks[i][4][0],newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]]]
                    sub4 = detectInter(sub2,lines[j],"ai")
                    if len(sub4) > 0:
                        sub5 = False
                if sub5:
                    sub = 1
                else:
                    sub = 0
            elif not newBlocks[i][0] and not newBlocks[i][1] and not newBlocks[i][2] and not newBlocks[i][3]:
                sub5 = True
                for j in range(len(p)):
                    sub2 = [[newBlocks[i][4][0],newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]],[newBlocks[i][4][0]+s,newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]+s],[newBlocks[i][4][0],newBlocks[i][4][1]]]
                    sub4 = detectInter(sub2,lines[j],"ai")
                    if len(sub4) > 0:
                        sub5 = False
                if sub5:
                    sub = 2
                else:
                    sub = 0
            classBlocks.append([newBlocks[i][4][0],newBlocks[i][4][1],sub,newBlocks[i]])
            if sub == 1:
                confirmed.append([newBlocks[i][4][0],newBlocks[i][4][1],s])
        sortedBlocks = [classBlocks[0]]
        for i in range(1,len(classBlocks)):
            count = i-1
            run = True
            while run:
                if classBlocks[i][0] > sortedBlocks[count][0]:
                    sortedBlocks = insertIn(classBlocks[i],sortedBlocks,count+1)
                    run = False
                if classBlocks[i][0] == sortedBlocks[count][0]:
                    if classBlocks[i][1] > sortedBlocks[count][1]:
                        sortedBlocks = insertIn(classBlocks[i],sortedBlocks,count+1)
                        run = False
                if count == 0 and run:
                    sortedBlocks = insertIn(classBlocks[i],sortedBlocks,0)
                    run = False
                count -= 1
        classBlocks = sortedBlocks
        for i in range(len(classBlocks)):
            adjCheck = [-1,-1,-1,-1,-1]
            if i < len(classBlocks)-1:
                if classBlocks[i+1][0] == classBlocks[i][0] and classBlocks[i+1][1] == classBlocks[i][1]+s:
                   adjCheck[0] = classBlocks[i+1][2]
                run = True
                count = i+1
                while run:
                    if classBlocks[count][0]-classBlocks[i][0] > s:
                        run = False
                    if classBlocks[count][0]-classBlocks[i][0] == s:
                        if classBlocks[count][1] == classBlocks[i][1]:
                            adjCheck[1] = classBlocks[count][2]
                        if classBlocks[count][1] == classBlocks[i][1]+s:
                            adjCheck[4] = classBlocks[count][2]
                            run = False
                        if classBlocks[count][1] > classBlocks[i][1]:
                            run = False
                    count += 1
                    if count == len(classBlocks):
                       run = False
            if i > 0:
                if classBlocks[i-1][0] == classBlocks[i][0] and classBlocks[i-1][1] == classBlocks[i][1]-s:
                    adjCheck[2] = classBlocks[i-1][2]
                run = True
                count = i-1
                while run:
                    if classBlocks[count][0]-classBlocks[i][0] < -s:
                        run = False
                    if classBlocks[count][0]-classBlocks[i][0] == -s:
                        if classBlocks[count][1] == classBlocks[i][1]:
                            adjCheck[3] = classBlocks[count][2]
                            run = False
                        if classBlocks[count][1]<classBlocks[i][1]:
                           run=False
                    count -= 1
                    if count == -1:
                       run = False
            classBlocks[i].append(adjCheck)
        newPoints = []
        for i in range(len(classBlocks)):
            newPoints.append([classBlocks[i][0],classBlocks[i][1],classBlocks[i][3][0]])
            if classBlocks[i][2] == 0:
                if classBlocks[i][4][1] == -1:
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1],False])
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s/2,False])
                if classBlocks[i][4][1] == 2:
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s/2,False])
                if classBlocks[i][4][1] == 1 or classBlocks[i][4][1] == 3:
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s/2,True])
                if classBlocks[i][4][0] == -1:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s,False])
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s,False])
                if classBlocks[i][4][0] == 2:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s,False])
                if classBlocks[i][4][0] == 1 or classBlocks[i][4][0] == 3:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s,True])
                if (classBlocks[i][4][0] == -1 or classBlocks[i][4][0] == 2) and (classBlocks[i][4][1] == -1 or classBlocks[i][4][1] == 2) and (classBlocks[i][4][4] == -1 or classBlocks[i][4][4] == 2):
                    newPoints.append([classBlocks[i][0]+s,classBlocks[i][1]+s,False])
                if classBlocks[i][4][2] == -1 or classBlocks[i][4][2] == 2:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1],False])
                elif classBlocks[i][4][2] == 1 or classBlocks[i][4][2] == 3:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1],True])
                else:
                    newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1],-1])
                if classBlocks[i][4][3] == -1 or classBlocks[i][4][3] == 2:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s/2,False])
                elif classBlocks[i][4][3] == 1 or classBlocks[i][4][3] == 3:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s/2,True])
                else:
                    newPoints.append([classBlocks[i][0],classBlocks[i][1]+s/2,-1])
                newPoints.append([classBlocks[i][0]+s/2,classBlocks[i][1]+s/2,-1])
        for i in range(len(newPoints)):
            if newPoints[i][2] == -1:
                newPoints[i][2] = inPrism(p,[newPoints[i][0],newPoints[i][1]],d,df)
        sortedPoints = [newPoints[0]]
        for i in range(1,len(newPoints)):
            count = i-1
            run = True
            while run:
                if newPoints[i][0] > sortedPoints[count][0]:
                    sortedPoints = insertIn(newPoints[i],sortedPoints,count+1)
                    run = False
                if newPoints[i][0] == sortedPoints[count][0]:
                    if newPoints[i][1] > sortedPoints[count][1]:
                        sortedPoints = insertIn(newPoints[i],sortedPoints,count+1)
                        run = False
                if count == 0:
                   run = False
                count -= 1
        for i in range(len(sortedPoints)-1,0,-1):
            if sortedPoints[i][0] == sortedPoints[i-1][0] and sortedPoints[i][1] == sortedPoints[i-1][1]:
                sortedPoints[i-1:i] = []
        ac = []
        for i in range(len(classBlocks)):
            if classBlocks[i][2] == 3 or classBlocks[i][2] == 1:
                if not ((classBlocks[i][4][0] == 3 or classBlocks[i][4][0] == 1) and (classBlocks[i][4][1] == 3 or classBlocks[i][4][1] == 1) and (classBlocks[i][4][2] == 3 or classBlocks[i][4][2] == 1) and (classBlocks[i][4][3] == 3 or classBlocks[i][4][3] == 1)):
                    ac.append([classBlocks[i][0],classBlocks[i][1]])
                sub = True
                for j in range(4):
                    if not ((classBlocks[i][4][j] == 3 or classBlocks[i][4][j] == 1) and (classBlocks[i][4][(j+1)%4] == 3 or classBlocks[i][4][(j+1)%4] == 1) and (classBlocks[i][4][(j+2)%4] == 3 or classBlocks[i][4][(j+2)%4] == 1) and classBlocks[i][4][(j+3)%4] == -1):
                        sub = False
                for j in range(4):
                    if not ((classBlocks[i][4][j] == 3 or classBlocks[i][4][j] == 1) and (classBlocks[i][4][(j+1)%4] == 3 or classBlocks[i][4][(j+1)%4] == 1) and classBlocks[i][4][(j+2)%4] == -1 and classBlocks[i][4][(j+3)%4] == -1):
                        sub = False
                if sub:
                    ac.append([classBlocks[i][0],classBlocks[i][1]])
        final.append([sortedPoints,ac])
    return confirmed
def xor_bytes(data: bytes, value: int) -> bytes:
    return bytes(map(lambda x: x ^ value, data))
def search(string,target):
    sub = []
    points = []
    for i in range(len(string)-len(target)):
        if len(sub) < len(target):
            sub.append(string[i])
        else:
            s = True
            count = 0
            while s and count < len(target):
                if target[count] == sub[count]:
                    count += 1
                else:
                    s = False
            if s:
                points.append(i)
            sub[0:1] = []
            sub.append(string[i])
    return points
def printPara(x):
    print("x")
    for i in range(len(x.x.l)):
        if x.x.l[i][0] == 0:
            print(i, x.x.l[i][0], x.x.l[i][1].c, x.x.l[i][2], x.x.l[i][3])
        else:
            print(i, x.x.l[i][0], x.x.l[i][1], x.x.l[i][2], x.x.l[i][3])
    print(x.x.pt, "\ny")
    for i in range(len(x.y.l)):
        if x.y.l[i][0] == 0:
            print(i, x.y.l[i][0], x.y.l[i][1].c, x.y.l[i][2], x.y.l[i][3])
        else:
            print(i, x.y.l[i][0], x.y.l[i][1], x.y.l[i][2], x.y.l[i][3])
    print(x.y.pt)
def printFull(x):
    for i in range(len(x.l)):
        if x.l[i][0] == 0:
            print(i, x.l[i][0], x.l[i][1].c, x.l[i][2], x.l[i][3])
        else:
            print(i, x.l[i][0], x.l[i][1], x.l[i][2], x.l[i][3])
    print(x.pt)
def dPara(x):
    return para(dFull(x.x),dFull(x.y))
def estInt(f,df):
    sub = posToList(f,1,df)
    final = [0,0]
    for i in range(len(sub[0])-1):
        final[0] += (sub[0][i][0]+(sub[0][i+1][0]-sub[0][i][0])/2)*(sub[1][i+1]-sub[1][i])
        final[1] += (sub[0][i][1]+(sub[0][i+1][1]-sub[0][i][1])/2)*(sub[1][i+1]-sub[1][i])
    return final
def cent(ipl,dpl):
    final = [0,0]
    for i in range(len(ipl)):
        sub = estInt(ipl[i],dpl[i])
        final[0] += sub[0]/len(ipl)
        final[1] += sub[1]/len(ipl)
    return final
screen = pygame.display.set_mode((600,480))
pygame.display.set_caption("delta")
pygame.init()
fonts = [0]
for i in range(100):
    fonts.append(pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mvboli.ttf"), i+1))
titleText = fonts[50].render("menu", 1, (0,0,0))
def dispText(t,p,s,c):
    textLines = []
    sub = ""
    for i in range(len(t)):
        if not t[i] == "\n":
            sub += t[i]
        else:
            textLines.append(sub)
            sub = ""
    textLines.append(sub)
    for i in range(len(textLines)):
        text = fonts[s].render(textLines[i], 1, c)
        screen.blit(text, text.get_rect(centerx=p[0], centery=p[1]-(len(textLines)-1)*s/2+s*i))
class button:
    def __init__(self, r, t, ts, tc, sc, mc, dc, en):
        self.r = r
        self.t = t
        self.ts = ts
        self.tc = tc
        self.sc = sc
        self.mc = mc
        self.dc = dc
        self.en = en
    def disp(self):
        mp = pygame.mouse.get_pos()
        ir = False
        nr = [self.r[0]-self.r[2]/2,self.r[1]-self.r[3]/2,self.r[2],self.r[3]]
        if self.en:
            if mp[0] > nr[0] and mp[0] < nr[0]+nr[2] and mp[1] > nr[1] and mp[1] < nr[1]+nr[3]:
                pygame.draw.rect(screen, self.mc, nr)
                ir = True
            else:
                pygame.draw.rect(screen, self.sc, nr)
        else:
            pygame.draw.rect(screen, self.dc, nr)
        dispText(self.t,[nr[0]+nr[2]/2,nr[1]+nr[3]/2],self.ts,self.tc)
        pygame.draw.rect(screen, (0,0,0), nr, 2)
        return ir
class cButton:
    def __init__(self, c, r, sc, mc):
        self.c = c
        self.r = r
        self.sc = sc
        self.mc = mc
    def disp(self):
        mp = pygame.mouse.get_pos()
        ir = False
        if dis(mp[0],mp[1],self.c[0],self.c[1]) < self.r:
            pygame.draw.circle(screen, self.mc, self.c, self.r)
            ir = True
        else:
            pygame.draw.circle(screen, self.sc, self.c, self.r)
        pygame.draw.circle(screen, (0,0,0), self.c, self.r, 1)
        return ir
class eButton:
    def __init__(self, r, v, sc, mc, ec, ts, tc, se):
        self.r = r
        self.v = v
        self.sc = sc
        self.mc = mc
        self.ec = ec
        self.ts = ts
        self.tc = tc
        self.se = se
    def disp(self):
        mp = pygame.mouse.get_pos()
        ir = False
        nr = [self.r[0]-self.r[2]/2,self.r[1]-self.r[3]/2,self.r[2],self.r[3]]
        if mp[0] > nr[0] and mp[0] < nr[0]+nr[2] and mp[1] > nr[1] and mp[1] < nr[1]+nr[3]:
            ir = True
        if not self.se:
            if ir:
                pygame.draw.rect(screen, self.mc, nr)
            else:
                pygame.draw.rect(screen, self.sc, nr)
        else:
            pygame.draw.rect(screen, self.ec, nr)
        dispText(self.v,[nr[0]+nr[2]/2,nr[1]+nr[3]/2],self.ts,self.tc)
        pygame.draw.rect(screen, (0,0,0), nr, 2)
        return ir
def bCirc(p,c,bt,s):
    pygame.draw.circle(screen, c, p, s)
    pygame.draw.circle(screen, (0,0,0), p, s, bt)
def vCurve(c,t,a,col,hol):
    b1 = wrap(c,full([[0,poly([t/2]),0,False]],[[0]]),[1,0])
    b2 = wrap(slicePara(c,[1,0]),full([[0,poly([t/2]),0,False]],[[0]]),[1,0])
    final = []
    df = dPara(c)
    sp = c.f(0)
    ep = c.f(1)
    dsp = df.f(0)
    dep = df.f(1)
    if dsp[0] == 0 and dsp[1] == 0:
        dsp = df.f(0.000001)
    if dep[0] == 0 and dep[1] == 0:
        dep = df.f(0.999999)
    san = da(0,0,dsp[0],dsp[1])/180*math.pi
    ean = da(0,0,dep[0],dep[1])/180*math.pi
    for i in range(a+1):
        smp = b1.f(i/a)
        final.append([(smp[0]+cam[0])*zoom,300-(smp[1]-cam[1])*zoom])
    for i in range(int(t)):
        final.append([(ep[0]+t/2*math.cos(math.pi/t*i-math.pi/2+ean)+cam[0])*zoom,300-(ep[1]+t/2*math.sin(math.pi/t*i-math.pi/2+ean)-cam[1])*zoom])
    for i in range(a+1):
        smp = b2.f(i/a)
        final.append([(smp[0]+cam[0])*zoom,300-(smp[1]-cam[1])*zoom])
    for i in range(int(t)):
        final.append([(sp[0]+t/2*math.cos(math.pi/t*i+math.pi/2+san)+cam[0])*zoom,300-(sp[1]+t/2*math.sin(math.pi/t*i+math.pi/2+san)-cam[1])*zoom])
    pygame.draw.polygon(screen,col,final,hol)

def rendCurve(c,t):
    b1 = wrap(c,full([[0,poly([t/2]),0,False]],[[0]]),[1,0])
    b2 = wrap(slicePara(c,[1,0]),full([[0,poly([t/2]),0,False]],[[0]]),[1,0])
    final = []
    df = dPara(c)
    sp = c.f(0)
    ep = c.f(1)
    dsp = df.f(0)
    dep = df.f(1)
    if dsp[0] == 0 and dsp[1] == 0:
        dsp = df.f(0.000001)
    if dep[0] == 0 and dep[1] == 0:
        dep = df.f(0.999999)
    san = da(0,0,dsp[0],dsp[1])/180*math.pi
    ean = da(0,0,dep[0],dep[1])/180*math.pi
    for i in range(100):
        smp = b1.f(i/100)
        final.append([smp[0],smp[1]])
    for i in range(int(t)):
        final.append([ep[0]+t/2*math.cos(math.pi/t*i-math.pi/2+ean),ep[1]+t/2*math.sin(math.pi/t*i-math.pi/2+ean)])
    for i in range(100):
        smp = b2.f(i/100)
        final.append([smp[0],smp[1]])
    for i in range(int(t)):
        final.append([sp[0]+t/2*math.cos(math.pi/t*i+math.pi/2+san),sp[1]+t/2*math.sin(math.pi/t*i+math.pi/2+san)])
    return final
def dispCurve(p,col,h):
    final = []
    for i in range(len(p)):
        final.append([(p[i][0]+cam[0])*zoom,300-(p[i][1]-cam[1])*zoom])
    pygame.draw.polygon(screen,col,final,h)

menu = "main"
newProjectButton = button((300,250,100,30), "new project", 15, (0,0,0), (128,128,128),(159,159,159),0,True)
contProjectButton = button((300,300,100,30), "continue project", 10, (0,0,0), (128,128,128),(159,159,159),(64,64,64),False)
scroll = False
cam = [0,0]
drawMode = 0
drawButtonNames=["bezier\ncurve", "spiral", "translate", "composite\ncurve", "wrap", "tangent", "single\nwarp", "double\nwarp", "quad\nwarp", "bspline", "intersection"]
drawButtons = []
drawButtonSig = []
for i in range(len(drawButtonNames)):
    drawButtons.append(button((50+80*(i%5),350+int(i/5)*40,60,30), drawButtonNames[i], 10, (0,0,0), (159,159,159),(191,191,191),0,True))
    drawButtonSig.append(False)
drawInst = [[""],
            ["click to place the start point\npress z to cancel","click to place the control points\npress enter when done\npress z to undo","click to place the end point\npress z to undo","","click to add control points\npress enter when done","click a control point to delete it\npress enter when done"],
            ["click to place the center of the spiral\npress z to cancel",""],
            ["","","",""],
            ["","",""],
            ["","",""],
            ["","",""],
            ["","",""],
            ["","","",""],
            ["","","","","",""],
            ["click to place the start point\npress z to cancel","click to place the control points\npress enter when done\npress z to undo","click to place the end point\npress z to undo","","click to add control points\npress enter when done","click a control point to delete it\npress enter when done"],
            ["","",""],
            ]
sp = []
cp = []
ep = []
sc = None
spSig = False
cpButtons = []
cpSigs = []
epSig = False
drag = False
dragType = [0,0]
utilNames = ["editor level","thickness","color","z order"]
utilVals=[0,10,0,0]
utilButtons = []
utilButtonSig = []
for i in range(len(utilNames)):
    utilButtons.append(eButton((50+80*i,340,50,20), str(utilVals[i]), (159,159,159), (191,191,191), (223,223,223), 10, (0,0,0), False))
    utilButtonSig.append(False)
coreUtil = [
    [],
    [25,50,0,90],
    [],
    [],
    [1,0],
    [0,0],
    [100,100,0,0],
    [100,100,0,0],
    [100,100,0,0],
    [],
    [],
]
primUtil = [2,0,1]
def configUtil(t):
    utilButtons = []
    utilButtonSig = []
    if t == 1:
        utilNames = ["start radius","final radius","degree offset","degree amount","editor level","thickness","color","z order"]
    elif t == 4:
        utilNames = ["scale factor","translation","editor level","thickness","color","z order"]
    elif t == 5:
        utilNames = ["base point","sample point","editor level","thickness","color","z order"]
    elif t == 6 or t == 7 or t == 8:
        utilNames = ["scope width","scope height","translate x","translate y","editor level","thickness","color","z order"]
    else:
        utilNames = ["editor level","thickness","color","z order"]
    utilVals = []
    for i in range(len(coreUtil[t])):
        utilVals.append(coreUtil[t][i])
    utilVals.append(editorLevel)
    for i in range(3):
        utilVals.append(primUtil[i])
    if viewMode == 2 or viewMode == 3:
        utilNames[len(utilNames)-3:len(utilNames)] = []
        utilVals[len(utilVals)-3:len(utilVals)] = []
    for i in range(len(utilNames)):
        utilButtons.append(eButton((50+80*(i%4),340+int(i/4)*50,50,20), str(utilVals[i]), (159,159,159), (191,191,191), (223,223,223), 10, (0,0,0), False))
        utilButtonSig.append(False)
    return [utilButtons, utilButtonSig, utilNames, utilVals, t]
selectedUtil = -1
bezDrawButtonNames = ["add control\npoints","delete control\npoints"]
bezDrawButtons = []
bezDrawButtonSig = []
for i in range(len(bezDrawButtonNames)):
    bezDrawButtons.append(button((120+100*i,400,80,30), bezDrawButtonNames[i], 10, (0,0,0), (159,159,159),(191,191,191),0,True))
    bezDrawButtonSig.append(False)
finishButton = button((560,345,40,50), "finish", 10, (0,0,0), (96,191,96),(128,255,128),0,True)
finishSig = False
cancelButton = button((560,435,40,50), "cancel", 10, (0,0,0), (191,96,96),(255,128,128),0,True)
cancelSig = False
curves = [[],[],[],[]]
dCurves = [[],[],[],[]]
curvesUtil = [[],[],[],[]]
curveLines = []
modeNames = ["normal","glow","patch","aux"]
modeBColors = [[(191,96,96),(255,128,128)],[(96,96,191),(128,128,255)],[(96,191,96),(128,255,128)],[(191,191,96),(255,255,128)]]
modeButtons = []
modeButtonSig = []
defModeButtons = []
defModeButtonSig = []
for i in range(len(modeNames)):
    modeButtons.append(button((397.5+65*(i%2),370+int(i/2)*65,40,40), modeNames[i], 10, (0,0,0), modeBColors[i][0],modeBColors[i][1],0,True))
    defModeButtons.append(button((470,360+i*30,50,20), modeNames[i], 10, (0,0,0), modeBColors[i][0],modeBColors[i][1],0,True))
    modeButtonSig.append(False)
    defModeButtonSig.append(False)
viewMode = 0
pManageButtonNames = ["save","back","delete"]
pManageButtons = []
for i in range(len(pManageButtonNames)):
    pManageButtons.append(button((560,330+i*60,50,30), pManageButtonNames[i], 15, (0,0,0), (159,159,159),(191,191,191),0,True))
pManageButtonSig = [False,False,False]
newProject = True
contProjectSig = False
npwButton1 = button((200,350,100,50), "keep it", 25, (0,0,0), (159,159,159),(191,191,191),0,True)
npwSig1 = False
npwButton2 = button((400,350,100,50), "scrap it", 25, (0,0,0), (159,159,159),(191,191,191),0,True)
npwSig2 = False
sampT = 0
prevUtil = []
curveSig = [[],[],[],[]]
translateSeqTyp = [0]
translateSeqVal = [[50,50]]
translateSig = []
translateProtoSig = []
translateProtoButtons = []
translateButtons = []
translateButtonSelected = []
for i in range(6):
    translateProtoButtons.append(button((100+100*(i%3),350+int(i/3)*80,60,50), "", 15, (0,0,0), (159,159,159),(191,191,191),0,True))
    translateProtoSig.append(False)
    translateButtons.append([])
    translateSig.append([])
    translateButtons[i].append(button((100+100*(i%3),350+int(i/3)*80-12.5,60,25), "", 10, (0,0,0), (159,159,159),(191,191,191),0,True))
    translateButtons[i].append(eButton((100+100*(i%3)-15,350+int(i/3)*80+12.5,30,25), "", (159,159,159), (191,191,191), (223,223,223), 10, (0,0,0), False))
    translateButtons[i].append(eButton((100+100*(i%3)+15,350+int(i/3)*80+12.5,30,25), "", (159,159,159), (191,191,191), (223,223,223), 10, (0,0,0), False))
    for j in range(3):
        translateSig[i].append(False)
    translateButtonSelected.append([False,False])
translateButtons[0][1].v = "50"
translateButtons[0][2].v = "50"
translateNames = ["translation","rotation","scale"]
selectedTranslationPara = [-1,0]
translateButtonStrings = ["",""]
translateValueOffset = [0]
addTranslateParamButton = button((500,370,120,30), "add parameter", 10, (0,0,0), (159,159,159),(191,191,191),0,True)
delTranslateParamButton = button((500,410,120,30), "delete parameter", 10, (0,0,0), (159,159,159),(191,191,191),0,True)
continueButton = button((500,450,120,30), "continue", 15, (0,0,0), (159,159,159),(191,191,191),0,True)
addTranslateSig = False
delTranslateSig = False
continueSig = False
backButton = button((500,410,120,30), "back", 20, (0,0,0), (159,159,159),(191,191,191),0,True)
backSig = False
def reconfigTranslateParam():
    for i in range(6):
        if i < len(translateSeqVal):
            translateButtons[i][1].v = str(translateSeqVal[i][0])
            translateButtons[i][2].v = str(translateSeqVal[i][1])
translateParamPage = 0
prevParamButton = button((25,390,30,50), "<", 25, (0,0,0), (159,159,159),(191,191,191),(96,96,96),False)
prevPageSig = False
nextParamButton = button((375,390,30,50), ">", 25, (0,0,0), (159,159,159),(191,191,191),(96,96,96),False)
nextPageSig = False
cCurveX = []
cCurveY = []
prevUtilT = []
bCurve = []
sCurve = []
wrapParam = [[0,0,0],[0,0,0,"x"]]
curveValTypeButton = button((170,430,50,40), wrapParam[1][3], 20, (0,0,0), (159,159,159),(191,191,191),(96,96,96),True)
curveValSig = False
tangentParam = [0,0]
sWarpParam = [0,[]]
dWarpParam = [0,0,[]]
qWarpParam = [0,0,0,0,[]]
scl = []
bspParam = [3,0]
bspDegreeButton = eButton((120,440,80,30), str(3), (159,159,159), (191,191,191), (223,223,223), 20, (0,0,0), False)
bspModeButton = button((220,440,80,30), "straight", 15, (0,0,0), (159,159,159),(191,191,191),0,True)
bspDegreeSig = False
bspModeSig = False
curveParam = [[],[],[],[]]
cCurveXVal = []
cCurveYVal = []
undoModes = [4.01,5.01,6.01,7.01,8.01,8.02,9.01,9.02,9.03,9.04,11.01]
edit = False
mIntCurve = []
bIntCurves = []
intSig1 = False
intSig2 = False
intP1 = []
intP2 = []
intParam = [0,0]
intButton1 = eButton((120,400,80,30), str(intParam[0]), (159,159,159), (191,191,191), (223,223,223), 20, (0,0,0), False)
intButton2 = eButton((120,400,80,30), str(intParam[1]), (159,159,159), (191,191,191), (223,223,223), 20, (0,0,0), False)
editedCurve = []
linkPoints =[[],[],[],[]]
ddCurves = [[],[],[],[]]
def curveBox(c):
    final = [c.f(0),c.f(0)]
    for i in range(100):
        sp = c.f(i/100)
        if sp[0] < final[0][0]:
            final[0][0] = sp[0]
        if sp[1] < final[0][1]:
            final[0][1] = sp[1]
        if sp[0] > final[1][0]:
            final[1][0] = sp[0]
        if sp[1] > final[1][1]:
            final[1][1] = sp[1]
    return final
def directRender(cupa):
    cot = [[],[],[],[]]
    curvesFinal = [[],[],[],[]]
    dCurvesFinal = [[],[],[],[]]
    ddCurvesFinal = [[],[],[],[]]
    curveSigFinal = [[],[],[],[]]
    curveBoxes = [[],[],[],[]]
    utilSizes = [4,4,1,0]
    endPoints = [[],[],[],[]]
    for i in range(4):
        for j in range(len(cupa[i])):
            curveSigFinal[i].append(False)
            if cupa[i][j][0] == 1:
                cot[i].append(True)
                curvesFinal[i].append([bez(cupa[i][j][1],cupa[i][j][2],cupa[i][j][3])])
            elif cupa[i][j][0] == 2:
                cot[i].append(True)
                curvesFinal[i].append([spiral(cupa[i][j][1],cupa[i][j][2],cupa[i][j][3],cupa[i][j][4],cupa[i][j][5],cupa[i][j][6])])
            elif cupa[i][j][0] == 10:
                cot[i].append(True)
                px = [cupa[i][j][1][0]]
                py = [cupa[i][j][1][1]]
                for k in range(len(cupa[i][j][2])):
                    px.append(cupa[i][j][2][k][0])
                    py.append(cupa[i][j][2][k][1])
                px.append(cupa[i][j][3][0])
                py.append(cupa[i][j][3][1])
                sub = []
                sub2 = []
                for k in range(len(px)+(cupa[i][j][4][0]-2)*(not cupa[i][j][4][1])):
                    g = para(full([[0,customLeg(px,cupa[i][j][4][0],k,cupa[i][j][4][1]),0,False]],[[0]]),full([[0,customLeg(py,cupa[i][j][4][0],k,cupa[i][j][4][1]),0,False]],[[0]]))
                    sub.append(g)
                    sub2.append(curveBox(g))
                curvesFinal[i].append(sub)
            else:
                cot[i].append(False)
                curvesFinal[i].append([])
    run = False
    for i in range(4):
        if False in cot[i]:
            run = True
    while run:
        for i in range(4):
            for j in range(len(cupa[i])):
                if not cot[i][j]:
                    if cupa[i][j][0] == 3:
                        cot[i][j] = True
                        for k in range(len(cupa[i][j][1])):
                            if not cot[cupa[i][j][1][k][0]][cupa[i][j][1][k][1]]:
                                cot[i][j] = False
                        if cot[i][j]:
                            curvesFinal[i][j] = []
                            for k in range(len(cupa[i][j][1])):
                                curvesFinal[i][j].append(translateCurve(curvesFinal[cupa[i][j][1][k][0]][cupa[i][j][1][k][1]][cupa[i][j][1][k][2]],cupa[i][j][2],cupa[i][j][3]))
                    elif cupa[i][j][0] == 4:
                        if cot[cupa[i][j][1][0]][cupa[i][j][1][1]] and cot[cupa[i][j][2][0]][cupa[i][j][2][1]]:
                            cot[i][j] = True
                            curvesFinal[i][j] = [compCurve(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][0]][cupa[i][j][2][1]][cupa[i][j][2][2]])]
                    elif cupa[i][j][0] == 5:
                        if cot[cupa[i][j][1][0]][cupa[i][j][1][1]] and cot[cupa[i][j][2][0]][cupa[i][j][2][1]]:
                            cot[i][j] = True
                            if cupa[i][j][2][3]:
                                curvesFinal[i][j] = [wrap(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][0]][cupa[i][j][2][1]][cupa[i][j][2][2]].y,cupa[i][j][3])]
                            else:
                                curvesFinal[i][j] = [wrap(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][0]][cupa[i][j][2][1]][cupa[i][j][2][2]].x,cupa[i][j][3])]
                    elif cupa[i][j][0] == 6:
                        if cot[cupa[i][j][1][0]][cupa[i][j][1][1]] and cot[cupa[i][j][3][0]][cupa[i][j][3][1]]:
                            cot[i][j] = True
                            curvesFinal[i][j] = [tangent(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],cupa[i][j][2],curvesFinal[cupa[i][j][3][0]][cupa[i][j][3][1]][cupa[i][j][3][2]],cupa[i][j][4])]
                    elif cupa[i][j][0] == 7:
                        cot[i][j] = cot[cupa[i][j][1][0]][cupa[i][j][1][1]]
                        for k in range(len(cupa[i][j][2])):
                            if not cot[cupa[i][j][2][k][0]][cupa[i][j][2][k][1]]:
                                cot[i][j] = False
                        if cot[i][j]:
                            curvesFinal[i][j] = []
                            for k in range(len(cupa[i][j][2])):
                                curvesFinal[i][j].append(singleWarp(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][k][0]][cupa[i][j][2][k][1]][cupa[i][j][2][k][2]],cupa[i][j][3],cupa[i][j][4],[cupa[i][j][5],cupa[i][j][6]]))
                    elif cupa[i][j][0] == 8:
                        cot[i][j] = (cot[cupa[i][j][1][0]][cupa[i][j][1][1]] and cot[cupa[i][j][2][0]][cupa[i][j][2][1]])
                        for k in range(len(cupa[i][j][3])):
                            if not cot[cupa[i][j][3][k][0]][cupa[i][j][3][k][1]]:
                                cot[i][j] = False
                        if cot[i][j]:
                            curvesFinal[i][j] = []
                            for k in range(len(cupa[i][j][3])):
                                curvesFinal[i][j].append(doubleWarp(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][0]][cupa[i][j][2][1]][cupa[i][j][2][2]],curvesFinal[cupa[i][j][3][k][0]][cupa[i][j][3][k][1]][cupa[i][j][3][k][2]],cupa[i][j][4],cupa[i][j][5],[cupa[i][j][6],cupa[i][j][7]]))
                    elif cupa[i][j][0] == 9:
                        cot[i][j] = (cot[cupa[i][j][1][0]][cupa[i][j][1][1]] and cot[cupa[i][j][2][0]][cupa[i][j][2][1]] and cot[cupa[i][j][3][0]][cupa[i][j][3][1]] and cot[cupa[i][j][4][0]][cupa[i][j][4][1]])
                        for k in range(len(cupa[i][j][5])):
                            if not cot[cupa[i][j][5][k][0]][cupa[i][j][5][k][1]]:
                                cot[i][j] = False
                        if cot[i][j]:
                            curvesFinal[i][j] = []
                            for k in range(len(cupa[i][j][5])):
                                curvesFinal[i][j].append(quadWarp(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][0]][cupa[i][j][2][1]][cupa[i][j][2][2]],curvesFinal[cupa[i][j][3][0]][cupa[i][j][3][1]][cupa[i][j][3][2]],curvesFinal[cupa[i][j][4][0]][cupa[i][j][4][1]][cupa[i][j][4][2]],curvesFinal[cupa[i][j][5][k][0]][cupa[i][j][5][k][1]][cupa[i][j][5][k][2]],cupa[i][j][6],cupa[i][j][7],[cupa[i][j][8],cupa[i][j][9]]))
                    elif cupa[i][j][0] == 11:
                        sub = False
                        if cot[cupa[i][j][1][0]][cupa[i][j][1][1]]:
                            sub = True
                            for k in range(len(cupa[i][j][2])):
                                if not cot[cupa[i][j][2][k][0]][cupa[i][j][2][k][1]]:
                                    sub = False
                            if sub:
                                cot[i][j] = True
                                if len(cupa[i][j][2]) == 1:
                                    dc1 = dPara(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]])
                                    dc2 = dPara(curvesFinal[cupa[i][j][2][0][0]][cupa[i][j][2][0][1]][cupa[i][j][2][0][2]])
                                    intP = findInter(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][0][0]][cupa[i][j][2][0][1]][cupa[i][j][2][0][2]],dc1,dc2)
                                    if cupa[i][j][3][0]:
                                        curvesFinal[i][j] = [slicePara(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],[intP[cupa[i][j][3][0]][0],1])]
                                    else:
                                        curvesFinal[i][j] = [slicePara(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],[0,intP[cupa[i][j][3][0]][0]])]
                                else:
                                    dc1 = dPara(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]])
                                    dc2 = dPara(curvesFinal[cupa[i][j][2][0][0]][cupa[i][j][2][0][1]][cupa[i][j][2][0][2]])
                                    dc3 = dPara(curvesFinal[cupa[i][j][2][1][0]][cupa[i][j][2][1][1]][cupa[i][j][2][1][2]])
                                    intP1 = findInter(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][0][0]][cupa[i][j][2][0][1]][cupa[i][j][2][0][2]],dc1,dc2)
                                    intP2 = findInter(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],curvesFinal[cupa[i][j][2][1][0]][cupa[i][j][2][1][1]][cupa[i][j][2][1][2]],dc1,dc3)
                                    curvesFinal[i][j] = [slicePara(curvesFinal[cupa[i][j][1][0]][cupa[i][j][1][1]][cupa[i][j][1][2]],[intP1[cupa[i][j][3][0]][0],intP2[cupa[i][j][3][1]][0]])]
        run = False
        for i in range(4):
            if False in cot[i]:
                run = True
    for i in range(4):
        for j in range(len(cupa[i])):
            dCurvesFinal[i].append([])
            curveBoxes[i].append([])
            sub = []
            for k in range(len(curvesFinal[i][j])):
                dCurvesFinal[i][j].append(dPara(curvesFinal[i][j][k]))
                curveBoxes[i][j].append(curveBox(curvesFinal[i][j][k]))
                sub.append(curvesFinal[i][j][k].f(0))
                if k == len(curvesFinal[i][j])-1:
                    sub.append(curvesFinal[i][j][k].f(1))
            endPoints[i].append(sub)
    ddCurvesFinal = [[],[],[],[]]
    rounds = [[],[]]
    for i in range(4):
        for j in range(len(cupa[i])):
            ddCurvesFinal[i].append([])
            for k in range(len(curvesFinal[i][j])):
                ddCurvesFinal[i][j].append(dPara(dCurvesFinal[i][j][k]))
            if i < 2:
                rounds[i].append(isRounded(curvesFinal[i][j]))
    return [curvesFinal,dCurvesFinal,curveSigFinal,endPoints,ddCurvesFinal,curveBoxes,rounds]

def protoRender():
    dCurvesFinal = [[],[],[],[]]
    ddCurvesFinal = [[],[],[],[]]
    curveSigFinal = [[],[],[],[]]
    curveBoxes = [[],[],[],[]]
    utilSizes = [4,4,1,0]
    endPoints = [[],[],[],[]]
    for i in range(4):
        for j in range(len(curves[i])):
            curveSigFinal[i].append(False)
            dCurvesFinal[i].append([])
            curveBoxes[i].append([])
            sub = []
            for k in range(len(curves[i][j])):
                dCurvesFinal[i][j].append(dPara(curves[i][j][k]))
                curveBoxes[i][j].append(curveBox(curves[i][j][k]))
                sub.append(curves[i][j][k].f(0))
                if k == len(curves[i][j])-1:
                    sub.append(curves[i][j][k].f(1))
            endPoints[i].append(sub)
    ddCurvesFinal = [[],[],[],[]]
    rounds = [[],[]]
    for i in range(4):
        for j in range(len(curves[i])):
            ddCurvesFinal[i].append([])
            for k in range(len(curves[i][j])):
                ddCurvesFinal[i][j].append(dPara(dCurvesFinal[i][j][k]))
            if i < 2:
                rounds[i].append(isRounded(curves[i][j]))
    return [dCurvesFinal,curveSigFinal,endPoints,ddCurvesFinal,curveBoxes,rounds]
curveParamNum = 0
delete = False
def dependWeb(c,rt):
    final = [[c]]
    checked = [[],[],[],[]]
    for i in range(4):
        for j in range(len(curveParam[i])):
            if i == c[0] and j == c[1]:
                checked[i].append(True)
            else:
                checked[i].append(False)
    run = True
    while run:
        sub5 = []
        run = False
        for i in range(4):
            for j in range(len(curveParam[i])):
                if not checked[i][j]:
                    if curveParam[i][j][0] == 3:
                        sub = False
                        for k in range(len(curveParam[i][j][1])):
                            for m in range(len(final)):
                                for n in range(len(final[m])):
                                    if (curveParam[i][j][1][k][0] == final[m][n][0] and curveParam[i][j][1][k][1] == final[m][n][1]):
                                        sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    elif curveParam[i][j][0] == 4:
                        sub = False
                        for k in range(len(final)):
                            for m in range(len(final[k])):
                                if (curveParam[i][j][1][0] == final[k][m][0] and curveParam[i][j][1][1] == final[k][m][1]) or (curveParam[i][j][2][0] == final[k][m][0] and curveParam[i][j][2][1] == final[k][m][1]):
                                    sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    elif curveParam[i][j][0] == 5:
                        sub = False
                        for k in range(len(final)):
                            for m in range(len(final[k])):
                                if (curveParam[i][j][1][0] == final[k][m][0] and curveParam[i][j][1][1] == final[k][m][1]) or (curveParam[i][j][2][0] == final[k][m][0] and curveParam[i][j][2][1] == final[k][m][1]):
                                    sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    elif curveParam[i][j][0] == 6:
                        sub = False
                        for k in range(len(final)):
                            for m in range(len(final[k])):
                                if (curveParam[i][j][1][0] == final[k][m][0] and curveParam[i][j][1][1] == final[k][m][1]) or (curveParam[i][j][3][0] == final[k][m][0] and curveParam[i][j][3][1] == final[k][m][1]):
                                    sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    elif curveParam[i][j][0] == 7:
                        sub = False
                        for k in range(len(final)):
                            for m in range(len(final[k])):
                                if curveParam[i][j][1][0] == final[k][m][0] and curveParam[i][j][1][1] == final[k][m][1]:
                                    sub = True
                        if not sub:
                            for k in range(len(curveParam[i][j][2])):
                                for m in range(len(final)):
                                    for n in range(len(final[m])):
                                        if (curveParam[i][j][2][k][0] == final[m][n][0] and curveParam[i][j][2][k][1] == final[m][n][1]):
                                            sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    elif curveParam[i][j][0] == 8:
                        sub = False
                        for k in range(len(final)):
                            for m in range(len(final[k])):
                                if (curveParam[i][j][1][0] == final[k][m][0] and curveParam[i][j][1][1] == final[k][m][1]) or (curveParam[i][j][2][0] == final[k][m][0] and curveParam[i][j][2][1] == final[k][m][1]):
                                    sub = True
                        if not sub:
                            for k in range(len(curveParam[i][j][3])):
                                for m in range(len(final)):
                                    for n in range(len(final[m])):
                                        if (curveParam[i][j][3][k][0] == final[m][n][0] and curveParam[i][j][3][k][1] == final[m][n][1]):
                                            sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    elif curveParam[i][j][0] == 9:
                        sub = False
                        for k in range(len(final)):
                            for m in range(len(final[k])):
                                if (curveParam[i][j][1][0] == final[k][m][0] and curveParam[i][j][1][1] == final[k][m][1]) or (curveParam[i][j][2][0] == final[k][m][0] and curveParam[i][j][2][1] == final[k][m][1]) or (curveParam[i][j][3][0] == final[k][m][0] and curveParam[i][j][3][1] == final[k][m][1]) or  (curveParam[i][j][3][0] == final[k][m][0] and curveParam[i][j][3][1] == final[k][m][1]) or (curveParam[i][j][4][0] == final[k][m][0] and curveParam[i][j][4][1] == final[k][m][1]):
                                    sub = True
                        if not sub:
                            for k in range(len(curveParam[i][j][5])):
                                for m in range(len(final)):
                                    for n in range(len(final)):
                                        if (curveParam[i][j][5][k][0] == final[m][n][0] and curveParam[i][j][5][k][1] == final[m][n][1]):
                                            sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    elif curveParam[i][j][0] == 11:
                        sub = False
                        for k in range(len(final)):
                            for m in range(len(final[k])):
                                if (curveParam[i][j][1][0] == final[k][m][0] and curveParam[i][j][1][1] == final[k][m][1]):
                                    sub = True
                        for k in range(len(curveParam[i][j][2])):
                            for m in range(len(final)):
                                for n in range(len(final[m])):
                                    if (curveParam[i][j][2][k][0] == final[m][n][0] and curveParam[i][j][2][k][1] == final[m][n][1]):
                                        sub = True
                        checked[i][j] = sub
                        if sub:
                            sub5.append([i,j])
                    else:
                        checked[i][j] = True
        if len(sub5) == 0:
            run = False
        else:
            final.append(sub5)
    if rt == 0:
        return final
    else:
        finalP = []
        for i in range(4):
            finalP.append([])
            for j in range(len(curveParam[i])):
                finalP[i].append(False)
        for i in range(len(final)):
            for j in range(len(final[i])):
                finalP[final[i][j][0]][final[i][j][1]] = True
        return finalP
def partialRender(c):
    allEdits = dependWeb(c, 0)
    for i in range(len(allEdits)):
        for j in range(len(allEdits[i])):
            if curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 1:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = [bez(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3])]
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 2:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = [spiral(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][5],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][6])]
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 10:
                px = [curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]]
                py = [curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]]
                for k in range(len(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2])):
                    px.append(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][k][0])
                    py.append(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][k][1])
                px.append(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][0])
                py.append(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][1])
                sub = []
                sub2 = []
                for k in range(len(px)+(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][0]-2)*(not curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][1])):
                    g = para(full([[0,customLeg(px,curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][0],k,curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][1]),0,False]],[[0]]),full([[0,customLeg(py,curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][0],k,curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][1]),0,False]],[[0]]))
                    sub.append(g)
                    sub2.append(curveBox(g))
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = sub
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 3:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = []
                for k in range(len(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1])):
                    curves[allEdits[i][j][0]][allEdits[i][j][1]].append(translateCurve(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][k][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][k][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][k][2]],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3]))
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 4:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = [compCurve(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][2]])]
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 5:
                if curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][3]:
                    curves[allEdits[i][j][0]][allEdits[i][j][1]] = [wrap(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][2]].y,curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3])]
                else:
                    curves[allEdits[i][j][0]][allEdits[i][j][1]] = [wrap(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][2]].x,curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3])]
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 6:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = [tangent(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][2]],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4])]
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 7:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = []
                for k in range(len(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2])):
                    curves[allEdits[i][j][0]][allEdits[i][j][1]].append(singleWarp(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][k][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][k][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][k][2]],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4],[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][5],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][6]]))
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 8:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = []
                for k in range(len(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3])):
                    curves[allEdits[i][j][0]][allEdits[i][j][1]].append(doubleWarp(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][k][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][k][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][k][2]],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][5],[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][6],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][7]]))
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 9:
                curves[allEdits[i][j][0]][allEdits[i][j][1]] = []
                for k in range(len(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][5])):
                    curves[allEdits[i][j][0]][allEdits[i][j][1]].append(quadWarp(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][4][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][5][k][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][5][k][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][5][k][2]],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][6],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][7],[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][8],curveParam[allEdits[i][j][0]][allEdits[i][j][1]][9]]))
            elif curveParam[allEdits[i][j][0]][allEdits[i][j][1]][0] == 11:
                if len(curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2]) == 1:
                    dc1 = dPara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]])
                    dc2 = dPara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][2]])
                    intP = findInter(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][2]],dc1,dc2)
                    if curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][0]:
                        curves[allEdits[i][j][0]][allEdits[i][j][1]] = [slicePara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],[intP[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][0]][0],1])]
                    else:
                        curves[allEdits[i][j][0]][allEdits[i][j][1]] = [slicePara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],[0,intP[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][0]][0]])]
                else:
                    dc1 = dPara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]])
                    dc2 = dPara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][2]])
                    dc3 = dPara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1][2]])
                    intP1 = findInter(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][0][2]],dc1,dc2)
                    intP2 = findInter(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][2][1][2]],dc1,dc3)
                    curves[allEdits[i][j][0]][allEdits[i][j][1]] = [slicePara(curves[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][0]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][1]][curveParam[allEdits[i][j][0]][allEdits[i][j][1]][1][2]],[intP1[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][0]][0],intP2[curveParam[allEdits[i][j][0]][allEdits[i][j][1]][3][1]][0]])]
            sub = []
            cBoxes[allEdits[i][j][0]][allEdits[i][j][1]] = []
            dCurves[allEdits[i][j][0]][allEdits[i][j][1]] = []
            ddCurves[allEdits[i][j][0]][allEdits[i][j][1]] = []
            for k in range(len(curves[allEdits[i][j][0]][allEdits[i][j][1]])):
                dCurves[allEdits[i][j][0]][allEdits[i][j][1]].append(dPara(curves[allEdits[i][j][0]][allEdits[i][j][1]][k]))
                ddCurves[allEdits[i][j][0]][allEdits[i][j][1]].append(dPara(dCurves[allEdits[i][j][0]][allEdits[i][j][1]][k]))
                cBoxes[allEdits[i][j][0]][allEdits[i][j][1]].append(curveBox(curves[allEdits[i][j][0]][allEdits[i][j][1]][k]))
                sub.append(curves[allEdits[i][j][0]][allEdits[i][j][1]][k].f(0))
                if k == len(curves[allEdits[i][j][0]][allEdits[i][j][1]])-1:
                    sub.append(curves[allEdits[i][j][0]][allEdits[i][j][1]][k].f(1))
            linkPoints[allEdits[i][j][0]][allEdits[i][j][1]] = sub
            if allEdits[i][j][0] < 2:
                rounded[allEdits[i][j][0]][allEdits[i][j][1]] = isRounded(curves[allEdits[i][j][0]][allEdits[i][j][1]])
                exportObjCache[allEdits[i][j][0]][allEdits[i][j][1]] = createElementObjects(allEdits[i][j][0],curves[allEdits[i][j][0]][allEdits[i][j][1]],curvesUtil[allEdits[i][j][0]][allEdits[i][j][1]],curveNodes[allEdits[i][j][0]][allEdits[i][j][1]],dCurves[allEdits[i][j][0]][allEdits[i][j][1]])
            elif viewMode == 2:
                exportObjCache[allEdits[i][j][0]][allEdits[i][j][1]] = createElementObjects(2,curves[allEdits[i][j][0]][allEdits[i][j][1]],curvesUtil[allEdits[i][j][0]][allEdits[i][j][1]],patchSides[allEdits[i][j][1]],dCurves[allEdits[i][j][0]][allEdits[i][j][1]])
def addCurve(nc,vm):
    final = []
    if nc[0] == 1:
        final = [bez(nc[1],nc[2],nc[3])]
    elif nc[0] == 2:
        final = [spiral(nc[1],nc[2],nc[3],nc[4],nc[5],nc[6])]
    elif nc[0] == 10:
        px = [nc[1][0]]
        py = [nc[1][1]]
        for k in range(len(nc[2])):
            px.append(nc[2][k][0])
            py.append(nc[2][k][1])
        px.append(nc[3][0])
        py.append(nc[3][1])
        sub = []
        sub2 = []
        for k in range(len(px)+(nc[4][0]-2)*(not nc[4][1])):
            g = para(full([[0,customLeg(px,nc[4][0],k,nc[4][1]),0,False]],[[0]]),full([[0,customLeg(py,nc[4][0],k,nc[4][1]),0,False]],[[0]]))
            sub.append(g)
            sub2.append(curveBox(g))
        final = sub
    elif nc[0] == 3:
        final = []
        for k in range(len(nc[1])):
            final.append(translateCurve(curves[nc[1][k][0]][nc[1][k][1]][nc[1][k][2]],nc[2],nc[3]))
    elif nc[0] == 4:
        final = [compCurve(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][0]][nc[2][1]][nc[2][2]])]
    elif nc[0] == 5:
        if nc[2][3]:
            final = [wrap(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][0]][nc[2][1]][nc[2][2]].y,nc[3])]
        else:
            final = [wrap(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][0]][nc[2][1]][nc[2][2]].x,nc[3])]
    elif nc[0] == 6:
        final = [tangent(curves[nc[1][0]][nc[1][1]][nc[1][2]],nc[2],curves[nc[3][0]][nc[3][1]][nc[3][2]],nc[4])]
    elif nc[0] == 7:
        final = []
        for k in range(len(nc[2])):
            final.append(singleWarp(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][k][0]][nc[2][k][1]][nc[2][k][2]],nc[3],nc[4],[nc[5],nc[6]]))
    elif nc[0] == 8:
        final = []
        for k in range(len(nc[3])):
            final.append(doubleWarp(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][0]][nc[2][1]][nc[2][2]],curves[nc[3][k][0]][nc[3][k][1]][nc[3][k][2]],nc[4],nc[5],[nc[6],nc[7]]))
    elif nc[0] == 9:
        final = []
        for k in range(len(nc[5])):
            final.append(quadWarp(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][0]][nc[2][1]][nc[2][2]],curves[nc[3][0]][nc[3][1]][nc[3][2]],curves[nc[4][0]][nc[4][1]][nc[4][2]],curves[nc[5][k][0]][nc[5][k][1]][nc[5][k][2]],nc[6],nc[7],[nc[8],nc[9]]))
    elif nc[0] == 11:
        if len(nc[2]) == 1:
            dc1 = dPara(curves[nc[1][0]][nc[1][1]][nc[1][2]])
            dc2 = dPara(curves[nc[2][0][0]][nc[2][0][1]][nc[2][0][2]])
            intP = findInter(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][0][0]][nc[2][0][1]][nc[2][0][2]],dc1,dc2)
            if nc[3][1]:
                final = [slicePara(curves[nc[1][0]][nc[1][1]][nc[1][2]],[intP[nc[3][0]][0],1])]
            else:
                final = [slicePara(curves[nc[1][0]][nc[1][1]][nc[1][2]],[0,intP[nc[3][0]][0]])]
        else:
            dc1 = dPara(curves[nc[1][0]][nc[1][1]][nc[1][2]])
            dc2 = dPara(curves[nc[2][0][0]][nc[2][0][1]][nc[2][0][2]])
            dc3 = dPara(curves[nc[2][1][0]][nc[2][1][1]][nc[2][1][2]])
            intP1 = findInter(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][0][0]][nc[2][0][1]][nc[2][0][2]],dc1,dc2)
            intP2 = findInter(curves[nc[1][0]][nc[1][1]][nc[1][2]],curves[nc[2][1][0]][nc[2][1][1]][nc[2][1][2]],dc1,dc3)
            final = [slicePara(curves[nc[1][0]][nc[1][1]][nc[1][2]],[intP1[nc[3][0]][0],intP2[nc[3][1]][0]])]
    curves[vm].append(final)
    if vm < 3:
        isGearElement[vm].append([])
    dispPoints[vm].append([])
    dCurves[vm].append([])
    ddCurves[vm].append([])
    cBoxes[vm].append([])
    sub = []
    for k in range(len(final)):
        dCurves[vm][-1].append(dPara(curves[vm][-1][k]))
        ddCurves[vm][-1].append(dPara(dCurves[vm][-1][k]))
        cBoxes[vm][-1].append(curveBox(curves[vm][-1][k]))
        sub.append(curves[vm][-1][k].f(0))
        if k == len(curves[vm][-1])-1:
            sub.append(curves[vm][-1][k].f(1))
        if vm < 2:
            dispPoints[vm][-1].append(rendCurve(curves[vm][-1][k],curvesUtil[vm][-1][1]))
        else:
            dispPoints[vm][-1].append(rendCurve(curves[vm][-1][k],5))
        if vm < 3:
            isGearElement[vm][-1].append(False)
    curveSig[vm].append(False)
    linkPoints[vm].append(sub)
    if vm < 2:
        rounded[vm].append(isRounded(final))
        exportObjCache[vm].append(createElementObjects(vm,curves[vm][-1],curvesUtil[vm][-1],curveNodes[vm][-1],dCurves[vm][-1]))
    elif vm == 2:
        exportObjCache[vm].append(createElementObjects(2,curves[2][-1],curvesUtil[2][-1],patchSides[-1],dCurves[2][-1]))
colors = []
cB = []
cO = []
finalRef = [1,2,3,6,32,21,25,20]
def export():
    sampLev = level("result delta","",2)
    with open(mFilePath, 'rb') as f:
        eDat = f.read()
    dDat = xor_bytes(eDat, 11)
    cDat = base64.b64decode(dDat, altchars=b'-_')
    fDat = zlib.decompress(cDat[10:], -zlib.MAX_WBITS)
    with open("result_gamma.txt",'wb') as f:
        f.write(fDat)
    with open("result_gamma.txt",'r') as f:
        dStr = f.read()
    count = -12
    run = True
    while run:
        if dStr[count] == dStr[count-4] == dStr[count-8] == ">":
            run = False
        else:
            count -= 1
    bp = count+len(dStr)-3
    levIn = -1
    for i in range(len(allLevels)):
        if allLevels[i].n == "result delta":
            levIn = i
    if levIn > -1:
        sDat = gzip.decompress(base64.urlsafe_b64decode(allLevels[levIn].s.encode('utf-8'))).decode()
        finalString = ""
        sub = search(sDat,"|")
        for i in range(sub[5]):
            finalString += sDat[i]
    else:
        finalString = "kS38,1_40_2_125_3_255_11_255_12_255_13_255_4_-1_6_1000_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1001_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1009_7_1_15_1_18_0_8_1|1_255_2_255_3_255_11_255_12_255_13_255_4_-1_6_1002_5_1_7_1_15_1_18_0_8_1|1_125_2_255_3_0_11_255_12_255_13_255_4_-1_6_1005_5_1_7_1_15_1_18_0_8_1|1_0_2_255_3_255_11_255_12_255_13_255_4_-1_6_1006_5_1_7_1_15_1_18_0_8_1|"
        for i in range(1,len(colors)):
            finalString += "1_"
            finalString += str(colors[i][0])
            finalString += "_2_"
            finalString += str(colors[i][1])
            finalString += "_3_"
            finalString += str(colors[i][2])
            finalString += "_11_255_12_255_13_255_4_-1_5_"
            finalString += str(cB[i])
            finalString += "_6_"
            finalString += str(i)
            finalString += "_7_"
            finalString += str(cO[i])
            finalString += "_15_1_18_0_8_1|"
        finalString += (",kA13,0,kA15,0,kA16,0,kA14,,kA6,0,kA7,0,kA17,0,kA18,0,kS39,0,kA2,0,kA3,0,kA8,0,kA4,0,kA9,0,kA10,0,kA11,0;")

    sub = compEnc64(currObjStream)
    sub2 = gzip.decompress(base64.urlsafe_b64decode(sub.encode('utf-8'))).decode()
    count = 0
    if len(sub2) > 0:
        while not sub2[count] == ";":
            count += 1
        count += 1
        for i in range(count,len(sub2)):
            finalString += sub2[i]
    for i in range(3):
        for j in range(len(exportObjCache[i])):
            for k in range(len(exportObjCache[i][j])):
                if not isGearElement[i][j][k]:
                    finalString += gzip.decompress(base64.urlsafe_b64decode(compEnc64(exportObjCache[i][j][k]).encode('utf-8'))).decode()
                    finalString += ";"
    for j in range(len(exportObjCache[3])):
        if not isGearElement[3][j]:
            if len(prismUtilVals[j][3]) == 0:
                finalString += gzip.decompress(base64.urlsafe_b64decode(compEnc64(exportObjCache[3][j]).encode('utf-8'))).decode()
                finalString += ";"
            else:
                gradApp = ",41,1,43,"
                gradVals = [0,1,1]
                for k in range(len(prismUtilVals[j][3])):
                    if gradients[prismUtilVals[j][3][k]][2] == 0:
                        if gradients[prismUtilVals[j][3][k]][3] == 0:
                            gradVals[0] += (prismCenters[j][0]-gradients[prismUtilVals[j][3][k]][0])/(gradients[prismUtilVals[j][3][k]][1]-gradients[prismUtilVals[j][3][k]][0])*(gradients[prismUtilVals[j][3][k]][5]-gradients[prismUtilVals[j][3][k]][4])+gradients[prismUtilVals[j][3][k]][4]
                        else:
                            gradVals[gradients[prismUtilVals[j][3][k]][3]] *= (prismCenters[j][0]-gradients[prismUtilVals[j][3][k]][0])/(gradients[prismUtilVals[j][3][k]][1]-gradients[prismUtilVals[j][3][k]][0])*(gradients[prismUtilVals[j][3][k]][5]-gradients[prismUtilVals[j][3][k]][4])+gradients[prismUtilVals[j][3][k]][4]
                    else:
                        if gradients[prismUtilVals[j][3][k]][3] == 0:
                            gradVals[0] += (prismCenters[j][1]-gradients[prismUtilVals[j][3][k]][0])/(gradients[prismUtilVals[j][3][k]][1]-gradients[prismUtilVals[j][3][k]][0])*(gradients[prismUtilVals[j][3][k]][5]-gradients[prismUtilVals[j][3][k]][4])+gradients[prismUtilVals[j][3][k]][4]
                        else:
                            gradVals[gradients[prismUtilVals[j][3][k]][3]] *= (prismCenters[j][1]-gradients[prismUtilVals[j][3][k]][0])/(gradients[prismUtilVals[j][3][k]][1]-gradients[prismUtilVals[j][3][k]][0])*(gradients[prismUtilVals[j][3][k]][5]-gradients[prismUtilVals[j][3][k]][4])+gradients[prismUtilVals[j][3][k]][4]
                for k in range(len(gradVals)):
                    gradApp += str(gradVals[k])
                    gradApp += "a"
                gradApp += "0a0"
                sub = ";"
                sub += gzip.decompress(base64.urlsafe_b64decode(compEnc64(exportObjCache[3][j]).encode('utf-8'))).decode()
                sub += ";"
                sub2 = levelStringParse(sub)
                for k in range(len(sub2)):
                    finalString += sub2[k].expStringApp(gradApp)
    cgObj = []
    for i in range(len(customGears)):
        cgObj.append([])
        for j in range(3):
            for k in range(len(customGears[i][j])):
                sub = ";"
                sub += gzip.decompress(base64.urlsafe_b64decode(compEnc64(exportObjCache[j][customGears[i][j][k][0]][customGears[i][j][k][1]]).encode('utf-8'))).decode()
                sub += ";"
                sub2 = levelStringParse(sub)
                for m in range(len(sub2)):
                    cgObj[i].append(sub2[m])
        for j in range(len(customGears[i][3])):
            sub = ";"
            sub += gzip.decompress(base64.urlsafe_b64decode(compEnc64(exportObjCache[3][customGears[i][3][j]]).encode('utf-8'))).decode()
            sub += ";"
            sub2 = levelStringParse(sub)
            for m in range(len(sub2)):
                cgObj[i].append(sub2[m])
    for i in range(len(cgPos)):
        for j in range(len(cgObj[cgPos[i][2]])):
            sub = cgObj[cgPos[i][2]][j]
            sub.x += cgPos[i][0]-customGears[cgPos[i][2]][4][0]
            sub.y += cgPos[i][1]-customGears[cgPos[i][2]][4][1]
            finalString += sub.expString()
            sub.x -= cgPos[i][0]-customGears[cgPos[i][2]][4][0]
            sub.y -= cgPos[i][1]-customGears[cgPos[i][2]][4][1]
        finalString += "1,1764,2,"
        finalString += str(cgPos[i][0])
        finalString += ",3,"
        finalString += str(cgPos[i][1])
        finalString += ";1,1346,2,"
        if cgPos[i][0]-(600+customGears[cgPos[i][2]][5]) < -29:
            finalString += str(-29)
        else:
            finalString += str(cgPos[i][0]-(600+customGears[cgPos[i][2]][5]))
        finalString += ",3,"
        finalString += str(cgPos[i][1])
        finalString += ";1,1616,2,"
        finalString += str(cgPos[i][0]+450+customGears[cgPos[i][2]][5])
        finalString += ",3,"
        finalString += str(cgPos[i][1])
        finalString += ";"
    sampLev.s = base64.urlsafe_b64encode(gzip.compress(finalString.encode('utf-8'))).decode()
    fullLevStr = "<k>k_"
    fullLevStr += str(levIn)
    fullLevStr += "</k><d>"
    fullLevStr += sampLev.expString()
    fullLevStr += "</d>"
    tString = ""
    if levIn > -1:
        if levIn < len(allLevels)-1:
            for i in range(lsp[levIn]):
                tString += dStr[i]
            for i in range(len(fullLevStr)):
                tString += fullLevStr[i]
            for i in range(lsp[levIn+1],len(dStr)):
                tString += dStr[i]
        else:
            for i in range(lsp[levIn]):
                tString += dStr[i]
            for i in range(len(fullLevStr)):
                tString += fullLevStr[i]
            for i in range(bp,len(dStr)):
                tString += dStr[i]
    else:
        for i in range(bp):
            tString += dStr[i]
        for i in range(len(fullLevStr)):
            tString += fullLevStr[i]
        for i in range(bp,len(dStr)):
            tString += dStr[i]
    with open("result_gamma.txt",'w') as f:
        f.write(tString)
    with open("result_gamma.txt",'rb') as f:
        rDat = f.read()
    cDat = zlib.compress(rDat)
    dCrc = zlib.crc32(rDat)
    ds = len(rDat)
    cDat = (b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x0b' + cDat[2:-4] + struct.pack('I I', dCrc, ds))
    nDat = base64.b64encode(cDat, altchars=b'-_')
    eDat = xor_bytes(nDat, 11)
    with open(mFilePath, 'wb') as f:
        f.write(eDat)
    print("exported")
def showBitsL(num,l):
    finalString = ""
    for i in range(l):
        finalString += str(math.floor(num/pow(2,(l-1)-i)%2))
    return finalString
def bitToDec(s):
    final = 0
    for i in range(8):
        if s[i] == "1":
            final += pow(2,7-i)
    return final
def parse(l):
    final = 0
    for i in range(len(l)):
        final += l[i]*pow(256,len(l)-1-i)
    return final
def nRect(x,y,w,h,r,c):
    m = math.sqrt(pow(w/2,2)+pow(h/2,2))
    an = math.pi/2
    if abs(w) > 0:
        an = math.atan(h/w)
    final = []
    for i in range(4):
        final.append([(x+m*math.cos(math.pi*(i%2)+an*pow(-1,i)+math.pi*int(i/2)+r/180*math.pi)+cam[0])*zoom,300-(y+m*math.sin(math.pi*(i%2)+an*pow(-1,i)+math.pi*int(i/2)+r/180*math.pi)-cam[1])*zoom])
    pygame.draw.polygon(screen, c, final)
objImg = []
for i in range(1916):
    objImg.append(0)
refSheets = [pygame.image.load("C:\\Program Files (x86)\\Steam\\steamapps\\common\Geometry Dash\\Resources\\GJ_GameSheet-uhd.png"),pygame.image.load("C:\\Program Files (x86)\\Steam\\steamapps\\common\Geometry Dash\\Resources\\GJ_GameSheet02-uhd.png")]
objSubs = [
    [0,[1879,2567,120,120],1],
    ]
for i in range(len(objSubs)):
    objImg[objSubs[i][2]] = refSheets[objSubs[i][0]].subsurface(objSubs[i][1])
class block:
    def __init__(self, t, x, y, r, s, h, v, tpOff, gr, c, el, z, hsv):
        self.t = t
        self.x = x
        self.y = y
        self.r = r
        self.s = s
        self.h = h
        self.v = v
        self.tpOff = tpOff
        self.gr = gr
        self.c = c
        self.el = el
        self.z = z
        self.hsv = hsv
    def disp2(self):
        if not objImg[self.t] == 0:
            sub = pygame.transform.scale(objImg[objSubs[i][2]], (30*zoom,30*zoom))
            screen.blit(sub, (self.x-15)*zoom+cam[0], 300-((self.y+15)*zoom+cam[1]))
    def disp(self):
        if self.t == 1:
            nRect(self.x,self.y,30*self.s,30*self.s,-self.r*pow(-1,self.h^self.v),(128,128,128))
        elif self.t == 10:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(0,128,255))
        elif self.t == 11:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(255,255,0))
        elif self.t == 12:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(0,255,0))
        elif self.t == 47:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(255,0,0))
        elif self.t == 111:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(255,102,0))
        elif self.t == 660:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(0,128,255))
        elif self.t == 745:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(191,191,191))
        elif self.t == 1331:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(64,0,255))
        elif self.t == 45:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(255,153,0))
        elif self.t == 46:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(0,191,255))
        elif self.t == 99:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(0,255,128))
        elif self.t == 101:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(255,0,128))
        elif self.t == 286:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(255,204,0))
        elif self.t == 287:
            nRect(self.x,self.y,30*self.s,90*self.s,-self.r*pow(-1,self.h^self.v),(0,0,255))
        elif self.t == 747:
            nRect(self.x,self.y,30*self.s,90*self.s,self.r*pow(-1,self.h^self.v),(0,64,255))
            nRect(self.x,self.y+self.tpOff,30*self.s,90*self.s,self.r*pow(-1,self.h^self.v),(255,51,0))
        elif self.t == 1704 or self.t == 1751:
            final = []
            sub = [0,135,225]
            for i in range(3):
                ra = 15
                if i > 0:
                    ra = 15*math.sqrt(2)
                final.append([((self.x+ra*math.cos(sub[i]-self.r))+cam[0])*zoom,300-(self.y+ra*math.sin(sub[i]-self.r)-cam[1])*zoom])
            if self.t == 1704:
                pygame.draw.polygon(screen, (0,255,0), final)
            else:
                pygame.draw.polygon(screen, (255,0,255), final)
        if (self.x+cam[0])*zoom > 0:
            if self.t == 36:
                pygame.draw.circle(screen, (255,255,0), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*15*zoom)
            elif self.t == 141:
                pygame.draw.circle(screen, (255,0,255), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*15*zoom)
            elif self.t == 1333:
                pygame.draw.circle(screen, (255,128,0), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*15*zoom)
            elif self.t == 84:
                pygame.draw.circle(screen, (0,255,255), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*15*zoom)
            elif self.t == 1022:
                pygame.draw.circle(screen, (0,255,0), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*15*zoom)
            elif self.t == 1330:
                pygame.draw.circle(screen, (0,0,0), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*15*zoom)
            elif self.t == 186:
                pygame.draw.circle(screen, (0,0,0), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*41*zoom)
            elif self.t == 187:
                pygame.draw.circle(screen, (0,0,0), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*30*zoom)
            elif self.t == 188:
                pygame.draw.circle(screen, (0,0,0), ((self.x+cam[0])*zoom,300-(self.y-cam[1])*zoom), self.s*21*zoom)
    def dp(self):
        print(self.t,self.x,self.y,self.r,self.s,self.h,self.hsv)
    def expString(self):
        final = "1,"
        final += str(self.t)
        final += ",2,"
        final += str(self.x)
        final += ",3,"
        final += str(self.y)
        final += ",6,"
        final += str(self.r)
        final += ",32,"
        final += str(self.s)
        final += ",4,"
        if self.h:
            final += "1"
        else:
            final += "0"
        final += ",5,"
        if self.v:
            final += "1"
        else:
            final += "0"
        final += ",54,"
        final += str(self.tpOff)
        final += ",21,"
        final += str(self.c)
        final += ",20,"
        final += str(self.el)
        final += ",25,"
        final += str(self.z)
        if len(self.gr) > 0:
            final += ",57,"
            for i in range(len(self.gr)):
                final += str(self.gr[i])
                if i < len(self.gr)-1:
                    final += "."
        final += ";"
        return final
    def expStringApp(self,app):
        final = "1,"
        final += str(self.t)
        final += ",2,"
        final += str(self.x)
        final += ",3,"
        final += str(self.y)
        final += ",6,"
        final += str(self.r)
        final += ",32,"
        final += str(self.s)
        final += ",4,"
        if self.h:
            final += "1"
        else:
            final += "0"
        final += ",5,"
        if self.v:
            final += "1"
        else:
            final += "0"
        final += ",54,"
        final += str(self.tpOff)
        final += ",21,"
        final += str(self.c)
        final += ",20,"
        final += str(self.el)
        final += ",25,"
        final += str(self.z)
        if len(self.gr) > 0:
            final += ",57,"
            for i in range(len(self.gr)):
                final += str(self.gr[i])
                if i < len(self.gr)-1:
                    final += "."
        final += app
        final += ";"
        return final

class loaded:
    def __init__(self, l):
        self.l = l
        self.count = 0
    def lPar(self,n):
        final = []
        for i in range(n):
            final.append(self.l[self.count])
            self.count += 1
        return parse(final)
    def sPar(self):
        self.count += 1
        return self.l[self.count-1]
    def iPar(self):
        sLen = self.l[self.count]
        sub = []
        self.count += 1
        for k in range(sLen%128):
            sub.append(self.l[self.count+k])
        self.count += sLen%128
        return parse(sub)
    def trPar(self):
        sub = []
        sub2 = parse([self.l[self.count],self.l[self.count+1]])
        sub.append(int(sub2/16384))
        sub.append(sub2%16384)
        sub.append(self.l[self.count+2])
        self.count += 3
        return sub
    def fPar(self):
        sub5 = self.l[self.count]
        self.count += 1
        isNeg = int(sub5/128)
        isFloat = int(sub5/64)%2
        nLen = sub5%64
        sub6 = 0
        for p in range(nLen):
            sub6 += self.l[self.count]*pow(256,nLen-1-p)
            self.count += 1
        if isFloat:
            sub7 = 0
            for p in range(5):
                sub7 += self.l[self.count]*pow(256,4-p)
                self.count += 1
            sub6 += sub7/pow(2,40)
        return sub6*pow(-1,isNeg)
def load():
    fileTest = []
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "deltaSaveData.dat")):
        with open("deltaSaveData.dat", 'rb') as f:
            fileTest = f.read()
    projects = []
    count = 3
    while count < len(fileTest):
        projects.append([count,parse([fileTest[count-3],fileTest[count-2],fileTest[count-1]])])
        count += projects[-1][1]+3
    loadedData = []
    for i in range(len(projects)):
        loadedData.append([])
        for j in range(projects[i][1]):
            loadedData[i].append(fileTest[projects[i][0]+j])
    paramLists = []
    paramUtil = []
    paramNodes = []
    projZooms = []
    projCam = []
    projPris = []
    projObjects = []
    aPatchSides = []
    projPrisUtil = []
    projCurves = []
    projExpCache = []
    projEL = []
    projFillModes = []
    projPresets = []
    projDispPoints = []
    projPrisDispPoints = []
    projCustomGears = []
    projCgPos = []
    projGrad = []
    for i in range(len(projects)):
        dat = loaded(loadedData[i])
        paramLists.append([])
        paramUtil.append([])
        paramNodes.append([])
        projPris.append([])
        projObjects.append([])
        aPatchSides.append([])
        projPrisUtil.append([])
        projCurves.append([])
        projFillModes.append([])
        projPresets.append([])
        projDispPoints.append([])
        projPrisDispPoints.append([])
        projCustomGears.append([])
        projCgPos.append([])
        projGrad.append([])
        projZooms.append(dat.sPar()/10+0.5)
        projCam.append([dat.iPar(),dat.iPar()])
        for j in range(4):
            paramLists[i].append([])
            paramUtil[i].append([])
            paramNodes[i].append([])
            curveAmt = dat.lPar(2)
            while len(paramLists[i][j]) < curveAmt:
                samp = dat.sPar()
                sub = []
                sub.append(int(samp/16)+1)
                sub2 = []
                if j < 2:
                    for k in range(3):
                        sub2.append(int((samp%pow(2,4-k))/pow(2,3-k)))
                elif j == 2:
                    aPatchSides[i].append(int((samp%8)/2))
                paramNodes[i][j].append(sub2)
                if sub[0] == 1:
                    sub.append([dat.iPar()/1000,dat.iPar()/1000])
                    cpAmt = dat.sPar()
                    sub.append([])
                    for m in range(cpAmt):
                        sub[-1].append([dat.iPar()/1000,dat.iPar()/1000])
                    sub.append([dat.iPar()/1000,dat.iPar()/1000])
                elif sub[0] == 2:
                    for m in range(6):
                        sub.append(dat.iPar()/1000)
                elif sub[0] == 3:
                    tcAmt = dat.sPar()
                    sub2 = []
                    for k in range(tcAmt):
                        sub2.append(dat.trPar())
                    sub.append(sub2)
                    tpAmt = dat.sPar()+1
                    sub2 = []
                    for k in range(math.ceil(tpAmt/4)):
                        sub3 = dat.sPar()
                        for m in range(4):
                            sub2.append(int((int(sub3)/pow(4,3-m))%4))
                    sub2[tpAmt:len(sub2)] = []
                    sub.append(sub2)
                    sub2 = []
                    for m in range(tpAmt):
                        sub3 = []
                        for n in range(2-(sub[-1][m] == 1)):
                            sub3.append(dat.iPar()/1000)
                        sub2.append(sub3)
                    sub.append(sub2)
                elif sub[0] == 4:
                    for k in range(2):
                        sub.append(dat.trPar())
                elif sub[0] == 5:
                    xOrY = samp%2 == 1
                    for k in range(2):
                        sub.append(dat.trPar())
                        if k == 1:
                            sub[-1].append(xOrY)
                    sub2 = []
                    for n in range(2):
                        sub2.append(dat.iPar()/1000)
                    sub.append(sub2)
                elif sub[0] == 6:
                    for m in range(2):
                        sub.append(dat.trPar())
                        sub.append(dat.iPar()/1000)
                elif sub[0] == 7:
                    sub.append(dat.trPar())
                    scAmt = dat.sPar()
                    sub2 = []
                    for m in range(scAmt):
                        sub2.append(dat.trPar())
                    sub.append(sub2)
                    for m in range(4):
                        cpxLen = dat.sPar()
                        sub.append(dat.iPar()/1000)
                elif sub[0] == 8:
                    for n in range(2):
                        sub.append(dat.trPar())
                    scAmt = dat.sPar()
                    sub2 = []
                    for m in range(scAmt):
                        sub2.append(dat.trPar())
                    sub.append(sub2)
                    for m in range(4):
                        sub.append(dat.iPar()/1000)
                elif sub[0] == 9:
                    for n in range(4):
                        sub.append(dat.trPar())
                    scAmt = dat.sPar()
                    sub2 = []
                    for m in range(scAmt):
                        sub2.append(dat.trPar())
                    sub.append(sub2)
                    for m in range(4):
                        sub.append(dat.iPar()/1000)
                elif sub[0] == 10:
                    sub.append([dat.iPar()/1000,dat.iPar()/1000])
                    cpAmt = dat.sPar()
                    sub.append([])
                    for m in range(cpAmt):
                        sub[-1].append([dat.iPar()/1000,dat.iPar()/1000])
                    sub.append([dat.iPar()/1000,dat.iPar()/1000])
                    sub2 = dat.sPar()
                    sub.append([sub2%128,int(sub2/128)])
                elif sub[0] == 11:
                    bLen = samp%2+1
                    sub.append(dat.trPar())
                    sub2 = []
                    for m in range(bLen):
                        sub2.append(dat.trPar())
                    sub.append(sub2)
                    sub3 = []
                    sub3.append(dat.sPar())
                    sub3.append(dat.sPar())
                    sub.append(sub3)
                paramLists[i][j].append(sub)
                sub2 = []
                sub2.append(dat.sPar())
                if j < 2:
                    sub2.append(dat.lPar(2)/100)
                    sub2.append(dat.lPar(2))
                    sub2.append((dat.sPar()+128)%256-128)
                paramUtil[i][j].append(sub2)
        prisAmt = dat.lPar(2)
        for j in range(prisAmt):
            sideAmt = dat.sPar()
            sub = []
            for k in range(sideAmt):
                sub2 = []
                sub3 = dat.lPar(2)
                sub2.append(int(sub3/16384))
                sub2.append(sub3%8192)
                sub2.append(dat.sPar())
                if int((int(sub3/256)%64)/32):
                    sub2.append(True)
                else:
                    sub2.append(False)
                sub.append(sub2)
            projPris[i].append(sub)
            sub4 = []
            sub4.append(dat.sPar())
            sub5 = dat.lPar(2)
            sub4.append(sub5%32768)
            projFillModes[i].append(int(sub5/32768))
            sub4.append((parse(dat.sPar())+128)%256-128)
            sub6 = dat.sPar()
            sub7 = []
            for j in range(sub6):
                sub7.append(dat.sPar())
            sub4.append(sub7)
            projPrisUtil[i].append(sub4)
        objAmt = dat.lPar(3)
        for j in range(objAmt):
            projObjects[i].append(dat.sPar())
        for j in range(4):
            cAmt = dat.lPar(2)
            cL = []
            for k in range(cAmt):
                scAmt = dat.lPar(2)
                subCL = []
                for m in range(scAmt):
                    xplAmt = dat.lPar(2)
                    xl = []
                    for n in range(xplAmt):
                        subx = [0,0,0,0]
                        sub2 = dat.sPar()
                        subx[0] = int(sub2/8)%4
                        subx[2] = int(sub2/2)%4
                        subx[3] = (sub2%2 == 1)
                        if subx[0] == 0:
                            sub3 = dat.sPar()
                            sub4 = []
                            for o in range(sub3):
                                sub4.append(dat.fPar())
                            subx[1] = poly(sub4)
                        elif subx[0] == 1:
                            sub9 = loadedData[i][count]
                            count += 1
                            sub10 = []
                            for n in range(sub9):
                                sub8 = dat.lPar(2)
                                count += 2
                                if sub8 >= 32768:
                                    sub10.append([])
                                sub10[-1].append(sub8%32768)
                            subx[1] = sub10
                        elif subx[0] == 2:
                            subx[1] = [dat.lPar(2),dat.lPar(2)]
                        xl.append(subx)
                    xptLen = dat.sPar()
                    xpt = []
                    for n in range(xptLen):
                        sub8 = dat.lPar(2)
                        if sub8 >= 32768:
                            xpt.append([])
                        xpt[-1].append(sub8%32768)
                    yplAmt = dat.lPar(2)
                    yl = []
                    for n in range(yplAmt):
                        suby = [0,0,0,0]
                        sub2 = dat.sPar()
                        suby[0] = int(sub2/8)%4
                        suby[2] = int(sub2/2)%4
                        suby[3] = (sub2%2 == 1)
                        if suby[0] == 0:
                            sub3 = dat.sPar()
                            sub4 = []
                            for o in range(sub3):
                                sub4.append(dat.fPar())
                            suby[1] = poly(sub4)
                        elif suby[0] == 1:
                            sub9 = dat.sPar()
                            sub10 = []
                            for n in range(sub9):
                                sub8 = dat.lPar(2)
                                if sub8 >= 32768:
                                    sub10.append([])
                                sub10[-1].append(sub8%32768)
                            suby[1] = sub10
                        elif suby[0] == 2:
                            suby[1] = [dat.lPar(2),dat.lPar(2)]
                        yl.append(suby)
                    yptLen = dat.sPar()
                    ypt = []
                    for n in range(yptLen):
                        sub8 = dat.lPar(2)
                        if sub8 >= 32768:
                            ypt.append([])
                        ypt[-1].append(sub8%32768)
                    subCL.append(para(full(xl,xpt),full(yl,ypt)))
                cL.append(subCL)
            projCurves[i].append(cL)
        sub7 = []
        for k in range(3):
            sub = dat.lPar(2)
            sub2 = []
            for j in range(sub):
                sub3 = dat.sPar()
                sub4 = []
                for m in range(sub3):
                    sub5 = dat.lPar(3)
                    sub6 = []
                    for n in range(sub5):
                        sub6.append(dat.sPar())
                    sub4.append(sub6)
                sub2.append(sub4)
            sub7.append(sub2)
        sub = dat.lPar(2)
        sub2 = []
        for j in range(sub):
            sub3 = dat.lPar(3)
            sub4 = []
            for m in range(sub3):
                sub4.append(dat.sPar())
            sub2.append(sub4)
        sub7.append(sub2)
        projExpCache.append(sub7)
        projEL.append(dat.sPar())
        sub = dat.sPar()
        for j in range(sub):
            sub2 = dat.sPar()
            sub5 = []
            for k in range(sub2):
                sub5.append([dat.lPar(2),dat.sPar()])
            projPresets[i].append(sub5)
        for j in range(4):
            sub = dat.lPar(2)
            sub6 = []
            for k in range(sub):
                sub2 = dat.sPar()
                sub5 = []
                for k in range(sub2):
                    sub3 = dat.lPar(2)
                    sub4 = []
                    for m in range(sub3):
                        sub4.append([dat.iPar()/1000,dat.iPar()/1000])
                    sub5.append(sub4)
                sub6.append(sub5)
            projDispPoints[i].append(sub6)
        sub = dat.lPar(2)
        for o in range(sub):
            sub2 = dat.lPar(2)
            sub5 = []
            for m in range(sub2):
                sub5.append([dat.iPar()/1000,dat.iPar()/1000])
            projPrisDispPoints[i].append(sub5)
        sub = dat.sPar()
        for j in range(sub):
            sub2 = []
            for k in range(3):
                sub3 = dat.sPar()
                sub4 = []
                for m in range(sub3):
                    sub4.append(dat.lPar(3))
                sub2.append(sub4)
            sub3 = dat.sPar()
            sub4 = []
            for k in range(sub3):
                sub4.append(dat.lPar(2))
            sub2.append(sub4)
            sub2.append([dat.iPar()/1000,dat.iPar()/1000])
            sub2.append(dat.sPar())
            projCustomGears[i].append(sub2)
        sub = dat.lPar(2)
        for j in range(sub):
            sub2 = []
            sub2.append(dat.iPar()/1000)
            sub2.append(dat.iPar()/1000)
            sub2.append(dat.sPar())
            projCgPos[i].append(sub2)
        sub = dat.sPar()
        for j in range(sub):
            sub2 = []
            sub2.append(dat.iPar()/1000)
            sub2.append(dat.iPar()/1000)
            sub3 = dat.sPar()
            sub2.append(int(sub3/128))
            sub2.append(int((sub3%128)/32))
            if sub2[3] == 0:
                sub2.append(dat.iPar())
                sub2.append(dat.iPar())
            else:
                sub2.append(dat.sPar()/255)
                sub2.append(dat.sPar()/255)
            projGrad[i].append(sub2)
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "deltaSaveData.dat")):
        with open("deltaSaveBackup.dat", 'wb') as f:
            for i in range(len(fileTest)):
                f.write(int(fileTest[i]).to_bytes(1, byteorder='big'))
    return [paramLists,paramUtil,paramNodes,projZooms,projCam,projPris,projObjects,aPatchSides,projPrisUtil,projCurves,projExpCache,projEL,projFillModes,projPresets,projDispPoints,projPrisDispPoints,projCustomGears,projCgPos,projGrad]
loadData = load()
loadableParam = loadData[0]
loadableUtil = loadData[1]
loadableNodes = loadData[2]
loadableZooms = loadData[3]
loadableCam = loadData[4]
loadablePris = loadData[5]
loadableObjStr = loadData[6]
loadableObj = []
alpU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp = "abcdefghijklmnopqrstuvwxyz"
def enc64(n):
    if n < 26:
        return alpU[n]
    elif n >= 26 and n < 52:
        return alp[n-26]
    elif n >= 52 and n < 62:
        return str(n-52)
    elif n == 62:
        return "-"
    else:
        return "_"
def compEnc64(l):
    count = 0
    final = ""
    pad = 0
    while count < len(l):
        sub = []
        pad = 0
        for i in range(3):
            if count+i < len(l):
                sub.append(l[count+i])
            else:
                pad += 1
        if len(sub) > 0:
            final += enc64(int(sub[0]/4))
            if len(sub) == 1:
                final += enc64((sub[0]%4)*16)
        if len(sub) > 1:
            final += enc64((sub[0]%4)*16+int(sub[1]/16))
            if len(sub) == 2:
                final += enc64((sub[1]%16)*4)
        if len(sub) > 2:
            final += enc64((sub[1]%16)*4+int(sub[2]/64))
            final += enc64(sub[2]%64)
        count += 3
    for i in range(pad):
        final += "="
    return final
def levelStringParse(s):
    sub3 = []
    vh = []
    sub = []
    sub2 = []
    read = False
    dots = 0
    for i in range(len(s)):
        if read:
            if s[i] == ";":
                if dots <= 1:
                    if len(sub2) == 1:
                        if sub2[0] == 43:
                            vh2 = []
                            sub5 = []
                            for j in range(len(vh)):
                                if vh[j] == "a":
                                    sub5.append(strToDec(vh2))
                                    vh2 = []
                                else:
                                    vh2.append(vh[j])
                            sub5.append(strToDec(vh2))
                            sub.append(sub5)
                            vh = []
                        else:
                            sub2.append(strToDec(vh))
                            sub.append(sub2)
                else:
                    if sub2[0] == 57:
                        sub4 = []
                        vh2 = []
                        for j in range(len(vh)):
                            if vh[j] == ".":
                                sub4.append(strToDec(vh2))
                                vh2 = []
                            else:
                                vh2.append(vh[j])
                        sub4.append(strToDec(vh2))
                        sub2.append(sub4)
                        sub.append(sub2)
                sub3.append(sub)
                sub = []
                sub2 = []
                vh = []
                dots = 0
            elif s[i] == ",":
                if dots <= 1:
                    if len(sub2) == 1:
                        if sub2[0] == 43:
                            vh2 = []
                            sub5 = []
                            for j in range(len(vh)):
                                if vh[j] == "a":
                                    sub5.append(strToDec(vh2))
                                    vh2 = []
                                else:
                                    vh2.append(vh[j])
                            sub5.append(strToDec(vh2))
                            sub2.append(sub5)
                            if len(sub2)%2 == 0:
                                sub.append(sub2)
                                sub2 = []
                            vh = []
                        else:
                            sub2.append(strToDec(vh))
                            if len(sub2)%2 == 0:
                                sub.append(sub2)
                                sub2 = []
                    else:
                        sub2.append(strToDec(vh))
                        if len(sub2)%2 == 0:
                            sub.append(sub2)
                            sub2 = []
                else:
                    if sub2[0] == 57:
                        sub4 = []
                        vh2 = []
                        for j in range(len(vh)):
                            if vh[j] == ".":
                                sub4.append(strToDec(vh2))
                                vh2 = []
                            else:
                                vh2.append(vh[j])
                        sub4.append(strToDec(vh2))
                        sub2.append(sub4)
                        sub.append(sub2)
                vh = []
                dots = 0
            else:
                vh.append(s[i])
                if s[i] == ".":
                    dots += 1
                elif s[i] == "a":
                    dots = 0
        if s[i] == ";":
            read = True
    final = []
    for j in range(len(sub3)):
        t = 0
        x = 0
        y = 0
        r = 0
        s = 1
        h = False
        v = False
        tpOff = 100
        gr = []
        el = 0
        c = 0
        z = 1
        hsv = [0,1,1,0,0]
        for k in range(len(sub3[j])):
            if sub3[j][k][0] == 1:
                t = sub3[j][k][1]
            elif sub3[j][k][0] == 2:
                x = sub3[j][k][1]
            elif sub3[j][k][0] == 3:
                y = sub3[j][k][1]
            elif sub3[j][k][0] == 4:
                if sub3[j][k][1] == 1:
                    h = True
            elif sub3[j][k][0] == 5:
                if sub3[j][k][1] == 1:
                    v = True
            elif sub3[j][k][0] == 6:
                r = sub3[j][k][1]
            elif sub3[j][k][0] == 32:
                s = sub3[j][k][1]
            elif sub3[j][k][0] == 54:
                tpOff = sub3[j][k][1]
            elif sub3[j][k][0] == 57:
                gr = sub3[j][k][1]
            elif sub3[j][k][0] == 21:
                c = sub3[j][k][1]
            elif sub3[j][k][0] == 20:
                el = sub3[j][k][1]
            elif sub3[j][k][0] == 25:
                z = sub3[j][k][1]
            elif sub3[j][k][0] == 43:
                hsv = sub3[j][k][1]
        final.append(block(t,x,y,r,s,h,v,tpOff,gr,c,el,z,hsv))
    return final
for i in range(len(loadableObjStr)):
    sub = compEnc64(loadableObjStr[i])
    sub2 = gzip.decompress(base64.urlsafe_b64decode(sub.encode('utf-8'))).decode()
    loadableObj.append(levelStringParse(sub2))
loadablePatchSides = loadData[7]
loadablePrisUtil = loadData[8]
loadableProjCurves = loadData[9]
loadableExpCache = loadData[10]
loadableEL = loadData[11]
loadableFillModes = loadData[12]
loadablePresets = loadData[13]
loadableDispPoints = loadData[14]
loadablePrisDispPoints = loadData[15]
loadableCustomGears = loadData[16]
loadableCgPos = loadData[17]
loadableGrad = loadData[18]
loadProjectButton = button((300,350,100,30), "load project", 15, (0,0,0), (128,128,128),(159,159,159),(64,64,64),(len(loadableParam) > 0))
loadProjectSig = False
projectButtons = []
projectSig = []
for i in range(10):
    projectButtons.append(button((200+int(i/5)*200,80+(i%5)*80,100,50), "project "+str(i+1), 20, (0,0,0), (128,128,128),(159,159,159),(64,64,64),True))
    projectSig.append(False)
projectNum = -1
def deleteProject(n):
    fileTest = []
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "deltaSaveData.dat")):
        with open("deltaSaveData.dat", 'rb') as f:
            fileTest = f.read()
    projects = []
    count = 3
    while count < len(fileTest):
        projects.append([count,parse([fileTest[count-3],fileTest[count-2],fileTest[count-1]])])
        count += projects[-1][1]+3
    with open("deltaSaveData.dat", 'wb') as f:
        for i in range(len(projects)):
            if not i == n:
                for j in range(3):
                    f.write((int(projects[i][1]/pow(256,2-j))%256).to_bytes(1, byteorder='big'))
                for j in range(projects[i][1]):
                    f.write(int(fileTest[projects[i][0]+j]).to_bytes(1, byteorder='big'))
translatedCurves = []
curveNodes = [[],[],[],[]]
nodeManageButtons = []
nodeManageSig = []
nodeNames = ["start", "center", "end"]
for i in range(3):
    nodeManageButtons.append(button((511.25,360+i*35,15,15), "", 15, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True))
    nodeManageSig.append(False)
sampleNodes = [True, True, True]
zoom = 1
zoomButtons = [button((20,285,15,15), "-", 15, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True),button((45,285,15,15), "+", 15, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True)]
zoomSig = [False,False]
inc = [[30,0],[30,0]]
useIncrements = False
editIncButtons = []
editIncSig = []
for i in range(4):
    editIncButtons.append(eButton((200+200*int(i/2)-25+(i%2)*50,450,30,20), str(inc[int(i/2)][i%2]), (159,159,159), (191,191,191), (223,223,223), 10, (0,0,0), False))
    editIncSig.append(False)
selInc = -1
potLink = 0
canLink = False
linkedPoint = 0
fillerMode = 0
samplePrism = []
def viewDirec(c,a,r):
    for i in range(a-1):
        if r:
            smp = c.f(1-((i+1)/a))
        else:
            smp = c.f((i+1)/a)
        if (smp[0]+cam[0])*zoom > 0:
            pygame.draw.circle(screen, (255-i*255/(a-2),i*255/(a-2),0), ((smp[0]+cam[0])*zoom,300-(smp[1]-cam[1])*zoom), 5)
fillerUtilNames = ["editor level","color","z order"]
fillerUtilVals=[0,0,1]
fillerUtilButtons = []
fillerUtilButtonSig = []
for i in range(len(fillerUtilNames)):
    fillerUtilButtons.append(eButton((50+80*i,340,50,20), str(fillerUtilVals[i]), (159,159,159), (191,191,191), (223,223,223), 10, (0,0,0), False))
    fillerUtilButtonSig.append(False)
selectedFUtil = -1
def vPrism(cl,col):
    final = []
    for i in range(len(cl)):
        for j in range(10):
            sapo = []
            if cl[i][3]:
                sapo = curves[cl[i][0]][cl[i][1]][cl[i][2]].f(1-(j/10))
            else:
                sapo = curves[cl[i][0]][cl[i][1]][cl[i][2]].f(j/10)
            final.append([(sapo[0]+cam[0])*zoom,300-(sapo[1]-cam[1])*zoom])
    pygame.draw.polygon(screen, col, final, 0)
prisms = []
finishFSig = False
cancelFSig = False
with open(mFilePath, 'rb') as f:
    eDat = f.read()
dDat = xor_bytes(eDat, 11)
cDat = base64.b64decode(dDat, altchars=b'-_')
fDat = zlib.decompress(cDat[10:], -zlib.MAX_WBITS)
with open("result_gamma.txt",'wb') as f:
    f.write(fDat)
with open("result_gamma.txt",'r') as f:
    dStr = f.read()
class level:
    def __init__(self, n, s, f):
        self.n = n
        self.s = s
        self.f = f
    def expString(self):
        final = "<k>kCEK</k><i>4</i><k>k84</k><i>"
        final += str(self.f)
        final += "</i><k>k2</k><s>"
        final += "result delta"
        final += "</s><k>k4</k><s>"
        final += str(self.s)
        final += "</s><k>k5</k><s>Player</s><k>k13</k><t /><k>k21</k><i>2</i><k>k16</k><i>1</i><k>k80</k><i>5</i><k>k50</k><i>35</i><k>k47</k><t /><k>k48</k><i>18</i><k>kI1</k><r>0</r><k>kI2</k><r>36</r><k>kI3</k><r>1</r><k>kI6</k><d><k>0</k><s>0</s><k>1</k><s>0</s><k>2</k><s>0</s><k>3</k><s>0</s><k>4</k><s>0</s><k>5</k><s>0</s><k>6</k><s>0</s><k>7</k><s>0</s><k>8</k><s>0</s><k>9</k><s>0</s><k>10</k><s>0</s><k>11</k><s>0</s><k>12</k><s>0</s></d>"
        return final
read = False
sub = ""
sub2 = []
lspp = []
for i in range(len(dStr)):
    if dStr[i] == ">":
        read = True
    elif dStr[i] == "<":
        read = False
        if len(sub) > 0:
            sub2.append(sub)
            lspp.append(i-len(sub)-3)
        sub = ""
    else:
        if read:
            sub += dStr[i]
allLevels = []
lsp = []
for i in range(len(sub2)):
    if sub2[i][0] == "k" and sub2[i][1] == "_":
        allLevels.append(level(0,0,0))
        lsp.append(lspp[i])
    elif sub2[i] == "k2":
        allLevels[-1].n = sub2[i+1]
    elif sub2[i] == "k4":
        allLevels[-1].s = sub2[i+1]
    elif sub2[i] == "k84":
        allLevels[-1].f = sub2[i+1]
objs = []
for i in range(len(allLevels)):
    if allLevels[i].f == "1":
        sDat = gzip.decompress(base64.urlsafe_b64decode(allLevels[i].s.encode('utf-8'))).decode()
        fDat = ""
        add = False
        for j in range(len(sDat)):
            if add:
                fDat += sDat[j]
            if sDat[j] == ";":
                add = True
        objs.append(fDat)
finObj = []
for i in range(len(objs)):
    finObj.append(levelStringParse(objs[i]))
loadLayoutButton = button((300,400,100,30), "load layout", 15, (0,0,0), (128,128,128),(159,159,159),(64,64,64),len(finObj) > 0)
loadLayoutSig = False
layoutButtons = []
layoutSig = []
for i in range(10):
    layoutButtons.append(button((200+int(i/5)*200,80+(i%5)*80,100,50), "layout "+str(i+1), 20, (0,0,0), (128,128,128),(159,159,159),(64,64,64),True))
    layoutSig.append(False)
layoutObj = []
def qComp(a,b):
    if a == b:
        return True
    else:
        if round(math.log10(abs(a-b))) <= -2:
            return True
        else:
            return False
editMode = 0
prismSig = []
patchSideMode = 0
patchSideButton = button(((315+377.5)/2,390,40,30), "east", 15, (0,0,0), (128,128,128),(159,159,159),(64,64,64),True)
patchSideSig = False
def perpLine(c,m):
    cp = c.f(0.5)
    dc = dPara(c)
    dp = dc.f(0.5)
    an = 0
    if abs(dp[0]) > 0:
        an = math.atan(dp[1]/dp[0])
    else:
        if dp[1] > 0:
            an = math.pi/2
        else:
            an = -math.pi/2
    if dp[0] < 0:
        an += math.pi
    sp = [(cp[0]+cam[0])*zoom,300-(cp[1]-cam[1])*zoom]
    ep1 = [(cp[0]+25*math.cos(an-math.pi/2)+cam[0])*zoom,300-(cp[1]+25*math.sin(an-math.pi/2)-cam[1])*zoom]
    ep2 = [(cp[0]+25*math.cos(an+math.pi/2)+cam[0])*zoom,300-(cp[1]+25*math.sin(an+math.pi/2)-cam[1])*zoom]
    if m == 0 or m == 2:
        pygame.draw.line(screen, (0,255,0),  sp, ep1, int(5*zoom))
    if m == 1 or m == 2:
        pygame.draw.line(screen, (0,255,0),  sp, ep2, int(5*zoom))
patchSides = []
curvesInRange = []
subSelectedCurve = 0
prismUtilVals = []
editedPrism = 0
editorLevel = 0
eLevelButtons = [button((580,285,15,15), ">", 15, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True),button((535,285,15,15), "<", 15, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True),button((505,285,25,15), "all", 10, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True)]
eLevelSig = [False,False,False]
cBoxes = [[],[],[],[]]
visRange = [[-cam[0],cam[1]],[600/zoom-cam[0],300/zoom+cam[1]]]
copy = False
def optPara(x):
    return para(optFull(x.x),optFull(x.y))
rounded = [[],[]]
def isRounded(x):
    stpo = x[0].f(0)
    enpo = x[-1].f(1)
    return qComp(stpo[0],enpo[0]) and qComp(stpo[1],enpo[1])
intBits = []
for i in range(256):
    intBits.append(showBitsL(i,8))
class byteStream:
    l = []
    b = ""
    def byte(self,n):
        self.l.append(n)
    def lInt(self,n):
        sLen = 0
        if abs(round(n)) > 0:
            sLen = math.ceil(math.log(abs(round(n)),256))
        self.l.append(sLen+128*(n < 0))
        for i in range(sLen):
            self.l.append(math.floor(abs(round(n))/pow(256,sLen-i-1))%256)
    def fInt(self,n,le):
        for i in range(le):
            self.l.append(math.floor(abs(round(n))/pow(256,le-i-1))%256)
    def mBit(self,n,le):
        sub = showBitsL(n,le)
        for i in range(len(sub)):
            self.b += sub[i]
            if len(self.b) == 8:
                self.l.append(bitToDec(self.b))
                self.b = ""
    def sBit(self,s):
        self.b += str(s)
        if len(self.b) == 8:
            self.l.append(bitToDec(self.b))
            self.b = ""
    def trip(self,c):
        self.l.append(c[0]*64+int(c[1]/256))
        self.l.append(c[1]%256)
        self.l.append(c[2])
    def bBit(self,c):
        if c:
            self.sBit(1)
        else:
            self.sBit(0)
    def flo(self,n):
        isFloat = not qComp(abs(n)%1,0)
        self.bBit(n < 0)
        self.bBit(isFloat)
        cLen = 0
        if abs(n) > 0:
            cLen = math.ceil(math.log(abs(n)+1, 256))
        self.mBit(cLen, 6)
        self.fInt(abs(int(n)), cLen)
        if isFloat:
            self.fInt((abs(n)%1)*pow(2,40), 5)
    def fill(self):
        while len(self.b) < 8:
            self.b += str(0)
        self.l.append(bitToDec(self.b))
        self.b = ""
    def get(self):
        return self.l
    def readLast(self,n):
        final = []
        for i in range(n):
            final.append(self.l[i-n])
        print(final)
    def readFull(self):
        final = []
        for i in range(len(self.l)):
            final.append(self.l[i])
        print(final)
def save():
    final = []
    st = byteStream()
    st.byte((zoom-0.5)*10)
    st.lInt(cam[0])
    st.lInt(cam[1])
    for i in range(4):
        st.fInt(len(curveParam[i]),2)
        for j in range(len(curveParam[i])):
            st.mBit(curveParam[i][j][0]-1,4)
            if i < 2:
                for k in range(3):
                    st.bBit(curveNodes[i][j][k])
            elif i == 2:
                st.sBit(0)
                st.mBit(patchSides[j],2)
            else:
                st.mBit(0,3)
            if curveParam[i][j][0] == 5:
                st.bBit(curveParam[i][j][2][3])
            elif curveParam[i][j][0] == 11:
                st.bBit(len(curveParam[i][j][2]) == 2)
            else:
                st.sBit(0)
            if curveParam[i][j][0] == 1:
                st.lInt(curveParam[i][j][1][0]*1000)
                st.lInt(curveParam[i][j][1][1]*1000)
                st.byte(len(curveParam[i][j][2]))
                for k in range(len(curveParam[i][j][2])):
                    st.lInt(curveParam[i][j][2][k][0]*1000)
                    st.lInt(curveParam[i][j][2][k][1]*1000)
                st.lInt(curveParam[i][j][3][0]*1000)
                st.lInt(curveParam[i][j][3][1]*1000)
            elif curveParam[i][j][0] == 2:
                for k in range(1,7):
                    st.lInt(curveParam[i][j][k]*1000)
            elif curveParam[i][j][0] == 3:
                st.byte(len(curveParam[i][j][1]))
                for k in range(len(curveParam[i][j][1])):
                    st.trip(curveParam[i][j][1][k])
                st.byte(len(curveParam[i][j][2])-1)
                for k in range(len(curveParam[i][j][2])):
                    st.mBit(curveParam[i][j][2][k],2)
                st.fill()
                for k in range(len(curveParam[i][j][3])):
                    for m in range(len(curveParam[i][j][3][k])):
                        st.lInt(abs(curveParam[i][j][3][k][m])*1000)
            elif curveParam[i][j][0] == 4:
                for k in range(1,3):
                    st.trip(curveParam[i][j][k])
            elif curveParam[i][j][0] == 5:
                for k in range(1,3):
                    st.trip(curveParam[i][j][k])
                for m in range(len(curveParam[i][j][3])):
                    st.lInt(curveParam[i][j][3][m]*1000)
            elif curveParam[i][j][0] == 6:
                for k in range(2):
                    st.trip(curveParam[i][j][1+k*2])
                    st.lInt(curveParam[i][j][2+k*2]*1000)
            elif curveParam[i][j][0] == 7:
                st.trip(curveParam[i][j][1])
                st.byte(len(curveParam[i][j][2]))
                for k in range(len(curveParam[i][j][2])):
                    st.trip(curveParam[i][j][2][k])
                for k in range(4):
                    st.lInt(curveParam[i][j][3+k]*1000)
            elif curveParam[i][j][0] == 8:
                for k in range(1,3):
                    st.trip(curveParam[i][j][k])
                st.byte(len(curveParam[i][j][3]))
                for k in range(len(curveParam[i][j][3])):
                    st.trip(curveParam[i][j][3][k])
                for k in range(4):
                    st.lInt(curveParam[i][j][4+k]*1000)
            elif curveParam[i][j][0] == 9:
                for k in range(1,5):
                    st.trip(curveParam[i][j][k])
                st.byte(len(curveParam[i][j][5]))
                for k in range(len(curveParam[i][j][5])):
                    st.trip(curveParam[i][j][5][k])
                for k in range(4):
                    st.lInt(curveParam[i][j][6+k]*1000)
            elif curveParam[i][j][0] == 10:
                st.lInt(curveParam[i][j][1][0]*1000)
                st.lInt(curveParam[i][j][1][1]*1000)
                st.byte(len(curveParam[i][j][2]))
                for k in range(len(curveParam[i][j][2])):
                    st.lInt(curveParam[i][j][2][k][0]*1000)
                    st.lInt(curveParam[i][j][2][k][1]*1000)
                st.lInt(curveParam[i][j][3][0]*1000)
                st.lInt(curveParam[i][j][3][1]*1000)
                if curveParam[i][j][4][1]:
                    st.sBit(1)
                else:
                    st.sBit(0)
                st.mBit(curveParam[i][j][4][0],7)
            elif curveParam[i][j][0] == 11:
                st.trip(curveParam[i][j][1])
                for k in range(len(curveParam[i][j][2])):
                    st.trip(curveParam[i][j][2][k])
                st.byte(curveParam[i][j][3][0])
                st.byte(curveParam[i][j][3][1])
            st.byte(curvesUtil[i][j][0])
            if i < 2:
                st.fInt(curvesUtil[i][j][1]*100,2)
                st.fInt(curvesUtil[i][j][2],2)
                st.byte(curvesUtil[i][j][3]%256)
    st.fInt(len(prisms),2)
    for i in range(len(prisms)):
        st.byte(len(prisms[i]))
        for j in range(len(prisms[i])):
            st.fInt(prisms[i][j][0]*16384+prisms[i][j][3]*8192+prisms[i][j][1],2)
            st.byte(prisms[i][j][2])
        st.byte(prismUtilVals[i][0])
        st.fInt(prismUtilVals[i][1]+fillModes[i]*32768,2)
        st.byte(prismUtilVals[i][2]%256)
        st.byte(len(prismUtilVals[i][3]))
        for j in range(len(prismUtilVals[i][3])):
            st.byte(prismUtilVals[i][3][j])
    st.fInt(len(currObjStream),3)
    for i in range(len(currObjStream)):
        st.byte(currObjStream[i])
    for i in range(len(curves)):
        st.fInt(len(curves[i]),2)
        for j in range(len(curves[i])):
            st.fInt(len(curves[i][j]),2)
            for k in range(len(curves[i][j])):
                st.fInt(len(curves[i][j][k].x.l),2)
                for m in range(len(curves[i][j][k].x.l)):
                    st.mBit(0,3)
                    st.mBit(curves[i][j][k].x.l[m][0],2)
                    st.mBit(curves[i][j][k].x.l[m][2],2)
                    st.bBit(curves[i][j][k].x.l[m][3])
                    if curves[i][j][k].x.l[m][0] == 0:
                        st.byte(len(curves[i][j][k].x.l[m][1].c))
                        for n in range(len(curves[i][j][k].x.l[m][1].c)):
                            st.flo(curves[i][j][k].x.l[m][1].c[n])
                    elif curves[i][j][k].x.l[m][0] == 1:
                        sub2 = 0
                        for n in range(len(curves[i][j][k].x.l[m][1])):
                            sub2 += len(curves[i][j][k].x.l[m][1][n])
                        st.byte(sub2)
                        for n in range(len(curves[i][j][k].x.l[m][1])):
                            for o in range(len(curves[i][j][k].x.l[m][1][n])):
                                st.fInt(curves[i][j][k].x.l[m][1][n][o]+(o == 0)*32768, 2)
                    elif curves[i][j][k].x.l[m][0] == 2:
                        st.fInt(curves[i][j][k].x.l[m][1][0], 2)
                        st.fInt(curves[i][j][k].x.l[m][1][1], 2)
                sub2 = 0
                for m in range(len(curves[i][j][k].x.pt)):
                    sub2 += len(curves[i][j][k].x.pt[m])
                st.byte(sub2)
                for m in range(len(curves[i][j][k].x.pt)):
                    for n in range(len(curves[i][j][k].x.pt[m])):
                        st.fInt(curves[i][j][k].x.pt[m][n]+(n == 0)*32768, 2)
                st.fInt(len(curves[i][j][k].y.l),2)
                for m in range(len(curves[i][j][k].y.l)):
                    st.mBit(0,3)
                    st.mBit(curves[i][j][k].y.l[m][0],2)
                    st.mBit(curves[i][j][k].y.l[m][2],2)
                    st.bBit(curves[i][j][k].y.l[m][3])
                    if curves[i][j][k].y.l[m][0] == 0:
                        st.byte(len(curves[i][j][k].y.l[m][1].c))
                        for n in range(len(curves[i][j][k].y.l[m][1].c)):
                            st.flo(curves[i][j][k].y.l[m][1].c[n])
                    elif curves[i][j][k].y.l[m][0] == 1:
                        sub2 = 0
                        for n in range(len(curves[i][j][k].y.l[m][1])):
                            sub2 += len(curves[i][j][k].y.l[m][1][n])
                        st.byte(sub2)
                        for n in range(len(curves[i][j][k].y.l[m][1])):
                            for o in range(len(curves[i][j][k].y.l[m][1][n])):
                                st.fInt(curves[i][j][k].y.l[m][1][n][o]+(o == 0)*32768, 2)
                    elif curves[i][j][k].y.l[m][0] == 2:
                        st.fInt(curves[i][j][k].y.l[m][1][0], 2)
                        st.fInt(curves[i][j][k].y.l[m][1][1], 2)
                sub2 = 0
                for m in range(len(curves[i][j][k].y.pt)):
                    sub2 += len(curves[i][j][k].y.pt[m])
                st.byte(sub2)
                for m in range(len(curves[i][j][k].y.pt)):
                    for n in range(len(curves[i][j][k].y.pt[m])):
                        st.fInt(curves[i][j][k].y.pt[m][n]+(n == 0)*32768, 2)
    for i in range(3):
        st.fInt(len(exportObjCache[i]),2)
        for j in range(len(exportObjCache[i])):
            st.byte(len(exportObjCache[i][j]))
            for k in range(len(exportObjCache[i][j])):
                st.fInt(len(exportObjCache[i][j][k]),3)
                for m in range(len(exportObjCache[i][j][k])):
                    st.byte(exportObjCache[i][j][k][m])
    st.fInt(len(exportObjCache[3]),2)
    for j in range(len(exportObjCache[3])):
        st.fInt(len(exportObjCache[3][j]),3)
        for k in range(len(exportObjCache[3][j])):
            st.byte(exportObjCache[3][j][k])
    st.byte(editorLevel)
    st.byte(len(presets))
    for i in range(len(presets)):
        st.byte(len(presets[i]))
        for j in range(len(presets[i])):
            st.fInt(presets[i][j][0],2)
            st.byte(presets[i][j][1])
    for i in range(4):
        st.fInt(len(dispPoints[i]),2)
        for j in range(len(dispPoints[i])):
            st.byte(len(dispPoints[i][j]))
            for k in range(len(dispPoints[i][j])):
                st.fInt(len(dispPoints[i][j][k]), 2)
                for m in range(len(dispPoints[i][j][k])):
                    st.lInt(dispPoints[i][j][k][m][0]*1000)
                    st.lInt(dispPoints[i][j][k][m][1]*1000)
    st.fInt(len(prismDispPoints),2)
    for j in range(len(prismDispPoints)):
        st.fInt(len(prismDispPoints[j]), 2)
        for k in range(len(prismDispPoints[j])):
            st.lInt(prismDispPoints[j][k][0]*1000)
            st.lInt(prismDispPoints[j][k][1]*1000)
    st.byte(len(customGears))
    for i in range(len(customGears)):
        for j in range(3):
            st.byte(len(customGears[i][j]))
            for k in range(len(customGears[i][j])):
                st.fInt(customGears[i][j][k][0],2)
                st.byte(customGears[i][j][k][1])
        st.byte(len(customGears[i][3]))
        for j in range(len(customGears[i][3])):
            st.fInt(customGears[i][3][j],2)
        st.lInt(customGears[i][4][0]*1000)
        st.lInt(customGears[i][4][1]*1000)
        st.byte(customGears[i][5])
    st.fInt(len(cgPos),2)
    for i in range(len(cgPos)):
        st.lInt(cgPos[i][0]*1000)
        st.lInt(cgPos[i][1]*1000)
        st.byte(cgPos[i][2])
    st.byte(len(gradients))
    for i in range(len(gradients)):
        st.lInt(gradients[i][0]*1000)
        st.lInt(gradients[i][1]*1000)
        st.bBit(gradients[i][2] == 1)
        st.mBit(gradients[i][3],2)
        st.fill()
        if gradients[i][3] == 0:
            st.lInt(gradients[i][4])
            st.lInt(gradients[i][5])
        else:
            st.byte(int(gradients[i][4]*255))
            st.byte(int(gradients[i][5]*255))
    fBytes = st.get()
    fileTest = []
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "deltaSaveData.dat")):
        with open("deltaSaveData.dat", 'rb') as f:
            fileTest = f.read()
    projects = []
    count = 3
    while count < len(fileTest):
        projects.append([count,parse([fileTest[count-3],fileTest[count-2],fileTest[count-1]])])
        count += projects[-1][1]+3
    if projectNum == -1:
        with open("deltaSaveData.dat", 'wb') as f:
            for i in range(len(fileTest)):
                f.write(int(fileTest[i]).to_bytes(1, byteorder='big'))
            for k in range(3):
                f.write((int(len(fBytes)/pow(256,2-k))%256).to_bytes(1, byteorder='big'))
            for i in range(len(fBytes)):
                f.write(int(fBytes[i]).to_bytes(1, byteorder='big'))
    else:
        with open("deltaSaveData.dat", 'wb') as f:
            for i in range(len(projects)):
                if i == projectNum:
                    for k in range(3):
                        f.write((int(len(fBytes)/pow(256,2-k))%256).to_bytes(1, byteorder='big'))
                    for i in range(len(fBytes)):
                        f.write(int(fBytes[i]).to_bytes(1, byteorder='big'))
                else:
                    for j in range(3):
                        f.write(((projects[i][1]/pow(256,2-j))%256).to_bytes(1, byteorder='big'))
                    for j in range(projects[i][1]):
                        f.write(int(fileTest[projects[i][0]+j]).to_bytes(1, byteorder='big'))
    print("saved")

b64alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
def dec64(c):
    count = 0
    while not c == b64alp[count]:
        count += 1
    return count
def compConv64(l):
    count = 0
    final = []
    while count < len(l):
        sub = []
        pad = 0
        for i in range(4):
            if not l[count+i] == "=":
                sub.append(dec64(l[count+i]))
            else:
                sub.append(0)
                pad += 1
        final.append(sub[0]*4+int(sub[1]/16))
        final.append((sub[1]%16)*16+int(sub[2]/4))
        final.append((sub[2]%4)*64+sub[3])
        count += 4
    final[len(final)-pad:len(final)] = []
    return final
currObjStream = []
exportObjCache = [[],[],[],[]]
def createElementObjects(t,main,ut,no,dMain):
    objects = []
    if t == 0:
        if isRounded(main):
            for m in range(len(main)):
                objects.append([])
                cData = posToList(main[m],ut[1],dMain[m])[0]
                for j in range(len(cData)-1):
                    objects[m].append([1764,cData[j][0],cData[j][1],0,ut[1]/7.5,ut[2]+1,ut[3],ut[0]])
                    obj = objLine([cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1]],ut[1])
                    for k in range(len(obj)):
                        objects[m].append(obj[k])
                        objects[m][-1].append(ut[2]+1)
                        objects[m][-1].append(ut[3])
                        objects[m][-1].append(ut[0])
        else:
            for m in range(len(main)):
                objects.append([])
                cData = posToList(main[m],ut[1],dMain[m])[0]
                for j in range(len(cData)-1):
                    if j == 0 and m == 0 and no[0] == 1:
                        objects[m].append([1764,cData[j][0],cData[j][1],0,ut[1]/7.5,ut[2]+1,ut[3],ut[0]])
                    elif (j > 0 or m > 0) and (j < len(cData)-1 or m < len(main)-1) and no[1] == 1:
                        objects[m].append([1764,cData[j][0],cData[j][1],0,ut[1]/7.5,ut[2]+1,ut[3],ut[0]])
                    obj = objLine([cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1]],ut[1])
                    for k in range(len(obj)):
                        objects[m].append(obj[k])
                        objects[m][-1].append(ut[2]+1)
                        objects[m][-1].append(ut[3])
                        objects[m][-1].append(ut[0])
                if m == len(main)-1 and no[2] == 1:
                    objects[m].append([1764,cData[-1][0],cData[-1][1],0,ut[1]/7.5,ut[2]+1,ut[3],ut[0]])
    elif t == 1:
        if isRounded(main):
            for m in range(len(main)):
                objects.append([])
                cData = posToList(main[m],ut[1],dMain[m])[0]
                for j in range(len(cData)-1):
                    objects[m].append([1888,cData[j][0],cData[j][1],0,ut[1]/10,ut[2]+1,ut[3],ut[0]])
        else:
            for m in range(len(main)):
                objects.append([])
                cData = posToList(main[m],ut[1],dMain[m])[0]
                for j in range(len(cData)-1):
                    if j == 0 and m == 0 and no[0] == 1:
                        objects[m].append([1888,cData[j][0],cData[j][1],0,ut[1]/10,ut[2]+1,ut[3],ut[0]])
                    elif (j > 0 or m > 0) and (j < len(cData)-1 or m < len(main)-1):
                        objects[m].append([1888,cData[j][0],cData[j][1],0,ut[1]/10,ut[2]+1,ut[3],ut[0]])
                if m == len(main)-1 and no[2] == 1:
                    objects[m].append([1888,cData[-1][0],cData[-1][1],0,ut[1]/10,ut[2]+1,ut[3],ut[0]])
    elif t == 2:
        for m in range(len(main)):
            objects.append([])
            cData = posToList(main[m],15,dMain[m])[0]
            for j in range(len(cData)-1):
                an = da(cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1])
                if no == 0 or no == 2:
                    objects[m].append([39,cData[j][0]+math.sqrt(261)*math.cos(-math.atan(2/5)+an*math.pi/180)*dis(cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1])/30,cData[j][1]+math.sqrt(261)*math.sin(-math.atan(2/5)+an*math.pi/180)*dis(cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1])/30,-an+180,dis(cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1])/30,0,0,ut[0]])
                if no == 1 or no == 2:
                    objects[m].append([39,cData[j][0]+math.sqrt(261)*math.cos(math.atan(2/5)+an*math.pi/180)*dis(cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1])/30,cData[j][1]+math.sqrt(261)*math.sin(math.atan(2/5)+an*math.pi/180)*dis(cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1])/30,-an,dis(cData[j][0],cData[j][1],cData[j+1][0],cData[j+1][1])/30,0,0,ut[0]])
    elif t == 3:
        filler = []
        sPrism = []
        dsPrism = []
        ddsPrism = []
        if main[0][0] < 2:
            sW = curvesUtil[main[0][0]][main[0][1]][1]
        else:
            sW = 10
        for j in range(len(main)):
            if main[j][3]:
                sPrism.append(slicePara(curves[main[j][0]][main[j][1]][main[j][2]],[1,0]))
                dsPrism.append(dPara(sPrism[-1]))
                ddsPrism.append(dPara(dsPrism[-1]))
            else:
                sPrism.append(curves[main[j][0]][main[j][1]][main[j][2]])
                dsPrism.append(dCurves[main[j][0]][main[j][1]][main[j][2]])
                ddsPrism.append(ddCurves[main[j][0]][main[j][1]][main[j][2]])
            est = 10
            if main[j][0] < 2:
                est = curvesUtil[main[j][0]][main[j][1]][1]
            if est < sW:
                sW = est
        cD = direction(dsPrism,ddsPrism,100)
        if no == 0:
            filler = fillPrism(sPrism,sW,cD,dsPrism)
        else:
            filler = antiFillPrism(sPrism,sW,cD,dsPrism)
        for x in range(len(filler)):
            if filler[x][2] > 20:
                objects.append([211,filler[x][0]+filler[x][2]/2,filler[x][1]+filler[x][2]/2,0,math.ceil(filler[x][2]/30*100)/100,ut[1],ut[2],ut[0]])
            elif filler[x][2] < 20 and filler[x][2] > 10:
                objects.append([916,filler[x][0]+filler[x][2]/2,filler[x][1]+filler[x][2]/2,0,1,ut[1],ut[2],ut[0]])
            else:
                objects.append([917,filler[x][0]+filler[x][2]/2,filler[x][1]+filler[x][2]/2,0,math.ceil(filler[x][2]/7.5*100)/100,ut[1],ut[2],ut[0]])
    if t < 3:
        fl = []
        for m in range(len(objects)):
            final = ""
            for i in range(len(objects[m])):
                for j in range(len(objects[m][i])):
                    final += str(finalRef[j])
                    final += ","
                    final += str(objects[m][i][j])
                    if j < len(objects[m][i])-1:
                        final += ","
                final += ";"
            cFinal = base64.urlsafe_b64encode(gzip.compress(final.encode('utf-8'))).decode()
            ccFinal = compConv64(cFinal)
            fl.append(ccFinal)
        return fl
    else:
        final = ""
        for i in range(len(objects)):
            for j in range(len(objects[i])):
                final += str(finalRef[j])
                final += ","
                final += str(objects[i][j])
                if j < len(objects[i])-1:
                    final += ","
            final += ";"
        cFinal = base64.urlsafe_b64encode(gzip.compress(final.encode('utf-8'))).decode()
        ccFinal = compConv64(cFinal)
        return ccFinal
fillerModeButton = button((120,400,80,30), "normal", 15, (0,0,0), (159,159,159),(191,191,191),0,True)
fillerModeSig = False
fillMode = 0
fillModes = []
applyGradButton = button((220,400,80,30), "apply\ngradients", 10, (0,0,0), (159,159,159),(191,191,191),(64,64,64),False)
applyGradSig = False
applyGrad = False
gradButtons = []
gradSigs = []
for i in range(10):
    gradButtons.append(button((100+(i%5)*100,360+int(i/5)*60,80,40), "---", 20, (0,0,0), (159,159,159), (191,191,191), (64,64,64), True))
    gradSigs.append(False)
potMultiInt = False
pmibNotice = button((65,220,115,70), "this border curve\nintersects the main\ncurve more than once\n\npress d to intersect\nthis border curve twice", 10, (0,0,0), (128,128,128),(191,191,191),(128,128,128),False)
presetMode = 0
configPresetButtons = []
configPresetSigs = []
configPresetNames = ["create\nnew preset", "view\npreset", "delete\npreset"]
for i in range(3):
    configPresetButtons.append(button((150+i*150,390,120,60), configPresetNames[i], 20, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True))
    configPresetSigs.append(False)
samplePreset = []
presets = []
presetButtons = []
presetSigs = []
for i in range(10):
    presetButtons.append(button((100+(i%5)*100,360+int(i/5)*60,80,40), "---", 20, (0,0,0), (159,159,159), (191,191,191), (64,64,64), True))
    presetSigs.append(False)
presetCenters = []
presetPage = 0
prevC = []
configPresetButtons[1].en = False
mainPresetButton = button((130,430,60,30), "configure\npresets", 10, (0,0,0), (159,159,159),(191,191,191),0,True)
mainPresetSig = False
usePresetButton = button((200,440,100,30), "use presets", 15, (0,0,0), (159,159,159),(191,191,191),(64,64,64),True)
usePresetSig = False
dispPoints = [[],[],[],[]]
scPoints = []
def dispBox(b,o,c):
    final = []
    for j in range(2):
        final.append([])
        for k in range(2):
            if k == 0:
                final[j].append((b[j][k]+o*pow(-1,j+1)+cam[0])*zoom)
            else:
                final[j].append(300-(b[j][k]+o*pow(-1,j+1)-cam[1])*zoom)
    pygame.draw.line(screen, c, (final[0][0],final[0][1]), (final[0][0],final[1][1]), 2)
    pygame.draw.line(screen, c, (final[0][0],final[0][1]), (final[1][0],final[0][1]), 2)
    pygame.draw.line(screen, c, (final[1][0],final[0][1]), (final[1][0],final[1][1]), 2)
    pygame.draw.line(screen, c, (final[0][0],final[1][1]), (final[1][0],final[1][1]), 2)
def inBox(b,p,o):
    if p[0] > b[0][0]-o and p[0] < b[1][0]+o and p[1] > b[0][1]-o and p[1] < b[1][1]+o:
        return True
    else:
        return False
sclPoints = []
customGearButton = button((210,430,60,30), "custom\ngear", 10, (0,0,0), (159,159,159),(191,191,191),0,True)
customGearSig = False
customGears = []
customGearMode = 0
sampleCustomGear = [[],[],[],[],[],50]
pBoxes = []
prismDispPoints = []
subSelectedPrism = 0
prismsInRange = []
customGearType = 0
cgmButtons = [
    eButton((120,340,80,30), str(customGearType), (159,159,159), (191,191,191), (223,223,223), 15, (0,0,0), False),
    eButton((240,340,80,30), str(50), (159,159,159), (191,191,191), (223,223,223), 15, (0,0,0), False),
    button((360,340,80,30), "edit gear", 15, (0,0,0), (159,159,159),(191,191,191),0,True),
    eButton((120,390,80,30), "add gears", (159,159,159), (191,191,191), (223,223,223), 15, (0,0,0), False),
    eButton((240,390,100,30), "delete gears", (159,159,159), (191,191,191), (223,223,223), 15, (0,0,0), False),
    button((360,390,80,30), "create new\ngear type", 10, (0,0,0), (159,159,159),(191,191,191),0,True),
    eButton((480,340,80,30), "delete\ngear type", (159,159,159), (191,191,191), (223,223,223), 10, (0,0,0), False),
]
cgmSigs = [False,False,False,False,False,False,False]
addCustomGears = False
deleteCustomGears = False
cgPos = []
cgmBackButton = button((480,390,80,30), "back", 15, (0,0,0), (159,159,159),(191,191,191),0,True)
cgmBackSig = False
editedCustomGear = -1
cgExpCache = []
isGearElement = [[],[],[],[]]
samplePrismDisp = []
gradientButton = button((290,430,60,30), "gradient\nfield", 10, (0,0,0), (159,159,159),(191,191,191),0,True)
gradientSig = False
gradientMode = 0
gradients = []
sampleGrad = [0,0,0,0,0,360]
gradOrientButton = button((300,450,100,30), "horizontal", 10, (0,0,0), (159,159,159),(191,191,191),0,True)
gradOrientSig = False
gradManageButtons = [
    eButton((120,360,80,40), str(sampleGrad[4]), (159,159,159), (191,191,191), (223,223,223), 15, (0,0,0), False),
    eButton((240,360,80,40), str(sampleGrad[5]), (159,159,159), (191,191,191), (223,223,223), 15, (0,0,0), False),
    button((360,360,80,40), "hue", 15, (0,0,0), (159,159,159),(191,191,191),0,True),
    button((480,360,80,40), "finish", 15, (0,0,0), (96,191,96),(128,255,128),0,True),
]
gradManageSigs = [False,False,False,False]
gradLimits = [[],[],[]]
gradManageNames = ["minimum:","maximum:","type:"]
sampleGradients = []
prismCenters = []
while True:
    curvesInRange = []
    prismsInRange = []
    canLink = False
    visRange = [[-cam[0],cam[1]],[600/zoom-cam[0],300/zoom+cam[1]]]
    c = pygame.mouse.get_rel()
    mp = pygame.mouse.get_pos()
    if menu == "main":
        pygame.draw.rect(screen, (191,191,191), (0,0,600,480))
        screen.blit(titleText, titleText.get_rect(centerx=300, centery=175))
        newProjectSig = newProjectButton.disp()
        contProjectSig = contProjectButton.disp()
        loadProjectSig = loadProjectButton.disp()
        loadLayoutSig = loadLayoutButton.disp()
    elif menu == "load":
        pygame.draw.rect(screen, (191,191,191), (0,0,600,480))
        for i in range(10):
            if i >= len(loadableParam):
                projectButtons[i].en = False
                projectButtons[i].t = "---"
            projectSig[i] = projectButtons[i].disp()
    elif menu == "load_layout":
        pygame.draw.rect(screen, (191,191,191), (0,0,600,480))
        for i in range(10):
            if i >= len(finObj):
                layoutButtons[i].en = False
                layoutButtons[i].t = "---"
            layoutSig[i] = layoutButtons[i].disp()
    elif menu == "editor":
        pygame.draw.rect(screen, (255,255,255), (0,0,600,480))
        for i in range(math.ceil(20/zoom)):
            pygame.draw.line(screen, (240,240,240), ((i*30+(cam[0]%30))*zoom,0), ((i*30+(cam[0]%30))*zoom,300), 2)
        for i in range(math.ceil(10/zoom)):
            pygame.draw.line(screen, (240,240,240), (0,300-((i+1)*30-(cam[1]%30))*zoom), (600,300-((i+1)*30-(cam[1]%30))*zoom), 2)
        pygame.draw.line(screen, (0,0,0), (cam[0]*zoom,0), (cam[0]*zoom,300), 2)
        pygame.draw.line(screen, (0,0,0), (0,300+cam[1]*zoom), (600,300+cam[1]*zoom), 2)
        for i in range(len(layoutObj)):
            layoutObj[i].disp()
        for i in range(len(prisms)):
            if (prismUtilVals[i][0] == editorLevel) or editorLevel == -1:
                pCol = (0,0,0)
                if (edit and editMode == 1 and fillerMode == 0) or (customGearMode == 2 and viewMode == 3):
                    if inBox(pBoxes[i], [mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1]], 15):
                        prismsInRange.append(i)
                    else:
                        prismSig[i] = False
                dispCurve(prismDispPoints[i], pCol, 0)
        for i in range(len(curves[viewMode])):
            show = False
            if editorLevel == -1:
                show = True
                if viewMode == 3 and customGearMode > 0:
                    show = False
            else:
                if curvesUtil[viewMode][i][0] == editorLevel:
                    show = True
            if show:
                for j in range(len(curves[viewMode][i])):
                    if cBoxes[viewMode][i][j][0][0] < visRange[1][0] and cBoxes[viewMode][i][j][1][0] > visRange[0][0] and cBoxes[viewMode][i][j][0][1] < visRange[1][1] and cBoxes[viewMode][i][j][1][1] > visRange[0][1]:
                        if drawMode == 3 or drawMode == 4 or drawMode == 4.01 or drawMode == 5 or drawMode == 5.01 or drawMode == 6 or drawMode == 6.01 or drawMode == 7 or drawMode == 7.01 or drawMode == 8 or drawMode == 8.01 or drawMode == 8.02 or (drawMode >= 9 and drawMode < 9.05) or drawMode == 11 or drawMode == 11.01 or presetMode == 2 or customGearMode == 2:
                            if viewMode < 2:
                                if inBox(cBoxes[viewMode][i][j], [mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1]], 10+curvesUtil[viewMode][i][1]/2):
                                    curvesInRange.append([i,j])
                                else:
                                    curveSig[viewMode][i] = False
                            else:
                                if inBox(cBoxes[viewMode][i][j], [mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1]], 12.5):
                                    curvesInRange.append([i,j])
                                else:
                                    curveSig[viewMode][i] = False
                        elif drawMode == 0 and ((edit and editMode == 0) or delete or fillerMode == 1 or copy):
                            if viewMode < 2:
                                if inBox(cBoxes[viewMode][i][j], [mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1]], 10+curvesUtil[viewMode][i][1]/2):
                                    curvesInRange.append([i,j])
                                else:
                                    curveSig[viewMode][i] = False
                            else:
                                if inBox(cBoxes[viewMode][i][j], [mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1]], 12.5):
                                    curvesInRange.append([i,j])
                                else:
                                    curveSig[viewMode][i] = False
                        if edit and (drawMode == 3.03 or drawMode == 4.02 or drawMode == 5.02 or drawMode == 6.02 or drawMode == 7.02 or drawMode == 8.03 or drawMode == 9.05 or drawMode == 11.02 or (drawMode >= 1.03 and drawMode < 2) or drawMode == 2.01):
                            if not viewMode == editedCurve[0] or not i == editedCurve[1]:
                                dispCurve(dispPoints[viewMode][i][j], (0,0,0), 0)
                        else:
                            dispCurve(dispPoints[viewMode][i][j], (0,0,0), 0)
        if subSelectedCurve >= len(curvesInRange):
            subSelectedCurve = len(curvesInRange)-1
        if subSelectedCurve <= -1:
            subSelectedCurve = 0
        if subSelectedPrism >= len(prismsInRange):
            subSelectedPrism = len(prismsInRange)-1
        if subSelectedPrism <= -1:
            subSelectedPrism = 0
        for i in range(len(curvesInRange)):
            sCol = (0,0,0)
            if i == subSelectedCurve:
                sCol = (0,255,0)
                curveSig[viewMode][curvesInRange[i][0]] = True
                curveParamNum = curvesInRange[i][1]
            else:
                if not curvesInRange[i][0] == curvesInRange[subSelectedCurve][0]:
                    curveSig[viewMode][curvesInRange[i][0]] = False
            if viewMode < 2:
                dispBox(cBoxes[viewMode][curvesInRange[i][0]][curvesInRange[i][1]],10+curvesUtil[viewMode][curvesInRange[i][0]][curvesInRange[i][1]]/2, sCol)
            else:
                dispBox(cBoxes[viewMode][curvesInRange[i][0]][curvesInRange[i][1]],12.5, sCol)
            if i == subSelectedCurve:
                dispCurve(dispPoints[viewMode][curvesInRange[i][0]][curvesInRange[i][1]], (0,255,0), 0)
        for i in range(len(prismsInRange)):
            sCol = (0,0,0)
            if i == subSelectedPrism:
                sCol = (0,255,0)
                prismSig[prismsInRange[i]] = True
            else:
                prismSig[prismsInRange[i]] = False
            dispBox(pBoxes[prismsInRange[i]],15, sCol)
            if i == subSelectedPrism:
                dispCurve(prismDispPoints[prismsInRange[i]], (0,255,0), 0)
        if customGearMode == 2:
            if viewMode < 3:
                for i in range(len(sampleCustomGear[viewMode])):
                    dispCurve(dispPoints[viewMode][sampleCustomGear[viewMode][i][0]][sampleCustomGear[viewMode][i][1]], (0,0,255), 0)
            else:
                for i in range(len(sampleCustomGear[3])):
                    dispCurve(prismDispPoints[sampleCustomGear[3][i]], (0,0,255), 0)
            if (sampleCustomGear[4][0]+cam[0])*zoom > 0:
                bCirc([(sampleCustomGear[4][0]+cam[0])*zoom,300-(sampleCustomGear[4][1]-cam[1])*zoom],(255,0,127),1,4)
        elif customGearMode == 3:
            bCirc([(customGears[customGearType][4][0]+cam[0])*zoom,300-(customGears[customGearType][4][1]-cam[1])*zoom],(255,0,127),1,4)
            pygame.draw.circle(screen, (255,0,0), ((customGears[customGearType][4][0]+cam[0])*zoom,300-(customGears[customGearType][4][1]-cam[1])*zoom), customGears[customGearType][5]*zoom, int(2*zoom))
        if fillerMode == 1:
            for i in range(len(samplePrism)):
                viewDirec(curves[samplePrism[i][0]][samplePrism[i][1]][samplePrism[i][2]],10,samplePrism[i][3])
        elif fillerMode == 2:
            dispCurve(samplePrismDisp, (0,0,0), 0)
        elif presetMode == 2:
            for i in range(len(samplePreset)):
                vCurve(curves[3][samplePreset[i][0]][samplePreset[i][1]],10,10,(0,255,0), 0)
        elif presetMode == 3 or presetMode == 4 or presetMode == 5:
            if True in presetSigs:
                for i in range(len(presetSigs)):
                    if presetSigs[i]:
                        for j in range(len(presets[i])):
                            vCurve(curves[3][presets[i][j][0]][presets[i][j][1]],10,10,(255,0,127), 0)
        if customGearMode == 1:
            if useIncrements:
                samp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                samp2 = [(samp[0]+cam[0])*zoom,300-(samp[1]-cam[1])*zoom]
                bCirc(samp2,(255,0,127),1,4)
            else:
                bCirc(mp,(255,0,127),1,4)
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 0
        if addCustomGears:
            if useIncrements:
                samp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                samp2 = [(samp[0]+cam[0])*zoom,300-(samp[1]-cam[1])*zoom]
                bCirc(samp2,(127,0,255),1,4)
            else:
                bCirc(mp,(127,0,255),1,4)
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 0
        for i in range(len(cgPos)):
            gCol = (0,0,0)
            if cgPos[i][2] == customGearType:
                gCol = (0,127,255)
            if deleteCustomGears:
                gDist = dis(mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1],cgPos[i][0],cgPos[i][1])
                if gDist < customGears[cgPos[i][2]][5]:
                    gCol = (0,255,255)
            pygame.draw.circle(screen, gCol, ((cgPos[i][0]+cam[0])*zoom,300-(cgPos[i][1]-cam[1])*zoom), int(customGears[cgPos[i][2]][5]*zoom), int(2*zoom))
        if gradientMode == 1 or gradientMode == 2:
            if gradientMode == 2:
                if sampleGrad[2] == 0:
                    pygame.draw.line(screen, (255,0,0), ((sampleGrad[0]+cam[0])*zoom,0), ((sampleGrad[0]+cam[0])*zoom,300), 2)
                else:
                    pygame.draw.line(screen, (255,0,0), (0,300-(sampleGrad[0]-cam[1])*zoom), (600,300-(sampleGrad[0]-cam[1])*zoom), 2)
            if sampleGrad[2] == 0:
                if useIncrements:
                    samp = round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1]
                    samp2 = (samp+cam[0])*zoom
                    pygame.draw.line(screen, (0,0,0), (samp2,0), (samp2,300), 2)
                else:
                    pygame.draw.line(screen, (0,0,0), (mp[0],0), (mp[0],300), 2)
            else:
                if useIncrements:
                    samp = round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]
                    samp2 = 300-(samp-cam[1])*zoom
                    pygame.draw.line(screen, (0,0,0), (0,samp2), (600,samp2), 2)
                else:
                    pygame.draw.line(screen, (0,0,0), (0,mp[1]), (600,mp[1]), 2)
        if gradientMode == 3:
            if sampleGrad[2] == 0:
                pygame.draw.line(screen, (255,0,0), ((sampleGrad[0]+cam[0])*zoom,0), ((sampleGrad[0]+cam[0])*zoom,300), 2)
                pygame.draw.line(screen, (0,255,0), ((sampleGrad[1]+cam[0])*zoom,0), ((sampleGrad[1]+cam[0])*zoom,300), 2)
            else:
                pygame.draw.line(screen, (255,0,0), (0,300-(sampleGrad[0]-cam[1])*zoom), (600,300-(sampleGrad[0]-cam[1])*zoom), 2)
                pygame.draw.line(screen, (0,255,0), (0,300-(sampleGrad[1]-cam[1])*zoom), (600,300-(sampleGrad[1]-cam[1])*zoom), 2)
        for i in range(len(gradients)):
            if gradients[i][2] == 0:
                pygame.draw.line(screen, (0,0,0), ((gradients[i][0]+cam[0])*zoom,0), ((gradients[i][0]+cam[0])*zoom,300), 2)
                pygame.draw.line(screen, (0,0,0), ((gradients[i][1]+cam[0])*zoom,0), ((gradients[i][1]+cam[0])*zoom,300), 2)
            else:
                pygame.draw.line(screen, (0,0,0), (0,300-(gradients[i][0]-cam[1])*zoom), (600,300-(gradients[i][0]-cam[1])*zoom), 2)
                pygame.draw.line(screen, (0,0,0), (0,300-(gradients[i][1]-cam[1])*zoom), (600,300-(gradients[i][1]-cam[1])*zoom), 2)
        if drawMode == 1 or drawMode == 2 or drawMode == 10:
            if useIncrements:
                samp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                samp2 = [(samp[0]+cam[0])*zoom,300-(samp[1]-cam[1])*zoom]
                bCirc(samp2,(0,255,0),1,4)
            else:
                bCirc(mp,(0,255,0),1,4)
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 0
        elif drawMode == 1.01 or drawMode == 10.01:
            bCirc([(sp[0]+cam[0])*zoom,300-(sp[1]-cam[1])*zoom],(0,255,0),1,4)
            for i in range(len(cp)):
                bCirc([(cp[i][0]+cam[0])*zoom,300-(cp[i][1]-cam[1])*zoom],(255,255,0),1,4)
            if useIncrements:
                samp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                samp2 = [(samp[0]+cam[0])*zoom,300-(samp[1]-cam[1])*zoom]
                bCirc(samp2,(255,255,0),1,4)
            else:
                bCirc(mp,(255,255,0),1,4)
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 1
        elif drawMode == 1.02 or drawMode == 10.02:
            bCirc([(sp[0]+cam[0])*zoom,300-(sp[1]-cam[1])*zoom],(0,255,0),1,4)
            for i in range(len(cp)):
                bCirc([(cp[i][0]+cam[0])*zoom,300-(cp[i][1]-cam[1])*zoom],(255,255,0),1,4)
            if useIncrements:
                samp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                samp2 = [(samp[0]+cam[0])*zoom,300-(samp[1]-cam[1])*zoom]
                bCirc(samp2,(255,0,0),1,4)
            else:
                bCirc(mp,(255,0,0),1,4)
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 2
        elif drawMode >= 1.03 and drawMode < 2:
            if edit:
                dispCurve(scPoints,(255,0,0),0)
            else:
                dispCurve(scPoints,(0,0,0),0)
            if viewMode == 2:
                perpLine(sc,patchSideMode)
            spSig = False
            if (sp[0]+cam[0])*zoom > 0:
                spSig = cButton([(sp[0]+cam[0])*zoom,300-(sp[1]-cam[1])*zoom],4,(0,255,0),(128,255,128)).disp()
            for i in range(len(cp)):
                cpSigs[i] = False
                if cp[i][0]+cam[0] > 0:
                    cpSigs[i] = cButton([(cp[i][0]+cam[0])*zoom,300-(cp[i][1]-cam[1])*zoom],4,(255,255,0),(255,255,128)).disp()
            epSig = False
            if ep[0]+cam[0] > 0:
                epSig = cButton([(ep[0]+cam[0])*zoom,300-(ep[1]-cam[1])*zoom],4,(255,0,0),(255,128,128)).disp()
            if drawMode == 1.04:
                if useIncrements:
                    samp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                    samp2 = [(samp[0]+cam[0])*zoom,300-(samp[1]-cam[1])*zoom]
                    bCirc(samp2,(255,255,0),1,4)
                else:
                    bCirc(mp,(255,255,0),1,4)
                    for j in range(4):
                        for i in range(len(linkPoints[j])):
                            for k in range(len(linkPoints[j][i])):
                                if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                    pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                    potLink = [j,i,k]
                                    canLink = True
                                    linkedPoint = 1
        elif drawMode >= 10.03 and drawMode < 11:
            for i in range(len(scl)):
                if edit:
                    vCurve(scl[i],5,10,(255,0,0), 0)
                else:
                    vCurve(scl[i],sampT,10,(0,0,0), 0)
                if viewMode == 2:
                    perpLine(scl[i],patchSideMode)
            spSig = False
            if (sp[0]+cam[0])*zoom > 0:
                spSig = cButton([(sp[0]+cam[0])*zoom,300-(sp[1]-cam[1])*zoom],4,(0,255,0),(128,255,128)).disp()
            for i in range(len(cp)):
                cpSigs[i] = False
                if (cp[i][0]+cam[0])*zoom > 0:
                    cpSigs[i] = cButton([(cp[i][0]+cam[0])*zoom,300-(cp[i][1]-cam[1])*zoom],4,(255,255,0),(255,255,128)).disp()
            epSig = False
            if (ep[0]+cam[0])*zoom > 0:
                epSig = cButton([(ep[0]+cam[0])*zoom,300-(ep[1]-cam[1])*zoom],4,(255,0,0),(255,128,128)).disp()
            if drawMode == 10.04:
                if useIncrements:
                    samp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                    samp2 = [(samp[0]+cam[0])*zoom,300-(samp[1]-cam[1])*zoom]
                    bCirc(samp2,(255,255,0),1,4)
                else:
                    bCirc(mp,(255,255,0),1,4)
                    for j in range(4):
                        for i in range(len(linkPoints[j])):
                            for k in range(len(linkPoints[j][i])):
                                if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                    pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                    potLink = [j,i,k]
                                    canLink = True
                                    linkedPoint = 1
        elif drawMode == 2.01:
            if edit:
                dispCurve(scPoints,(255,0,0),0)
            else:
                dispCurve(scPoints,(0,0,0),0)
            spSig = False
            if (sp[0]+cam[0])*zoom > 0:
                spSig = cButton([(sp[0]+cam[0])*zoom,300-(sp[1]-cam[1])*zoom],4,(0,255,0),(128,255,128)).disp()
        elif drawMode == 3:
            for i in range(len(translatedCurves)):
                vCurve(curves[translatedCurves[i][0]][translatedCurves[i][1]][translatedCurves[i][2]],10,100,(0,255,0), 0)
        elif drawMode == 7.01:
            for i in range(len(sWarpParam[1])):
                vCurve(curves[sWarpParam[1][i][0]][sWarpParam[1][i][1]][sWarpParam[1][i][2]],10,10,(0,255,0), 0)
        elif drawMode == 8.02:
            for i in range(len(dWarpParam[2])):
                vCurve(curves[dWarpParam[2][i][0]][dWarpParam[2][i][1]][dWarpParam[2][i][2]],10,100,(0,255,0), 0)
        elif drawMode == 9.04:
            for i in range(len(qWarpParam[4])):
                vCurve(curves[qWarpParam[4][i][0]][qWarpParam[4][i][1]][qWarpParam[4][i][2]],10,100,(0,255,0), 0)
        elif drawMode == 3.01 or drawMode == 3.02:
            for i in range(len(scl)):
                vCurve(scl[i],10,100,(255,0,0), 0)
        elif drawMode == 4.02 or drawMode == 5.02 or drawMode == 6.02 or drawMode == 11.02:
            if edit:
                dispCurve(scPoints,(255,0,0),0)
            else:
                dispCurve(scPoints,(0,0,0),0)
            if viewMode == 2:
                perpLine(sc,patchSideMode)
        elif drawMode == 3.03 or drawMode == 7.02 or drawMode == 8.03 or drawMode == 9.05:
            for i in range(len(scl)):
                if edit:
                    dispCurve(sclPoints[i],(255,0,0), 0)
                else:
                    dispCurve(sclPoints[i],(0,0,0), 0)
        elif drawMode == 11.01:
            vCurve(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],10,100,(0,255,0), 0)
            for i in range(len(bIntCurves)):
                vCurve(curves[bIntCurves[i][0]][bIntCurves[i][1]][bIntCurves[i][2]],10,100,(0,0,255), 0)
        dispText("zoom",[32.5,265],10,(0,0,0))
        for i in range(2):
            zoomSig[i] = zoomButtons[i].disp()
        dispText("editor level",[600-42.5,265],10,(0,0,0))
        if editorLevel > -1:
            dispText(str(editorLevel),[600-42.5,285],10,(0,0,0))
        else:
            dispText("all",[600-42.5,285],10,(0,0,0))
        for i in range(3):
            eLevelSig[i] = eLevelButtons[i].disp()
        dispText(str(round(zoom*100))+"%",[70,285],10,(0,0,0))
        if potMultiInt:
            pmibNotice.disp()
        pygame.draw.rect(screen, (128,128,128), (0,300,600,180))
        pygame.draw.line(screen, (0,0,0), (0,300), (600,300), 2)
        if drawMode == 0:
            if edit:
                for i in range(len(modeButtons)):
                    modeButtonSig[i] = modeButtons[i].disp()
                if editMode == 0:
                    dispText("select a curve to edit\npress z to cancel",[200,390],20,(0,0,0))
                else:
                    dispText("select a prism to edit\npress z to cancel",[200,390],20,(0,0,0))
                dispText("curve type",[430,325],20,(0,0,0))
            elif delete:
                for i in range(len(modeButtons)):
                    modeButtonSig[i] = modeButtons[i].disp()
                dispText("select a curve to delete\npress z to exit",[200,390],20,(0,0,0))
                dispText("curve type",[430,325],20,(0,0,0))
            elif copy:
                for i in range(len(modeButtons)):
                    modeButtonSig[i] = modeButtons[i].disp()
                dispText("select a curve to copy\npress z to exit",[200,390],20,(0,0,0))
                dispText("curve type",[430,325],20,(0,0,0))
            elif fillerMode == 1:
                for i in range(len(modeButtons)):
                    modeButtonSig[i] = modeButtons[i].disp()
                dispText("select curves to use as prism sides\npress c to continue\nwhen the prism is closed\npress z to exit",[200,390],20,(0,0,0))
                dispText("curve type",[430,325],20,(0,0,0))
            elif fillerMode == 2:
                if applyGrad:
                    dispText("select gradients to apply to the prism",[300,320],20,(0,0,0))
                    dispText("press z to exit",[300,460],20,(0,0,0))
                    for i in range(10):
                        gradSigs[i] = gradButtons[i].disp()
                        if i in sampleGradients:
                            dispText("selected",[100+(i%5)*100,390+int(i/5)*60],10,(0,0,0))
                else:
                    for i in range(len(fillerUtilButtons)):
                        fillerUtilButtonSig[i] = fillerUtilButtons[i].disp()
                        dispText(fillerUtilNames[i],[fillerUtilButtons[i].r[0],fillerUtilButtons[i].r[1]-20],10,(0,0,0))
                    finishFSig = finishButton.disp()
                    cancelFSig = cancelButton.disp()
                    for i in range(len(modeButtons)):
                        modeButtonSig[i] = modeButtons[i].disp()
                    dispText("view: "+modeNames[viewMode],[40,470],10,(0,0,0))
                    dispText("view mode",[430,325],20,(0,0,0))
                    dispText("fill mode",[120,370],15,(0,0,0))
                    fillerModeSig = fillerModeButton.disp()
                    applyGradSig = applyGradButton.disp()
                    gradString = "current: "
                    if len(sampleGradients) == 0:
                        gradString += "none"
                    else:
                        for i in range(len(sampleGradients)):
                            gradString += str(i)
                            if i < len(sampleGradients)-1:
                                gradString += ", "
                    dispText(gradString,[220,425],10,(0,0,0))
            elif presetMode == 1:
                for i in range(3):
                    configPresetSigs[i] = configPresetButtons[i].disp()
                dispText("press z to exit",[300,450],20,(0,0,0))
            elif presetMode == 2:
                dispText("select a curves for the preset\npress enter to continue\npress z to exit",[300,390],20,(0,0,0))
            elif presetMode == 3 or presetMode == 4:
                if presetMode == 3:
                    dispText("hover over a preset to view it, click to delete",[300,320],20,(0,0,0))
                else:
                    dispText("hover over a preset to view it",[300,320],20,(0,0,0))
                dispText("press z to exit",[300,460],20,(0,0,0))
                for i in range(10):
                    presetSigs[i] = presetButtons[i].disp()
                    if i < len(presets):
                        if presetSigs[i]:
                            if len(prevC) == 0:
                                prevC = [cam[0],cam[1]]
                            cam = [-presetCenters[i][0]+300/zoom,presetCenters[i][1]-150/zoom]
                if not True in presetSigs:
                    if len(prevC) > 0:
                        cam = [prevC[0],prevC[1]]
                        prevC = []
            elif customGearMode == 1:
                dispText("select a center for the custom gear",[300,390],20,(0,0,0))
                if useIncrements:
                    for i in range(4):
                        editIncSig[i] = editIncButtons[i].disp()
                    dispText("x",[200,425],15,(0,0,0))
                    dispText("y",[400,425],15,(0,0,0))
                    for i in range(2):
                        dispText("size",[175+200*i,465],10,(0,0,0))
                        dispText("offset",[225+200*i,465],10,(0,0,0))
            elif customGearMode == 2:
                for i in range(len(modeButtons)):
                    modeButtonSig[i] = modeButtons[i].disp()
                dispText("select curves/prisms to use\nas custom gear parts\npress enter to continue\npress z to exit",[200,390],20,(0,0,0))
                dispText("curve type",[430,325],20,(0,0,0))
                dispText("view: "+modeNames[viewMode],[40,470],10,(0,0,0))
            elif customGearMode == 3:
                dispText("gear type:",[120,315],10,(0,0,0))
                dispText("gear radius:",[240,315],10,(0,0,0))
                for i in range(7):
                    cgmSigs[i] = cgmButtons[i].disp()
                cgmBackSig = cgmBackButton.disp()
                if useIncrements:
                    for i in range(4):
                        editIncSig[i] = editIncButtons[i].disp()
                    dispText("x",[200,425],15,(0,0,0))
                    dispText("y",[400,425],15,(0,0,0))
                    for i in range(2):
                        dispText("size",[175+200*i,465],10,(0,0,0))
                        dispText("offset",[225+200*i,465],10,(0,0,0))
            elif gradientMode == 1:
                dispText("select a start value for the gradient",[300,390],20,(0,0,0))
                gradOrientSig = gradOrientButton.disp()
            elif gradientMode == 2:
                dispText("select a end value for the gradient",[300,390],20,(0,0,0))
                gradOrientSig = gradOrientButton.disp()
            elif gradientMode == 3:
                for i in range(len(gradManageButtons)):
                    gradManageSigs[i] = gradManageButtons[i].disp()
                for i in range(len(gradManageNames)):
                    dispText(gradManageNames[i],[120+120*i,325],15,(0,0,0))
            else:
                for i in range(len(drawButtons)):
                    drawButtonSig[i] = drawButtons[i].disp()
                dispText("view: "+modeNames[viewMode],[40,470],10,(0,0,0))
                for i in range(len(pManageButtons)):
                    pManageButtonSig[i] = pManageButtons[i].disp()
                if projectNum == -1:
                    dispText("new project",[560,470],10,(0,0,0))
                else:
                    dispText("project #"+str(projectNum+1),[560,470],10,(0,0,0))
                for i in range(len(defModeButtons)):
                    defModeButtonSig[i] = defModeButtons[i].disp()
                dispText("view type",[470,325],15,(0,0,0))
                mainPresetSig = mainPresetButton.disp()
                customGearSig = customGearButton.disp()
                gradientSig = gradientButton.disp()
            if gradientMode > 0:
                if useIncrements:
                    for i in range(4):
                        editIncSig[i] = editIncButtons[i].disp()
                    dispText("x",[200,425],15,(0,0,0))
                    dispText("y",[400,425],15,(0,0,0))
                    for i in range(2):
                        dispText("size",[175+200*i,465],10,(0,0,0))
                        dispText("offset",[225+200*i,465],10,(0,0,0))
        elif drawMode == 1.03 or drawMode == 2.01 or drawMode == 3.03 or drawMode == 4.02 or drawMode == 5.02 or drawMode == 6.02 or drawMode == 7.02 or drawMode == 8.03 or drawMode == 9.05 or drawMode == 10.03 or drawMode == 11.02:
            for i in range(len(utilButtons)):
                utilButtonSig[i] = utilButtons[i].disp()
                dispText(utilNames[i],[utilButtons[i].r[0],utilButtons[i].r[1]-20],10,(0,0,0))
            finishSig = finishButton.disp()
            cancelSig = cancelButton.disp()
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("curve type",[430,325],20,(0,0,0))
            dispText("view: "+modeNames[viewMode],[40,470],10,(0,0,0))
            if viewMode < 2:
                dispText("nodes",[511.25,340],15,(0,0,0))
                for i in range(3):
                    nodeManageSig[i] = nodeManageButtons[i].disp()
                    dispText(nodeNames[i],[511.25,372+i*35],10,(0,0,0))
                    if sampleNodes[i]:
                        pygame.draw.circle(screen, (0,0,0), [511.25,360+i*35], 4)
            elif viewMode == 2:
                dispText("direction",[(315+377.5)/2,365],10,(0,0,0))
                patchSideSig = patchSideButton.disp()
        elif drawMode == 3:
            if presetMode == 0:
                for i in range(len(modeButtons)):
                    modeButtonSig[i] = modeButtons[i].disp()
                dispText("select curves to translate\npress enter to continue\npress z to cancel",[200,375],20,(0,0,0))
                dispText("curve type",[430,325],20,(0,0,0))
                usePresetSig = usePresetButton.disp()
            else:
                dispText("hover over a preset to view it, click to select",[300,320],20,(0,0,0))
                dispText("press z to exit",[300,460],20,(0,0,0))
                for i in range(10):
                    presetSigs[i] = presetButtons[i].disp()
                    if i < len(presets):
                        if presetSigs[i]:
                            if len(prevC) == 0:
                                prevC = [cam[0],cam[1]]
                            cam = [-presetCenters[i][0]+300/zoom,presetCenters[i][1]-150/zoom]
                if not True in presetSigs:
                    if len(prevC) > 0:
                        cam = [prevC[0],prevC[1]]
                        prevC = []
        elif drawMode == 3.01 or drawMode == 3.02:
            for i in range(6):
                if i+translateParamPage*6 < len(translateSeqTyp):
                    translateProtoSig[i] = translateProtoButtons[i].disp()
                    translateButtons[i][0].t = translateNames[translateSeqTyp[i+translateParamPage*6]]
                    translateSig[i][0] = translateButtons[i][0].disp()
                    if translateSeqTyp[i+translateParamPage*6] == 0 or translateSeqTyp[i+translateParamPage*6] == 2:
                        translateButtons[i][1].r = (100+100*(i%3)-15,350+int(i/3)*80+12.5,30,25)
                        translateSig[i][2] = translateButtons[i][2].disp()
                        dispText("x",[100+100*(i%3)-15,350+int(i/3)*80+30],10,(0,0,0))
                        dispText("y",[100+100*(i%3)+15,350+int(i/3)*80+30],10,(0,0,0))
                    else:
                        translateButtons[i][1].r = (100+100*(i%3),350+int(i/3)*80+12.5,60,25)
                        dispText("degrees",[100+100*(i%3),350+int(i/3)*80+30],10,(0,0,0))
                    translateSig[i][1] = translateButtons[i][1].disp()
                else:
                    sampleButton = button((100+100*(i%3),350+int(i/3)*80,60,50), "---", 20, (0,0,0), (159,159,159),(191,191,191),(96,96,96),False)
                    sampleButton.disp()
            prevPageSig = prevParamButton.disp()
            nextPageSig = nextParamButton.disp()
            dispText("page "+str(translateParamPage+1)+" of "+str(int((len(translateSeqTyp)-1)/6)+1),[200,312],10,(0,0,0))
        elif drawMode == 4:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a curve to use as\nreference for x coordinates\npress z to cancel",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 4.01:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a curve to use as\nreference for y coordinates\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 5:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a base curve\npress z to cancel",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 5.01:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a curve's values to\nmap onto the base\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 6 or drawMode == 7:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a base curve\npress z to cancel",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 6.01:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a curve to\nmap onto the base\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 7.01:
            if presetMode == 0:
                for i in range(len(modeButtons)):
                    modeButtonSig[i] = modeButtons[i].disp()
                dispText("select a curve to\nmap onto the base\npress z to undo",[200,390],20,(0,0,0))
                dispText("curve type",[430,325],20,(0,0,0))
                usePresetSig = usePresetButton.disp()
            else:
                dispText("hover over a preset to view it, click to select",[300,320],20,(0,0,0))
                dispText("press z to exit",[300,460],20,(0,0,0))
                for i in range(10):
                    presetSigs[i] = presetButtons[i].disp()
                    if i < len(presets):
                        if presetSigs[i]:
                            if len(prevC) == 0:
                                prevC = [cam[0],cam[1]]
                            cam = [-presetCenters[i][0]+300/zoom,presetCenters[i][1]-150/zoom]
                if not True in presetSigs:
                    if len(prevC) > 0:
                        cam = [prevC[0],prevC[1]]
                        prevC = []
        elif drawMode == 8:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select the lower base curve\npress z to cancel",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 8.01:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select the upper base curve\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 8.02:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a curve to\nmap onto the bases\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 9:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select the southern axis\npress z to cancel",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 9.01:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select the northern axis\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 9.02:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select the western axis\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 9.03:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select the eastern axis\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 9.04:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select a curve to\nmap onto the axes\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 11:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select the main curve to\npress z to cancel",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        elif drawMode == 11.01:
            for i in range(len(modeButtons)):
                modeButtonSig[i] = modeButtons[i].disp()
            dispText("select one or two border curves\npress enter when done\npress z to undo",[200,390],20,(0,0,0))
            dispText("curve type",[430,325],20,(0,0,0))
        if drawMode == 1.03:
            for i in range(len(bezDrawButtons)):
                bezDrawButtonSig[i] = bezDrawButtons[i].disp()
        elif drawMode == 3.01:
            dispText("input the translation sequence\npress enter when done",[500,330],10,(0,0,0))
            addTranslateSig = addTranslateParamButton.disp()
            delTranslateSig = delTranslateParamButton.disp()
            continueSig = continueButton.disp()
        elif drawMode == 3.02:
            dispText("click on a translation\nparameter to delete it",[500,360],10,(0,0,0))
            backSig = backButton.disp()
        elif drawMode == 5.02:
            curveValSig = curveValTypeButton.disp()
            dispText("axis",[170,460],10,(0,0,0))
        elif drawMode == 10.03:
            for i in range(len(bezDrawButtons)):
                bezDrawButtonSig[i] = bezDrawButtons[i].disp()
            bspDegreeSig = bspDegreeButton.disp()
            bspModeSig = bspModeButton.disp()
            dispText("degree",[120,465],10,(0,0,0))
            dispText("end type",[220,465],10,(0,0,0))
        elif drawMode == 11.02:
            intSig1 = intButton1.disp()
            intSig2 = intButton2.disp()
            dispText("point number\n("+str(len(intP1))+" total)",[120,430],10,(0,0,0))
            if len(bIntCurves) == 1:
                dispText("end mode",[220,425],10,(0,0,0))
            else:
                dispText("point number\n("+str(len(intP2))+" total)",[220,430],10,(0,0,0))
        if useIncrements and (((drawMode >= 1 and drawMode <= 1.02) or drawMode == 1.04) or drawMode == 2 or ((drawMode >= 10 and drawMode <= 10.02) or drawMode == 10.04)):
            for i in range(4):
                editIncSig[i] = editIncButtons[i].disp()
            dispText("x",[200,425],15,(0,0,0))
            dispText("y",[400,425],15,(0,0,0))
            for i in range(2):
                dispText("size",[175+200*i,465],10,(0,0,0))
                dispText("offset",[225+200*i,465],10,(0,0,0))
        dispText(drawInst[int(drawMode)][round((drawMode%1)*100)],[300,390],20,(0,0,0))
    elif menu == "new_project_warning":
        pygame.draw.rect(screen, (191,191,191), (0,0,600,480))
        dispText("warning",[300,150],50,(0,0,0))
        dispText("a project is already in the works\ndo you want to keep it or scrap it",[300,250],30,(0,0,0))
        npwSig1 = npwButton1.disp()
        npwSig2 = npwButton2.disp()
    if scroll:
        cam[0] += c[0]/zoom
        cam[1] += c[1]/zoom
    if drag:
        if dragType[0] == 1:
            if useIncrements:
                sp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
            else:
                sp = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 3
            if int(drawMode) == 1:
                sc = bez(sp,cp,ep)
                scPoints = rendCurve(sc, sampT)
            elif int(drawMode) == 2:
                sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                scPoints = rendCurve(sc, sampT)
            elif int(drawMode) == 10:
                scl = []
                px = [sp[0]]
                py = [sp[1]]
                for j in range(len(cp)):
                    px.append(cp[j][0])
                    py.append(cp[j][1])
                px.append(ep[0])
                py.append(ep[1])
                scl = []
                sclPoints = []
                for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                    g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                    scl.append(g)
                    sclPoints.append(rendCurve(g,sampT))
        elif dragType[0] == 2:
            if useIncrements:
                cp[dragType[1]] = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
            else:
                cp[dragType[1]] = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 4
            if int(drawMode) == 1:
                sc = bez(sp,cp,ep)
                scPoints = rendCurve(sc, sampT)
            elif int(drawMode) == 10:
                scl = []
                px = [sp[0]]
                py = [sp[1]]
                for j in range(len(cp)):
                    px.append(cp[j][0])
                    py.append(cp[j][1])
                px.append(ep[0])
                py.append(ep[1])
                scl = []
                sclPoints = []
                for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                    g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                    scl.append(g)
                    sclPoints.append(rendCurve(g,sampT))
        elif dragType[0] == 3:
            if useIncrements:
                ep = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
            else:
                ep = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                for j in range(4):
                    for i in range(len(linkPoints[j])):
                        for k in range(len(linkPoints[j][i])):
                            if dis(mp[0]/zoom-cam[0],(300-mp[1])/zoom+cam[1],linkPoints[j][i][k][0],linkPoints[j][i][k][1]) < 10*zoom:
                                pygame.draw.circle(screen, (0,0,0), ((linkPoints[j][i][k][0]+cam[0])*zoom,300-(linkPoints[j][i][k][1]-cam[1])*zoom), 10*zoom, 1)
                                potLink = [j,i,k]
                                canLink = True
                                linkedPoint = 5
            if int(drawMode) == 1:
                sc = bez(sp,cp,ep)
                scPoints = rendCurve(sc, sampT)
            elif int(drawMode) == 10:
                scl = []
                px = [sp[0]]
                py = [sp[1]]
                for j in range(len(cp)):
                    px.append(cp[j][0])
                    py.append(cp[j][1])
                px.append(ep[0])
                py.append(ep[1])
                scl = []
                sclPoints = []
                for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                    g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                    scl.append(g)
                    sclPoints.append(rendCurve(g,sampT))
        elif dragType[0] == 4:
            if useIncrements:
                sampleGrad[dragType[1]] = round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1]
            else:
                sampleGrad[dragType[1]] = mp[0]/zoom-cam[0]
        elif dragType[0] == 5:
            if useIncrements:
                sampleGrad[dragType[1]] = round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]
            else:
                sampleGrad[dragType[1]] = ((300-mp[1])/zoom)+cam[1]
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if newProjectSig:
                newProjectSig = False
                contProjectButton.en = True
                usePresetButton.en = False
                if newProject:
                    menu = "editor"
                    newProject = False
                else:
                    menu = "new_project_warning"
            elif contProjectSig:
                contProjectSig = False
                menu = "editor"
            elif loadProjectSig:
                loadProjectSig = False
                menu = "load"
            elif loadLayoutSig:
                loadLayoutSig = False
                menu = "load_layout"
            elif True in projectSig:
                for i in range(len(projectSig)):
                    if projectSig[i]:
                        projectSig[i] = False
                        curveParam = loadableParam[i]
                        curvesUtil = loadableUtil[i]
                        curveNodes = loadableNodes[i]
                        zoom = loadableZooms[i]
                        cam = loadableCam[i]
                        prisms = loadablePris[i]
                        prismSig = []
                        for j in range(len(prisms)):
                            prismSig.append(False)
                        layoutObj = loadableObj[i]
                        patchSides = loadablePatchSides[i]
                        prismUtilVals = loadablePrisUtil[i]
                        curves = loadableProjCurves[i]
                        currObjStream = loadableObjStr[i]
                        exportObjCache = loadableExpCache[i]
                        editorLevel = loadableEL[i]
                        fillModes = loadableFillModes[i]
                        presets = loadablePresets[i]
                        if len(presets) == 0:
                            usePresetButton.en = False
                        dispPoints = loadableDispPoints[i]
                        prismDispPoints = loadablePrisDispPoints[i]
                        customGears = loadableCustomGears[i]
                        cgPos = loadableCgPos[i]
                        gradients = loadableGrad[i]
                        applyGradButton.en = len(gradients) > 0
                        presetCenters = []
                        if len(presets) > 0:
                            configPresetButtons[1].en = True
                            for j in range(len(presets)):
                                finalBox = curveBox(curves[3][presets[j][0][0]][presets[j][0][1]])
                                for k in range(1,len(presets[j])):
                                    sampBox = curveBox(curves[3][presets[j][k][0]][presets[j][k][1]])
                                    if sampBox[0][0] < finalBox[0][0]:
                                        finalBox[0][0] = sampBox[0][0]
                                    if sampBox[0][1] < finalBox[0][1]:
                                        finalBox[0][1] = sampBox[0][1]
                                    if sampBox[1][0] > finalBox[1][0]:
                                        finalBox[1][0] = sampBox[1][0]
                                    if sampBox[1][1] > finalBox[1][1]:
                                        finalBox[1][1] = sampBox[1][1]
                                presetCenters.append([(finalBox[0][0]+finalBox[1][0])/2, (finalBox[0][1]+finalBox[1][1])/2])
                        curveData = protoRender()
                        dCurves = curveData[0]
                        curveSig = curveData[1]
                        linkPoints = curveData[2]
                        ddCurves = curveData[3]
                        cBoxes = curveData[4]
                        rounded = curveData[5]
                        pBoxes = []
                        if len(prisms) > 0:
                            for j in range(len(prisms)):
                                finalBox = curveBox(curves[prisms[j][0][0]][prisms[j][0][1]][prisms[j][0][2]])
                                for k in range(1,len(prisms[j])):
                                    sampBox = curveBox(curves[prisms[j][k][0]][prisms[j][k][1]][prisms[j][k][2]])
                                    if sampBox[0][0] < finalBox[0][0]:
                                        finalBox[0][0] = sampBox[0][0]
                                    if sampBox[0][1] < finalBox[0][1]:
                                        finalBox[0][1] = sampBox[0][1]
                                    if sampBox[1][0] > finalBox[1][0]:
                                        finalBox[1][0] = sampBox[1][0]
                                    if sampBox[1][1] > finalBox[1][1]:
                                        finalBox[1][1] = sampBox[1][1]
                                pBoxes.append(finalBox)
                        for j in range(3):
                            isGearElement.append([])
                            for k in range(len(curves[j])):
                                isGearElement[j].append([])
                                for m in range(len(curves[j][k])):
                                    isGearElement[j][k].append(False)
                        for j in range(len(prisms)):
                            isGearElement[3].append(False)
                        for j in range(len(customGears)):
                            for k in range(3):
                                for m in range(len(customGears[j][k])):
                                    isGearElement[k][customGears[j][k][m][0]][customGears[j][k][m][1]] = True
                            for k in range(len(customGears[j][3])):
                                isGearElement[3][customGears[j][3][k]] = True
                        projectNum = i
                        menu = "editor"
            elif True in layoutSig:
                for i in range(len(layoutSig)):
                    if layoutSig[i]:
                        layoutSig[i] = False
                        layoutObj = finObj[i]
                        menu = "editor"
            elif npwSig1:
                npwSig1 = False
                menu = "editor"
            elif npwSig2:
                npwSig2 = False
                curves = [[],[],[],[]]
                curvesUtil = [[],[],[],[]]
                newProject = True
                menu = "editor"
            if menu == "editor":
                if mp[1] < 300:
                    if (drawMode >= 3.01 and drawMode < 4) or drawMode == 4.02 or drawMode == 5.02 or drawMode == 6.02 or drawMode == 7.02 or drawMode == 8.03 or drawMode == 9.05 or drawMode == 11.02:
                        scroll = True
                    elif drawMode == 0:
                        if edit or copy:
                            if True in curveSig[viewMode]:
                                for i in range(len(curveSig[viewMode])):
                                    if curveSig[viewMode][i]:
                                        curveSig[viewMode][i] = False
                                        editedCurve = [viewMode, i]
                                        if viewMode == 2:
                                            patchSideMode = patchSides[editedCurve[1]]
                                        sampleNodes = curveNodes[viewMode][i]
                                        if len(sampleNodes) == 0:
                                            sampleNodes = [True,True,True]
                                        if curveParam[viewMode][i][0] == 1:
                                            sp = [curveParam[viewMode][i][1][0],curveParam[viewMode][i][1][1]]
                                            cp = []
                                            cpSigs = []
                                            for j in range(len(curveParam[viewMode][i][2])):
                                                cp.append(curveParam[viewMode][i][2][j])
                                                cpSigs.append(False)
                                            ep = [curveParam[viewMode][i][3][0],curveParam[viewMode][i][3][1]]
                                            sc = bez(sp,cp,ep)
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[1]
                                            else:
                                                sampT = 5
                                            drawMode = 1.03
                                        elif curveParam[viewMode][i][0] == 2:
                                            sp = [curveParam[viewMode][i][1],curveParam[viewMode][i][2]]
                                            sc = spiral(sp[0],sp[1],curveParam[viewMode][i][3],curveParam[viewMode][i][4],curveParam[viewMode][i][5],curveParam[viewMode][i][6])
                                            coreUtil[curveParam[viewMode][i][0]-1] = [curveParam[viewMode][i][3],curveParam[viewMode][i][4],curveParam[viewMode][i][5],curveParam[viewMode][i][6]]
                                            utils = configUtil(curveParam[viewMode][i][0]-1)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[1]
                                            else:
                                                sampT = 5
                                            drawMode = 2.01
                                        elif curveParam[viewMode][i][0] == 3:
                                            translatedCurves = []
                                            for j in range(len(curveParam[viewMode][i][1])):
                                                translatedCurves.append(curveParam[viewMode][i][1][j])
                                            translateSeqTyp = []
                                            translateSeqVal = []
                                            for j in range(len(curveParam[viewMode][i][2])):
                                                translateSeqTyp.append(curveParam[viewMode][i][2][j])
                                                translateSeqVal.append(curveParam[viewMode][i][3][j])
                                            scl = []
                                            for j in range(len(translatedCurves)):
                                                scl.append(translateCurve(curves[translatedCurves[j][0]][translatedCurves[j][1]][translatedCurves[j][2]],translateSeqTyp,translateSeqVal))
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[1]
                                            else:
                                                sampT = 5
                                            drawMode = 3.03
                                        elif curveParam[viewMode][i][0] == 4:
                                            cCurveXVal = [curveParam[viewMode][i][1][0],curveParam[viewMode][i][1][1],curveParam[viewMode][i][1][2]]
                                            cCurveYVal = [curveParam[viewMode][i][2][0],curveParam[viewMode][i][2][1],curveParam[viewMode][i][2][2]]
                                            cCurveX = []
                                            cCurveX.append(curves[cCurveXVal[0]][cCurveXVal[1]][cCurveXVal[2]])
                                            cCurveY = []
                                            cCurveY.append(curves[cCurveYVal[0]][cCurveYVal[1]][cCurveYVal[2]])
                                            sc = compCurve(cCurveX[0],cCurveY[0])                                            
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[1]
                                            else:
                                                sampT = 5
                                            drawMode = 4.02
                                        elif curveParam[viewMode][i][0] == 5:
                                            wrapParam[0] = [curveParam[viewMode][i][1][0],curveParam[viewMode][i][1][1],curveParam[viewMode][i][1][2]]
                                            wrapParam[1] = [curveParam[viewMode][i][2][0],curveParam[viewMode][i][2][1],curveParam[viewMode][i][2][2],"x"]
                                            if curveParam[viewMode][i][1][1]:
                                                wrapParam[1][2] = "y"
                                            if wrapParam[1][2] == "y":
                                                sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[0][2]].y,curveParam[viewMode][i][3])
                                            else:
                                                sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].x,curveParam[viewMode][i][3])
                                            coreUtil[curveParam[viewMode][i][0]-1] = [curveParam[viewMode][i][3][0],curveParam[viewMode][i][3][1]]
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[3]
                                            else:
                                                sampT = 5
                                            drawMode = 5.02
                                        elif curveParam[viewMode][i][0] == 6:
                                            tangentParam = [curveParam[viewMode][i][1],curveParam[viewMode][i][3]]
                                            sc = tangent(curves[tangentParam[0][0]][tangentParam[0][1]][tangentParam[0][2]],curveParam[viewMode][i][2],curves[tangentParam[1][0]][tangentParam[1][1]][tangentParam[1][2]],curveParam[viewMode][i][4])
                                            coreUtil[curveParam[viewMode][i][0]-1] = [curveParam[viewMode][i][2],curveParam[viewMode][i][4]]
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[3]
                                            else:
                                                sampT = 5
                                            drawMode = 6.02
                                        elif curveParam[viewMode][i][0] == 7:
                                            sWarpParam[0] = curveParam[viewMode][i][1]
                                            sWarpParam[1] = curveParam[viewMode][i][2]
                                            scl = []
                                            for j in range(len(sWarpParam[1])):
                                                scl.append(singleWarp(curves[sWarpParam[0][0]][sWarpParam[0][1]][sWarpParam[0][2]],curves[sWarpParam[1][j][0]][sWarpParam[1][j][1]][sWarpParam[1][j][2]],curveParam[viewMode][i][3],curveParam[viewMode][i][4],[curveParam[viewMode][i][5],curveParam[viewMode][i][6]]))
                                            coreUtil[curveParam[viewMode][i][0]-1] = [curveParam[viewMode][i][3],curveParam[viewMode][i][4],curveParam[viewMode][i][5],curveParam[viewMode][i][6]]
                                            utils = configUtil(curveParam[viewMode][i][0]-1)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[5]
                                            else:
                                                sampT = 5
                                            drawMode = 7.02
                                        elif curveParam[viewMode][i][0] == 8:
                                            dWarpParam[0] = curveParam[viewMode][i][1]
                                            dWarpParam[1] = curveParam[viewMode][i][2]
                                            dWarpParam[2] = curveParam[viewMode][i][3]
                                            scl = []
                                            for j in range(len(dWarpParam[2])):
                                                scl.append(doubleWarp(curves[dWarpParam[0][0]][dWarpParam[0][1]][dWarpParam[0][2]],curves[dWarpParam[1][0]][dWarpParam[1][1]],curves[dWarpParam[2][j][0]][dWarpParam[2][j][1]][dWarpParam[2][j][2]],curveParam[viewMode][i][4],curveParam[viewMode][i][5],[curveParam[viewMode][i][6],curveParam[viewMode][i][7]]))
                                            coreUtil[i] = [curveParam[viewMode][i][3],curveParam[viewMode][i][4],curveParam[viewMode][i][5],curveParam[viewMode][i][6]]
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[5]
                                            else:
                                                sampT = 5
                                            drawMode = 8.03
                                        elif curveParam[viewMode][i][0] == 9:
                                            qWarpParam[0] = curveParam[viewMode][i][1]
                                            qWarpParam[1] = curveParam[viewMode][i][2]
                                            qWarpParam[2] = curveParam[viewMode][i][3]
                                            qWarpParam[3] = curveParam[viewMode][i][4]
                                            qWarpParam[4] = curveParam[viewMode][i][5]
                                            scl = []
                                            for j in range(len(qWarpParam[4])):
                                                scl.append(quadWarp(curves[qWarpParam[0][0]][qWarpParam[0][1]][qWarpParam[0][2]],curves[qWarpParam[1][0]][qWarpParam[1][1]][qWarpParam[1][2]],curves[qWarpParam[2][0]][qWarpParam[2][1]][qWarpParam[2][2]],curves[qWarpParam[3][0]][qWarpParam[3][1]][qWarpParam[3][2]],curves[qWarpParam[4][j][0]][qWarpParam[4][j][1]][qWarpParam[4][j][2]],curveParam[viewMode][i][6],curveParam[viewMode][i][7],[curveParam[viewMode][i][8],curveParam[viewMode][i][9]]))
                                            coreUtil[i] = [curveParam[viewMode][i][3],curveParam[viewMode][i][4],curveParam[viewMode][i][5],curveParam[viewMode][i][6]]
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[5]
                                            else:
                                                sampT = 5
                                            drawMode = 9.05
                                        elif curveParam[viewMode][i][0] == 10:
                                            sp = [curveParam[viewMode][i][1][0],curveParam[viewMode][i][1][1]]
                                            cp = []
                                            cpSigs = []
                                            for j in range(len(curveParam[viewMode][i][2])):
                                                cp.append(curveParam[viewMode][i][2][j])
                                                cpSigs.append(False)
                                            ep = [curveParam[viewMode][i][3][0],curveParam[viewMode][i][3][1]]
                                            px = [sp[0]]
                                            py = [sp[1]]
                                            for j in range(len(cp)):
                                                px.append(cp[j][0])
                                                py.append(cp[j][1])
                                            px.append(ep[0])
                                            py.append(ep[1])
                                            scl = []
                                            for j in range(len(px)+(curveParam[viewMode][i][4][0]-2)*(curveParam[viewMode][i][4][1] == 0)):
                                                g = para(full([[0,customLeg(px,curveParam[viewMode][i][4][0],j,curveParam[viewMode][i][4][1]),0,False]],[[0]]),full([[0,customLeg(py,curveParam[viewMode][i][4][0],j,curveParam[viewMode][i][4][1]),0,False]],[[0]]))
                                                scl.append(g)
                                            bspParam = curveParam[viewMode][i][4]
                                            bspDegreeButton = eButton((120,440,80,30), str(bspParam[0]), (159,159,159), (191,191,191), (223,223,223), 20, (0,0,0), False)
                                            if bspParam[1]:
                                                bspModeButton = button((220,440,80,30), "rounded", 15, (0,0,0), (159,159,159),(191,191,191),0,True)
                                            else:
                                                bspModeButton = button((220,440,80,30), "straight", 15, (0,0,0), (159,159,159),(191,191,191),0,True)
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[1]
                                            else:
                                                sampT = 5
                                            drawMode = 10.03
                                        elif curveParam[viewMode][i][0] == 11:
                                            mIntCurve = curveParam[viewMode][i][1]
                                            bIntCurves = curveParam[viewMode][i][2]
                                            intParam = curveParam[viewMode][i][3]
                                            if len(curveParam[viewMode][i][2]) == 1:
                                                intP = findInter(curves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],curves[curveParam[viewMode][i][2][0][0]][curveParam[viewMode][i][2][0][1]][curveParam[viewMode][i][2][0][2]],dCurves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],dCurves[curveParam[viewMode][i][2][0][0]][curveParam[viewMode][i][2][0][1]][curveParam[viewMode][i][2][0][2]])
                                                if curveParam[viewMode][i][3][1]:
                                                    sc = slicePara(curves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],[intP[curveParam[viewMode][i][3][0]][0],1])
                                                else:
                                                    sc = slicePara(curves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],[0,intP[curveParam[viewMode][i][3][0]][0]])
                                                if curveParam[viewMode][i][3][1] == 1:
                                                    intButton2 = button((220,400,80,30), "end", 20, (0,0,0), (159,159,159),(191,191,191),0,True)
                                                else:
                                                    intButton2 = button((220,400,80,30), "start", 20, (0,0,0), (159,159,159),(191,191,191),0,True)
                                            else:
                                                intP1 = findInter(curves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],curves[curveParam[viewMode][i][2][0][0]][curveParam[viewMode][i][2][0][1]][curveParam[viewMode][i][2][0][2]],dCurves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],dCurves[curveParam[viewMode][i][2][0][0]][curveParam[viewMode][i][2][0][1]][curveParam[viewMode][i][2][0][2]])
                                                intP2 = findInter(curves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],curves[curveParam[viewMode][i][2][1][0]][curveParam[viewMode][i][2][1][1]][curveParam[viewMode][i][2][1][2]],dCurves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],dCurves[curveParam[viewMode][i][2][1][0]][curveParam[viewMode][i][2][1][1]][curveParam[viewMode][i][2][1][2]])
                                                intButton2 = eButton((220,400,80,30), str(curveParam[viewMode][i][3][1]), (159,159,159), (191,191,191), (223,223,223), 20, (0,0,0), False)
                                                sc = slicePara(curves[curveParam[viewMode][i][1][0]][curveParam[viewMode][i][1][1]][curveParam[viewMode][i][1][2]],[intP1[curveParam[viewMode][i][3][0]][0],intP2[curveParam[viewMode][i][3][1]][0]])
                                            utils = configUtil(i)
                                            utilButtons = utils[0]
                                            utilButtonSig = utils[1]
                                            utilNames = utils[2]
                                            utilVals = utils[3]
                                            if viewMode < 2:
                                                sampT = utilVals[1]
                                            else:
                                                sampT = 5
                                            drawMode = 11.02
                                        if int(drawMode) == 1 or int(drawMode) == 2 or int(drawMode) == 4 or int(drawMode) == 5 or int(drawMode) == 6 or int(drawMode) == 11:
                                            scPoints = rendCurve(sc, sampT)
                                        else:
                                            sclPoints = []
                                            for j in range(len(scl)):
                                                sclPoints.append(rendCurve(scl[j],sampT))
                        elif delete:
                            if True in curveSig[viewMode]:
                                for i in range(len(curveSig[viewMode])-1,-1,-1):
                                    if curveSig[viewMode][i]:
                                        curveSig[viewMode][i] = False
                                        deleteables = dependWeb([viewMode, i], 1)
                                        deleteablePrisms = []
                                        for k in range(len(prisms)):
                                            deleteablePrisms.append(False)
                                        prismShift = []
                                        prismDec = 0
                                        for k in range(4):
                                            for m in range(len(deleteables[k])):
                                                if deleteables[k][m]:
                                                    for j in range(len(prisms)):
                                                        for n in range(len(prisms[j])):
                                                            if prisms[j][n][0] == k and prisms[j][n][1] == m:
                                                                deleteablePrisms[j] = True
                                                                prismDec += 1
                                                        prismShift.append(prismDec)
                                        for k in range(len(deleteablePrisms)-1,-1,-1):
                                            if deleteablePrisms[k]:
                                                prisms[k:k+1] = []
                                                isGearElement[3][k:k+1] = []
                                                exportObjCache[3][k:k+1] = []
                                                for m in range(len(customGears)):
                                                    for n in range(len(customGears[m][3])):
                                                        if customGears[m][3][n] == k:
                                                            customGears[m][3][n:n+1] = []
                                            else:
                                                for m in range(len(customGears)):
                                                    for n in range(len(customGears[m][3])):
                                                        if customGears[m][3][n] == k:
                                                            customGears[m][3][n] -= prismShift[k]
                                        grandShift = [[],[],[],[]]
                                        for j in range(4):
                                            count = 0
                                            decrem = 0
                                            for k in range(len(deleteables[j])):
                                                if deleteables[j][k]:
                                                    decrem += 1
                                                    grandShift[j].append(0)
                                                else:
                                                    grandShift[j].append(decrem)
                                                count += 1
                                        for j in range(4):
                                            for k in range(len(curveParam[j])):
                                                if curveParam[j][k][0] == 3:
                                                    for m in range(len(curveParam[j][k][1])):
                                                        curveParam[j][k][1][m][1] -= grandShift[curveParam[j][k][1][m][0]][curveParam[j][k][1][m][1]]
                                                elif curveParam[j][k][0] == 4:
                                                    curveParam[j][k][1][1] -= grandShift[curveParam[j][k][1][0]][curveParam[j][k][1][1]]
                                                    curveParam[j][k][2][1] -= grandShift[curveParam[j][k][2][0]][curveParam[j][k][2][1]]
                                                elif curveParam[j][k][0] == 5:
                                                    curveParam[j][k][1][1] -= grandShift[curveParam[j][k][1][0]][curveParam[j][k][1][1]]
                                                    curveParam[j][k][2][1] -= grandShift[curveParam[j][k][2][0]][curveParam[j][k][2][1]]
                                                elif curveParam[j][k][0] == 6:
                                                    curveParam[j][k][1][1] -= grandShift[curveParam[j][k][1][0]][curveParam[j][k][1][1]]
                                                    curveParam[j][k][3][1] -= grandShift[curveParam[j][k][3][0]][curveParam[j][k][3][1]]
                                                elif curveParam[j][k][0] == 7:
                                                    curveParam[j][k][1][1] -= grandShift[curveParam[j][k][1][0]][curveParam[j][k][1][1]]
                                                    for m in range(len(curveParam[j][k][2])):
                                                        curveParam[j][k][2][m][1] -= grandShift[curveParam[j][k][2][m][0]][curveParam[j][k][2][m][1]]
                                                elif curveParam[j][k][0] == 8:
                                                    curveParam[j][k][1][1] -= grandShift[curveParam[j][k][1][0]][curveParam[j][k][1][1]]
                                                    curveParam[j][k][2][1] -= grandShift[curveParam[j][k][2][0]][curveParam[j][k][2][1]]
                                                    for m in range(len(curveParam[j][k][3])):
                                                        curveParam[j][k][3][m][1] -= grandShift[curveParam[j][k][3][m][0]][curveParam[j][k][3][m][1]]
                                                elif curveParam[j][k][0] == 9:
                                                    curveParam[j][k][1][1] -= grandShift[curveParam[j][k][1][0]][curveParam[j][k][1][1]]
                                                    curveParam[j][k][2][1] -= grandShift[curveParam[j][k][2][0]][curveParam[j][k][2][1]]
                                                    curveParam[j][k][3][1] -= grandShift[curveParam[j][k][3][0]][curveParam[j][k][3][1]]
                                                    curveParam[j][k][4][1] -= grandShift[curveParam[j][k][4][0]][curveParam[j][k][4][1]]
                                                    for m in range(len(curveParam[j][k][5])):
                                                        curveParam[j][k][5][m][1] -= grandShift[curveParam[j][k][5][m][0]][curveParam[j][k][5][m][1]]
                                        for j in range(len(prisms)):
                                            for k in range(len(prisms[j])):
                                                if not grandShift[prisms[j][k][0]][prisms[j][k][1]] == None:
                                                    prisms[j][k][1] -= grandShift[prisms[j][k][0]][prisms[j][k][1]]
                                        for j in range(len(customGears)):
                                            for k in range(3):
                                                for m in range(len(customGears[j][k])-1,-1,-1):
                                                    customGears[j][k][m][0] -= grandShift[k][customGears[j][k][m][0]]
                                                    for n in range(len(deleteables[k])):
                                                        if deleteables[k][n]:
                                                            if customGears[j][k][m][0] == n:
                                                                customGears[j][k][m:m+1] = []
                                        for j in range(4):
                                            for k in range(len(curveParam[j])-1,-1,-1):
                                                if deleteables[j][k]:
                                                    curveParam[j][k:k+1] = []
                                                    curvesUtil[j][k:k+1] = []
                                                    curveNodes[j][k:k+1] = []
                                                    curves[j][k:k+1] = []
                                                    dCurves[j][k:k+1] = []
                                                    curveSig[j][k:k+1] = []
                                                    linkPoints[j][k:k+1] = []
                                                    ddCurves[j][k:k+1] = []
                                                    cBoxes[j][k:k+1] = []
                                                    dispPoints[j][k:k+1] = []
                                                    if j == 2:
                                                        patchSides[k:k+1] = []
                                                    if j < 3:
                                                        exportObjCache[j][k:k+1] = []
                                                        isGearElement[j][k:k+1] = []
                        elif fillerMode == 1:
                            if True in curveSig[viewMode]:
                                for i in range(len(curveSig[viewMode])):
                                    if curveSig[viewMode][i]:
                                        curveSig[viewMode][i] = False
                                        sub = -1
                                        for j in range(len(samplePrism)):
                                            if samplePrism[j][0] == viewMode and samplePrism[j][1] == i and samplePrism[j][2] == curveParamNum:
                                                sub = j
                                        if sub == -1:
                                            if len(samplePrism) == 0:
                                                samplePrism.append([viewMode,i,curveParamNum,False])
                                            else:
                                                prevP1 = curves[samplePrism[-1][0]][samplePrism[-1][1]][samplePrism[-1][2]].f(not samplePrism[-1][3])
                                                prevP2 = curves[samplePrism[-1][0]][samplePrism[-1][1]][samplePrism[-1][2]].f(samplePrism[-1][3])
                                                currP1 = curves[viewMode][i][curveParamNum].f(0)
                                                currP2 = curves[viewMode][i][curveParamNum].f(1)
                                                if qComp(prevP1[0],currP1[0]) and qComp(prevP1[1],currP1[1]):
                                                    samplePrism.append([viewMode,i,curveParamNum,False])
                                                elif qComp(prevP1[0],currP2[0]) and qComp(prevP1[1],currP2[1]):
                                                    samplePrism.append([viewMode,i,curveParamNum,True])
                                                elif qComp(prevP2[0],currP1[0]) and qComp(prevP2[1],currP1[1]):
                                                    samplePrism[-1][3] = True
                                                    samplePrism.append([viewMode,i,curveParamNum,False])
                                                elif qComp(prevP2[0],currP2[0]) and qComp(prevP2[1],currP2[1]):
                                                    samplePrism[-1][3] = True
                                                    samplePrism.append([viewMode,i,curveParamNum,True])
                                        else:
                                            samplePrism[sub:len(samplePrism)] = []
                            else:
                                scroll = True
                        elif presetMode == 2:
                            if True in curveSig[viewMode]:
                                for i in range(len(curveSig[viewMode])):
                                    if curveSig[viewMode][i]:
                                        curveSig[viewMode][i] = False
                                        sub = -1
                                        for j in range(len(samplePreset)):
                                            if samplePreset[j][0] == i and samplePreset[j][1] == curveParamNum:
                                                sub = j
                                        if sub == -1:
                                            samplePreset.append([i,curveParamNum])
                                        else:
                                            samplePreset[sub:sub+1] = []
                            else:
                                scroll = True
                        elif customGearMode == 2:
                            if True in curveSig[viewMode] and viewMode < 3:
                                for i in range(len(curveSig[viewMode])):
                                    if curveSig[viewMode][i]:
                                        curveSig[viewMode][i] = False
                                        sub = -1
                                        for j in range(len(sampleCustomGear[viewMode])):
                                            if sampleCustomGear[viewMode][j][0] == i and sampleCustomGear[viewMode][j][1] == curveParamNum:
                                                sub = j
                                        if sub == -1:
                                            sampleCustomGear[viewMode].append([i,curveParamNum])
                                        else:
                                            sampleCustomGear[viewMode][sub:sub+1] = []
                            else:
                                scroll = True
                        elif customGearMode == 1:
                            if useIncrements:
                                sampleCustomGear[4] = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                            else:
                                sampleCustomGear[4] = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                            customGearMode = 2
                        elif addCustomGears:
                            if useIncrements:
                                cgPos.append([round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1],customGearType])
                            else:
                                cgPos.append([mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1],customGearType])
                        elif deleteCustomGears:
                            for i in range(len(cgPos)-1,-1,-1):
                                gDist = dis(mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1],cgPos[i][0],cgPos[i][1])
                                if gDist < customGears[cgPos[i][2]][5]:
                                    cgPos[i:i+1] = []
                        elif gradientMode == 3:
                            if sampleGrad[2] == 0:
                                if abs(mp[0]-(sampleGrad[0]+cam[0])*zoom) < 15:
                                    drag = True
                                    dragType = [4,0]
                                elif abs(mp[0]-(sampleGrad[1]+cam[0])*zoom) < 15:
                                    drag = True
                                    dragType = [4,1]
                            else:
                                if abs(mp[1]-(300-(sampleGrad[0]-cam[1])*zoom)) < 15:
                                    drag = True
                                    dragType = [5,0]
                                elif abs(mp[1]-(300-(sampleGrad[1]-cam[1])*zoom)) < 15:
                                    drag = True
                                    dragType = [5,1]
                        else:
                            scroll = True
                    elif drawMode == 1:
                        if useIncrements:
                            sp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                        else:
                            sp = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                        drawMode = 1.01
                    elif drawMode == 1.01 or drawMode == 1.04:
                        if useIncrements:
                            cp.append([round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]])
                        else:
                            cp.append([(mp[0]/zoom)-cam[0],((300-mp[1])/zoom)+cam[1]])
                        if drawMode == 1.04:
                            cpSigs.append(False)
                            sc = bez(sp,cp,ep)
                            scPoints = rendCurve(sc, sampT)
                    elif drawMode == 1.02:
                        if useIncrements:
                            ep = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                        else:
                            ep = [(mp[0]/zoom)-cam[0],(300-mp[1])/zoom+cam[1]]
                        if viewMode > 1:
                            sampT = 5
                        else:
                            sampT = utilVals[1]
                        sc = bez(sp,cp,ep)
                        scPoints = rendCurve(sc, sampT)
                        for i in range(len(cp)):
                            cpSigs.append(False)
                        drawMode = 1.03
                    elif drawMode == 1.03:
                        if spSig:
                            drag = True
                            dragType = [1,0]
                        elif True in cpSigs:
                            drag = True
                            dragType[0] = 2
                            for i in range(len(cpSigs)):
                                if cpSigs[i]:
                                    dragType[1] = i
                        elif epSig:
                            drag = True
                            dragType = [3,0]
                        else:
                            scroll = True
                    elif drawMode == 1.05:
                        if True in cpSigs:
                            for i in range(len(cpSigs)):
                                if cpSigs[i]:
                                    sub = i
                            cp[sub:sub+1] = []
                            cpSigs[sub:sub+1] = []
                            sc = bez(sp,cp,ep)
                            scPoints = rendCurve(sc, sampT)
                        else:
                            scroll = True
                    elif drawMode == 2:
                        if useIncrements:
                            sp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                        else:
                            sp = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                        sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                        scPoints = rendCurve(sc, sampT)
                        if viewMode > 1:
                            sampT = 5
                        else:
                            sampT = utilVals[5]
                        drawMode = 2.01
                    elif drawMode == 2.01:
                        if spSig:
                            drag = True
                            dragType = [1,0]
                        else:
                            scroll = True
                    elif drawMode == 3:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    sub = -1
                                    for j in range(len(translatedCurves)):
                                        if translatedCurves[j][0] == viewMode and translatedCurves[j][1] == i and translatedCurves[j][2] == curveParamNum:
                                            sub = j
                                    if sub == -1:
                                        translatedCurves.append([viewMode,i,curveParamNum])
                                    else:
                                        translatedCurves[sub:sub+1] = []
                        else:
                            scroll = True
                    elif drawMode == 4:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    cCurveX.append(curves[viewMode][i][curveParamNum])
                                    cCurveXVal = [viewMode, i,curveParamNum]
                                    drawMode = 4.01
                        else:
                            scroll = True
                    elif drawMode == 4.01:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    cCurveY.append(curves[viewMode][i][curveParamNum])
                                    cCurveYVal = [viewMode, i,curveParamNum]
                                    sc = compCurve(cCurveX[0],cCurveY[0])
                                    scPoints = rendCurve(sc, sampT)
                                    drawMode = 4.02
                        else:
                            scroll = True
                    elif drawMode == 5:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    wrapParam[0] = [viewMode, i,curveParamNum]
                                    drawMode = 5.01
                        else:
                            scroll = True
                    elif drawMode == 5.01:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    wrapParam[1] = [viewMode, i,curveParamNum,"x"]
                                    sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].x,[1,0])
                                    scPoints = rendCurve(sc, sampT)
                                    drawMode = 5.02
                        else:
                            scroll = True
                    elif drawMode == 6:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    tangentParam[0] = [viewMode, i,curveParamNum]
                                    drawMode = 6.01
                        else:
                            scroll = True
                    elif drawMode == 6.01:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    tangentParam[1] = [viewMode, i,curveParamNum]
                                    sc = tangent(curves[tangentParam[0][0]][tangentParam[0][1]][tangentParam[0][2]],0,curves[tangentParam[1][0]][tangentParam[1][1]][tangentParam[1][2]],0)
                                    scPoints = rendCurve(sc, sampT)
                                    drawMode = 6.02
                        else:
                            scroll = True
                    elif drawMode == 7:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    sWarpParam[0] = [viewMode, i,curveParamNum]
                                    drawMode = 7.01
                        else:
                            scroll = True
                    elif drawMode == 7.01:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    sub = -1
                                    for j in range(len(sWarpParam[1])):
                                        if sWarpParam[1][j][0] == viewMode and sWarpParam[1][j][1] == i and sWarpParam[1][j][2] == curveParamNum:
                                            sub = j
                                    if sub == -1:
                                        sWarpParam[1].append([viewMode, i,curveParamNum])
                                    else:
                                        sWarpParam[1][sub:sub+1] = []
                        else:
                            scroll = True
                    elif drawMode == 8:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    dWarpParam[0] = [viewMode, i,curveParamNum]
                                    drawMode = 8.01
                        else:
                            scroll = True
                    elif drawMode == 8.01:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    dWarpParam[1] = [viewMode, i,curveParamNum]
                                    drawMode = 8.02
                        else:
                            scroll = True
                    elif drawMode == 8.02:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    dWarpParam[2].append([viewMode, i,curveParamNum])
                        else:
                            scroll = True
                    elif drawMode == 9:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    qWarpParam[0] = [viewMode, i,curveParamNum]
                                    drawMode = 9.01
                        else:
                            scroll = True
                    elif drawMode == 9.01:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    qWarpParam[1] = [viewMode, i,curveParamNum]
                                    drawMode = 9.02
                        else:
                            scroll = True
                    elif drawMode == 9.02:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    qWarpParam[2] = [viewMode, i,curveParamNum]
                                    drawMode = 9.03
                        else:
                            scroll = True
                    elif drawMode == 9.03:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    qWarpParam[3] = [viewMode, i,curveParamNum]
                                    drawMode = 9.04
                        else:
                            scroll = True
                    elif drawMode == 9.04:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    qWarpParam[4].append([viewMode, i,curveParamNum])
                        else:
                            scroll = True
                    elif drawMode == 10:
                        if useIncrements:
                            sp = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                        else:
                            sp = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                        drawMode = 10.01
                    elif drawMode == 10.01 or drawMode == 10.04:
                        if useIncrements:
                            cp.append([round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]])
                        else:
                            cp.append([mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]])
                        if drawMode == 10.04:
                            cpSigs.append(False)
                            px = [sp[0]]
                            py = [sp[1]]
                            for k in range(len(cp)):
                                px.append(cp[k][0])
                                py.append(cp[k][1])
                            px.append(ep[0])
                            py.append(ep[1])
                            scl = []
                            sclPoints = []
                            for k in range(len(px)+(bspParam[0]-2)*(not bspParam[1])):
                                g = para(full([[0,customLeg(px,bspParam[0],k,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],k,bspParam[1]),0,False]],[[0]]))
                                scl.append(g)
                                sclPoints.append(rendCurve(g,sampT))
                    elif drawMode == 10.02:
                        if useIncrements:
                            ep = [round((mp[0]/zoom-cam[0]+inc[0][1])/inc[0][0])*inc[0][0]-inc[0][1],round(((300-mp[1])/zoom+cam[1]+inc[1][1])/inc[1][0])*inc[1][0]-inc[1][1]]
                        else:
                            ep = [mp[0]/zoom-cam[0],((300-mp[1])/zoom)+cam[1]]
                        if viewMode > 1:
                            sampT = 5
                        else:
                            sampT = utilVals[1]
                        px = [sp[0]]
                        py = [sp[1]]
                        for j in range(len(cp)):
                            px.append(cp[j][0])
                            py.append(cp[j][1])
                        px.append(ep[0])
                        py.append(ep[1])
                        scl = []
                        sclPoints = []
                        for j in range(len(px)+1):
                            g = para(full([[0,customLeg(px,3,j,0),0,False]],[[0]]),full([[0,customLeg(py,3,j,0),0,False]],[[0]]))
                            scl.append(g)
                            sclPoints.append(rendCurve(g,sampT))
                        for i in range(len(cp)):
                            cpSigs.append(False)
                        drawMode = 10.03
                    elif drawMode == 10.03:
                        if spSig:
                            drag = True
                            dragType = [1,0]
                        elif True in cpSigs:
                            drag = True
                            dragType[0] = 2
                            for i in range(len(cpSigs)):
                                if cpSigs[i]:
                                    dragType[1] = i
                        elif epSig:
                            drag = True
                            dragType = [3,0]
                        else:
                            scroll = True
                    elif drawMode == 10.05:
                        if True in cpSigs:
                            for i in range(len(cpSigs)):
                                if cpSigs[i]:
                                    sub = i
                            cp[sub:sub+1] = []
                            cpSigs[sub:sub+1] = []
                            px = [sp[0]]
                            py = [sp[1]]
                            for j in range(len(cp)):
                                px.append(cp[j][0])
                                py.append(cp[j][1])
                            px.append(ep[0])
                            py.append(ep[1])
                            scl = []
                            sclPoints = []
                            for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                                g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                                scl.append(g)
                                sclPoints.append(rendCurve(g,sampT))
                        else:
                            scroll = True
                    elif drawMode == 11:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    mIntCurve = [viewMode, i,curveParamNum]
                                    drawMode = 11.01
                        else:
                            scroll = True
                    elif drawMode == 11.01:
                        if True in curveSig[viewMode]:
                            for i in range(len(curveSig[viewMode])):
                                if curveSig[viewMode][i]:
                                    curveSig[viewMode][i] = False
                                    if not (viewMode == mIntCurve[0] and i == mIntCurve[1] and curveParamNum == mIntCurve[2]):
                                        testInt = findInter(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],curves[viewMode][i][curveParamNum],dCurves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],dCurves[viewMode][i][curveParamNum])
                                        if len(testInt) > 0:
                                            bIntCurves.append([viewMode, i,curveParamNum])
                                            if len(testInt) >= 2:
                                                potMultiInt = True
                                        if len(bIntCurves) == 2:
                                            if bIntCurves[0][0] == bIntCurves[1][0] and bIntCurves[0][1] == bIntCurves[1][1] and bIntCurves[0][2] == bIntCurves[1][2]:
                                                bIntCurves = []
                                                potMultiInt = False
                                            else:
                                                intP1 = findInter(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],curves[bIntCurves[0][0]][bIntCurves[0][1]][bIntCurves[0][2]],dCurves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],dCurves[bIntCurves[0][0]][bIntCurves[0][1]][bIntCurves[0][2]])
                                                intP2 = findInter(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],curves[bIntCurves[1][0]][bIntCurves[1][1]][bIntCurves[1][2]],dCurves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],dCurves[bIntCurves[1][0]][bIntCurves[1][1]][bIntCurves[1][2]])
                                                sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[0][0],intP2[0][0]])
                                                scPoints = rendCurve(sc, sampT)
                                                intParam = [0,0]
                                                intButton2 = eButton((220,400,80,30), str(intParam[1]), (159,159,159), (191,191,191), (223,223,223), 20, (0,0,0), False)
                                                potMultiInt = False
                                                drawMode = 11.02
                        else:
                            scroll = True
                if True in drawButtonSig:
                    for i in range(len(drawButtons)):
                        if drawButtonSig[i]:
                            drawMode = i+1
                            utils = configUtil(i)
                            utilButtons = utils[0]
                            utilButtonSig = utils[1]
                            utilNames = utils[2]
                            utilVals = utils[3]
                            if viewMode < 2:
                                if i == 1 or i == 6 or i == 7 or i == 8:
                                    sampT = utilVals[5]
                                elif i == 4 or i == 5:
                                    sampT = utilVals[3]
                                else:
                                    sampT = utilVals[1]
                            else:
                                sampT = 5
                            drawButtonSig[i] = False
                elif True in utilButtonSig:
                    for i in range(len(utilButtonSig)):
                        if utilButtonSig[i]:
                            if not utilButtons[i].se:
                                utilButtons[i].se = True
                                selectedUtil = i
                            else:
                                utilButtons[i].se = False
                                selectedUtil = -1
                            utilButtonSig[i] = False
                        else:
                            utilButtons[i].se = False
                elif True in bezDrawButtonSig:
                    for i in range(len(utilButtons)):
                        utilButtons[i].se = False
                    for i in range(len(bezDrawButtonSig)):
                        if bezDrawButtonSig[i]:
                            if int(drawMode) == 1:
                                drawMode = 1.03+(i+1)/100
                            elif int(drawMode) == 10:
                                drawMode = 10.03+(i+1)/100
                            bezDrawButtonSig[i] = False
                elif finishSig:
                    if edit:
                        edit = False
                        if int(drawMode) == 2 or int(drawMode) == 7 or int(drawMode) == 8 or int(drawMode) == 9:
                            if viewMode < 2:
                                curvesUtil[editedCurve[0]][editedCurve[1]] = [utilVals[4],utilVals[5],utilVals[6],utilVals[7]]
                            else:
                                curvesUtil[editedCurve[0]][editedCurve[1]] = [utilVals[4]]
                        elif int(drawMode) == 5 or int(drawMode) == 6:
                            curvesUtil[editedCurve[0]][editedCurve[1]] = [utilVals[2],utilVals[3],utilVals[4],utilVals[5]]
                        else:
                            curvesUtil[editedCurve[0]][editedCurve[1]] = utilVals
                        curveNodes[editedCurve[0]][editedCurve[1]] = sampleNodes
                        if int(drawMode) == 1:
                            curveParam[editedCurve[0]][editedCurve[1]] = [1,sp,cp,ep]
                        elif int(drawMode) == 2:
                            curveParam[editedCurve[0]][editedCurve[1]] = [2,sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3]]
                        elif int(drawMode) == 3:
                            curveParam[editedCurve[0]][editedCurve[1]] = [3,translatedCurves,translateSeqTyp,translateSeqVal]
                        elif int(drawMode) == 4:
                            curveParam[editedCurve[0]][editedCurve[1]] = [4,cCurveXVal,cCurveYVal]
                        elif int(drawMode) == 5:
                            curveParam[editedCurve[0]][editedCurve[1]] = [5,wrapParam[0],[wrapParam[1][0],wrapParam[1][1],wrapParam[1][2],(wrapParam[1][3] == "y")],[utilVals[0],utilVals[1]]]
                        elif int(drawMode) == 6:
                            curveParam[editedCurve[0]][editedCurve[1]] = [6,tangentParam[0],utilVals[0],tangentParam[1],utilVals[1]]
                        elif int(drawMode) == 7:
                            curveParam[editedCurve[0]][editedCurve[1]] = [7,sWarpParam[0],sWarpParam[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3]]
                        elif int(drawMode) == 8:
                            curveParam[editedCurve[0]][editedCurve[1]] = [8,dWarpParam[0],dWarpParam[1],dWarpParam[2],utilVals[0],utilVals[1],utilVals[2],utilVals[3]]
                        elif int(drawMode) == 9:
                            curveParam[editedCurve[0]][editedCurve[1]] = [9,qWarpParam[0],qWarpParam[1],qWarpParam[2],qWarpParam[3],qWarpParam[4],utilVals[0],utilVals[1],utilVals[2],utilVals[3]]
                        elif int(drawMode) == 10:
                            curveParam[editedCurve[0]][editedCurve[1]] = [10,sp,cp,ep,bspParam]
                        elif int(drawMode) == 11:
                            curveParam[editedCurve[0]][editedCurve[1]] = [11,mIntCurve,bIntCurves,intParam]
                        if viewMode == 2:
                            patchSides[editedCurve[1]] = patchSideMode
                        partialRender(editedCurve)
                    else:
                        copy = False
                        curveNodes[viewMode].append(sampleNodes)
                        if int(drawMode) == 2 or int(drawMode) == 7 or int(drawMode) == 8 or int(drawMode) == 9:
                            if viewMode < 2:
                                curvesUtil[viewMode].append([utilVals[4],utilVals[5],utilVals[6],utilVals[7]])
                            else:
                                curvesUtil[viewMode].append([utilVals[4]])
                        elif int(drawMode) == 5 or int(drawMode) == 6:
                            if viewMode < 2:
                                curvesUtil[viewMode].append([utilVals[2],utilVals[3],utilVals[4],utilVals[5]])
                            elif viewMode == 2:
                                curvesUtil[viewMode].append([utilVals[2]])
                            else:
                                curvesUtil[viewMode].append([])
                        else:
                            curvesUtil[viewMode].append(utilVals)
                        if int(drawMode) == 1:
                            curveParam[viewMode].append([1,sp,cp,ep])
                        elif int(drawMode) == 2:
                            curveParam[viewMode].append([2,sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3]])
                        elif int(drawMode) == 3:
                            curveParam[viewMode].append([3,translatedCurves,translateSeqTyp,translateSeqVal])
                        elif int(drawMode) == 4:
                            curveParam[viewMode].append([4,cCurveXVal,cCurveYVal])
                        elif int(drawMode) == 5:
                            curveParam[viewMode].append([5,wrapParam[0],[wrapParam[1][0],wrapParam[1][1],wrapParam[1][2],(wrapParam[1][3] == "y")],[utilVals[0], utilVals[1]]])
                        elif int(drawMode) == 6:
                            curveParam[viewMode].append([6,tangentParam[0],utilVals[0],tangentParam[1],utilVals[1]])
                        elif int(drawMode) == 7:
                            curveParam[viewMode].append([7,sWarpParam[0],sWarpParam[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3]])
                        elif int(drawMode) == 8:
                            curveParam[viewMode].append([8,dWarpParam[0],dWarpParam[1],dWarpParam[2],utilVals[0],utilVals[1],utilVals[2],utilVals[3]])
                        elif int(drawMode) == 9:
                            curveParam[viewMode].append([9,qWarpParam[0],qWarpParam[1],qWarpParam[2],qWarpParam[3],qWarpParam[4],utilVals[0],utilVals[1],utilVals[2],utilVals[3]])
                        elif int(drawMode) == 10:
                            curveParam[viewMode].append([10,sp,cp,ep,bspParam])
                        elif int(drawMode) == 11:
                            curveParam[viewMode].append([11,mIntCurve,bIntCurves,intParam])
                        if viewMode == 2:
                            patchSides.append(patchSideMode)
                        addCurve(curveParam[viewMode][-1],viewMode)
                    cCurveX = []
                    cCurveY = []
                    prevUtil = []
                    for i in range(len(utilVals)):
                        prevUtil.append(utilVals[i])
                    finishSig = False
                    cp = []
                    bIntCurves = []
                    mIntCurve = []
                    intParam = [0,0]
                    intButton1.v = "0"
                    intButton2.v = "0"
                    for i in range(4):
                        for j in range(len(curveSig[i])):
                            curveSig[i][j] = False
                    if viewMode < 2:
                        if int(drawMode) == 2 or int(drawMode) == 7 or int(drawMode) == 8 or int(drawMode) == 9:
                            coreUtil[int(drawMode)-1] = []
                            for i in range(4):
                                coreUtil[int(drawMode)-1].append(utilVals[i])
                            primUtil = []
                            for i in range(3):
                                primUtil.append(utilVals[i+5])
                        elif int(drawMode) == 5 or int(drawMode) == 6:
                            coreUtil[int(drawMode)-1] = []
                            for i in range(2):
                                coreUtil[int(drawMode)-1].append(utilVals[i])
                            primUtil = []
                            for i in range(3):
                                primUtil.append(utilVals[i+3])
                        else:
                            primUtil = []
                            for i in range(3):
                                primUtil.append(utilVals[i+1])
                    presetMode = 0
                    drawMode = 0
                elif cancelSig:
                    cancelSig = False
                    cp = []
                    translateSeqTyp = [0]
                    translateSeqVal = [[50,50]]
                    edit = False
                    copy = False
                    mIntCurve = []
                    bIntCurves = []
                    intParam = [0,0]
                    intButton1.v = "0"
                    intButton2.v = "0"
                    tangentParam = [0,0]
                    sWarpParam = [0,[]]
                    dWarpParam = [0,0,[]]
                    qWarpParam = [0,0,0,0,[]]
                    for i in range(4):
                        for j in range(len(curveSig[i])):
                            curveSig[i][j] = False
                    drawMode = 0
                elif True in modeButtonSig:
                    for i in range(len(modeButtons)):
                        if modeButtonSig[i]:
                            modeButtonSig[i] = False
                            pview = viewMode
                            viewMode = i
                            if drawMode > 0:
                                utils = configUtil(int(drawMode)-1)
                                utilButtons = utils[0]
                                utilButtonSig = utils[1]
                                utilNames = utils[2]
                                utilVals = utils[3]
                                if len(prevUtil) == 0:
                                    if viewMode < 2:
                                        if int(drawMode) == 2 or int(drawMode) == 6 or int(drawMode) == 7 or int(drawMode) == 8:
                                            sampT = utilVals[5]
                                        elif int(drawMode) == 4 or int(drawMode) == 5:
                                            sampT = utilVals[3]
                                        else:
                                            sampT = utilVals[1]
                                    else:
                                        sampT = 5
                elif True in pManageButtonSig:
                    for i in range(len(pManageButtonSig)):
                        if pManageButtonSig[i]:
                            pManageButtonSig[i] = False
                            if i == 0:
                                save()
                                if projectNum == -1:
                                    test = load()
                                    projectNum = len(test[0])-1
                            elif i == 1:
                                menu = "main"
                            elif i == 2:
                                dCurves = [[],[],[],[]]
                                curveSig = [[],[],[],[]]
                                linkPoints = [[],[],[],[]]
                                ddCurves = [[],[],[],[]]
                                cBoxes = [[],[],[],[]]
                                rounded = [[],[]]
                                curves = [[],[],[],[]]
                                curvesUtil = [[],[],[],[]]
                                curveParam = [[],[],[],[]]
                                newProject = True
                                contProjectButton.en = False
                                deleteProject(projectNum)
                                loadData = load()
                                loadableParam = loadData[0]
                                loadableUtil = loadData[1]
                                loadableNodes = loadData[2]
                                loadableZooms = loadData[3]
                                loadableCam = loadData[4]
                                loadablePris = loadData[5]
                                loadableObjStr = loadData[6]
                                loadableObj = []
                                for j in range(len(loadableObjStr)):
                                    sub = compEnc64(loadableObjStr[j])
                                    sub2 = gzip.decompress(base64.urlsafe_b64decode(sub.encode('utf-8'))).decode()
                                    loadableObj.append(levelStringParse(sub2))
                                loadablePatchSides = loadData[7]
                                loadablePrisUtil = loadData[8]
                                loadableProjCurves = loadData[9]
                                loadableExpCache = loadData[10]
                                loadableEL = loadData[11]
                                loadableFillModes = loadData[12]
                                loadablePresets = loadData[13]
                                loadableDispPoints = loadData[14]
                                loadablePrisDispPoints = loadData[15]
                                loadableCustomGears = loadData[16]
                                loadableCgPos = loadData[17]
                                loadableGrad = loadData[18]
                                loadProjectButton.en = (len(loadableParam) > 0)
                                projectNum = -1
                                menu = "main"
                elif True in defModeButtonSig:
                    for i in range(len(defModeButtons)):
                        if defModeButtonSig[i]:
                            defModeButtonSig[i] = False
                            viewMode = i
                elif True in translateProtoSig:
                    if drawMode == 3.01:
                        selectedTranslationPara = [-1,0]
                        for i in range(len(translateProtoSig)):
                            translateButtons[i][1].se = False
                            translateButtons[i][2].se = False
                            if translateProtoSig[i]:
                                translateProtoSig[i] = False
                                if translateSig[i][0]:
                                    translateSeqTyp[i] += 1
                                    if translateSeqTyp[i] == 3:
                                        translateSeqTyp[i] = 0
                                    scl = []
                                    sclPoints = []
                                    for j in range(len(translatedCurves)):
                                        scl.append(translateCurve(curves[translatedCurves[j][0]][translatedCurves[j][1]][translatedCurves[j][2]],translateSeqTyp,translateSeqVal))
                                        sclPoints.append(rendCurve(scl[-1],sampT))
                                elif translateSig[i][1]:
                                    if translateButtons[i][1].se:
                                        translateButtons[i][1].se = False
                                    else:
                                        translateButtons[i][1].se = True
                                        selectedTranslationPara = [i,1]
                                elif translateSig[i][2]:
                                    if translateButtons[i][2].se:
                                        translateButtons[i][2].se = False
                                    else:
                                        translateButtons[i][2].se = True
                                        selectedTranslationPara = [i,2]
                    elif drawMode == 3.02:
                        for i in range(len(translateProtoSig)):
                            if translateProtoSig[i]:
                                translateProtoSig[i] = False
                                translateSeqTyp[i:i+1] = []
                                translateSeqVal[i:i+1] = []
                                if translateParamPage > int((len(translateSeqVal)-1)/6):
                                    translateParamPage = int((len(translateSeqVal)-1)/6)
                                    nextParamButton.en = False
                                if translateParamPage == 0:
                                    prevParamButton.en = False
                                reconfigTranslateParam()
                                scl = []
                                sclPoints = []
                                for j in range(len(translatedCurves)):
                                    scl.append(translateCurve(curves[translatedCurves[j][0]][translatedCurves[j][1]][translatedCurves[j][2]],translateSeqTyp,translateSeqVal))
                                    sclPoints.append(rendCurve(scl[-1],sampT))
                elif addTranslateSig:
                    addTranslateSig = False
                    translateSeqTyp.append(0)
                    translateSeqVal.append([50,50])
                    reconfigTranslateParam()
                    translateParamPage = int((len(translateSeqVal)-1)/6)
                    if len(translateSeqVal) > 6:
                        prevParamButton.en = True
                    scl = []
                    sclPoints = []
                    for j in range(len(translatedCurves)):
                        scl.append(translateCurve(curves[translatedCurves[j][0]][translatedCurves[j][1]][translatedCurves[j][2]],translateSeqTyp,translateSeqVal))
                        sclPoints.append(rendCurve(scl[-1],sampT))
                elif delTranslateSig:
                    delTranslateSig = False
                    translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].se = False
                    selectedTranslationPara = [-1,0]
                    drawMode = 3.02
                elif continueSig:
                    continueSig = False
                    drawMode = 3.03
                elif backSig:
                    backSig = False
                    drawMode = 3.01
                elif nextPageSig:
                    nextPageSig = False
                    reconfigTranslateParam()
                    translateParamPage += 1
                    prevParamButton.en = True
                    if translateParamPage == int((len(translateSeqVal)-1)/6):
                        nextParamButton.en = False
                elif prevPageSig:
                    prevPageSig = False
                    reconfigTranslateParam()
                    translateParamPage -= 1
                    nextParamButton.en = True
                    if translateParamPage == 0:
                        prevParamButton.en = False
                elif curveValSig:
                    curveValSig = False
                    if wrapParam[1][3] == "x":
                        wrapParam[1][3] = "y"
                        sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].y,[utilVals[0],utilVals[1]])
                        scPoints = rendCurve(sc, sampT)
                    else:
                        wrapParam[1][3] = "x"
                        sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].x,[utilVals[0],utilVals[1]])
                        scPoints = rendCurve(sc, sampT)
                    curveValTypeButton.t = wrapParam[1][3]
                elif bspModeSig:
                    bspModeSig = False
                    if bspParam[1] == 0:
                        bspParam[1] = 1
                        bspModeButton.t = "rounded"
                        px = [sp[0]]
                        py = [sp[1]]
                        for j in range(len(cp)):
                            px.append(cp[j][0])
                            py.append(cp[j][1])
                        px.append(ep[0])
                        py.append(ep[1])
                        scl = []
                        sclPoints = []
                        for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                            g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                            scl.append(g)
                            sclPoints.append(rendCurve(scl[-1],sampT))
                    else:
                        bspParam[1] = 0
                        bspModeButton.t = "straight"
                        px = [sp[0]]
                        py = [sp[1]]
                        for j in range(len(cp)):
                            px.append(cp[j][0])
                            py.append(cp[j][1])
                        px.append(ep[0])
                        py.append(ep[1])
                        scl = []
                        sclPoints = []
                        for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                            g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                            scl.append(g)
                            sclPoints.append(rendCurve(scl[-1],sampT))
                elif bspDegreeSig:
                    bspDegreeSig = False
                    if bspDegreeButton.se:
                        bspDegreeButton.se = False
                    else:
                        bspDegreeButton.se = True
                elif intSig1:
                    intSig1 = False
                    if intButton1.se:
                        intButton1.se = False
                    else:
                        intButton1.se = True
                elif intSig2:
                    intSig2 = False
                    if len(bIntCurves) == 1:
                        if intButton2.t == "start":
                            intButton2.t = "end"
                            intParam[1] = 1
                            sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[intParam[0]][0],1])
                            scPoints = rendCurve(sc, sampT)
                        else:
                            intButton2.t = "start"
                            intParam[1] = 0
                            sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[0,intP1[intParam[0]][0]])
                            scPoints = rendCurve(sc, sampT)
                    else:
                        if intButton2.se:
                            intButton2.se = False
                        else:
                            intButton2.se = True
                elif True in nodeManageSig:
                    for i in range(3):
                        if nodeManageSig[i]:
                            nodeManageSig[i] = False
                            if sampleNodes[i]:
                                sampleNodes[i] = False
                            else:
                                sampleNodes[i] = True
                elif True in editIncSig:
                    for i in range(4):
                        editIncButtons[i].se = False
                    for i in range(4):
                        if editIncSig[i]:
                            editIncSig[i] = False
                            if editIncButtons[i].se:
                                editIncButtons[i].se = False
                                selInc = -1
                            else:
                                editIncButtons[i].se = True
                                selInc = i
                elif True in fillerUtilButtonSig:
                    for i in range(len(fillerUtilButtonSig)):
                        if fillerUtilButtonSig[i]:
                            if not fillerUtilButtons[i].se:
                                fillerUtilButtons[i].se = True
                                selectedFUtil = i
                            else:
                                fillerUtilButtons[i].se = False
                                selectedFUtil = -1
                            fillerUtilButtonSig[i] = False
                        else:
                            fillerUtilButtons[i].se = False
                elif finishFSig:
                    finishFSig = False
                    sub = []
                    for i in range(len(fillerUtilVals)):
                        sub.append(fillerUtilVals[i])
                    sub.append(sampleGradients)
                    if edit:
                        prismUtilVals[editedPrism] = sub
                        if not fillModes[editedPrism] == fillMode:
                            exportObjCache[3][editedPrism] = createElementObjects(3,samplePrism,fillerUtilVals,fillMode,0)
                        fillModes[editedPrism] = fillMode
                        edit = False
                        editMode = 0
                    else:
                        prisms.append(samplePrism)
                        isGearElement[3].append(False)
                        prismUtilVals.append(sub)
                        fillModes.append(fillMode)
                        exportObjCache[3].append(createElementObjects(3,samplePrism,fillerUtilVals,fillMode,0))
                        prismSig.append(False)
                        prismDispPoints.append(samplePrismDisp)
                        finalBox = curveBox(curves[samplePrism[0][0]][samplePrism[0][1]][samplePrism[0][2]])
                        for k in range(1,len(samplePrism)):
                            sampBox = curveBox(curves[samplePrism[k][0]][samplePrism[k][1]][samplePrism[k][2]])
                            if sampBox[0][0] < finalBox[0][0]:
                                finalBox[0][0] = sampBox[0][0]
                            if sampBox[0][1] < finalBox[0][1]:
                                finalBox[0][1] = sampBox[0][1]
                            if sampBox[1][0] > finalBox[1][0]:
                                finalBox[1][0] = sampBox[1][0]
                            if sampBox[1][1] > finalBox[1][1]:
                                finalBox[1][1] = sampBox[1][1]
                        pBoxes.append(finalBox)
                        cList = []
                        dList = []
                        for k in range(len(samplePrism)):
                            cList.append(curves[samplePrism[k][0]][samplePrism[k][1]][samplePrism[k][2]])
                            dList.append(dCurves[samplePrism[k][0]][samplePrism[k][1]][samplePrism[k][2]])
                        prismCenters.append(cent(cList,dList))
                        samplePrism = []
                    selectedFUtil = -1
                    for i in range(4):
                        for j in range(len(curveSig[i])):
                            curveSig[i][j] = False
                    fillerMode = 0
                elif cancelFSig:
                    samplePrism = []
                    cancelFSig = False
                    fillerMode = 0
                elif patchSideSig:
                    patchSideSig = False
                    if patchSideMode == 0:
                        patchSideButton.t = "west"
                        patchSideMode = 1
                    elif patchSideMode == 1:
                        patchSideButton.t = "both"
                        patchSideMode = 2
                    elif patchSideMode == 2:
                        patchSideButton.t = "east"
                        patchSideMode = 0
                elif True in prismSig:
                    for i in range(len(prisms)):
                        if prismSig[i]:
                            prismSig[i] = False
                            if edit:
                                fillerUtilVals = prismUtilVals[i]
                                for j in range(3):
                                    fillerUtilButtons[j].v = str(fillerUtilVals[j])
                                samplePrism = prisms[i]
                                editedPrism = i
                                fillerMode = 2
                            else:
                                if customGearMode == 2 and viewMode == 3:
                                    sub = -1
                                    for j in range(len(sampleCustomGear[3])):
                                        if i == sampleCustomGear[3][j]:
                                            sub = j
                                    if sub == -1:
                                        sampleCustomGear[3].append(i)
                                    else:
                                        sampleCustomGear[3][sub:sub+1] = []
                elif True in eLevelSig:
                    for i in range(3):
                        if eLevelSig[i]:
                            eLevelSig[i] = False
                            if i == 0:
                                eLevelButtons[1].en = True
                                editorLevel += 1
                                if editorLevel == 255:
                                    eLevelButtons[i].en = False
                            elif i == 1:
                                eLevelButtons[0].en = True
                                editorLevel -= 1
                                if editorLevel == -1:
                                    eLevelButtons[i].en = False
                            else:
                                editorLevel = -1
                                eLevelButtons[1].en = False
                elif True in zoomSig:
                    for i in range(2):
                        if zoomSig[i]:
                            zoomSig[i] = False
                            if i == 0:
                                zoomButtons[1].en = True
                                zoom -= 0.1
                                if round(zoom,2) == 0.5:
                                    zoomButtons[i].en = False
                            else:
                                zoomButtons[0].en = True
                                zoom += 0.1
                                if round(zoom,2) == 2.5:
                                    zoomButtons[i].en = False
                elif True in configPresetSigs:
                    for i in range(3):
                        if configPresetSigs[i]:
                            configPresetSigs[i] = False
                            if i == 0:
                                viewMode = 3
                                presetMode = 2
                            elif i == 1 or i == 2:
                                presetButtons = []
                                presetSigs = []
                                prevC = [cam[0],cam[1]]
                                for j in range(10):
                                    if j < len(presets):
                                        presetButtons.append(button((100+(j%5)*100,360+int(j/5)*60,80,40), "preset "+str(j+1), 15, (0,0,0), (159,159,159), (191,191,191), (64,64,64), True))
                                    else:
                                        presetButtons.append(button((100+(j%5)*100,360+int(j/5)*60,80,40), "---", 15, (0,0,0), (159,159,159), (191,191,191), (64,64,64), False))
                                    presetSigs.append(False)
                                if i == 2:
                                    presetMode = 3
                                elif i == 1:
                                    presetMode = 4
                elif True in presetSigs:
                    for i in range(10):
                        if presetSigs[i]:
                            if presetMode == 3:
                                presetSigs[i] = False
                                presetButtons = []
                                presetSigs = []
                                presets[i:i+1] = []
                                for j in range(10):
                                    if j < len(presets):
                                        presetButtons.append(button((100+(j%5)*100,360+int(j/5)*60,80,40), "preset "+str(i+1), 15, (0,0,0), (159,159,159), (191,191,191), (64,64,64), True))
                                    else:
                                        presetButtons.append(button((100+(j%5)*100,360+int(j/5)*60,80,40), "---", 15, (0,0,0), (159,159,159), (191,191,191), (64,64,64), False))
                                    presetSigs.append(False)
                                if len(presets) == 0:
                                    presetMode = 1
                                    configPresetButtons[1].en = False
                                    usePresetButton.en = False
                                    cam = [prevC[0],prevC[1]]
                                    prevC = []
                            elif presetMode == 5:
                                presetSigs[i] = False
                                sampT = 5
                                if drawMode == 3:
                                    translatedCurves = []
                                    for j in range(len(presets[i])):
                                        translatedCurves.append([3,presets[i][j][0],presets[i][j][1]])
                                    scl = []
                                    sclPoints = []
                                    for j in range(len(translatedCurves)):
                                        scl.append(translateCurve(curves[translatedCurves[j][0]][translatedCurves[j][1]][translatedCurves[j][2]],translateSeqTyp,translateSeqVal))
                                        sclPoints.append(rendCurve(scl[-1],sampT))
                                    utils = configUtil(int(drawMode)-1)
                                    utilButtons = utils[0]
                                    utilButtonSig = utils[1]
                                    utilNames = utils[2]
                                    utilVals = utils[3]
                                    drawMode = 3.01
                                elif drawMode == 7.01:
                                    sWarpParam[1] = []
                                    for j in range(len(presets[i])):
                                        sWarpParam[1].append([3,presets[i][j][0],presets[i][j][1]])
                                    scl = []
                                    sclPoints = []
                                    for j in range(len(sWarpParam[1])):
                                        scl.append(singleWarp(curves[sWarpParam[0][0]][sWarpParam[0][1]][sWarpParam[0][2]],curves[sWarpParam[1][j][0]][sWarpParam[1][j][1]][sWarpParam[1][j][2]],100,100,[0,0]))
                                        sclPoints.append(rendCurve(scl[-1],sampT))
                                    utils = configUtil(int(drawMode)-1)
                                    utilButtons = utils[0]
                                    utilButtonSig = utils[1]
                                    utilNames = utils[2]
                                    utilVals = utils[3]
                                    drawMode = 7.02
                                cam = [prevC[0],prevC[1]]
                                presetMode = 0
                elif fillerModeSig:
                    fillerModeSig = False
                    if fillMode == 0:
                        fillerModeButton.t = "anti"
                        fillMode = 1
                    elif fillMode == 1:
                        fillerModeButton.t = "normal"
                        fillMode = 0
                elif applyGradSig:
                    applyGradSig = False
                    applyGrad = True
                    gradButtons = []
                    gradSigs = []
                    for i in range(10):
                        if i < len(gradients):
                            gradButtons.append(button((100+(i%5)*100,360+int(i/5)*60,80,40), str(i), 20, (0,0,0), (159,159,159), (191,191,191), (64,64,64), True))
                        else:
                            gradButtons.append(button((100+(i%5)*100,360+int(i/5)*60,80,40), "---", 20, (0,0,0), (159,159,159), (191,191,191), (64,64,64), False))
                        gradSigs.append(False)
                elif mainPresetSig:
                    mainPresetSig = False
                    pview = viewMode
                    viewMode = 3
                    presetMode = 1
                elif usePresetSig:
                    usePresetSig = False
                    viewMode = 3
                    presetButtons = []
                    presetSigs = []
                    prevC = [cam[0],cam[1]]
                    for j in range(10):
                        if j < len(presets):
                            presetButtons.append(button((100+(j%5)*100,360+int(j/5)*60,80,40), "preset "+str(j+1), 15, (0,0,0), (159,159,159), (191,191,191), (64,64,64), True))
                        else:
                            presetButtons.append(button((100+(j%5)*100,360+int(j/5)*60,80,40), "---", 15, (0,0,0), (159,159,159), (191,191,191), (64,64,64), False))
                        presetSigs.append(False)
                    presetMode = 5
                elif customGearSig:
                    customGearSig = False
                    if len(customGears) == 0:
                        modeButtons[3].t = "prisms"
                        modeNames[3] = "prisms"
                        customGearMode = 1
                    else:
                        customGearMode = 3
                elif True in cgmSigs:
                    for i in range(7):
                        if cgmSigs[i]:
                            cgmSigs[i] = False
                            if i == 0 or i == 1:
                                if cgmButtons[i].se:
                                    cgmButtons[i].se = False
                                else:
                                    cgmButtons[i].se = True
                                if i == 0:
                                    cgmButtons[1].se = False
                                    cgmButtons[1].v = str(customGears[customGearType][5])
                                    if cgmButtons[i].se == False:
                                        cgmButtons[i].v = str(customGearType)
                                else:
                                    cgmButtons[0].se = False
                                    cgmButtons[0].v = str(customGearType)
                                    if cgmButtons[i].se == False:
                                        cgmButtons[i].v = str(customGears[customGearType][5])
                            elif i == 2:
                                sampleCustomGear = customGears[customGearType]
                                editedCustomGear = customGearType
                                customGearMode = 2
                            elif i == 3:
                                deleteCustomGears = False
                                cgmButtons[4].se = False
                                if addCustomGears:
                                    addCustomGears = False
                                else:
                                    addCustomGears = True
                                cgmButtons[3].se = addCustomGears
                            elif i == 4:
                                addCustomGears = False
                                cgmButtons[3].se = False
                                if deleteCustomGears:
                                    deleteCustomGears = False
                                else:
                                    deleteCustomGears = True
                                cgmButtons[4].se = deleteCustomGears
                            elif i == 5:
                                sampleCustomGear = [[],[],[],[],[],50]
                                customGearMode = 1
                elif cgmBackSig:
                    cgmBackSig = False
                    for i in range(3):
                        for j in range(len(curves[i])):
                            for k in range(len(curves[i][j])):
                                isGearElement[i][j][k] = False
                    for i in range(len(prisms)):
                        isGearElement[3][i] = False
                    for i in range(len(customGears)):
                        for j in range(3):
                            for k in range(len(customGears[i][j])):
                                isGearElement[j][customGears[i][j][k][0]][customGears[i][j][k][1]] = True
                        for j in range(len(customGears[i][3])):
                            isGearElement[3][customGears[i][3][j]] = True
                    deleteCustomGears = False
                    customGearMode = 0
                elif gradientSig:
                    gradientSig = False
                    gradientMode = 1
                elif gradOrientSig:
                    gradOrientSig = False
                    gradientMode = 1
                    if sampleGrad[2] == 0:
                        sampleGrad[2] = 1
                        gradOrientButton.t = "vertical"
                    else:
                        sampleGrad[2] = 0
                        gradOrientButton.t = "horizontal"
                elif True in gradManageSigs:
                    for i in range(len(gradManageSigs)):
                        if gradManageSigs[i]:
                            gradManageSigs[i] = False
                            if i == 0 or i == 1:
                                if gradManageButtons[i].se:
                                    gradManageButtons[i].se = False
                                else:
                                    gradManageButtons[i].se = True
                            elif i == 2:
                                if sampleGrad[3] == 0:
                                    sampleGrad[3] = 1
                                    gradManageButtons[2].t = "saturation"
                                    if sampleGrad[4] < 0:
                                        sampleGrad[4] = 0
                                        gradManageButtons[0].v = str(0)
                                    if sampleGrad[5] > 1:
                                        sampleGrad[5] = 1
                                        gradManageButtons[1].v = str(1)
                                elif sampleGrad[3] == 1:
                                    sampleGrad[3] = 2
                                    gradManageButtons[2].t = "brightness"
                                    if sampleGrad[4] < 0:
                                        sampleGrad[4] = 0
                                        gradManageButtons[0].v = str(0)
                                    if sampleGrad[5] > 1:
                                        sampleGrad[5] = 1
                                        gradManageButtons[1].v = str(1)
                                elif sampleGrad[3] == 2:
                                    sampleGrad[3] = 0
                                    gradManageButtons[2].t = "hue"
                            elif i == 3:
                                sub = []
                                for i in range(len(sampleGrad)):
                                    sub.append(sampleGrad[i])
                                gradients.append(sub)
                                if len(gradients) > 0:
                                    applyGradButton.en = True
                                gradientMode = 0
                elif True in gradSigs:
                    for i in range(10):
                        if gradSigs[i]:
                            gradSigs[i] = False
                            sub = -1
                            for j in range(len(sampleGradients)):
                                if sampleGradients[j] == i:
                                    sub = j
                            if sub == -1:
                                sampleGradients.append(i)
                            else:
                                sampleGradients[sub:sub+1] = []
        if event.type == MOUSEBUTTONUP:
            if scroll:
                scroll = False
            if drag:
                drag = False
        if event.type == KEYDOWN:
            if event.key == 108:
                if canLink:
                    if linkedPoint == 0:
                        sp = linkPoints[potLink[0]][potLink[1]][potLink[2]]
                        drawMode += 0.01
                    elif linkedPoint == 1:
                        cp.append(linkPoints[potLink[0]][potLink[1]][potLink[2]])
                    elif linkedPoint == 2:
                        ep = linkPoints[potLink[0]][potLink[1]][potLink[2]]
                        if int(drawMode) == 1:
                            if viewMode > 1:
                                sampT = 10
                            else:
                                sampT = utilVals[1]
                            sc = bez(sp,cp,ep)
                            scPoints = rendCurve(sc, sampT)
                            for i in range(len(cp)):
                                cpSigs.append(False)
                            drawMode = 1.03
                        elif int(drawMode) == 2:
                            sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                            if viewMode > 1:
                                sampT = 10
                            else:
                                sampT = utilVals[5]
                            scPoints = rendCurve(sc, sampT)
                            drawMode = 2.01
                        elif int(drawMode) == 10:
                            if viewMode > 1:
                                sampT = 10
                            else:
                                sampT = utilVals[1]
                            px = [sp[0]]
                            py = [sp[1]]
                            for j in range(len(cp)):
                                px.append(cp[j][0])
                                py.append(cp[j][1])
                            px.append(ep[0])
                            py.append(ep[1])
                            scl = []
                            sclPoints = []
                            for j in range(len(px)+1):
                                g = para(full([[0,customLeg(px,3,j,0),0,False]],[[0]]),full([[0,customLeg(py,3,j,0),0,False]],[[0]]))
                                scl.append(g)
                                sclPoints.append(rendCurve(scl[-1],sampT))
                            for i in range(len(cp)):
                                cpSigs.append(False)
                            drawMode = 10.03
                    elif linkedPoint == 3:
                        sp = linkPoints[potLink[0]][potLink[1]][potLink[2]]
                        if int(drawMode) == 1:
                            sc = bez(sp,cp,ep)
                            scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 2:
                            sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                            scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 10:
                            px = [sp[0]]
                            py = [sp[1]]
                            for j in range(len(cp)):
                                px.append(cp[j][0])
                                py.append(cp[j][1])
                            px.append(ep[0])
                            py.append(ep[1])
                            scl = []
                            sclPoints = []
                            for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                                g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                                scl.append(g)
                                sclPoints.append(rendCurve(scl[-1],sampT))
                        drag = False
                    elif linkedPoint == 4:
                        cp[dragType[1]] = linkPoints[potLink[0]][potLink[1]][potLink[2]]
                        if int(drawMode) == 1:
                            sc = bez(sp,cp,ep)
                            scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 2:
                            sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                            scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 10:
                            px = [sp[0]]
                            py = [sp[1]]
                            for j in range(len(cp)):
                                px.append(cp[j][0])
                                py.append(cp[j][1])
                            px.append(ep[0])
                            py.append(ep[1])
                            scl = []
                            sclPoints = []
                            for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                                g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                                scl.append(g)
                                sclPoints.append(rendCurve(scl[-1],sampT))
                        drag = False
                    elif linkedPoint == 5:
                        ep = linkPoints[potLink[0]][potLink[1]][potLink[2]]
                        if int(drawMode) == 1:
                            sc = bez(sp,cp,ep)
                            scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 2:
                            sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                            scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 10:
                            px = [sp[0]]
                            py = [sp[1]]
                            for j in range(len(cp)):
                                px.append(cp[j][0])
                                py.append(cp[j][1])
                            px.append(ep[0])
                            py.append(ep[1])
                            scl = []
                            sclPoints = []
                            for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                                g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                                scl.append(g)
                                sclPoints.append(rendCurve(scl[-1],sampT))
                        drag = False
            if event.key == 102:
                if fillerMode == 0 and drawMode == 0:
                    for i in range(len(drawButtonSig)):
                        drawButtonSig[i] = False
                    fillerMode = 1
            if event.key == 99:
                if fillerMode == 1:
                    startP = curves[samplePrism[0][0]][samplePrism[0][1]][samplePrism[0][2]].f(samplePrism[0][3])
                    endP = curves[samplePrism[-1][0]][samplePrism[-1][1]][samplePrism[-1][2]].f(not samplePrism[-1][3])
                    if not (qComp(startP[0],endP[0]) and qComp(startP[1],endP[1])):
                        curveParam[3].append([1,endP,[],startP])
                        addCurve(curveParam[3][-1],3)
                        samplePrism.append([3,len(curveParam[3])-1,0,False])
                    samplePrismDisp = []
                    for i in range(len(samplePrism)):
                        if samplePrism[i][3]:
                            for j in range(100):
                                samplePrismDisp.append(curves[samplePrism[i][0]][samplePrism[i][1]][samplePrism[i][2]].f(1-j/100))
                        else:
                            for j in range(100):
                                samplePrismDisp.append(curves[samplePrism[i][0]][samplePrism[i][1]][samplePrism[i][2]].f(j/100))
                    fillerMode = 2
                elif fillerMode == 0:
                    for i in range(len(drawButtonSig)):
                        drawButtonSig[i] = False
                    copy = True
            if event.key == 105:
                if not drawMode == 0 or customGearMode == 1 or addCustomGears or gradientMode > 0:
                    if useIncrements:
                        useIncrements = False
                    else:
                        useIncrements = True
            if event.key == 120:
                export()
            if event.key == 101:
                if not edit:
                    for i in range(len(drawButtonSig)):
                        drawButtonSig[i] = False
                    edit = True
                else:
                    if editMode == 0:
                        editMode = 1
                    else:
                        editMode = 0
            if event.key == 100:
                if drawMode == 0:
                    if not delete:
                        for i in range(len(drawButtonSig)):
                            drawButtonSig[i] = False
                        delete = True
                elif drawMode == 11.01:
                    if potMultiInt:
                        bIntCurves.append(bIntCurves[0])
                        intP = findInter(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],curves[bIntCurves[0][0]][bIntCurves[0][1]][bIntCurves[0][2]],dCurves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],dCurves[bIntCurves[0][0]][bIntCurves[0][1]][bIntCurves[0][2]])
                        sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP[0][0],intP[1][0]])
                        scPoints = rendCurve(sc, sampT)
                        intParam = [0,1]
                        intButton2 = eButton((220,400,80,30), str(intParam[1]), (159,159,159), (191,191,191), (223,223,223), 20, (0,0,0), False)
                        potMultiInt = False
                        drawMode = 11.02
            if event.key == 13:
                if drawMode == 1.01:
                    drawMode = 1.02
                elif drawMode == 1.04 or drawMode == 1.05:
                    drawMode = 1.03
                elif drawMode == 10.01:
                    drawMode = 10.02
                elif drawMode == 10.04 or drawMode == 10.05:
                    drawMode = 10.03
                elif drawMode == 11.01:
                    if len(bIntCurves) == 1:
                        intP1 = findInter(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],curves[bIntCurves[0][0]][bIntCurves[0][1]][bIntCurves[0][2]],dCurves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],dCurves[bIntCurves[0][0]][bIntCurves[0][1]][bIntCurves[0][2]])
                        sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[0,intP1[0][0]])
                        scPoints = rendCurve(sc, sampT)
                        intParam = [0,0]
                        intButton2 = button((220,400,80,30), "start", 20, (0,0,0), (159,159,159),(191,191,191),0,True)
                        potMultiLink = False
                        drawMode = 11.02
                elif drawMode == 3:
                    scl = []
                    sclPoints = []
                    for i in range(len(translatedCurves)):
                        scl.append(translateCurve(curves[translatedCurves[i][0]][translatedCurves[i][1]][translatedCurves[i][2]],translateSeqTyp,translateSeqVal))
                        sclPoints.append(rendCurve(scl[-1],sampT))
                    drawMode = 3.01
                elif drawMode == 7.01:
                    scl = []
                    sclPoints = []
                    for i in range(len(sWarpParam[1])):
                        scl.append(singleWarp(curves[sWarpParam[0][0]][sWarpParam[0][1]][sWarpParam[0][2]],curves[sWarpParam[1][i][0]][sWarpParam[1][i][1]][sWarpParam[1][i][2]],100,100,[0,0]))
                        sclPoints.append(rendCurve(scl[-1],sampT))
                    drawMode = 7.02
                elif drawMode == 8.02:
                    scl = []
                    sclPoints = []
                    for i in range(len(dWarpParam[2])):
                        scl.append(doubleWarp(curves[dWarpParam[0][0]][dWarpParam[0][1]][dWarpParam[0][2]],curves[dWarpParam[1][0]][dWarpParam[1][1]][dWarpParam[1][2]],curves[dWarpParam[2][i][0]][dWarpParam[2][i][1]][dWarpParam[2][i][2]],100,100,[0,0]))
                        sclPoints.append(rendCurve(scl[-1],sampT))
                    drawMode = 8.03
                elif drawMode == 9.04:
                    scl = []
                    sclPoints = []
                    for i in range(len(qWarpParam[4])):
                        scl.append(quadWarp(curves[qWarpParam[0][0]][qWarpParam[0][1]][qWarpParam[0][2]],curves[qWarpParam[1][0]][qWarpParam[1][1]][qWarpParam[1][2]],curves[qWarpParam[2][0]][qWarpParam[2][1]][qWarpParam[2][2]],curves[qWarpParam[3][0]][qWarpParam[3][1]][qWarpParam[3][2]],curves[qWarpParam[4][i][0]][qWarpParam[4][i][1]][qWarpParam[4][i][2]],100,100,[0,0]))
                        sclPoints.append(rendCurve(scl[-1],sampT))
                    drawMode = 9.05
                elif presetMode == 2:
                    presets.append(samplePreset)
                    finalBox = curveBox(curves[3][samplePreset[0][0]][samplePreset[0][1]])
                    for i in range(1,len(samplePreset)):
                        sampBox = curveBox(curves[3][samplePreset[i][0]][samplePreset[i][1]])
                        if sampBox[0][0] < finalBox[0][0]:
                            finalBox[0][0] = sampBox[0][0]
                        if sampBox[0][1] < finalBox[0][1]:
                            finalBox[0][1] = sampBox[0][1]
                        if sampBox[1][0] > finalBox[1][0]:
                            finalBox[1][0] = sampBox[1][0]
                        if sampBox[1][1] > finalBox[1][1]:
                            finalBox[1][1] = sampBox[1][1]
                    presetCenters.append([(finalBox[0][0]+finalBox[1][0])/2, (finalBox[0][1]+finalBox[1][1])/2])
                    samplePreset = []
                    configPresetButtons[1].en = True
                    usePresetButton.en = True
                    presetMode = 1
                elif customGearMode == 2:
                    if editedCustomGear == -1:
                        sub = []
                        for i in range(len(sampleCustomGear)):
                            sub.append(sampleCustomGear[i])
                        customGears.append(sub)
                        customGearType = len(customGears)-1
                        cgmButtons[0].v = str(len(customGears)-1)
                    else:
                        sub = []
                        for i in range(len(sampleCustomGear)):
                            sub.append(sampleCustomGear[i])
                        customGears[editedCustomGear] = sub
                        editedCustomGear = -1
                    customGearMode = 3
                elif gradientMode == 1 or gradientMode == 2:
                    if sampleGrad[2] == 0:
                        sampleGrad[gradientMode-1] = mp[0]/zoom-cam[0]
                    else:
                        sampleGrad[gradientMode-1] = ((300-mp[1])/zoom)+cam[1]
                    gradientMode += 1
            if event.key == 122:
                if edit and drawMode == 0:
                    edit = False
                if delete:
                    delete = False
                if drawMode == 1.02:
                    ep = []
                    drawMode = 1.01
                elif drawMode == 1.01:
                    if len(cp) > 0:
                        cp[len(cp)-1:len(cp)] = []
                    else:
                        drawMode = 1
                elif drawMode == 1 or drawMode == 2 or drawMode == 3 or drawMode == 4 or drawMode == 5 or drawMode == 6 or drawMode == 7 or drawMode == 8 or drawMode == 9 or drawMode == 10 or drawMode == 11:
                    sp = []
                    drawMode = 0
                elif drawMode == 10.02:
                    ep = []
                    drawMode = 10.01
                elif drawMode == 10.01:
                    if len(cp) > 0:
                        cp[len(cp)-1:len(cp)] = []
                    else:
                        drawMode = 10
                elif drawMode in undoModes:
                    drawMode -= 0.01
                elif copy and drawMode == 0:
                    copy = False
                elif fillerMode == 1:
                    samplePrism = []
                    fillerMode = 0
                if presetMode == 2 or presetMode == 3 or presetMode == 4 or presetMode == 5:
                    presetMode = 1
                elif presetMode == 1:
                    presetMode = 0
                if customGearMode == 1:
                    if len(customGears) == 0:
                        customGearMode = 0
                        modeButtons[3].t = "aux"
                        modeNames[3] = "aux"
                    else:
                        customGearMode = 3
                elif customGearMode == 2:
                    customGearMode = 1
                if fillerMode == 2 and applyGrad:
                    for i in range(10):
                        gradSigs[i] = False
                    applyGrad = False
            if selectedUtil > -1:
                if event.key >= 48 and event.key < 58:
                    if not len(utilButtons[selectedUtil].v) == 1:
                        utilButtons[selectedUtil].v += str(event.key-48)
                    else:
                        if not utilButtons[selectedUtil].v[0] == "0":
                            utilButtons[selectedUtil].v += str(event.key-48)
                    utilVals[selectedUtil] = strToDec(utilButtons[selectedUtil].v)
                    if int(drawMode) == 2:
                        if selectedUtil < 4:
                            sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                            scPoints = rendCurve(sc, sampT)
                        elif selectedUtil == 5:
                            sampT = utilVals[5]
                            scPoints = rendCurve(sc, sampT)
                    elif int(drawMode) == 5:
                        if selectedUtil == 3:
                            sampT = utilVals[3]
                            scPoints = rendCurve(sc, sampT)
                        elif selectedUtil < 2:
                            if wrapParam[1][3] == "x":
                                sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].x,[utilVals[0],utilVals[1]])
                                scPoints = rendCurve(sc, sampT)
                            else:
                                sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].y,[utilVals[0],utilVals[1]])
                                scPoints = rendCurve(sc, sampT)
                    elif int(drawMode) == 6:
                        if selectedUtil == 3:
                            sampT = utilVals[3]
                            scPoints = rendCurve(sc, sampT)
                        elif selectedUtil < 2:
                            sc = tangent(curves[tangentParam[0][0]][tangentParam[0][1]][tangentParam[0][2]],utilVals[0],curves[tangentParam[1][0]][tangentParam[1][1]][tangentParam[1][2]],utilVals[1])
                            scPoints = rendCurve(sc, sampT)
                    elif int(drawMode) == 7:
                        if selectedUtil < 4 or selectedUtil == 5:
                            if selectedUtil == 5:
                                sampT = utilVals[5]
                            scl = []
                            sclPoints = []
                            for i in range(len(sWarpParam[1])):
                                scl.append(singleWarp(curves[sWarpParam[0][0]][sWarpParam[0][1]][sWarpParam[0][2]],curves[sWarpParam[1][i][0]][sWarpParam[1][i][1]][sWarpParam[1][i][2]],utilVals[0],utilVals[1],[utilVals[2],utilVals[3]]))
                                sclPoints.append(rendCurve(scl[-1],sampT))
                    elif int(drawMode) == 8:
                        if selectedUtil < 4 or selectedUtil == 5:
                            if selectedUtil == 5:
                                sampT = utilVals[5]
                            scl = []
                            sclPoints = []
                            for i in range(len(dWarpParam[2])):
                                scl.append(doubleWarp(curves[dWarpParam[0][0]][dWarpParam[0][1]][dWarpParam[0][2]],curves[dWarpParam[1][0]][dWarpParam[1][1]][dWarpParam[1][2]],curves[dWarpParam[2][i][0]][dWarpParam[2][i][1]][dWarpParam[2][i][2]],utilVals[0],utilVals[1],[utilVals[2],utilVals[3]]))
                                sclPoints.append(rendCurve(scl[-1],sampT))
                    elif int(drawMode) == 9:
                        if selectedUtil < 4 or selectedUtil == 5:
                            if selectedUtil == 5:
                                sampT = utilVals[5]
                            scl = []
                            sclPoints = []
                            for i in range(len(qWarpParam[4])):
                                scl.append(quadWarp(curves[qWarpParam[0][0]][qWarpParam[0][1]][qWarpParam[0][2]],curves[qWarpParam[1][0]][qWarpParam[1][1]][qWarpParam[1][2]],curves[qWarpParam[2][0]][qWarpParam[2][1]][qWarpParam[2][2]],curves[qWarpParam[3][0]][qWarpParam[3][1]][qWarpParam[3][2]],curves[qWarpParam[4][i][0]][qWarpParam[4][i][1]][qWarpParam[4][i][2]],utilVals[0],utilVals[1],[utilVals[2],utilVals[3]]))
                                sclPoints.append(rendCurve(scl[-1],sampT))
                    else:
                        if selectedUtil == 1:
                            sampT = utilVals[1]
                            if int(drawMode) == 3:
                                sclPoints = []
                                for i in range(len(scl)):
                                    sclPoints.append(rendCurve(scl[i],sampT))
                            else:
                                scPoints = rendCurve(sc, sampT)
                elif event.key == 8:
                    if len(utilButtons[selectedUtil].v) > 0:
                        sub = ""
                        for i in range(len(utilButtons[selectedUtil].v)-1):
                            sub += utilButtons[selectedUtil].v[i]
                        utilButtons[selectedUtil].v = sub
                    if len(utilButtons[selectedUtil].v) > 0 and not utilButtons[selectedUtil].v[-1] == "-" and not utilButtons[selectedUtil].v[-1] == ".":
                        utilVals[selectedUtil] = strToDec(utilButtons[selectedUtil].v)
                        if int(drawMode) == 2:
                            if selectedUtil < 4:
                                sc = spiral(sp[0],sp[1],utilVals[0],utilVals[1],utilVals[2],utilVals[3])
                                scPoints = rendCurve(sc, sampT)
                            elif selectedUtil == 5:
                                sampT = utilVals[5]
                                scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 5:
                            if selectedUtil == 3:
                                sampT = utilVals[3]
                                scPoints = rendCurve(sc, sampT)
                            elif selectedUtil < 2:
                                if wrapParam[1][3] == "x":
                                    sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].x,[utilVals[0],utilVals[1]])
                                    scPoints = rendCurve(sc, sampT)
                                else:
                                    sc = wrap(curves[wrapParam[0][0]][wrapParam[0][1]][wrapParam[0][2]],curves[wrapParam[1][0]][wrapParam[1][1]][wrapParam[1][2]].y,[utilVals[0],utilVals[1]])
                                    scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 6:
                            if selectedUtil == 3:
                                sampT = utilVals[3]
                                scPoints = rendCurve(sc, sampT)
                            elif selectedUtil < 2:
                                sc = tangent(curves[tangentParam[0][0]][tangentParam[0][1]][tangentParam[0][2]],utilVals[0],curves[tangentParam[1][0]][tangentParam[1][1]][tangentParam[1][2]],utilVals[1])
                                scPoints = rendCurve(sc, sampT)
                        elif int(drawMode) == 7:
                            if selectedUtil < 4 or selectedUtil == 5:
                                if selectedUtil == 5:
                                    sampT = utilVals[5]   
                                scl = []
                                sclPoints = []
                                for i in range(len(sWarpParam[1])):
                                    scl.append(singleWarp(curves[sWarpParam[0][0]][sWarpParam[0][1]][sWarpParam[0][2]],curves[sWarpParam[1][i][0]][sWarpParam[1][i][1]][sWarpParam[1][i][2]],utilVals[0],utilVals[1],[utilVals[2],utilVals[3]]))
                                    sclPoints.append(rendCurve(scl[-1],sampT))
                        elif int(drawMode) == 8:
                            if selectedUtil < 4 or selectedUtil == 5:
                                if selectedUtil == 5:
                                    sampT = utilVals[5]
                                scl = []
                                sclPoints = []
                                for i in range(len(dWarpParam[2])):
                                    scl.append(doubleWarp(curves[dWarpParam[0][0]][dWarpParam[0][1]][dWarpParam[0][2]],curves[dWarpParam[1][0]][dWarpParam[1][1]][dWarpParam[1][2]],curves[dWarpParam[2][i][0]][dWarpParam[2][i][1]][dWarpParam[2][i][2]],utilVals[0],utilVals[1],[utilVals[2],utilVals[3]]))
                                    sclPoints.append(rendCurve(scl[-1],sampT))
                        elif int(drawMode) == 9:
                            if selectedUtil < 4 or selectedUtil == 5:
                                if selectedUtil == 5:
                                    sampT = utilVals[5]
                                scl = []
                                sclPoints = []
                                for i in range(len(qWarpParam[4])):
                                    scl.append(quadWarp(curves[qWarpParam[0][0]][qWarpParam[0][1]][qWarpParam[0][2]],curves[qWarpParam[1][0]][qWarpParam[1][1]][qWarpParam[1][2]],curves[qWarpParam[2][0]][qWarpParam[2][1]][qWarpParam[2][2]],curves[qWarpParam[3][0]][qWarpParam[3][1]][qWarpParam[3][2]],curves[qWarpParam[4][i][0]][qWarpParam[4][i][1]][qWarpParam[4][i][2]],utilVals[0],utilVals[1],[utilVals[2],utilVals[3]]))
                                    sclPoints.append(rendCurve(scl[-1],sampT))
                        else:
                            if selectedUtil == 1:
                                sampT = utilVals[1]
                                if int(drawMode) == 3:
                                    sclPoints = []
                                    for i in range(len(scl)):
                                        sclPoints.append(rendCurve(scl[i],sampT))
                                else:
                                    scPoints = rendCurve(sc, sampT)
                elif event.key == 13:
                    if len(utilButtons[selectedUtil].v) == 0:
                        utilButtons[selectedUtil].v = str(utilVals[selectedUtil])
                    utilButtons[selectedUtil].se = False
                    selectedUtil = -1
                elif event.key == 45 and len(utilButtons[selectedUtil].v) == 0:
                    if (selectedUtil == 3 and int(drawMode) == 1) or ((selectedUtil == 7 or selectedUtil < 4) and (int(drawMode) == 2 or int(drawMode) == 7 or int(drawMode) == 8 or int(drawMode) == 9)) or ((selectedUtil == 5 or selectedUtil < 2) and (int(drawMode) == 5 or int(drawMode) == 6)):
                        utilButtons[selectedUtil].v += "-"
                elif event.key == 46 and len(utilButtons[selectedUtil].v) > 0:
                    if (selectedUtil == 1 and int(drawMode) == 1) or (selectedUtil < 4 and (int(drawMode) == 2 or int(drawMode) == 7 or int(drawMode) == 8 or int(drawMode) == 9)) or ((selectedUtil < 2 or selectedUtil == 3) and (int(drawMode) == 5 or int(drawMode) == 6)):
                        utilButtons[selectedUtil].v += "."
            elif selectedTranslationPara[0] > -1:
                if event.key >= 48 and event.key < 58:
                    if not len(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v) == 1:
                        translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v += str(event.key-48)
                    else:
                        if not translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v[0] == "0":
                            translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v += str(event.key-48)
                    translateSeqVal[selectedTranslationPara[0]+translateParamPage*6][selectedTranslationPara[1]-1] = strToDec(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v)
                    scl = []
                    sclPoints = []
                    for j in range(len(translatedCurves)):
                        scl.append(translateCurve(curves[translatedCurves[j][0]][translatedCurves[j][1]][translatedCurves[j][2]],translateSeqTyp,translateSeqVal))
                        sclPoints.append(rendCurve(scl[-1],sampT))
                elif event.key == 8:
                    if len(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v) > 0:
                        sub = ""
                        for i in range(len(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v)-1):
                            sub += translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v[i]
                        translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v = sub
                    if len(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v) > 0 and not translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v[-1] == "-" and not translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v[-1] == ".":
                        translateSeqVal[selectedTranslationPara[0]+translateParamPage*6][selectedTranslationPara[1]-1] = strToDec(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v)
                        scl = []
                        sclPoints = []
                        for j in range(len(translatedCurves)):
                            scl.append(translateCurve(curves[translatedCurves[j][0]][translatedCurves[j][1]][translatedCurves[j][2]],translateSeqTyp,translateSeqVal))
                            sclPoints.append(rendCurve(scl[-1],sampT))
                elif event.key == 13:
                    if len(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v) == 0:
                        translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v = str(translateSeqVal[selectedTranslationPara[0]+translateParamPage*6][selectedTranslationPara[1]-1])
                    translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].se = False
                    selectedTranslationPara[0] = -1
                elif event.key == 45 and len(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v) == 0:
                    translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v += "-"
                elif event.key == 46 and len(translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v) > 0:
                    translateButtons[selectedTranslationPara[0]][selectedTranslationPara[1]].v += "."
            elif bspDegreeButton.se:
                if event.key >= 48 and event.key < 58:
                    if not len(bspDegreeButton.v) == 1:
                        bspDegreeButton.v += str(event.key-48)
                    else:
                        if not bspDegreeButton.v[0] == "0":
                            bspDegreeButton.v += str(event.key-48)
                    bspParam[0] = strToDec(bspDegreeButton.v)
                    if bspParam[0] == 0:
                        bspParam[0] = 1
                        bspDegreeButton.v = str(bspParam[0])
                    px = [sp[0]]
                    py = [sp[1]]
                    for j in range(len(cp)):
                        px.append(cp[j][0])
                        py.append(cp[j][1])
                    px.append(ep[0])
                    py.append(ep[1])
                    scl = []
                    sclPoints = []
                    for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                        g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                        scl.append(g)
                        sclPoints.append(rendCurve(scl[-1],sampT))
                elif event.key == 8:
                    if len(bspDegreeButton.v) > 0:
                        sub = ""
                        for i in range(len(bspDegreeButton.v)-1):
                            sub += bspDegreeButton.v[i]
                        bspDegreeButton.v = sub
                    if len(bspDegreeButton.v) > 0:
                        bspParam[0] = strToDec(bspDegreeButton.v)
                        px = [sp[0]]
                        py = [sp[1]]
                        for j in range(len(cp)):
                            px.append(cp[j][0])
                            py.append(cp[j][1])
                        px.append(ep[0])
                        py.append(ep[1])
                        scl = []
                        sclPoints = []
                        for j in range(len(px)+(bspParam[0]-2)*(bspParam[1] == 0)):
                            g = para(full([[0,customLeg(px,bspParam[0],j,bspParam[1]),0,False]],[[0]]),full([[0,customLeg(py,bspParam[0],j,bspParam[1]),0,False]],[[0]]))
                            scl.append(g)
                            sclPoints.append(rendCurve(scl[-1],sampT))
                elif event.key == 13:
                    if len(bspDegreeButton.v) == 0:
                        bspDegreeButton.v = str(bspParam[0])
                    bspDegreeButton.se = False
            elif intButton1.se:
                if event.key >= 48 and event.key < 58:
                    if not len(intButton1.v) == 1:
                        intButton1.v += str(event.key-48)
                    else:
                        if not intButton1.v[0] == "0":
                            intButton1.v += str(event.key-48)
                    intParam[0] = strToDec(intButton1.v)
                    if intParam[0] > len(intP1)-1:
                        intParam[0] = len(intP1)-1
                        intButton1.v = str(intParam[0])
                    if len(bIntCurves) == 1:
                        if intParam[1] == 0:
                            sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[0,intP1[intParam[0]][0]])
                            scPoints = rendCurve(sc, sampT)
                        else:
                            sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[intParam[0]][0],1])
                            scPoints = rendCurve(sc, sampT)
                    else:
                        sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[intParam[0]][0],intP2[intParam[1]][0]])
                        scPoints = rendCurve(sc, sampT)
                elif event.key == 8:
                    if len(intButton1.v) > 0:
                        sub = ""
                        for i in range(len(intButton1.v)-1):
                            sub += intButton1.v[i]
                        intButton1.v = sub
                    if len(intButton1.v) > 0:
                        intParam[0] = strToDec(intButton1.v)
                        if len(bIntCurves) == 1:
                            if intParam[1] == 0:
                                sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[0,intP1[intParam[0]][0]])
                                scPoints = rendCurve(sc, sampT)
                            else:
                                sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[intParam[0]][0],1])
                                scPoints = rendCurve(sc, sampT)
                        else:
                            sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[intParam[0]][0],intP2[intParam[1]][0]])
                            scPoints = rendCurve(sc, sampT)
                elif event.key == 13:
                    if len(intButton1.v) == 0:
                        intButton1.v = str(intParam[0])
                    intButton1.se = False
            if len(bIntCurves) == 2:
                if intButton2.se:
                    if event.key >= 48 and event.key < 58:
                        if not len(intButton2.v) == 1:
                            intButton2.v += str(event.key-48)
                        else:
                            if not intButton2.v[0] == "0":
                                intButton2.v += str(event.key-48)
                        intParam[1] = strToDec(intButton2.v)
                        if intParam[1] > len(intP2)-1:
                            intParam[1] = len(intP2)-1
                            intButton2.v = str(intParam[1])
                        sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[intParam[0]][0],intP2[intParam[1]][0]])
                        scPoints = rendCurve(sc, sampT)
                    elif event.key == 8:
                        if len(intButton2.v) > 0:
                            sub = ""
                            for i in range(len(intButton2.v)-1):
                                sub += intButton2.v[i]
                            intButton2.v = sub
                        if len(intButton2.v) > 0:
                            intParam[1] = strToDec(intButton2.v)
                            sc = slicePara(curves[mIntCurve[0]][mIntCurve[1]][mIntCurve[2]],[intP1[intParam[0]][0],intP2[intParam[1]][0]])
                            scPoints = rendCurve(sc, sampT)
                    elif event.key == 13:
                        if len(intButton2.v) == 0:
                            intButton2.v = str(intParam[1])
                        intButton2.se = False
            if selInc > -1:
                if event.key >= 48 and event.key < 58:
                    if not len(editIncButtons[selInc].v) == 1:
                        editIncButtons[selInc].v += str(event.key-48)
                    else:
                        if not editIncButtons[selInc].v[0] == "0":
                            editIncButtons[selInc].v += str(event.key-48)
                    inc[int(selInc/2)][selInc%2] = strToDec(editIncButtons[selInc].v)*pow(-1,int(selInc/2)+1)
                elif event.key == 8:
                    if len(editIncButtons[selInc].v) > 0:
                        sub = ""
                        for i in range(len(editIncButtons[selInc].v)-1):
                            sub += editIncButtons[selInc].v[i]
                        editIncButtons[selInc].v = sub
                    if len(editIncButtons[selInc].v) > 0:
                        inc[int(selInc/2)][selInc%2] = strToDec(editIncButtons[selInc].v)*pow(-1,int(selInc/2)+1)
                elif event.key == 13:
                    if len(editIncButtons[selInc].v) == 0:
                        editIncButtons[selInc].v = str(inc[int(selInc/2)][selInc%2])
                    editIncButtons[selInc].se = False
            if selectedFUtil > -1:
                if event.key >= 48 and event.key < 58:
                    if not len(fillerUtilButtons[selectedFUtil].v) == 1:
                        fillerUtilButtons[selectedFUtil].v += str(event.key-48)
                    else:
                        if not fillerUtilButtons[selectedFUtil].v[0] == "0":
                            fillerUtilButtons[selectedFUtil].v += str(event.key-48)
                    fillerUtilVals[selectedFUtil] = strToDec(fillerUtilButtons[selectedFUtil].v)
                elif event.key == 8:
                    if len(fillerUtilButtons[selectedFUtil].v) > 0:
                        sub = ""
                        for i in range(len(fillerUtilButtons[selectedFUtil].v)-1):
                            sub += fillerUtilButtons[selectedFUtil].v[i]
                        fillerUtilButtons[selectedFUtil].v = sub
                    if len(fillerUtilButtons[selectedFUtil].v) > 0 and not fillerUtilButtons[selectedFUtil].v[-1] == "-" and not fillerUtilButtons[selectedFUtil].v[-1] == ".":
                        fillerUtilVals[selectedFUtil] = strToDec(fillerUtilButtons[selectedFUtil].v)
                elif event.key == 13:
                    if len(fillerUtilButtons[selectedFUtil].v) == 0:
                        fillerUtilButtons[selectedFUtil].v = str(fillerUtilVals[selectedFUtil])
                    fillerUtilButtons[selectedFUtil].se = False
                    selectedFUtil = -1
            if cgmButtons[0].se:
                if event.key >= 48 and event.key < 58:
                    if not len(cgmButtons[0].v) == 1:
                        cgmButtons[0].v += str(event.key-48)
                    else:
                        if not cgmButtons[0].v[0] == "0":
                            cgmButtons[0].v += str(event.key-48)
                    customGearType = strToDec(cgmButtons[0].v)
                    if customGearType >= len(customGears):
                        customGearType = len(customGears)-1
                        cgmButtons[0].v = str(customGearType)
                    cgmButtons[1].v = str(customGears[customGearType][5])
                elif event.key == 8:
                    if len(cgmButtons[0].v) > 0:
                        sub = ""
                        for i in range(len(cgmButtons[0].v)-1):
                            sub += cgmButtons[0].v[i]
                        cgmButtons[0].v = sub
                    if len(cgmButtons[0].v) > 0:
                        customGearType = strToDec(cgmButtons[0].v)
                        if customGearType >= len(customGears):
                            customGearType = len(customGears)-1
                            cgmButtons[0].v = str(customGearType)
                        cgmButtons[1].v = str(customGears[customGearType][5])
                elif event.key == 13:
                    if len(cgmButtons[0].v) == 0:
                        cgmButtons[0].v = str(customGearType)
                    cgmButtons[0].se = False
            if cgmButtons[1].se:
                if event.key >= 48 and event.key < 58:
                    if not len(cgmButtons[1].v) == 1:
                        cgmButtons[1].v += str(event.key-48)
                    else:
                        if not cgmButtons[1].v[0] == "0":
                            cgmButtons[1].v += str(event.key-48)
                    customGears[customGearType][5] = strToDec(cgmButtons[1].v)
                    if customGears[customGearType][5] > 255:
                        customGears[customGearType][5] = 255
                        cgmButtons[1].v = str(customGears[customGearType][5])
                    elif customGears[customGearType][5] < 10:
                        customGears[customGearType][5] = 10
                        cgmButtons[1].v = str(customGears[customGearType][5])
                elif event.key == 8:
                    if len(cgmButtons[1].v) > 0:
                        sub = ""
                        for i in range(len(cgmButtons[1].v)-1):
                            sub += cgmButtons[1].v[i]
                        cgmButtons[1].v = sub
                    if len(cgmButtons[1].v) > 0:
                        customGears[customGearType][5] = strToDec(cgmButtons[1].v)
                        if customGears[customGearType][5] > 255:
                            customGears[customGearType][5] = 255
                            cgmButtons[1].v = str(customGears[customGearType][5])
                        elif customGears[customGearType][5] < 10:
                            customGears[customGearType][5] = 10
                            cgmButtons[1].v = str(customGears[customGearType][5])
                elif event.key == 13:
                    if len(cgmButtons[1].v) == 0:
                        cgmButtons[1].v = str(customGears[customGearType][5])
                    cgmButtons[1].se = False
            for i in range(2):
                if gradManageButtons[i].se:
                    if event.key >= 48 and event.key < 58:
                        if not len(gradManageButtons[i].v) == 1:
                            gradManageButtons[i].v += str(event.key-48)
                        else:
                            if not gradManageButtons[i].v[0] == "0":
                                gradManageButtons[i].v += str(event.key-48)
                        sampleGrad[4+i] = strToDec(gradManageButtons[i].v)
                        if sampleGrad[3] > 0:
                            if sampleGrad[4+i] > 1:
                                sampleGrad[4+i] = 1
                                gradManageButtons[i].v = str(1)
                            elif sampleGrad[4+i] < 0:
                                sampleGrad[4+i] = 0
                                gradManageButtons[i].v = str(0)
                    elif event.key == 8:
                        if len(gradManageButtons[i].v) > 0:
                            sub = ""
                            for j in range(len(gradManageButtons[i].v)-1):
                                sub += gradManageButtons[i].v[j]
                            gradManageButtons[i].v = sub
                        if len(gradManageButtons[i].v) > 0 and not gradManageButtons[i].v[-1] == ".":
                            sampleGrad[4+i] = strToDec(gradManageButtons[i].v)
                            if sampleGrad[3] > 0:
                                if sampleGrad[4+i] > 1:
                                    sampleGrad[4+i] = 1
                                    gradManageButtons[i].v = str(1)
                                elif sampleGrad[4+i] < 0:
                                    sampleGrad[4+i] = 0
                                    gradManageButtons[i].v = str(0)
                    elif event.key == 13:
                        if len(gradManageButtons[i].v) == 0:
                            gradManageButtons[i].v = str(sampleGrad[4+i])
                        gradManageButtons[i].se = False
                    elif event.key == 45 and len(gradManageButtons[i].v) == 0 and sampleGrad[3] == 0:
                        gradManageButtons[i].v += "-"
                    elif event.key == 46 and len(gradManageButtons[i].v) > 0:
                        gradManageButtons[i].v += "."
            if event.key == K_RIGHT:
                if len(curvesInRange) > 0:
                    subSelectedCurve += 1
                    if subSelectedCurve >= len(curvesInRange):
                        subSelectedCurve = 0
                if len(prismsInRange) > 0:
                    subSelectedPrism += 1
                    if subSelectedPrism >= len(prismsInRange):
                        subSelectedPrism = 0
            if event.key == K_LEFT:
                if len(curvesInRange) > 0:
                    subSelectedCurve -= 1
                    if subSelectedCurve <= -1:
                        subSelectedCurve = len(curvesInRange)-1
                if len(prismsInRange) > 0:
                    subSelectedPrism -= 1
                    if subSelectedPrism <= -1:
                        subSelectedPrism = len(prismsInRange)-1
