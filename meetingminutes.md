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

# 11 Nov 2020

- Clear issues with current analysis - curve not being properly fitted, needs investigation.
- The 24 hour file is incorrect for this dataset.
  - This demonstrates why we may wish to allow the ignoring of a specific file.
  - Should we allow the choosing of files before lipids?
- Testing

  - Use outputs from prototype pipeline to find good outputs
  - There are various "warnings" we could presnet to the user if analysis is suspect i.e. if I0 intensity increases, bring it to the users attention.

- File being downloaded by adduct transformer - do I need it?
  - Irrelevant as we only need a small number of adducts, users can add their own adducts with values should they wish.

# 25 Nov 2020

- Discussion of the issue found that it was not actually a bug. I was simply entering very large values, causing the entire rt range to be considered, and so the monoisotopic intensity was always being chosen. Once normalised, this resulted in a straight line.

- I shall manage time as I see fit. There may potentially be no meeting next week dependent on progress

- Report table - have table on final page with lipids and files as rows/columns. Should analysis have any interesting warnings, we could double click on a particular table entry and be shown additional info on that particular lipid

# 18 Dec 2020

- **(5 mins) Progress update**
  - Discussion of lipid details screen - Users could potentially be defining large numbers of lipids and so another format may be better to accept entry(table or accordion view)
  - Likewise with summary screen.
  - Stretch goal - a method of saving previous runs so they can be run again - already in user stories/issues.
- **(2 mins) Plan**
  - Discussion of plan going forward.
  - Working through December/Jan, evaluating and dissertation planning in Jan, dissertation writing Feb/March.
  - **(1 min) -** discussion of remaining open issues.
- **(2 min) - Questions**
  - Discussion of the best kind of evaluation to carry out - quantitative metrics won't really work due to low participant count. Qualitative techniques such as think aloud walkthroughs would perhaps be best.

# 15 Jan 2021

- Presentation of updated progress
- Presentation of evaluation plan.
  - Discussion of timing - important not to take up too much of participants time, will aim for under 30 minutes.
- Discussion of ethics checklist
  - Ethics checklist should be signed by both student and supervisor ahead of evaluation.
- Discussion of cognitive walkthrough
  - Cognitive walkthrough would make a good evaluation technique.

# 22 Jan 2021

- Planned out diss structure, plan to start writing this weekend.
  - Can discuss each piece of dissertation once.
  - Good idea to get peers to read and see if they understand.
  - Should be written to be read by one of my peers.
  - Look at paper to find background work.
  - State of the art is doing it manually, and using excel to fit curve.
    - Show diagram of TOPPview values being put into table.
- Discussion of evaluation timing - no rush to get evaluations done at the moment. Don't chase replies for another week.
- Could have specific questions for Nicole during evaluation - e.g. How much time do you think this could have saved you?

# 5 Feb 2021

- Possibility of submitting a short paper to an open source venue.
  - Can refuse, write myself or delegate it to someone else.
- Progress update
  - Evaluations all completed, got good data and no real issues with them.
  - Started writing short "stubs" for each part of my dissertation, not ready for anything to be reviewed yet.

## 26 Feb 2021

- (**4** **minutes**) - presenting project update
  - Be careful about terminology - lipidomics vs metabolomics.
  - Images/diagrams would help a lot for understanding of the conditions, charges, etc
- (**3 minutes**) - discussion of name for software
  - Inferring isotopes is not correct phrase - perhaps "Lipid kinetics inference" instead - LiKIT/ LiKInS
- (**1 minutes**) - discussion of what to write for initial requirements gathering when everything was done through supervisor - just write what happened.
- (**1 minutes**) - discussion of web articles - no problem with referencing these.
- (**1 minutes**) - discussion surrounding manual analysis process and is it okay to use TOPPView as an example even though Nicole used XCalibur.

# 5 Mar 2021

- Presentation of progress update.

# 19 Mar 2021

- Motivations - focus more on tedious manual process over lipidomics.

- TOPPView figure - rather than screenshots, make a more abstract diagram to show the peaks and how they are extracted. Can then go into further detail i.e. "One would typically use software such as TOPPView or XCalibur to manually read peaks from each file"

# 2 Apr 2021

- Check functional vs non-functional requirements
- Discuss further isotopes, their distribution in nature
- Good, add further developments
- Presentation should stand up on its own while also being concise.
- Are my introduction and background sections correctly categorised? i.e I have lots of definitions within my introduction and don't really describe the problem until the background
  - **Moving lipids & lipidomics, isotopes & isotope labelling, mass spectrometry to background**
- Researchers are interested in the rate of reaction. Is this correct? Additionally, what is going into the reaction?
  - **Yes - reaction takes place within a biological system - labelled "food" is introduced and as the reaction takes place, the intensities of higher isotopes increase as food is metabolised.**
- The diagram you provided in feedback - should colour be used to codify the third dimension - i.e. it shall have straight lines
  - **Yes**
- Chapter summaries - considering leaving a list of terms at the end of introduction/background section. What are your thoughts?
  - **No problems**
- Professional conduct mark - Does that just come from you?
  - **Yes**
- General writing - how important is it and do you think mine is adequate.
  - **Good so far**
