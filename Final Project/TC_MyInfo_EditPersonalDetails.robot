*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Edit Personal Details
    Click Element    locator
    Click Element    locator
    Input Text    locator    text
    Input Text    locator    text
    Input Text    locator    text
    Click Element    locator