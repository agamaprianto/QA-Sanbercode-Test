*** Settings ***
Library         SeleniumLibrary
Resource        keyword.robot 

*** Test Cases ***
Open Browser
    TC_Login
Add Assign
    Click Element    id=menu_leave_viewLeaveModule
    Click Element    id=menu_leave_assignLeave
    Input Text    id=assignleave_txtEmployee_empName    agam123
    Click Element    id=assignleave_txtLeaveType
    Click Element    //option[contains(text(),'US - Personal')]
    Input Text    id=assignleave_txtFromDate    2022-08-02
    Input Text    id=assignleave_txtToDate    2022-08-07
    Input Text    id=assignleave_txtComment    test 05
    Click Element    id=assignBtn