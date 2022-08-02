*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Download Personal Data
    Click Element    id=menu_maintenance_purgeEmployee
    Click Element    id=menu_maintenance_accessEmployeeData
    Input Text    id=confirm_password    admin123
    Click Button    div.box:nth-child(1) div.inner form:nth-child(1) div.row div.input-field.col.s12.m12.l4:nth-child(2) > input:nth-child(2)
    Input Text    id=employee_empName    Admin A
    Click Element    //input[@id='']
    Click Element    id=btnDelete
    