# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:47:04 2023

@author: wiecz
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

fs = 2000 
dt = 1/fs

t1 = np.arange(0,2,dt)
t2 = np.arange(0,2/2., dt)
t4 = np.arange(0, 2/4., dt)
t8 = np.arange(0, 2/8., dt)
t16 = np.arange(0, 2/16., dt)


f_h0 = 246.94
f_c1 = 261.63
f_d1 = 293.66
f_e1 = 329.631
f_f1 = 349.23
f_g1 = 392.00
f_a1 = 440.00
f_c2 = 523.25

xh_8 = np.sin(2 * np.pi * f_h0 * t8 )


xc_2 = np.sin(2 * np.pi * f_c1 * t2 )
xc_4 = np.sin(2 * np.pi * f_c1 * t4 )
xc_8 = np.sin(2 * np.pi * f_c1 * t8 )

xd_2 = np.sin(2 * np.pi * f_d1 * t2 )
xd_4 = np.sin(2 * np.pi * f_d1 * t4 )
xd_8 = np.sin(2 * np.pi * f_d1 * t8 )

xe_2 = np.sin(2 * np.pi * f_e1 * t2 )
xe_4 = np.sin(2 * np.pi * f_e1 * t4 )
xe_8 = np.sin(2 * np.pi * f_e1 * t8 )

xf_2 = np.sin(2 * np.pi * f_f1 * t2 ) 
xf_4 = np.sin(2 * np.pi * f_f1 * t4 )
xf_8 = np.sin(2 * np.pi * f_f1 * t8 )

xg_2 = np.sin(2 * np.pi * f_g1 * t2 )
xg_4 = np.sin(2 * np.pi * f_g1 * t4 )
xg_8 = np.sin(2 * np.pi * f_g1 * t8 )
xg_16 = np.sin(2 * np.pi * f_g1 * t16 )


xa_4 = np.sin(2 * np.pi * f_a1 * t4 )
xa_8 = np.sin(2 * np.pi * f_a1 * t8 )

xc2_4 = np.sin(2 * np.pi * f_c2 * t4 )

przybierzeli = np.concatenate((xc_8, xh_8, xc_8, xd_8, xe_8, xd_8, xe_8, xf_8, xg_4, xa_4, xg_2, 
                    xc_8, xh_8, xc_8, xd_8, xe_8, xd_8, xe_8, xf_8, xg_4, xa_4, xg_2,
                    xc2_4, xg_8, xg_8, xa_8, xg_8, xf_8, xe_8, xf_4, xf_8, xa_8, xg_8, xf_8, xe_8, xd_8, xe_4, xf_4, xg_2, xe_4, xd_4, xc_2,
                    xc2_4, xg_8, xg_8, xa_8, xg_8, xf_8, xe_8, xf_4, xf_8, xa_8, xg_8, xf_8, xe_8, xd_8, xe_4, xf_4, xg_2, xe_4, xd_4, xc_2))

sd.play(przybierzeli,fs)