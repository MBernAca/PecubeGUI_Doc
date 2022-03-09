=========
Usage
=========

.. _runPecube:

---------------------------
Create a new Pecube project
---------------------------

To create and run a new Pecube project, go to *New input file* or press *Crtl+N* (*3*, see :doc:`introduction`),
a widow pops up and ask you to provide the name of the new project (Figure *2*). After clicking the “Ok” button (Figure *2*),
you will be able to provide and set all the Pecube input parameters for your project.
  
.. figure:: ../images/New_Project.png
  :align: center

  *Figure 2. Enter a new project name. This window shows up when clicking on the "New input file" action.*


The window should look like the Figure *3*. On the top left, you could find and access all the projects you have loaded into the interface,
and thus navigate through their respective parameters. The right part of the interface will host extra input parameters described in the next sections.

.. figure:: ../images/Input_Parameters_interface.png
  :align: center

  *Figure 3. Tab to set up the input parameters for Pecube. On the top left, you can check the name of your project (here: ‘PeGUI’)*
  
  
The input parameters are gathered into categories as referenced in the Pecube’s user guide. All the parameters are sorted in *9* categories: *Topography*, *Time evolution*, *Thermal*, *Data*, *Tectonic*, *Output*, *Isostasy*, *Inversion*, and *Miscellaneous* parameters. For more details on the meaning of each input parameter please refer to the Pecube’s user guide. However, you could access to a short description of each parameter by simply flying the mouse cursor over the parameter labels. After one second a text should appears describing the parameter.
  
In the following, I provide a description of all the tabs, and how to provide the input parameters in PecubeGUI. For a detail description of the parameters, please refer to the Pecube's user guide.

--------------------------
Providing input parameters
--------------------------

Topography tab
--------------

==================================


| I present in this section all kind of widgets you could find in PecubeGUI. When providing the project name, you will automatically be directed to the first tab that            presents the "Topography" parameters (Figure 3). All the default values of the input parameters are shown, so that you do not need to provide them if you want to keep these     default values. If you wish to change a parameter, simply click on the text box, and write your value. 
| PecubeGUI offers the possibility to simply load topographic file(s) from (1) a csv file containing one column of elevation, or (2) a serie of output files from a spm to be read by Pecube (see Pecube user guide – “Topography parameters”). For that purpose, click on ‘load file(s)’ (Figure 3) will allow you to select the files to load. A window pops up. The Figure 4 shows an example, where files from iSOSIA (Egholm et al., 2011) have been loaded.

.. figure:: ../images/spm_loader.png
    :height: 268
    :width: 350
    :align: center

    *Figure 4. Spm loader window.*
     
     
| This window recovers some characteristics of your spm model, which are shown on the top for checking (works for iSOSIA models only). Then, you are asked to provide the      starting and ending times of your model (in Ma), as well as the number of steps (i.e., the number of topographic files). The initial time is greater than the end time. This      is required as it will be used to automatically set the time values for the “Time evolution” tab.

| You are also able to provide a simple pre-spm history for the topographic evolution. For that purpose, click on “Pre-history” (Figure 4). You will be able to provide 4         parameters:

    *	*number of pre-steps*: how many steps for the pre-spm history do you want to provide topographic information
    *	*uplift rate*: this will be spatially uniform and apply to all pre-history steps 
    *	*sea-level temperature*
    *	*atmospheric lapse rate*


| PecubeGUI will start from the first topographic file provided and interpolate back the pre-spm topographic history according to the amplitude and offset parameters the user will provide in the next steps (see :ref:`Time evolution tab`).
| After clicking the “Ok” button, the files will be copied and pasted into “your_current_project_path\data\SPM”. In the meantime, the name “SPM/” is automatically provided to the input parameters “Topography file name”, as well as the grid resolution (i.e., nx and ny, only work with iSOSIA files, Figure 3).

.. figure:: ../images/setTopography.png
    :scale: 30
    :align: center

    *Figure 5. "Topography" tab with the topography shown on the left-hand side, after clicking the "Show topogaphy" button.*


| When loading a synthetic numerical model, you can let the latitude and longitude to zero. However, you need to provide the stepping distance in x (Δlon) and y (Δlat). For     simplicity, you can provide the values in km and then click on ‘Convert to lat/long’ button (Figure 3). This will automatically convert the values to longitude and           latitude distances that can be read by Pecube. Finally, you are able to check the topography you provided by clicking on “Show topography” (Figure 3). A new tab then          appears on the right-hand side of the interface (Figure 5). This tab serves to visualize the topography and check your topography history as provided in the :ref:`Time evolution tab`. You are indeed able to visualize the evolution of the topography by grabbing and sliding the slide bar in “Set time evolution” (Figure 5).


Time evolution tab
------------------

==================================

In this tab (Figure 6) you can provide all the parameters that control the time evolution of the Pecube model (see Pecube user guide for more details). The particularity in PecubeGUI is that you can provide the time evolution parameters (cf. “time_topo”,” amplification”, “offset”, and “output”) by filling in the table or by copying/pasting values from an excel file to the table. The number of rows in the table automatically adapts to the value written in the parameter “ntime” (Figure 5). 

.. figure:: ../images/Time_Evolution.png
    :scale: 30
    :align: center

    *Figure 6. "Time evolution" tab where to provide parameters related to the time evolution of the topography.*

| The default value for each parameter is also automatically provided. 


Thermal tab
-------------------

==================================

| In the :ref:`Thermal tab`, you will find all the parameters to set the thermal properties of the crust and the atmosphere. In PecubeGUI, the user is able to check for the 1D steady-state geotherm by simply clicking on "Show Geotherm" (Figure 7). A new tab will appears on the left-hand side of the interface, where the geotherm is shown. Additionnaly, the user can check the influence of the erosion rate on the geotherm by providing values in "Mean erosion rate" (Figure 7). The 1D steady-state geotherm is computed using the equation find in [Reiners-and-Brandon-2006]_ that accounts for the effect erosion rates on the thermal state of the crust.
| Moreover, the user can provide the specific heat capacity (J.kg\ :sup:`-1`\.K\ :sup:`-1`\) and the radioactive heat production (µW.m\ :sup:`-3`\). The total heat production (°C.Myr\ :sup:`-1`\) will automatically be updated (Figure 7).


.. figure:: ../images/Geotherm.png
  :scale: 30
  :align: center
  
  *Figure 7. "Geotherm" tab where to provide parameters related to Thermal properties of the crust and the atmosphere.*


Tectonic tab
-------------------

==================================

| This tab is related to the “Tectonic parameters” in the Pecube user guide. The tab comprises text boxes in the upper part and two tables at the bottom. To provide the input parameters, the tab is working as follow. You need to provide values for the input parameters “nfault”, “npoint”, and “nstep”. When provided, the size of the two tables will automatically adjust to provide the relevant parameters for the fault geometry (if any fault is defined) and the kinematic of the model. 
| An example of inputs taking “EXMP4” in Pecube user guide as an example, is shown in Figure 8.

.. figure:: ../images/Tectonic_tab.png
  :scale: 30
  :align: center
  
  *Figure 8. "Tectonic" tab where to provide parameters related to kinematic of rock uplift. The "EXMP4" in the Pecube's user guide is used as an example of input.*
  
| When finishing to provide all three previous parameters, the tables updated. We see here that the first table on the left allows to set the geometry of the two faults, and the second one on the right, to define the fault kinematics (i.e., the negative values define an inverse fault, see Pecube user guide for more details). For each table the cells are sorted according to the fault (i.e., as shown by the fault name “*fault 1*, *fault 2*, …, *fault_n*”), to help the user to provide the characteristics of each. One can also decide to not define faults. In that case, “nfault” needs to be set to "1" and “npoint” to “-1”. Then, the number of steps (nstep) defines the kinematic of the entire model (uniform uplift). 


Output tab
-------------------

==================================

This tab enables the user to set the outputs he/she wants that Pecube provides at the end of the model run (Figure 9). The first part (i.e., “Compute ages”) let you choose between three options:

*	*none*: Pecube will not predict any thermochronological ages
*	*for all nodes*: Pecube will predict thermochronological ages for all nodes at the surface of the Pecube model. This option will enable you to check any boxes in the next part (i.e., “Thermochronological systems”) and choose the thermochronological system you are interested to use. 
*	*sample specific*: Pecube will predict thermochronological ages only for specific sample locations provided by the user. For this option to work, you will need to provide a folder name where PecubeGUI will write some files that will be used by the Production-diffusion model. This has to be done in the *Data tab* in the “Data folder” text box. In the current version, only the AHe system can be selected. PecubeGUI uses the production-diffusion model developped by [Gautheron-et-al-2010]_.

.. figure:: ../images/Compute_age.png
  :scale: 30
  :align: center
  
  *Figure 9. "Output" tab where to define the thermochronometers to use. Here, the example is made with sample specific prediction for the (U-Th)/He on apatite system.*
  
| If you chose the “sample specific” option, then when clicking on “Age AHe” check box (the only one available in the current version) a new window will pop up (Figure 9). 
| This window shows extra parameters for the computation of AHe ages. These extra parameters include:

*	*Diffusion model*: the diffusion model for helium to use. The options are the Farley et al. (2000), Shuster et al. (2006), and the radiation damage models from Gautheron et al. (2009) and Flowers et al. (2009, RDAAM).
*	*Ea*: The activation energy (kJ.mol\ :sup:`-1`\). This is automatically updated according to the selected diffusion model, but it can be changed at the user’s discretion.
*	*rmr0*: “The reduced length of the more-resistant apatite at the time-temperature conditions where the reduced length of the less-resistant apatite falls to zero” [Ketcham-2005]_. This parameter is used in the annealing computation of radiation damages. The default value is 0.79.
*	*D0*: the diffusivity parameter value for infinite temperature (cm\ :sup:`2`\.s\ :sup:`-1`\). The value updates according to the selected diffusion model. 
*	*Number of iterations*: number of events (i.e. atoms) for the Monte carlo simulation.
*	*Number of samples*: choose the number of sample locations for which you want to compute ages. When providing the value of this parameter, the table below is automatically updated to account for the number of samples. In this table, you must provide the latitude and longitude of the sample’s locations as well as the number of grains (i.e., ages) to predict at that location. 
*	*Check sample locations*: Clicking this button will pop a window up where your surface topography is shown, with the sample locations provided (see example, Figure 11). It provides a way to check for your sample location.
*	*Grains characteristics*: when checking this box, a new window opens (Figure 10). It shows a table in which you can change the size (radius) of the grains, as well as their uranium and thorium concentration (in ppm). Default values are assigned automatically. In the current version, the grain is assumed spherical. The user can also provide zonation profile for each grain. For this purpose, simply check the box "Zonation" (Figure 10), and then you will be able to draw the zonation profile by adding and dragging points on the both curves representing uranium and thorium profiles. As the respective concentrations are averaged within layers in the grain, you need to provide the number you desire ("Number of layers", Figure 10). When finished to set the profile for the grain, click on "Save" to save the profile for that grain.
*	*4He/3He predictions*: allows to predict \ :sup:`4`\He/\ :sup:`3`\He profiles for each grain. When checked, a new window opens. Within this window, you can provide your heating schedule, with the number of steps, or let the default heating schedule. This will be used in the diffusion model to simulate a degassing experiment and compute \ :sup:`4`\He/\ :sup:`3`\He ratios. The heat is in °C and the duration in hours. The same heating schedule is used for each grain. 


.. important::
  When finished to provide all the parameters you need to click on “save samples file…” (Figure 9).
  This will create two files. The first one is named “sample_specific.txt” and can be found in the “data” folder of your current project.
  It stores the parameters for He age prediction that the Production-diffusion model will read (see the Sample_specific file description).
  The second one has the same name as the folder’s name provided in the Data parameters tab and stores the latitude and longitude of the sample’s locations.
  This file is used in Pecube to output thermal histories of these locations (do not forget to check “save PTT paths” in the Output parameters tab).


.. figure:: ../images/Grain_characteristics.png
  :scale: 30
  :align: center
  
  *Figure 10. Window that appears when checking the box "Grain characteristics" (Figure 9).*
  

.. figure:: ../images/Sample_location.png
  :scale: 50
  :align: center
  
  *Figure 11. Window that appears when clicking on "Check sample location". The surface topography of your model is shown with the location of your samples (white circles).*

The remaining tabs do not need details description. Simply fill the text boxes with your new values. The details for each input parameters can be found in the Pecube user guide, and short descriptions can be seen when flying the mouse cursor over the label each parameter.


------------------
Run a Pecube model
------------------

| To run a Pecube model, simply click on “Run Pecube” above the tabs (Figure 9). A new window pops up. According to your Preferences (cf. ‘2’, Figure 1) the latter will only show a progress bar of the Pecube run (Figure 10A, ‘Show console’ unchecked in Preferences) or additional information is provided if the console is enabled (Figure 10B, "Show console” checked in Preferences).

| PecubeGUI first runs Pecube as usual, and if the option “sample specific” is set (cf, previous section), then PecubeGUI will run the Production-diffusion model to compute grain specifics AHe ages. When the console is allowed to be shown, the state of the runs is written within it. At the end of the Pecube run, this window displays ‘Pecube run is finished!’ and you can click on the ‘Ok’ button to close the window.
| Note that you can also choose to not run Pecube but only the Production-diffusion model to compute AHe ages for sample-specific locations from an old Pecube project. This is useful when one wants to use e.g., another radiation damage model and do not want to run Pecube again. To do so, simply click on "Compute ages" (Figure 9).

.. note::
  When several projects are opened, the consoles are gathered in a single window to have a quick overview of all the running simulations.
  

----------------
Plotting results
----------------

In that section, I provide an overview of the chart part of PecubeGUI. There, you can plot results from your Pecube run. 


Plot 2D data
------------

==================================

In the current version, and depending on your input parameters, Pecube can output several files that you can then load into PecubeGUI to plot some results. These files are:

*	*TimeTemperature.csv*: this file stores the thermal path of each sample location you provided, either by writing directly in a file in the ‘Data’ folder of your project, or by specifying the locations in PecubeGUI when want to predict specific AHe ages (see ‘Output parameters’ tab). For this file to be created, you also need to check ‘save PTT paths’ in the ‘Output parameters’ tab.
*	*Graini_j*: This file stores the input parameters used for the production-diffusion model, and the resulting ages computed according to the thermal history provided. You will find in this file: the thermal history of the sample, its age evolution, and the degassing fractions of \ :sup:`4`\He and \ :sup:`3`\He (if defined by the user, see :ref:`Output tab`).
* *PecubeXXX.vtk*: This file is located in the "VTK" directory of your project. If loaded for 2D data plot, a window will show up and ask you which data to plot from the file. You can extract, for instance, the 2D spatial distribution of the temperature at a specified depth, or extract the depth of an isotherm.
* *AgeXXX.vtk*:  This file is located in the "VTK" directory of your project.  If loaded for 2D data plot, you can choose to plot the 2D spatial distribution of the erosion rate or the predicted ages, at the surface of the Pecube model (only with the "for all nodes" option, see :ref:`Output tab`).

To be able to plot 2D data in PecubeGUI, first switch to the chart's window by clicking on ‘show ouput’ (see Figure 1, n°5). You should see the window shown in Figure 12. On the left-hand side, you will find two tabs: *Data* and *Properties*. The first tab enables to load new data. 


.. figure:: ../images/Chart_window.png
  :scale: 30
  :align: center
  
  *Figure 12. Chart's window.*
  
  
To do so, simply click on ‘Add 2D data…’, then a window appears and ask you to choose a csv file to search for some data to plot. You can load any of the files mentioned above.


Visualize 3D data
-----------------

==================================

| PecubeGUI offers a 3D interactive interface where to visualize 3D models alongside with sample locations (if defined). The 3D interface is handling with pyvista [Sullivan-et-al-2019]_, which is an open-source package to read and manage vtk files. 
| To load a 3D model, click on “Add 3D model…” and select your vtk file from your Pecube project folder. A new tab will appear with a 3D environment and the 3D model (Figure 13).
| If you chose to predict ages at specific locations, those kocations will be automatically loaded with your 3D model. However, you can show/hide them by checking the box “show sample location(s)” on the properties tab (left side of the window, see Figure 13). On this tab, you have several options to set properties of the 3D model:

*	*Data range*: set the range of data for the colorbar.
*	*Current data*: list to choose the data to show (i.e., for the colormap).
* *X, Y, Z scales*: to scale the 3D model in the x, y, and z, directions.
* *Reset camera position*: reset the camera view to the initial position.
* *Clear plot*: remove the 3D model from the 3D interface.
* *Export image…*: save a screenshot of the 3D interface.
*	*Show box*: to show the axes of the 3D model.
*	*Show sample location(s)*: to show/hide sample locations within the 3D interface.


------------
Bibliography
------------

.. [Reiners-and-Brandon-2006] Reiners, P. W., & Brandon, M. T. (2006). Using thermochronology to understand orogenic erosion. Annu. Rev. Earth Planet. Sci., 34, 419-466.
.. [Gautheron-et-al-2010] Gautheron, C., & Tassan-Got, L. (2010). A Monte Carlo approach to diffusion applied to noble gas/helium thermochronology. Chemical Geology, 273(3-4), 212-224.
.. [Ketcham-2005] Ketcham, R. A. (2005). Forward and inverse modeling of low-temperature thermochronometry data. Reviews in mineralogy and geochemistry, 58(1), 275-314.
.. [Sullivan-et-al-2019] Sullivan et al., (2019). PyVista: 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK). Journal of Open Source Software, 4(37), 1450, https://doi.org/10.21105/joss.01450
