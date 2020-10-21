# Lipid Isotope Inference Software

This repository contains my Glasgow University Level 4 Individual Project, as well as my dissertation and all related documentation.

## Initial Project Proposal

> "Isotope labelling is a common experimental technique for measuring the activity of a particular chemical pathway. There does not currently exist any easy to use open source software for analysing the resulting data. In collaboration with Glasgow Polyomics and The University of the Highlands and Islands, we have developed a prototype pipeline in Python. In this project, you would work with the clients (wet lab scientists) to turn this prototype into usable software including, for example, standard data input / output and a GUI."

## Running software

### Windows Executable

If you are on windows, then you can download a simple .exe file from the most recent CI build, located [here](https://github.com/MarcElrick/level-4-individual-project/actions?query=workflow%3A%22Package+application+with+PyInstaller%22). NOTE: The executable version has significantly longer startup time that running the application with python. Simply click on the downloaded file, ignore any warnings, and it should run.

### Python

Otherwise, you can run the software using any Python version >= 3.7.

#### Installation

1. Install Python >= 3.7
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

## Dissertation

The PDF version of the dissertation is not in version control, however the most recent build of the PDF can be downloaded from the artefacts section of the most recent build, located [here](https://github.com/MarcElrick/level-4-individual-project/actions?query=workflow%3A%22Build+LaTeX+document%22).

## Documentation

- [Timelog :timer_clock:](https://github.com/MarcElrick/level-4-individual-project/blob/master/timelog.md)
- [Project Plan :world_map:](https://github.com/MarcElrick/level-4-individual-project/blob/master/plan.md)
- [Meeting Minutes :spiral_notepad:](https://github.com/MarcElrick/level-4-individual-project/blob/master/meetingminutes.md)
- Design documentation available in the [wiki :open_book:](https://github.com/MarcElrick/level-4-individual-project/wiki)
