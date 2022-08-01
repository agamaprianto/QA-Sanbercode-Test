*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Update Status
    Click Element    locator
    Input Text    locator    text
    Click Element    locator