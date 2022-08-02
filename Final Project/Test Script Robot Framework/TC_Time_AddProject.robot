*** Settings ***
Library         SeleniumLibrary
Library    DateTime
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Add Project
    Click Element    id=menu_time_viewTimeModule
    Click Element    id=menu_admin_ProjectInfo
    Click Element    id=menu_admin_viewProjects
    Click Element    id=btnAdd  
    Input Text    //input[@id='addProject_customerName']    apri123
    Input Text    id=addProject_projectName    agam123
    Input Text    //input[@id='addProject_projectAdmin_1']    Admin A
    Input Text    id=addProject_description    test QA
    Click Element    id=btnSave