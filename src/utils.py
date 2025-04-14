import pandas as pd 
import numpy as np
import streamlit as st

def commut(data, Age, L, i=0.035, n=1, type='non'):
    age = data[Age]
    l = data[L]
    #i = 0.035
    v = (1+i)**(-1)
    w = len(age)


    d, N, S, M, R = np.zeros(w), np.zeros(w), np.zeros(w), np.zeros(w), np.zeros(w)
    
    for k in range(w-1):
        d[k] = l[k]-l[k+1]
        
    data['d'] = d
    data['C'] = d*v**(age+0.5)
    data['D'] = l*v**age

    for x in age :
        for k in range(x, w):
            N[x] += data['D'][k]
            M[x] += data['C'][k]

    data['N'] = N
    data['M'] = M

    for x in age :
        for k in range(x, w):
            S[x] += data['N'][k]
            R[x] += data['M'][k]

    data['S'] = S
    data['R'] = R
    
    data['äx = Nx/Dx'] = data['N']/data['D']
    data['Ax=Mx/Dx'] = data['M']/data['D']
    
    ax = np.zeros(w)
    for x in range(w-1):
        if data['D'][x] != 0:
            ax[x] = data['N'][x+1]/data['D'][x]
        
    data['ax = N_(x+1)/Dx'] = ax
    
    if type == "Term immediate annuity":
        ax_n = np.zeros(w)
        for x in range(w-1):
            if data['D'][x] != 0 :
                if x+n <=106 :
                    ax_n[x] = (data['N'][x]-data['N'][x+n])/data['D'][x]
                
        
        data['ax:n (rente temporaire) =(N_(x)-N_(x+n))/Dx'] = ax_n
        
    if type == "Differed annuity":
        n_âx = np.zeros(w)
        for x in range(w-1):
            if data['D'][x] != 0:
                if x+n <=106 :
                    n_âx[x]= data['N'][x+n]/data['D'][x]
               
        data['n|äx = N_(x+n)/Dx'] = n_âx
    
    if type == "Term insurance - yearly":
        Ax_n = np.zeros(w)
        for x in range(w-1):
            if data['D'][x] != 0:
                if x+n <=106 :
                    Ax_n[x] = (data['M'][x]-data['M'][x+n])/data['D'][x]
                    
                
        data['A_x:n (temporaire décès) =(M_(x)-M_(x+n))/Dx'] = Ax_n
        
    if type == "Pure endowment":
        nEx = np.zeros(w)
        for x in range(w-1):
            if data['D'][x] != 0:
                if x+n <=106 :
                    nEx[x] = data['D'][x+n]/data['D'][x]
               
        data['nEx (Pure endowment) = D_(x+n)/Dx'] = nEx
    
    if type == "Endowment insurance - yearly":
        Ax_n_mixte = np.zeros(w)
        for x in range(w-1):
            if data['D'][x] != 0:
                if x+n <=106 :
                    Ax_n_mixte[x] = (data['M'][x]-data['M'][x+n]+data['D'][x+n])/data['D'][x]
                
                    
        data['A(x:n)_mixte =(M_(x)-M_(x+n)+D_(x+n))/Dx'] = Ax_n_mixte

    return data



