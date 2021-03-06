### Local Repository Structure

The GTFS data is too big to be saved within this Github repo, so please set up your local project tree as shown below. Note that you will need to locally create two directories for Data and Results (e.g., saving graphs and their associated data):

```
Project/
|
|--- Data/
|	  |
|	  |--- madrid_metro/
|	  |
|	  |--- caltrain/
|	  |
|	  |--- nyc_subway/
|	  |
|	  |--- ...
|
|
|--- Results/
|
|--- Source/ <--- clone the Github Transitcat repo here!
```


### Source Code Structure

If you're curious, our source code is organized as follows:

```
README.md <--- This file.
|
DjangoSite/
|
|--- DjangoSite/ <--- Django settings.
|	  |
|	  |--- ...
|
|
|--- snapData/
|	  |
|	  |--- (Assorted Django files for handling URL mappings, views, form submissions, and the model.)
|	  |
|	  |--- Backend/ <--- Python scripts for creating SNAP networks, calculating criticality, and computing isochrones.
|	  |    |
|	  |    |--- ...
|	  |
|	  |--- templates/ <--- HTML templates for the application.
|	  |    |
|	  |    |--- ...
```