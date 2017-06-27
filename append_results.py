# -*- coding: utf-8 -*-
"""
Append simulation results into one projection file per turn (i.e. sum up all separate simualations, but keep turns separated). 
"""

import numpy as np
import os
#import matplotlib.pyplot as plt

for folder in ('70100644Phantom_labelled_no_bed',
               '70114044Phantom_labelled_no_bed',
               '70122044Phantom_labelled_no_bed',
               '70135144Phantom_labelled_no_bed',
               '70141544Phantom_labelled_no_bed',
               '70153744Phantom_labelled_no_bed'):
	path = os.path.join('/my/output/',folder)
	phantomName = '/helical_proj_120kVSpectrum_' + folder + '_2000photons_per_Sim'

	iter = 0
	for turnNumber in range(0,23):
		for number_of_simu in range(60):
		    print('Running sim no: %i, turn no: %i' %(number_of_simu, turnNumber))
		    myFile = (path + phantomName + 
	        	  '_Sim_num_{}'.format(number_of_simu) + 
		          '_Turn_num_{}'.format(turnNumber) + 
		          '.npy')
		    if iter == 0: #turnNumber == 0:
		        projections = np.load(myFile)
		    else:
		        #None
	        	projections = np.append(projections,np.load(myFile),axis = 0)
		    if number_of_simu > 0:
		        projectionsTot += projections
		    else:
	        	projectionsTot = projections
		saveName = path + '/HelicalSkullCT_' + folder +'_Dose150mGy_Turn_' + str(turnNumber) + '.data.npy'
		print('Saving: %s' % saveName)
		np.save(saveName,projectionsTot)
    
#plt.imshow(projections[1:-1:20,:,10])

















