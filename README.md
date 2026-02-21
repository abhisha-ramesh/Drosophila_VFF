# A Physical Model of Drosophila Ventral Furrow Formation
This project simulates Drosophila Ventral Furrow Formation using Cellular Potts Model(aka Glazier-Graner-Hogeweg Model) using the [CompuCell3D(CC3D)](https://github.com/CompuCell3D/CompuCell3D)(Version 4.2.3) simulation software. The model investigates the role of longitudinal stiffness in the furrow formation of Drosophila melanogaster embryos during gastrulation. This simulation is part of the research presented in the paper "Highly dynamic mechanical transitions in embryonic cell populations during _Drosophila_ gastrulation" by Juan Manuel Gomez, Carlo Bevilacqua, Abhisha Thayambath, Jean-Karim Heriche, Maria Leptin, Julio M. Belmonte, and Robert Prevedel. This README file provides instructions on how to setup, run and modify this simulation using CC3D simulation environment. 

## Installing CC3D
The latest version of CC3D can be downloaded and installed from the [official website](https://compucell3d.org/) (supported on Windows, Mac and Linux). Simulations can be executed using [CompuCell3D Player](https://github.com/CompuCell3D/cc3d-player5/tree/master).

## How to run and modify simulation?
The simulation contains a .cc3d project file and a directory called Simulation where one can find all the Python Scripts. To load a simulation in CC3D Player or into [Twedit++](https://github.com/CompuCell3D/cc3d-twedit5/tree/master) (IDE for CC3D), use the .cc3d file. The simulation can be modified by loading the python scripts into Twedit++.

## Simulation Output and Analysis Pipeline
Each simulation run generates _furrow_depth.txt_ file inside the CC3DWorkSpace directory. The file contains time (in MCS which is the unit of time in the simulation) vs furrow depth data.

## Parameter Sweeps on HPC
To investigate the role of cell stiffness parameters (e.g. central vs peripheral stiffness or apical vs basal stiffness), simulations are executed on an HPC cluster.
For each parameter combination, 30 independent ensemble runs are performed and each run generates one _furrow_depth.txt_.

## Ensemble Average of Furrow Depth Data
After all simulations complete, the ensemble data are averaged using the _analysis_main.py_ file in _analysis_scripts_on_hpc_ directory (submitted using _submit.csh_ on an LSF system). For each parameter combination (e.g., λ_cent, λ_peri), a new file is generated containing time and average furrow depth (one file per stiffness parameter combination). 

## Phase Map Generation
After averaging, averaged files are copied from HPC. The final furrow depth (last time point) is extracted and a phase map is generated. An example is listed in _plot_phase_map_from_data.zip_ .


