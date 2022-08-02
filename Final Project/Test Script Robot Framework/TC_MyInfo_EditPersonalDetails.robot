*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Edit Personal Details
    Click Element    id=menu_pim_viewMyDetails
    Click Element    id=btnSave
    Input Text    id=personal_txtLicenNo    31730504971000
    Input Text    id=personal_txtNICNo    123456789
    Input Text    id=personal_txtEmpNickName    agamapri
    Click Element    id=btnSave