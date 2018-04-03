#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:04:40 2018

@author: drewburrier
"""

import numpy as np
import matplotlib.pyplot as plt

seabed = np.load('../data/Penobscot_Seabed.npy')
seabed *= -1
mi, ma = np.floor(np.nanmin(seabed)), np.ceil(np.nanmax(seabed))
step = 2
levels = np.arange(10*(mi//10), ma+step, step)
lws = [0.5 if level % 10 else 1 for level in levels]

# Make the plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1,1,1)
im = ax.imshow(seabed, cmap='GnBu_r', aspect=0.5, origin='lower')
cb = plt.colorbar(im, label="TWT [ms]")
cb.set_clim(mi, ma)
params = dict(linestyles='solid', colors=['black'], alpha=0.4)
cs = ax.contour(seabed, levels=levels, linewidths=lws, **params)
ax.clabel(cs, fmt='%d')
plt.show()