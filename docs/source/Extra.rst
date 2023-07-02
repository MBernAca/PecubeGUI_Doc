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
3. AHe flag, ZHe flag, AFT flag, KAr flag, BAr flag, MAr flag, HAr flag #Thermochronometer to compute 
4. do 4He/He3 ? (yes = 1; no = 0)
5. Number of events (Monte Carlo simulation)
6. Zonation ? (yes = 1; no = 0, not working in the current version)
7. Number of grain for each sample (each following line is for one sample)
8. Radius, U (ppm), Th (ppm), observed age (Ma), error (Ma) for each grain (each following line is for one grain)
9. Alpha Ejection model (dummy now), Ejection distances for alpha, Diffusion model, D0, Ea, rmr0 #AHe
10. Diffusion model, D0, Ea #Zircon
11. Annealing model, rmr0 #AFT
12. D0, Ea #Feldspar
13. D0, Ea #Biotite
14. D0, Ea #Muscovite
15. D0, Ea #Hornblende
