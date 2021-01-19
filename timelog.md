# Timelog

- Lipid Isotope Inference Software
- Marc Elrick
- 2316291E
- Dr Simon Rogers

## Week 1

### 30 September 2020

- _0.5 hours_ Introductory meeting with project supervisor.
- _1 hour_ Review meeting recording and generate meeting minutes.

## 2 Oct 2020

- _1 hour_ Read academic paper sent by supervisor.
- _1.5 hours_ Cloned prototype repo and began trying to run the jupyter notebook, fixing import issues.
- _0.5 hours_ Copied project template from project moodle page and initialised it. with correct timelog, readme etc.

## 3 Oct 2020

- _1 hour_ - Planned out which libraries are required, by analysing Jupiter notebook.
- _1 hour_ - Researched available libraries in other languages. Pretty much decided on Python.
- _0.5 hours_ - Listened to meeting recording again and took notes of steps for software to follow.

## 4 Oct 2020

- _1.5 hours_ - Gone through prototype code and commented, based on my understanding of the procedure.
- _0.5 hours_ - Outlined agenda for next supervisor meeting(6 Oct 2020)

## 6 Oct 2020

- _0.5 hours_ - Supervisor meeting.
- _1.5 hours_ - Installed PyCharm and attempted to setup CI/CD for dissertation. currently getting errors.
- _0.5 hours_ - Reviewed earlier meeting and generated meeting minutes.
- _0.5 hours_ - Created initial python project structure.

## 7 Oct 2020

- _1 hour_ - Created python CI pipeline on github actions which runs tests on commits/merges if there are any changes in the src folder.
- _0.5 hours_ - Attempted to fix CI pipeline for latex with no success :(. I did however find out how to manually run CI so no longer need to make commits just to trigger runs.

## 9 Oct 2020

- _0.5 hour_ - Created user stories for both "MVP" as well as for potential further development.

## 10 Oct 2020

- _0.5 hour_ - Created PR template.
- _0.5 hour_ - Created commit message template(viewable in wiki)
- _1 hour_ - Messing around with Qt Designer.
- _2 hours_ - Created wireframes in Figma to show Dr Rogers/Nicole for review before getting started on GUI.
- _0.5 hours_ - Documented readme and Wiki.

## 11 Oct 2020

- _0.5 hours_ - Finally got CI working for Dissertation. It is now possible to download a PDF build artefact from CI.
- _0.5 hours_ - Created issues on github

## 12 Oct 2020

- _1 hour_- Got prototype pipeline working on my machine and created a PR into the original repository.
- _2 hours_ - Started messing around with PyQt and set up directory structure for GUI components. I think this will likely need to be redone later, all in one file.

## 13 Oct 2020

- _1 hour_ - Continued work developing GUI - now have a nice framework set up for switching between screens.
- _1 hour_ - Further GUI work - now have a solid grasp on PyQt and have an idea of state management procedure.

## 14 Oct 2020

- _1 hour_ - Further work on gui, now dynamically loading all screens on next/back and have capability for disabling buttons if no on_next/on_back arg is provided.
- _1 hour_ - Trying to decipher testing PyQt applications for which there is ZERO documentation :pensive:
- _2 hours_ - EUREKA! have successfully written my first gui test, hopefully the rest should come easily now.

## 15 Oct 2020

- _1 hour_ - Working on GUI tests. Now have tests that verify all next/back buttons take the user to the correct page.
- _0.5 hour_ - Investigating how I can run updated CI without pushing to master and breaking current CI - Github actions has no way to do this, and so the only solution is to change the default branch, run tests and change back.
- _0.5 hour_ - Investigating if GUI tests can be run on CI without being able to load the application - This may well be impossible.

  - Having spent too much time on this, I finally decided to avoid running gui tests in CI, and only run unit tests for now. GUI tests are still good to have, and I will run locally.

- _1 hour_ - Working on GUI tests. Now have tests that verify all next/back buttons take the user to the correct page.

- _3 hours_ - GUI development, almost have step1 page layout done. Also, retried pyInstaller and it seems to successfully create an executable for my application. Making custom components with custom styles.

- _1 hour_ - Have been debugging an issue whereby pyinstaller could not find CSS static file. I instead decided to hardcode the css within the python file. Since it will not be a large file, this is not _too_ bad a smell at the moment, although I may need to reevaluate later.

- _1.5 hours_ - Set up CI for Windows with PyInstaller.

## 20 Oct 2020

- _0.5 hour_ - Set up CI for MacOS with PyInstaller.

## 21 Oct 2020

- _1.5 hours_ - Implemented state management for lipid screen.
- _0.5_ - Completed lipid screen for now.

## 22 Oct 2020

- _2 hours_ - Began implementing step 2 form(pick files). Having issues figuring out state management, as I need a way to add an unknown number of files. Enough for today.

## 24 Oct 2020

- _1 hour_ - Further implementation of file picker screen. Can now add rows correctly, as well as changing screen and rebuilding the UI. There is however an issues with deleting widgets(Qt layouts are not designed for this, so I think I need to switch to a QListWidget to properly handle deleting elements.)
- _1 hour_ - QListWidget was not suitable, as it is designed for one line, textual items. I finally managed to get it working by redrawing the entire panel on delete. I now have everything working statefully. Likely some refactoring needed, as some of the code is a bit cursed.

- _2 hours_ - More work on file picker screen. Form is fully working now and almost ready to close issue. While writing unit tests, I have realised that the way in which I store the index within pairings is not optimal, and things could easily go wrong with it. Looking at ways to remove it.

- _0.5 hours_ - Refactored so that index value is no longer explicitly stated. Removing this variable greatly reduces likelihood of error (before, pairings were in the form [filename, time, index], now index is not required)
- _0.5 hours_ - Completed unit tests for FileInputScreenState. I have opted not to write unit tests for LipidDetailsScreen, given that all methods are setters. There are no methods with any complex interactions.

## 25 Oct 2020\_

- _1 hour_ - Fixed a newly introduced bug in FilePickerScreen. The cause of this was that lambda functions evaluate their arguments when they are called, not when they are declared, and so the last item was always being deleted as that was the current value of the iterator variable i.
- _1 hour_ - Created a component that will display key-value pairs for the summary screen.

## 26 Oct 2020

- _3 hours_ - Almost completely implemented summary screen, correctly retrieving state from steps 1 and 2 by exposing a getter function, without making it possible to change anything in page 1 or 2 state.

## 27 Oct 2020

- _1 hour_ - Wrote unit tests and made visual improments to input summary screen.
- _0.5 hour_ - Implementing validation of lipid formula + mass calculation - Have added a red/green border round lipid field depending on if the formula entered is valid.

## 29 Oct 2020

- _1 hour_ - Next button is now disabled unless a valid formula is entered.
- _1 hour_ - Implemented monoisotopic mass calculation.

## 30 Oct 2020

- _1 hour_ - Added checkbox to manually override mass.
- _0.5 hours_ - Add file button now directly opens file dialog, removing a click.

## 31 Oct 2020

- _2.5 hour_ - Began work implementing lipid kinetics. Decyphering some code is proving challenging.

## 4 Nov 2020

- _2 hours_ - Continued work on lipid kinetics.

## 5 Nov 2020

- _2 hours_ - Further lipid kinetics work. Also created reduced test files, and figured out the cause of performance issues: AdductTransformer was downloading a file many times in its constructor, which was being called in a loop. By using a single AdductTransformer, we can do this much faster.

## 6 Nov 2020

- _1 hour_ - Further work on lipid kinetics - having issues where values are not being added to data matrix, trying to resolve.

## 7 Nov 2020

- _2 hours_ - Further work on lipid kinetics, full pipeline is now implemented. Now need to spend time working on tests for individual component functions.

## 8 Nov 2020

- _1 hour_ - Working on lipid kinetics tests. Added label property to lipids, need to add this ability on Lipid info page.

## 9 Nov 2020

- _1.5 hours_ - Writing tests for isotope pipeline - Have successfully written a test for get_max_mass which attempts to get the max value of a specific scan read from TOPPView.

## 10 Nov 2020

- _1 hour_ - Code cleanup
- _2.5 hours_ - Implemented importing adducts from csv file as well as calculating mass on fly when adducts change.

## 13 Nov 2020

- _2 Hours_ - Created form to add new custom adducts, as well as a menubar which can open this form or quit the application.

## 17 Nov 2020

- _1.5 hours_ - Hookd up form to write to csv files.
- _2 hours_ - Fixing issues with pyinstaller, namely that new values were not persistent. Had to switch to one-dir mode. Also removed unnecessary steps from builds.

## 18 Nov 2020

- _3 hours_ - Working on bug whereby all values in data matrix were being set to 0.2. I think this is being done when each row is normalised, and I think this may be because of floating point inaccuracies.

## 19 Nov 2020

- _0.5 hours_ - I hyave successfully identified, and partially rectified, the issue. A simple miss-indent was causing only the first isotope to be run.
- _1 hour_ - In actual fact, the issue was not a floating point error, but instead, was caused by an 'else' clause that was slightly unindented.
- _2 hours_ - Further work on lipid pipeline. Pleased to report that it is about ready to go, and I will soon start work on integrating with GUI.
- _2.5 hours_ - Work on integrating GUI with lipiid pipeline. We can successfully run from start to finish. Need to run analysis in a new thread and tie to progress bar.

## 20 Nov 2020

- _2.5 hours_ - Finished progress screen page. Loading bar increases as each file analysis is completed. Ready to merge.

## 9 Dec 2020

- _2 hours_ - Began preparing for switch to multiple lipids. Altered lipid screen state to accomodate for this.

## 11 Dec 2020

- _3 hours_ - Made GUI changes for multiple lipids - lipid forms are shown in a scroll area. Still need to link with state.

## 12 Dec 2020

- _2 hours_ - Final changes to lipid details screen - addition of label. Appropriate changes made to state.

- _3 hours_ - Complete reworking of summary screen with ScrollAreas and fixed to work with new lipid details screen.

- _1 hour_ - Fixed pipeline to work with multiple lipids.

## 13 Dec 2020

- _2 hours_ - Noticed that all pages are identical for multiple lipids. Attempted to find the cause but got nowhere.

## 14 Dec 2020

- _2 hours_ - Work on yesterday's bug - found it was caused by later lipid runs overwriting previous runs.

- _1 hour_ - Added console into progress screen to show what is happening within the analysis pipeline.

## 15 Dec 2020

- _1 hour_ - Re-implemented validation on lipid screen.
- _1 hour_ - Added restart button to progress screen.

## 16 Dec 2020

- _2 hours_ - Writing status report.

## 17 Dec 2020

- _2 hours_ - Finished rewriting unit tests.

## 19 Dec 2020

- _6 hours_ - Implemented multiple lipids making many changes throughout pipeline to accomodate this. Changes also required rewrites of lipid kinetics screen.

---

## Winter Break

---

## 28 Dec 2020

- _6 hours_ - Following final supervisor meeting, it was decided that another view style was required to make the software less unwieldy when working with lots of lipids. I therefore spent this time looking for a publicly available "collapsible" Qt widget that I could use. I found one publicly and it was as part of a pull request under an MIT license. I therefore decided to use and modify this for my own needs.

## 29 Dec 2020

- _2 hours_ - Yesterdays PR failed in CI - after running again, everything seems to have gone through without any problem. This is something to keep an eye on.

## 2 Jan 2020

- _2 hours_ - It turns out the previous tests were passing locally becuase I was running on another branch (duh). Spent time updating unit tests, as well as adding a few missing ones.

## 3 Jan 2020

- _1 hours_ - Triaged all dependencies to decide on a license and added license.

## 4 Jan 2020

- _5 hours_ - Fixed PyInstaller build. This was a massive issue and was very difficult to fix.

## 5 Jan 2020

- _2 hours_ - Added a release item to windows build. This should allow users to download and use for unit testing.

## 6 Jan 2020

- _5 hours_ - Implemented saving of lipid state.

## 7 Jan 2020

- _1.5 hours_ - Created new issues, created new branching strategy and separated build and release actions.
- _1.5 hours_ - Started implementing the selection of multiple files.

## 8 Jan 2020

- _2 hours_ - Finished implementing selection of multiple files.
- _3 hour_ - Fixed the validation mess of lipid details screen and fixed the custom Adduct form.

## 10 Jan 2020

- _0.5 hours_ - Spent some time cleaning up repo and merge PRs

## 11 Jan 2020

- _1 hour_ - Fixing mac build and linuc builds - had issues with the way pyinstaller works with mac. This may need revisited.
- _1 hours_ - Changed the default location of output files, output file now opened by default upon completion of analysis.

## 13 Jan 2020

- _3 hours_ - Spent time trying to fix mac build so that evaluation participants can use a mac.

## 14 Jan 2020

- _2 hours_ - Created powerpoint with evaluation plan. This will be used to give participants an idea of what to expect.

## 18 Jan 2020

- _3 hours_ - Attempted to fix mac build. This failed. I believe it may have something to do with Big Sur.

- _1 hour_ - Fixed bug where charge wasn't being preserved upon export/import. Also fixed bug where dialog windows were being preserved for export/import/new adduct.
