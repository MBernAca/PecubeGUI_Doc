======================
Quick use of PecubeGUI
======================

.. _QuickPecube:

This part aims to provide a quick overview on how to provide paramaters to run Pecube as is usually done with terminal. For more details about extended tools provided with PecubeGUI, please refer to :doc:`Usage`.

---------------------------
Create a new Pecube project
---------------------------

To create and run a new Pecube project, go to *New input file* or press *Crtl+N* (*3*, see :doc:`introduction`),
a widow pops up and ask you to provide the name of the new project (Figure *2*). After clicking the “Ok” button (Figure *2*),
you will be able to provide and set all the Pecube input parameters for your project.
  
.. figure:: ../images/New_Project.png
  :scale: 30
  :align: center

  *Figure 2. Enter a new project name. This window shows up when clicking on the "New input file" action.*


The window should look like the Figure *3*. On the top left, you could find and access all the projects you have loaded into the interface,
and thus navigate through their respective parameters. The right part of the interface will host extra input parameters described in :doc:`Usage`.

.. figure:: ../images/Input_Parameters_interface.png
  :align: center

  *Figure 3. Tab to set up the input parameters for Pecube. On the top left, you can check the name of your project (here: ‘PeGUI’)*
  
  
The input parameters are gathered into categories as referenced in the Pecube’s user guide. All the parameters are sorted in *9* categories: *Topography*, *Time evolution*, *Thermal*, *Data*, *Tectonic*, *Output*, *Isostasy*, *Inversion*, and *Miscellaneous* parameters. For more details on the meaning of each input parameter please refer to the Pecube’s user guide. However, you could access to a short description of each parameter by simply flying the mouse cursor over the parameter labels. After one second a text should appears describing the parameter.

--------------------------
Providing input parameters
--------------------------

Topography tab
--------------

==================================


| When providing the project name, you will automatically be directed to the first tab that presents the "Topography" parameters (Figure 3). All the default values of the input parameters are shown, so that you do not need to provide them if you want to keep these default values. If you wish to change a parameter, simply click on the text box, and write your value. 
| PecubeGUI offers the possibility to simply load topographic file(s), you could find more details in :doc:`Usage`.

| When loading a synthetic numerical model, you can let the latitude and longitude to zero. However, you need to provide the stepping distance in x (Δlon) and y (Δlat). For simplicity, you can provide the values in km and then click on ‘Convert to lat/long’ button (Figure 3). This will automatically convert the values to longitude and latitude distances that can be read by Pecube. Finally, you are able to check the topography you provided by clicking on “Show topography” (Figure 3). A new tab then appears on the right-hand side of the interface (Figure 5). This tab serves to visualize the topography and check your topography history as provided in the :ref:`Time-evolution-tab`. You are indeed able to visualize the evolution of the topography by grabbing and sliding the slide bar in “Set time evolution” (Figure 5).

.. _Time-evolution-tab:

Time evolution tab
--------------------

==================================

In this tab (Figure 4) you can provide all the parameters that control the time evolution of the Pecube model (see Pecube user guide for more details). The particularity in PecubeGUI is that you can provide the time evolution parameters (cf. “time_topo”,” amplification”, “offset”, and “output”) by filling in the table or by copying/pasting values from an excel file to the table. The number of rows in the table automatically adapts to the value written in the parameter “ntime” (Figure 4). 

.. figure:: ../images/Time_Evolution.png
    :scale: 30
    :align: center

    *Figure 4. "Time evolution" tab where to provide parameters related to the time evolution of the topography.*

| The default value for each parameter is also automatically provided. 

.. _Thermal-tab:

Thermal tab
-------------------

==================================

| In the :ref:`Thermal-tab`, you will find all the parameters to set the thermal properties of the crust and the atmosphere. In PecubeGUI, the user is able to check for the 1D steady-state geotherm by simply clicking on "Show Geotherm" (see :doc:`Usage` for more details). 

Tectonic tab
-------------------

==================================

| This tab is related to the “Tectonic parameters” in the Pecube user guide. The tab comprises text boxes in the upper part and two tables at the bottom. To provide the input parameters, the tab is working as follow. You need to provide values for the input parameters “nfault”, “npoint”, and “nstep”. When provided, the size of the two tables will automatically adjust to provide the relevant parameters for the fault geometry (if any fault is defined) and the kinematic of the model. 
| An example of inputs taking “EXMP4” in Pecube user guide as an example, is shown in Figure 5.

.. figure:: ../images/Tectonic_tab.png
  :scale: 30
  :align: center
  
  *Figure 5. "Tectonic" tab where to provide parameters related to kinematic of rock uplift. The "EXMP4" in the Pecube's user guide is used as an example of input.*
  
| When finishing to provide all three previous parameters, the tables updated. We see here that the first table on the left allows to set the geometry of the two faults, and the second one on the right, to define the fault kinematics (i.e., the negative values define an inverse fault, see Pecube user guide for more details). For each table the cells are sorted according to the fault (i.e., as shown by the fault name “*fault 1*, *fault 2*, …, *fault_n*”), to help the user to provide the characteristics of each. One can also decide to not define faults. In that case, “nfault” needs to be set to "1" and “npoint” to “-1”. Then, the number of steps (nstep) defines the kinematic of the entire model (uniform uplift). 

.. _Output-tab:

Output tab
-------------------

==================================

This tab enables the user to set the outputs he/she wants that Pecube provides at the end of the model run. The first part (i.e., “Compute ages”) let you choose between three options:

*	*none*: Pecube will not predict any thermochronological ages
*	*for all nodes*: Pecube will predict thermochronological ages for all nodes at the surface of the Pecube model. This option will enable you to check any boxes in the next part (i.e., “Thermochronological systems”) and to choose the thermochronological system you are interested to use. 
*	*sample specific*: Pecube will predict thermochronological ages only for specific sample locations provided by the user. For this option to work, you will need to provide a folder name where PecubeGUI will write some files that will be used by the Production-diffusion model. This has to be done in the *Data tab* in the “Data folder” text box. In the current version, only the AHe system can be selected. PecubeGUI uses the production-diffusion model developped by [Gautheron-et-al-2010]_.

| Fore more details on how to provide parameters to predict ages at specific locations, see :doc:`Usage`.

The remaining tabs do not need details description. Simply fill the text boxes with your new values. The details for each input parameters can be found in the Pecube user guide, and short descriptions can be seen when flying the mouse cursor over the label of each parameter.


------------------
Run a Pecube model
------------------

| To run a Pecube model, simply click on “Run Pecube” above the tabs (Figure 5). A new window pops up. According to your Preferences (cf. ‘2’, Figure 1) the latter will only show a progress bar of the Pecube run or additional information are provided if the console is enabled.

| PecubeGUI first runs Pecube as usual, and if the option “sample specific” is set (cf, previous section). When the console is allowed to be shown, the state of the runs is written within it. At the end of the Pecube run, this window displays ‘Pecube run is finished!’ and you can click on the ‘Ok’ button to close the window.

.. note::
  When several projects are opened, the consoles are gathered in a single window to have a quick overview of all the running simulations.
