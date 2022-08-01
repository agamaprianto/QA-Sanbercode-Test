*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Download Personal Data
    Click Element    locator
    Click Element    locator
    Input Text    locator    text
    Click Element    locator
    Input Text    locator    text
    Click Element    locator
    Click Element    locator
    