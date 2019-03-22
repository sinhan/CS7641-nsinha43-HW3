code repository: 

https://github.com/sinhan/CS7641-nsinha43-HW3
---------------------------
Requirements:

You will need to use python 3.x with this code, and to pip install the packages in requirements.txt. 
The main addition here is the tables module which does require HDF5. 
If you are using OS X with Homebrew you can simply brew install hdf5 before installing the requirements.
----------------------------
Run the code:

1)python run_experiment.py --all
2)python run_experiment.py --plot
3)Update the dim values in run_clustering.sh based on the optimal values found in 2 (perhaps by looking at the scree graphs)
4)./run_clustering.sh
5)python run_experiment.py --plot
---------------------------
Output:

Output CSVs and images are written to ./output and ./output/images respectively. 
Sub-folders will be created for each DR algorithm (ICA, PCA, etc) as well as the benchmark.
---------------------------

Clustering Experiments:
The experiments will output modified versions of the data sets after applying the DR methods. 
The script run_clustering.sh can be used to perform clustering on these modified datasets, using a specific number of components for the DR method.

BE SURE TO UPDATE THE VALUES IN THIS SCRIPT FOR YOUR DATASETS.
---------------------------


