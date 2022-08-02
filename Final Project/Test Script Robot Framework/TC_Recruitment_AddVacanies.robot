*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Add Vacancies
    Click Element    id=menu_recruitment_viewRecruitmentModule
    Click Element    id=menu_recruitment_viewJobVacancy
    Click Element    id=btnAdd
    Click Element    id=addJobVacancy_jobTitle
    Click Element    //option[contains(text(),'Automation Tester')]
    Input Text    id=addJobVacancy_name    QA Tester
    Input Text    id=addJobVacancy_hiringManager    Admin A
    Input Text    id=addJobVacancy_noOfPositions    3
    Input Text    id=addJobVacancy_description    Test 04
    Click Element    id=addJobVacancy_status
    Click Element    id=btnSave