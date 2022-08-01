*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Search Directory
    Click Element    locator
    Input Text    locator    text
    Click Element    locator
    Click Element    locator
    Click Element    locator