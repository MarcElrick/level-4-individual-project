# Lipid Kinetics Inference Software

This repository contains my Glasgow University Level 4 Individual Project, as well as my dissertation and all related documentation.

## Initial Project Proposal

> "Isotope labelling is a common experimental technique for measuring the activity of a particular chemical pathway. There does not currently exist any easy to use open source software for analysing the resulting data. In collaboration with Glasgow Polyomics and The University of the Highlands and Islands, we have developed a prototype pipeline in Python. In this project, you would work with the clients (wet lab scientists) to turn this prototype into usable software including, for example, standard data input / output and a GUI."

## Running software

### Windows Executable

1. Download `lipid_isotope_inference.zip` from the [latest release](https://github.com/MarcElrick/level-4-individual-project/releases/latest).
2. Extract this file to a suitable location.
3. Open the extracted file and run `main.exe`.
4. Accept any security warnings and run.

### Python

If not on Windows 10, you can run the software using any Python version >= 3.7. It is advised that you create a Python virtual environment for this. There are guides for both vanilla [Python](https://docs.python.org/3/tutorial/venv.html) and [Anaconda](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/).

#### Installation

1. Install Python >= 3.7 (activate virtual environment if using one)
2. Clone this GitHub repository:

```bash
git clone https://github.com/MarcElrick/level-4-individual-project
```

3. Install requirements:

```bash
cd level-4-individual-project
pip install -r requirements.txt
```

4. Run:

```bash
cd src
python main.py
```

## Documentation

- [Timelog :timer_clock:](https://github.com/MarcElrick/level-4-individual-project/blob/master/timelog.md)
- [Project Plan :world_map:](https://github.com/MarcElrick/level-4-individual-project/blob/master/plan.md)
- [Meeting Minutes :spiral_notepad:](https://github.com/MarcElrick/level-4-individual-project/blob/master/meetingminutes.md)
- Design documentation available in the [wiki :open_book:](https://github.com/MarcElrick/level-4-individual-project/wiki)
