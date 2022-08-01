*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Search Directory
    Click Element    id=menu_directory_viewDirectory
    Input Text    id=searchDirectory_emp_name_empName    Admin A
    Click Element    id=searchDirectory_job_title
    Click Element    //option[contains(text(),'Automation Tester')]
    Click Element    id=searchDirectory_location
    Click Element    //body/div[@id='wrapper']/div[@id='content']/div[1]/div[2]/form[1]/fieldset[1]/ol[1]/li[3]/select[1]/option[1]
    Click Element    id=searchBtn