import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
plt.rcParams.update({'text.usetex':True,
'font.family':'serif',
'font.serif':['Times New Roman'],
'figure.facecolor':[1,1,1,1],
#'axes.facecolor':[0,0,0,0],
'font.size':30})
fig = plt.figure(figsize = (8,6),dpi = 100)
#shape = [xs,ys,ye,xe]
shape = [0.1,0.05,0.8,0.9]
LS = '-'
LW = 2.5
fs = 24
ax = fig.add_axes(shape)
ax.set_xlim(xmin = 0,xmax = 1.)
ax.set_ylim(ymin = 0,ymax = 1.)
ax.axis('off')
nx = 100
ny = 100
topx = np.linspace(0,1,nx)
topy = 0.7*np.ones(ny)
boty = 0.1*np.ones(ny)
ax.plot(topx,topy,ls = LS, lw = LW, c= 'k')
ax.plot(topx,boty,ls = LS, lw = LW, c= 'k')
ax.arrow(0.5,0.8,0.0,0.1,head_width = 0.02,head_length =0.02,color = 'k',lw = LW)
ax.arrow(0.5,0.4,0.0,-0.1,head_width = 0.02,head_length =0.02,color = 'k',lw = LW)
ax.arrow(0.05,0.55,0.0,0.09,head_width = 0.015,head_length =0.015,color = 'k',lw =0.5*LW)
ax.arrow(0.05,0.55,0.07,0.00,head_width = 0.015,head_length =0.015,color = 'k',lw =0.5*LW)
ax.text(0.09,0.51,r'$x$'      ,fontsize  = 0.9*fs)
ax.text(0.02,0.60,r'$z$'      ,fontsize  = 0.9*fs)
ax.text(0.03,0.49,r'$y$'      ,fontsize  = 0.9*fs)
ax.scatter([0.05],[0.55],s = 200,marker = 'o',facecolor ='w',edgecolor = 'k')
ax.scatter([0.05],[0.55],s = 25,marker = 'o',edgecolor = 'k',facecolor = 'k')
ax.text(0.55,0.85,r'$\Omega$'      ,fontsize  = fs)
ax.text(0.55,0.35,r'$g$'           ,fontsize  = fs)
ax.text(0.15,0.025,r'$T=T_b$'         ,fontsize  = fs)
ax.text(0.15,0.725,r'$T=T_b+\Delta T$',fontsize  = fs)
ax.text(0.75,0.725,r'$z = H$',fontsize  = fs)
ax.text(0.75,0.025,r'$z = 0$'         ,fontsize  = fs)
fig.savefig('./VAR1.pdf'          )
