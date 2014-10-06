Rideshare Simulation
===========

This project was built by Telegraph Research to study the differences between dedicated and pooled ridesharing services. The results and report can be found [here](http://www.telegraphresearch.com/articles/).

## Getting Started
Please make sure that you have Python 3.4 installed on your machine. This version is required because some of the code uses the [Python statistics](https://docs.python.org/3/library/statistics.html) module.

## Customizing the Simulation

Most controls for the simulation are located in common.py. Here you can alter the timing system, vehicle and group variable distributions, and the number of vehicles used. If you wish to change the distribution of group size, that is located in group.py.

## Running the Simulation

Once you have set the variables in common.py, you can run the simulation by calling main.py.

```
python main.py
```

## Output and Analysis

Raw simulation data is saved in _output_. This just contains the log from each type of simulation for both vehicles and groups. To get important metrics of each vehicle, use analyze.py.

```
python analyze.py output/<filename> <analysis-output-name>.json
```

