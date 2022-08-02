*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Create Key Performance Indikator
    Click Element    id=menu__Performance
    Click Element    id=menu_performance_Configure
    Click Element    id=menu_performance_searchKpi
    Click Element    id=btnAdd
    Click Element    id=defineKpi360_jobTitleCode
    Click Element    //option[contains(text(),'Automation Tester')]
    Input Text    id=defineKpi360_keyPerformanceIndicators    Testing with robot framework
    Input Text    id=defineKpi360_minRating    0
    Input Text    id=defineKpi360_maxRating    100
    Click Element    id=saveBtn