###################
Active developments
###################


.. _developments:

.. rst-class:: section-header

PecubeGUI
*********


*Installation*
--------------

| A new installation method is currently under developments for the PecubeGUI package. Pecube and the user interface, will be installed via Pip and/or conda-forge environment. This new approach
will simplify both the installation of the user interface but also the installation of Pecube as well as its compilation.

| Scheduled release: November-December 2026.




Pecube 
******

*Trapped-charge predictions*
----------------------------

| The implementation of trapped-charge (TC) dating techniques in Pecube is currently under active development.
TC techniques provides the temporal resolution to constrain Quaternary-scale rock exhumation and landscape evolution. By coupling trapped-charge kinetics with the thermal histories predicted by Pecube,
modeled ages can be directly compared with observed luminescence and ESR data.
| TC dating methods are based on the accumulation of radiation-induced electrons and holes within defects in mineral crystal lattices. 
The trapped-charge population evolves through time as charges are both captured and released, with the rate of charge loss controlled by temperature. As a result, these systems record
the near-surface thermal history of rocks and sediments over timescales ranging from thousands to millions of years.

| Three trapped-charge systems are being incorporated into Pecube:

* *Thermoluminescence (TL)*, which measures light emitted during laboratory heating as trapped charges are released.
* *Optically and Infrared Stimulated Luminescence (OSL/IRSL)*, which use optical stimulation to quantify trapped-charge populations.
* *Electron Spin Resonance (ESR)*, which measures trapped charges through their paramagnetic signatures.

| The integration of these methods within Pecube will provide a unified framework for modeling both trapped-charge and conventional thermochronometric systems,
enabling improved constraints on recent exhumation rates, transient erosion events, and the thermal evolution of the shallow crust during the Quaternary.
| to know more about trapped-charge techniques: https://www.sciencedirect.com/science/article/pii/S0009254116304004

| Scheduled release: Early 2027

*IGM-Pecube coupling*
---------------------

| Pecube's code will be reformated as a modular fortran library to enable coupling Pecube with any landscape evolution model. Within the year 2027,
Pecube will be coupled with the glacial landscape evolution model IGM (Jouvet and Cordonnier, 2023) within the Swiss National fundation funded project "How (do) glaciers buzzsaw?" (grant number: 10008344).

| Scheduled release: Late 2027 - Early 2028
