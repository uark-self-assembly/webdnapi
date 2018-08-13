# webdnapi
A Python API for writing analysis scripts to be used with WebDNA

### Usage
Using the API is simple, just import `webdnapi.files` to expose the file loading functionality

#### Project Settings:
Project settings are stored on a single JSON file

Load this file by calling the corresponding load function:

```python
import webdnapi.files

settings = webdnapi.files.load_project_settings()
```

The returned object will have the following attributes:
* `file_string` - complete contents of the loaded file for advanced use cases
* `execution_time` - the elapsed time the simulation has run for
* `name` - the name of the project specified by the user
* `script_chain` - the list of analysis script uuids to be executed by the server upon simulation completion
* `generation` - An object with the following attributes:
    * `arguments`  - commandline arguments needed to execute the generation script
    * `files` - files needed for generation
    * `method` - the chosen method for creating an initial configuration

#### Input:
Simulation settings are stored in this file

Load with the following syntax:

```python
import webdnapi.files

input_settings = webdnapi.files.load_input()
```

The returned object will have the following attributes:
* `file_string` - complete contents of the input file for advanced use cases
* `settings` - a key, value dictionary of all specified settings and their corresponding values

#### oxDNA Log:
The output of oxDNA which contains meta-info

Load with the following syntax:
```python
import webdnapi.files

log = webdnapi.files.load_log()
```
The returned object will have the following attributes:
* `file_string` - complete contents of the log file

#### Standard Output
The stdout of the oxDNA simulation which lists information each n-th step

Load with the following syntax:

```python
import webdnapi.files

stdout = webdnapi.files.load_stdout()
```

The returned object will have the following attributes:
* `file_string` - complete contents of stdout file
* `steps` - list of steps, each step holds its relevant output from the file

#### Sequence
The sequence file contains the bases of each strand being simulated

Load with the following syntax:

```python
import webdnapi.files

sequence = webdnapi.files.load_sequence()
```

The returned object will have the following attributes:
* `file_string` - complete contents of sequence file for advanced use cases
* `strands` - list of all strands

#### Topology
The topology file contains information on each nucleotide in the simulation

Load with the following syntax:

```python
import webdnapi.files

topology = webdnapi.files.load_topology()
```

The returned object will have the following attributes:
* `file_string` - complete contents of topology file for advanced use cases
* `nucleotide_count` - number of nucleotides in the simulation
* `strand_count` - number of strands in the simulation
* `nucleotides` - list of all nucleotides and their corresponding information

#### Energy
The energy file contains meta-information about energy states in the simulation

Load with the following syntax:

```python
import webdnapi.files

energy = webdnapi.files.load_energy()
```

The returned object will have the following attributes:
* `file_string` - complete contents of energy file for advanced use cases
* `time_steps` - list of time steps and their corresponding energy information

#### External Forces
The external forces file contains data on all user defined forces in the simulation

Load with the following syntax:

```python
import webdnapi.files

topology = webdnapi.files.load_external_forces()
```

The returned object will have the following attributes:
* `file_string` - the complete contents of the force file for advanced use cases
* `forces` - a list of force objects, each force contains its own key, value dictionary of its attributes

#### Trajectory
The trajectory files contain configuration information about the current simulation.  These files can be very large, 
so expect some performance impact depending on the size of your simulation.

You can load either the initial configuration or last configuration with the following functions:

```python
import webdnapi.files

first_configuration = webdnapi.files.load_trajectory_initial()
last_configuration = webdnapi.files.load_trajectory_last()
```

The returned object of either function will have the following attributes:
* `time_step` - the time_step of the loaded configuration
* `box_length_x`, `box_length_y`, `box_length_z` - the length of the sides of the simulation box
* `energy_total`, `energy_potential`, `energy_kinetic` - the energies of the simulation at the current time_step
* `nucleotides` - a list of nucleotide objects each with the following attributes:
    * `pos_x`, `pos_y`, `pos_z` - position coordinates of nucleotide
    * `base_v_x`, `base_v_y`, `base_v_z` - baseversor of nucleotide
    * `normal_v_x`, `normal_v_y`, `normal_v_z` - normalversor of nucleotide
    * `velocity_x`, `velocity_y`, `velocity_z` - velocities of nucleotide
    * `ang_velocity_x`, `ang_velocity_y`, `ang_velocity_z` - angular velocities of nucleotide
