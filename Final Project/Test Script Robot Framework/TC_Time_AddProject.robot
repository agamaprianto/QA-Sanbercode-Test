*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Add Project
    Click Element    id=menu_time_viewTimeModule
    Click Element    id=menu_admin_ProjectInfo
    Click Element    id=menu_admin_viewProjects
    Click Element    id=btnAdd
    Click Element    id=addCustomerLink    
    Input Text    id=addCustomer_customerName    agam
    Click Element    id=dialogSave
    Input Text    id=addProject_projectName    agam123
    Input Text    id=addProject_projectAdmin_1    Admin A
    Input Text    id=addProject_description    test QA
    Click Element    id=btnSave