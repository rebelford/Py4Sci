# Quantitative Structure Property Relationships

This material was developed by Ehren Bucholtz in 2019 as part of the Cheminformatics OLCC and can be obtained at this [LibreTexts link](https://chem.libretexts.org/Courses/Intercollegiate_Courses/Cheminformatics/05%3A_5._Quantitative_Structure_Property_Relationships). It uses an old version of mordred and so we need to create an environment that runs the old packages.  But, Conda has issues resolving the environment and so we are going to use a yml file to create the environment.

1. Got to the folder that contains `mordred_rdkit_env.yml`
2. Deactivate any conda environment and run the following script.<br>
  `conda env create -f mordred_rdkit_env.yml`<br>
This will create the mordred_env enviroment (open the yml file and see what is being created).
3. Activate the new environment (`conda activate mordred_env`)
4. Install and register the ipkernel within your new env
   `pip install ipykernel`
   ` python -m ipykernel install --user --name mordred_env --display-name "Python3.7 (Mordred)"`
6. Install matplotlib (`conda install matplotlib`)
7. Install statsmodels (`conda install -c conda-forge statsmodels`)
8. Now open QSPR.ipynb in your Jupyter lab and connect it to the Mordred kernel.