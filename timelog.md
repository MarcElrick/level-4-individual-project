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

- _1 hour_ - Continued work developing GUI - now have a nice framework set uo for switching between screens.
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
