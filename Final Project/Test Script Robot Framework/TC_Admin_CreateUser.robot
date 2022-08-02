*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Create User
    Click Element    ${btnAdmin}
    Click Element    ${dropdownUserManagement}
    Click Element    ${dropdownUser}
    Click Element    ${btnAdd}
    Click Element    id=systemUser_userType
    Click Element    //option[contains(text(),'Admin')]
    Input Text       ${EmployeeNameId}               ${EmployeeName}
    Input Text       ${UsernameId}                   ${UserNameAdd}
    Click Element    id=systemUser_status
    Click Element    //option[contains(text(),'Disabled')]
    Input Text       ${PasswordId}                   ${Password}
    Input Text       ${ConfirmPasswordId}            ${Password}
    Click Element    //input[@id='btnSave']