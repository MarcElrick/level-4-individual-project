# User manual

## Install + Run

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

## Running With Real Data

Due to potential copyright and privacy concerns, full-size test files cannot be provided at this time. Instead, please run with the test file in this repository (located at `/src/tests/test_files`). Note that if you have downloaded the Windows executable, you will need to at least download these files from the GitHub repository.

## Entering Lipids

When entering lipid information, use the information from this table. Note that all test lipids are positively charged and so you will need to click the "Positive" radio button.

| Lipid Name | Lipid Formula | Adduct Formula | Number of Isotopes | Retenetion Time | RT Tolerance | m/z Tolerance | m\z Tolerance Units |
| ---------- | ------------- | -------------- | ------------------ | --------------- | ------------ | ------------- | ------------------- |
| PC 34:1    | C42H82NO8P    | [M+H]+         | 6                  | 660             | 20           | 5             | ppm                 |
| PC 34:2    | C42H80NO8P    | [M+H]+         | 6                  | 600             | 20           | 5             | ppm                 |
| PC 36:2    | C44H84NO8P    | [M+H]+         | 6                  | 638             |
| 20         | 5             | ppm            |

## Entering Files

As previously mentioned, choose files from `src/tests/test_files`. The associated time-points are simply the numbers at the start of the filename. Example: the timepoint for 72_pp_d20_pos_1.mzml is 72

## Defining Adducts

Variables for adduct calculations can be found [here](https://raw.githubusercontent.com/michaelwitting/adductDefinitions/master/adducts_pos.txt) and [here](https://raw.githubusercontent.com/michaelwitting/adductDefinitions/master/adducts_neg.txt) should you wish to define your own adducts.

## Things to Note:

- Output files **should** be opened automatically in the default `.xlsx` viewer on your system. Depending on system configuration, this may not happen. If this is the case, output files can be found at `\src\output\`
- The software has only been tested on Windows 10. While it should work on other systems (and has been run on MacOS during evaluations), stability cannot be guarenteed.
- The software occasionally crashes after output file has been created. This does not always happen and the cause of this is unknown but it does not affect the operation of the software (it just needs to be restarted between runs).
