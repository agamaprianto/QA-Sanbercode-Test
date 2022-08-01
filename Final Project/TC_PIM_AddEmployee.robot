*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Add Employee
    Click Element    id=menu_pim_viewPimModule
    Click Element    id=menu_pim_addEmployee
    Input Text    locator    Agam    
    Input Text    locator    apri  
    Input Text    locator    anto
    Input Text    locator    0101
    Click Element    locator