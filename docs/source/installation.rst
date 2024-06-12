.. _installation:


Install PecubeGUI
=================

Get PecubeGUI
-------------

| PecubeGUI-beta is now available ! This version has been tested for bugs and stability, and is close to its first official release. However, you might still face some unnoticed crashes/bugs. If it happens, please do not hesitate to report it here:  https://github.com/MBernAca/PecubeGUI_Doc/issues.

| We release this version to give the community a first appreciation of PecubeGUI. 


MacOS
---------

Two packages exist for PecubeGUI-beta on MacOs. For MacOs with Apple chip M1 or M2, and for MacOS with intel chip. For the latter, PecubeGUI only work for Os version >11 (BigSur).

You can download the package on this page: http://erc-cooler.eu/portfolio-Maxime_PecubeGUI.html

To use PecubeGUI on macOS, first install the pakage by clicking on the PecubeGUI.pkg.
An installation process window will appear, you just have to follow the steps.

.. note::
 When trying to open the package, the system might complain saying it cannot open it because it is not registered in the Apple Store. To circumvent this, just roght click on the package, click 'open', and accept to open anyway (after the warning).

| With this installation package you can run Pecube forward models, however you will not be able to run in inversion mode. To do this, you will need the mpi package and to recompile Pecube. While procedures can vary from systems, here are some instruction to install mpi and compile Pecube:

  * open a terminal console
  * If you do not have homebrew installed, write: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)", otherwise skip this step.
  * Install gcc: brew install gcc
  * Install mpi: brew install open-mpi
  * Compile Pecube: go to Pecube directory -> cd /path-to-Pecube/  -> write: ./bin/compile.sh


Windows
-----------

You can download the package on this page: http://erc-cooler.eu/portfolio-Maxime_PecubeGUI.html

After downloading the PecubeGUI_installer.exe file, clicking on it will start an installation process. You just have to follow the instructions and PecubeGUI will be installed on your local machine.


.. important::
  In the current version, you need to keep the *Pecube* directory where it is installed by the installation process. In a later version, you will able to move the Pecube directory to another location in you computer. Thus, the next time you will open PecubeGUI, it will simply ask you to locate the Pecube directory at its new location. This functionality will enable the user to dowload and update PecubeGUI without erasing the *Pecube* directory where all the Pecube projects are stored.


| With this installation package you can run Pecube forward models, however you will not be able to run in inversion mode. To do this, you will need the mpi package and to recompile Pecube. While procedures can vary from systems, here are some instruction to install mpi and compile Pecube:

  * Download Msys2: https://www.msys2.org/
  * Open MSYS2 MINGW
  * Write: pacman -S mingw-w64-x86_64-gcc-fortran
  * Write: pacman -S mingw-w64-x86_64-msmpi
  * Write: pacman -S make
  * install mpi for the Windows console: https://www.microsoft.com/en-us/download/details.aspx?id=57467.
  * Go to your Pecube directory within the terminal: cd path-to-Pecube-directory/
  * write: ./bin/compile.sh



How to cite
------------

 If you use PecubeGUI for your research please cite: M. Bernard, P. van der Beek, J. Braun, X. Robert, C. Colleps, K. Gallagher, W. Guenthner, J. Amalberti, & I. Wapenhans. (2023). PecubeGUI-beta (1.0.0-beta). Zenodo. https://doi.org/10.5281/zenodo.8362722
