# WebSecProbe
PRIVATE IN DEV REPO FOR WAVS FRAMEWORK
# Project: WAVS Framework in Python
## Objective of subject
`Web Application Vulnerability Scanning` using `Python` and browser automation libraries allowing efficient `scanning of web application`.
## Base Setup / Environment
- Python
- Beautiful Soup
## Identify possible vulnerabilities
- Automate the submission of form's payload
- log and analyze the response
## Session Handling
> Mainting session
## Crawling
- Extract other same domain/page url to be scanned.
## Reporting
- log response in a structural manner 
- give a referrence for the value
--
## Development Strategy
### Phases
  - [x] Planning
  - [ ] Design
  - [ ] Moduling
  - [ ] Coding
  - [ ] Packaging
  - [ ] Testing
  - [ ] Writing documentary
  - [ ] Advertising
## Logic
```
**Suite**
    |
    |
    v
**main file** <-------> [needed testing module (like:headermodule)]
         {collects logs}            /\|
                                     ||
                                     |v
                         [needed submodule(s) , like x-frame...]
                                    /\|
     returns response from the server|| sends/post request to server/page
                                     ||
                                     |v
                                   **[server]**
```
 
