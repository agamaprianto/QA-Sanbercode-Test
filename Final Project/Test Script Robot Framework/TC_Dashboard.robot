*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Open TimeSheet
    Click Element    id=menu_dashboard_index
    Click Element    //tbody/tr[1]/td[3]/div[1]/a[1]/img[1]
    Input Text    id=employee    Admin A
    Click Element    id=btnView