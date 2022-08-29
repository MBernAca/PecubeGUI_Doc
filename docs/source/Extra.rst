.. _Extra:

=================
Extra information
=================

------------------
Sample_setting.txt
------------------

This file is located in the "data" directory of the Pecube's project main directory. This is where the relevant information for the Production-diffusion model are stored by PecubeGUI. Here is the significance of each line of the file.

1. Number of samples
2. Number of grains
3. AHe flag, ZHe flag, AFT flag #Thermochronometer to compute 
4. do 4He/He3 ? (yes = 1; no = 0)
5. Number of events (Monte Carlo simulation)
6. Zonation ? (yes = 1; no = 0)
7. Number of grain for each sample (each following line is for one sample)
8. Radius, U (ppm), Th (ppm), observed age (Ma), error (Ma) for each grain (each following line is for one grain)
9. Alpha Ejection model, Ejection distances for alpha, Diffusion model, D0, Ea, rmr0 #AHe
10. Diifusion model, D0, Ea #Zircon
11. Annealing model, rmr0 #AFT
12. Number of step heating
13. Temperature (°C), Duration (hours) (each following line is for each step)
14. Length of the zonation array
15. Thickness of the layer, normalized concentration (each following lines is for the profile of grain i)
