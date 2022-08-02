*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Create Job Titles
    Click Element    ${btnAdmin}    
    Click Element    id=menu_admin_Job
    Click Element    id=menu_admin_viewJobTitleList
    Click Element    ${btnAdd}
    Input Text    id=jobTitle_jobTitle            Quality Assurance
    Input Text    id=jobTitle_jobDescription      Testing Software
    Input Text    id=jobTitle_note                Test 001
    Click Element    ${btnSave}