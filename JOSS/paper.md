---
title: 'Integrated hydrologic model development and postprocessing for GSFLOW using pyGSFLOW'  
tags:
  - Python
  - hydrology
  - integrated hydrologic modeling
  - groundwater
  - surfacewater
  - GSFLOW
  - MODFLOW
  - PRMS  
authors:
  - name: Joshua D. Larsen^[corresponding author]
    ocrid: 0000-0002-1218-800X
    affiliation: 1
  - name: Ayman Alzraiee
    ocrid: 0000-0001-7576-3449
    affiliation: 1
  - name: Richard G. Niswonger
    ocrid: 0000-0001-6397-2403
    affiliation: 2  
affiliations:
  - name: U.S. Geological Survey, California Water Science Center, Sacramento, CA
    index: 1
  - name: U.S. Geological Survey, Water Mission Area, Menlo Park, CA
    index: 2  
date: 19 March 2021
bibliography: paper.bib
---

# Overview
Text goes here

# Introduction
Paste introduction text here

# Statement of need
Paste statement of need text here

# pyGSFLOW
Paste body text here

![Mean squared error in streamflow preditions for three PRMS parameters
(gsflow_coef, snarea_curve, and ssr2gw_rate) during calibration experiments
on the Santa Rosa Plain Integrated Hydrologic Model, Santa Rosa,
California.](calibration_example.png)


more body text

![Mean recharge for the entire simulation from MODFLOW is overlain with a
spatial contour plot of PRMS ssr2gw_rate which is a multiplier that scales
the volume of recharge from PRMS to MODFLOW. MODFLOW’s IBOUND array
(black is inactive cells) is also plotted to distinguish active versus
inactive model cells, Sagehen Creek GSFLOW model,
Truckee, California.](sagehen_plot.png)


more body text

# Package architecture
Paste package text here

![Hierarchical representation of the pyGSFLOW package. Each sub-package lists
the model building classes within each package. The GSFlowModel class interacts
with each of these listed modules and the FloPy
package.](Package_architecture.png)


# Conclusion
Paste conclusion text here

# References


