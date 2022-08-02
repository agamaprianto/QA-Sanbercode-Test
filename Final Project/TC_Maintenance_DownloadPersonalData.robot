*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Download Personal Data
    Click Element    id=menu_maintenance_purgeEmployee
    Click Element    id=menu_maintenance_accessEmployeeData
    Input Text    id=confirm_password    agam123
    Click Element    //input[@id='']
    Input Text    id=employee_empName    Admin A
    Click Element    //input[@id='']
    Click Element    id=btnDelete
    