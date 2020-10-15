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
- _1 hour_ - Trying to decypher testing PyQt applications for which there is ZERO documentation :pensive:
- _2 hours_ - EUREKA! have successfully written my first gui test, hopefully the rest should come easily now.

## 15 Oct 2020

- _1 hour_ - Working on GUI tests. Now have tests that verify all next/back buttons take the user to the correct page.

- _3 hours_ - GUI development, almost have step1 page layout done. Also, retried pyInstaller and it seems to successfully create an executable for my application. Making custom components with custom styles.

- _1 hour_ - Have been debugging an issue whereby pyinstaller could not find CSS static file. I instead decided to hardcode the css within the python file. Since it will not be a large file, this is not _too_ bad a smell at the moment, although I may need to reevaluate later.
