=====
Extra
=====

.. _Extra:


------------------
Sample_setting.txt
------------------

This file is located in the "data" directory of the Pecube's project main directory. This is where the relevant information for the Production-diffusion model are stored by PecubeGUI. Here is the significance of each line of the file.

1. Number of samples
2. Number of grains
3. nx, ny, Lat0, Long0, :math:`{\delta}`lat, :math:`{\delta}`lon, nskip
4. Diffusion model, D0, Ea, rmr0
5. do 4He/He3 ?
6. Number of events (Monte Carlo simulation)
7. Zonation ?
8. Number of grain for each sample (each following line is for one sample)
9. Radius, U (ppm), Th (ppm) for each grain (each following line is for one grain)
10. Number of step heating
11. Temperature (°C), Duration (hours) (each following line is for each step)
12. Length of the zonation array
13. Thickness of the layer, normalized concentration (each following lines is for the profile of grain i)
