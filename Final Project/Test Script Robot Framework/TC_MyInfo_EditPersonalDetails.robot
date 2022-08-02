*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Edit Personal Details
    Click Element    id=menu_pim_viewMyDetails
    Click Element    id=btnSave
    Input Text    id=personal_txtEmpFirstName   QA
    Input Text    id=personal_txtEmpLastName   Sanbercode
    Input Text    id=personal_txtLicenNo    31730504971000
    Click Element    id=btnSave