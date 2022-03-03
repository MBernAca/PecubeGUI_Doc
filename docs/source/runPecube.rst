=========
RunPecube
=========

.. _runPecube:

---------------------------
Create a new Pecube project
---------------------------

To create and run a new Pecube project, go to *New input file* or press *Crtl+N* (*3*, see introduction),
a widow pops up and ask you to provide the name of the new project (Figure *2*). After clicking the “Ok” button (Figure *2*),
you will be able to provide and set all the Pecube input parameters for your project.
  
.. figure:: ../images/New_Project.png

  *Figure 2. Enter a new project name. This window shows up when clicking on the "New input file" action.*


The window should look like the Figure *3*. On the top left, you could find and access all the projects you have loaded into the interface,
and thus navigate through their respective parameters. The right part of the interface will host extra input parameters described in the next sections.

.. figure:: ../images/Input_Parameters_interface.png

  *Figure 3. Tab to set up the input parameters for Pecube. On the top left, you can check the name of your project (here: ‘PeGUI’)*
  
  
  The input parameters are presented by categories as referenced in the Pecube’s user guide. All the parameters are sorted in *9* categories: *Topography*, *Time evolution*, *Thermal*, *Data*, *Tectonic*, *Output*, *Isostasy*, *Inversion*, and *Miscellaneous* parameters. For more details on the meaning of each input parameter please refer to the Pecube’s user guide. However, you could access to a short description of each parameter by simply flying the mouse cursor over the parameter labels. After one second a text should appears describing the parameter.
  
In the following, I provide a description of all the tabs, and how to provide the input parameters in PecubeGUI. For a detail description of the parameters, please refer to the Pecube user guide.

--------------------------
Providing input parameters
--------------------------

Topography tab:
---------------

==================================

  I present in this section all kind of widgets you could find in PecubeGUI. When providing the project name, you will automatically be directed to the first tab that presents the “Topography parameters” (Figure 3). All the default values of the input parameters are shown, so that you do not need to provide them if you want to keep these default values. If you wish to change a parameter, simply click on the text box, and write your value. 
  PecubeGUI offers the possibility to simply load topographic file(s) from (1) a csv file containing one column of elevation, or (2) output files from a spm to be read by Pecube (see Pecube user guide – “Topography parameters”). For that purpose, click on ‘load file(s)…’ (Figure 3) will allow you to select the files to load. A window pops up and Figure 4 shows an example, where files from iSOSIA (Egholm et al., 2011) have been loaded.

.. figure:: ../images/spm_loader.png
  :height: 268
  :width: 350
  :align: center

  *Figure 4. Spm loader window.*

This window recovers some characteristics of your spm model, which are shown on the top for checking (works for iSOSIA models only). Then, you are asked to provide the starting and ending times of your model (in Ma), as well as the number of steps (i.e., the number of topographic files). The initial time is greater than the end time. This is required as it will be used to automatically set the time values for the “Time evolution parameters” table.

You are also able to provide a simple pre-spm history for the topographic evolution. For that purpose, click on “Pre-history” (Figure 4). You will be able to provide 4 parameters:

  *	The number of pre-steps: how many steps for the pre-spm history do you want to provide topographic information
  *	The uplift rate: this will be spatially uniform and apply to all pre-history steps 
  *	The sea-level temperature
  *	The atmospheric lapse rate


| If provided, PecubeGUI will start from the first topographic file provided and interpolate back the pre-spm topographic history according to the amplitude and offset parameters the user will provide in the next steps (see next sections).
| After clicking the “Ok” button, the files will be copied and pasted into “your_current_project_path\data\SPM”. In parallel, the name “SPM/” is automatically provided to the input parameters “Topography file name”, as well as for the grid resolution (i.e., nx and ny, only work with iSOSIA files, Figure 3).

.. figure:: ../images/setTopography.png
  :scale: 50
  :align: center
  
  *Figure 5. "Topography" tab with the topography shown on the left-hand side, after clicking the "Show topogaphy" button.*
 

When loading a synthetic numerical model, you can let the latitude and longitude to zero. However, you need to provide the stepping distance in x (Δlon) and y (Δlat). For simplicity, you can provide the values in km and then click on ‘Convert to lat/long’ button (Figure 3). This will automatically convert the values to longitude and latitude distances that can be read by Pecube. Finally, you are able to check the topography you provided by clicking on “Show topography” (Figure 3). A new tab then appears on the right-hand side of the interface (Figure 5). This tab serves to visualize the topography and check your topography history as provided in the “Time evolution” part (see next section). You are indeed able to visualize the evolution of the topography by grabbing and sliding the slide bar in “Set time evolution” (Figure 5).


Time evolution tab:
-------------------

==================================

In this tab (Figure 6) you can provide all the parameters controlling the time evolution of the Pecube model (see Pecube user guide for more details). The particularity in PecubeGUI is that you can provide the time evolution parameters (cf. “time_topo”,” amplification”, “offset”, and “output”) by filling the table or by copying/pasting values from an excel file to the table. The number of rows in the table automatically adapts to the value written in the parameter “ntime” (Figure 5). 

.. figure:: ../images/Time_Evolution.png
  :height: 514
  :width: 594
  :align: center
  
  *Figure 6. "Time evolution" tab where to provide parameters related to the time evolution of the topography.*
  
| The default value for each parameter is also automatically provided. 
| The following tabs named “Thermal parameters” and “Data parameters” have similar widgets as presented so far. For text boxes simply click to edit the new value of the parameter.


Tectonic tab:
-------------------

==================================

|  This tab is related to the “Tectonic parameters” in the Pecube user guide. The tab comprises text boxes in the upper part and two tables at the bottom. To provide the input parameters, the tab is working as follow. You need to provide values for the input parameters “nfault”, “npoint”, and “nstep”. When provided, the size of the two tables will automatically adjust to provide the relevant parameters for the fault geometry (if any fault defined) and the kinematic of the model. 
| An example of inputs taking “EXMP4” in Pecube user guide as an example, is shown in Figure 6.

.. figure:: ../images/Tectonic_tab.png
  :height: 506
  :width: 613
  :align: center
  
  *Figure 7. "Tectonic" tab where to provide parameters related to kinematic of rock uplift. The "EXMP4" in the Pecube's user guide is used as an example of input.*
  
| When finishing to provide all three previous parameters, the tables updated. We see here that the first table on the left allows to set the geometry of the two faults, and the second one on the right, to define the fault kinematics (i.e., the negative values define an inverse fault, see Pecube user guide for more details). For each table the cells are sorted according to the fault (i.e., as shown by the fault name “fault 1, fault 2, …, fault_n”), to help the user to provide the characteristics of each. One can also decide to not define faults. In that case, “nfault” needs to be set to one and “npoint” to “-1”. Then, the number of steps (nstep) defines the kinematic of the entire model (uniform uplift). 
