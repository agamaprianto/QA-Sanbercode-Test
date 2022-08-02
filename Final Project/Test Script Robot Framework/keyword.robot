*** Settings ***
Library         SeleniumLibrary

*** Variable ***
### Var Login ###
${url}      https://opensource-demo.orangehrmlive.com/
${username}     id=txtUsername
${password}     id=txtPassword  
${nama}     Admin
${sandi}    admin123
${btnLogin}     id=btnLogin
### var Menu Admin ###
${btnAdmin}        id=menu_admin_viewAdminModule
${dropdownUserManagement}    id=menu_admin_UserManagement
${dropdownUser}              id=menu_admin_viewSystemUsers
#btn#
${btnAdd}              id=btnAdd
${btnSave}             id=btnSave
#Inputan#
${EmployeeName}        Admin A
${UserNameAdd}            agam12345
${Password}            Agam12345#
#ID#
${EmployeeNameId}        id=systemUser_employeeName_empName
${UsernameId}            id=systemUser_userName
${PasswordId}            id=systemUser_password   
${ConfirmPasswordId}     id=systemUser_confirmPassword
#Var Search User#
${SearchUser}        id=searchSystemUser_userName
${dropdownUserRole}        id=searchSystemUser_userType
${SearchEmployeeName}        id=searchSystemUser_employeeName_empName
${dropdownStatusUser}        id=searchSystemUser_status
${btnSearch}                id=searchBtn

*** Keywords ***
TC_Login
    Open Browser    ${url}          gc
    Input Text      ${username}     ${nama}
    Input Text      ${password}     ${sandi}
    Click Element   ${btnLogin}

Menu Admin
    Click Element    ${btnAdmin}
    Click Element    ${dropdownUserManagement}
    Click Element    ${dropdownUser}
    