*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Add Employee
    Click Element    id=menu_pim_viewPimModule
    Click Element    id=menu_pim_addEmployee
    Input Text    id=firstName    Agam    
    Input Text    id=middleName    apri  
    Input Text    id=lastName    anto
    Input Text    id=employeeId    0101
    Click Element    id=btnSave