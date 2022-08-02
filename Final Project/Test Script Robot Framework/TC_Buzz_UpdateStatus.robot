*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Update Status
    Click Element    id=menu_buzz_viewBuzz
    Input Text    id=createPost_content    QA Sanbercode
    Click Element    id=postSubmitBtn