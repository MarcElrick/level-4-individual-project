## 30 Sept 2020

- (3.5 minutes) Presentation on the basics of isotopic labelling, how it works, with beer brewing example - By using isotopic labelling, we can see how the consumption of different isotopes affects the production of a product we are interested in.
- (1 minute) Mention of who I will be working with and the motivation behind the project - Dr Phil Whitfield and UHI PHD student, looking to automate isotope labelling process.
- (2.5 minutes) Discussion re. python prototype and which possible technology stacks we can use to provide a GUI for biologists. Deployed web interface? Java application? interface?
- (9 minutes) Presenting example of the data that we are dealing with and format of Liquid Chromatography Mass Spectrometry input data that needs to be analysed. Discussion of the entire process from input, to how data is analysed/processed to required output.
- (2 minutes) Looking at maximum intensity can be easier than peak picking as a strategy, as well as being much faster than peak picking.
- (1 minute) Discussion of understanding of the entire process and where to find resources - Git repo
- (2 minutes) Discussed possibility of using university domain to host, as well as packaging a python project, or dockerised web app. Uploading files to a web app could cause delays as input files are large.
- (1 minutes) Discussion of plan going forward - get to grips with project, email introduction to clients
- (1 minute) Brief discussion regarding clients/points of contact, and paper describing kinetic curve fitting.

## 6 Oct 2020

- (1 minute) - discussion of my understanding of the chemistry.
- (8 minutes) - discussion of my understanding of the software process behind extracting data.
- (3 minutes) - outline of my development plan going forward.
- (2.5 minutes) - outline technology choices.
- (2 minutes) - discussion of libraries that I found in protoptype pipeline and whether or not they are needed.
- (1.5 minutes) - discussion of the aims of the experiments and what scientists are interested in(key point - manipulating charges is done by either adding a proton/removing an electron)
- (3 minues) - discussion surrounding newly available data files.
- (3 minutes) - discussion of changes that are required in prototype pipeline.
- (3 minutes) - Plan going forward: Complete tasks for week 3 in project plan, organise meeting with Phil and Nicole for some time next week.

## 13 Oct 2020

- No meeting this week. Progress update sent to supervisor.

## 20 Oct 2020

- (**5 minutes**) Showing progress mentioned in last weeks report and showing overall GitHub Repo.
- (**2 minutes**) Overview of PyInstaller and the various packaging methods.
- (**4 minutes**) Discussion of progress compared with project plan. Discussion of multiple lipid functionality.
- (**7 minutes**) Presentation of wireframes, in depth discussion about required changes.
- (**2 minutes**) Discussion surrounding GUI tests, concluded that they are probably unnecessary. Also discussed the possibility of trimming down test files to speed up test suite.
- (**2 minute**) Discussion of this weeks plan.
- (**3 minute**) Discussion about the usage of mass-spec-utils, concluded that I should make PRs for proposed changes.
- (**3 minutes**) - Discussion of stretch goal - can we have a graphical view that allows user to click points and move those points to adjust retention time and mass tolerance.

## 27 Oct 2020

- Overview and demonstration of this weeks progress.
  - Mass entry could be done with an override checkbox, by default mass field is greyed out, and when checkbox is clicked, mass field becomes editable. This will remove temptation to change computed mass unless necessary
- MacOS application tested and appears to run well
- Discussion of tests for page1 state - we agree that testing a basic class with variables and setters was not worth doing.
- Discussion of meeting next week
  - I shall organise a meeting with Phil, Nicole, Simon and Ronan Daly, proposing 9.30am next week.

## 3 Nov 2020

- Progress update
- Discussion of my questions:
  - If ppm, convert to Da for every mass value.
  - How many decimal places for mass - four to six will be enough for display purposes, although should still use full value in calculation.
- Ask about importance of mass override. - it could make things very difficult if we are overriding for one isotope and not for others.
- Suggestions
  - Adding adducts - allow biologists to add their own adducts/deducts to a finite list
  - Name adducts - allow biologists to name adducts to make them easier to find.
  - Proteowizard - use MS convert to cut files down to a very small size for running tests.
  - pymzml - There may be a better structure to parse mzml files than previously used.
  - Potentially separate positive and negative adducts to pos/neg mode.
