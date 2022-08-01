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
    Click Element    locator
    Input Text    locator    text
    Input Text    locator    text
    Click Element    locator
    Input Text    locator    text
    Input Text    locator    text
    Input Text    locator    text
    Click Element    locator