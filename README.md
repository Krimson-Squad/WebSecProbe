# WebSecProbe


[![krimson-squad - WebSecProbe](https://img.shields.io/static/v1?label=krimson-squad&message=WebSecProbe&color=red&logo=github)](https://github.com/krimson-squad/WebSecProbe "Go to GitHub repo")
[![stars - WebSecProbe](https://img.shields.io/github/stars/krimson-squad/WebSecProbe?style=social)](https://github.com/krimson-squad/WebSecProbe)
[![forks - WebSecProbe](https://img.shields.io/github/forks/krimson-squad/WebSecProbe?style=social)](https://github.com/krimson-squad/WebSecProbe)





[![GitHub tag](https://img.shields.io/github/tag/krimson-squad/WebSecProbe?include_prereleases=&sort=semver&color=red)](https://github.com/krimson-squad/WebSecProbe/releases/)
[![issues - WebSecProbe](https://img.shields.io/github/issues/krimson-squad/WebSecProbe)](https://github.com/krimson-squad/WebSecProbe/issues)

## Documentation

<div align="center">

[![view - Documentation](https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge)](/docs/ "Go to project documentation")

</div>

` THIS REPO/PROJECT IS MADE FOR DEVELOPMENT PURPOSE, YET TO BE DEPLOYED !`
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
### Logic
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
### Module structure
- Main modules
- Scanner modules
- Utility modules
- Config modules
- Report modules
- External modules
