*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
    Menu Admin
Search User
    Input Text        ${SearchUser}            ${UserNameAdd}
    Click Element     ${dropdownUserRole}
    Input Text        ${SearchEmployeeName}    ${EmployeeName}
    Click Element     ${dropdownStatusUser}
    Click Element     ${btnSearch}