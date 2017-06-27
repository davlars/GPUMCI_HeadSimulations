# GPUMCI_HeadSimulations
Example code of running GPUMCI on realistic skull phantoms (nifit-format) on GPU-cluster. Project part of the KTH-SSF-LCR-project. 

## Files

### ```HelicalCT_Head_Geriatrics.py```
Main run file. Imports x-ray spectrum, phantom, sets up geometry, potential gain, phantom material definition, etc. and simulates using GPUMCI (in-house MC-based simualation package). Embarrassingly parallel simulations setup for GPU-cluster. 

### ```run_GPU_cluster```
Bash script to run ```HelicalCT_Head_Geriatrics.py``` in parallell on GPU-cluster

### ```spectrumGeriatrics.txt```
Standard spectrum (W-anode, 120 kVp, 0.05 rel. voltage ripple, air kerma: 66*10^-6 Gy, mean energy: 64.5 keV, window shielding: 30 mm Be, 7 mm Al, 0.1 mm Cu) used for head simulations. File given in two column form, 1st column: keV, 2nd column: intensity. Values are normalized when imported in ```HelicalCT_Head_Geriatrics.py```.

### ```path_to_phantom```
Definng path to skull phantoms on KTH imagingnas (files not include on github because of 1) proprietary nature, and 2) file size). 

### ```append_results.py```
Script to append output files from ```HelicalCT_Head_Geriatrics.py```. Script sums upp all simulations, but conserves dicsrete turns, i.e. raw output files on the form

```
mySim_Sim_num_0_Turn_num_0.py
mySim_Sim_num_1_Turn_num_0.py
mySim_Sim_num_2_Turn_num_0.py
.
.
.
mySim_Sim_num_N_Turn_num_0.py
mySim_Sim_num_0_Turn_num_1.py
mySim_Sim_num_1_Turn_num_1.py
mySim_Sim_num_2_Turn_num_1.py
.
.
.
mySim_Sim_num_N_Turn_num_1.py
```
is converted to
```
mySim_all_Sim_num_Turn_num_0.py
mySim_all_Sim_num_Turn_num_1.py
```
### ```Substances.py```
Substances used in GPUMCI, with white_matter, gray_matter, and bone stochiometric composition defined and ready for attenuation table generation in GPUCMI. 

## Reconstruction

To reconstruct generated data, feel free to use the code found in [ad-skull-reconstruction](https://github.com/davlars/ad-skull-reconstruction).

## Requirements

To run the above, you have to have [odl](https://github.com/odlgroup/odl) (with dependencies) installed, along with [xraylib](https://github.com/tschoonj/xraylib) (for generating attenuation tables) and GPUMCI (KTH in-house software. Contact [@davlars](https://github.com/davlars) or [@adler-j](https://github.com/adler-j) for more information). 
