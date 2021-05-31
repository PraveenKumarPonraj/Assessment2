ASSESSMENT -2
           
  INTRODUCTION:    
        This Project is all about there will be a Non-Profit School where the Fees from the students is only used 
        to pay the teachers and the other non-teaching staff. We have to maintain the students' attendance, where 
        they have to pay some amount if they take a day off in a month. If the teachers take a day off some amount
        will be deducted from their salary, same case for the non-teaching staff. We have to get the attendance 
        for 10 daysand calculate the fees for the students and the salary for the teachers and non-teaching staff.

                                                   We can also assume any salary and fees for them and the salary
        for teachers and non-teaching staff varies.In the end of the calculation, no money has to be left with the 
        school is the target of the solution. Whatever the fees are paid has to be converted to salaries.


  Resources:
                The recommended way to install Connector/Python is via pip.
                Make sure you have a recent pip version installed on your system. 
                If your system already has pip installed, you might need to update it. 
                Or you can use the standalone pip installer.

                INSTALL-> pip install mysql-connector-python
                Please refer to the installation tutorial for installation alternatives.
  Additional Resources:
            1.mysql Connector
            2.Python Forum
            3.mysql workbench
            4.mysql client command line


HOW TO INSTALL THE PROJECT:
                 1.Install Git Version Control [ https://git-scm.com/ ]

                 2.Install Python Latest Version [ https://www.python.org/downloads/ ]

                 3.Install Pip (Package Manager) [ https://pip.pypa.io/en/stable/installing/ ]

Installation
1. Create a Folder where you want to save the project

2. Create a Virtual Environment and Activate

Install Virtual Environment First
$  pip install virtualenv


Create Virtual Environment
$  python -m venv venv


Activate Virtual Environment
$  source venv/scripts/activate

CLONE THE PROJECT 


FEATURES:
To Display Student Details
To Display Staff Details
To Display Student Attendance
To Display Payment Details

EXPLANATION:
STEP-1:
      First we have to import mysql Connector as global and enter the hostname,username,password,and DB name to connnect 
      to the mysql server

STEP-2:
      We declare different functions to implement the process.
      First one is (STUDENT_DETAILS )this function is used to display 
      all the details of students like their ID,name,department and their 
      Fees amount
STEP-3:
      Next function is (STAFF_DETAILS)this function is used to display 
      all the details of Staffs like their ID,name,department,attendance
      and their LOP amount.
STEP-4:
      Next function (Student_Attendance) In this function we trace the 
      students attendance for 10 days and update it into a  table.
      If the students takes leave then they have to pay the fine amount
      and that also calculated and stored in a table.
STEP-5:
      (PAYMENT_DETAIL)  IN this function we solving the total  calculation
      from the remiaing tables according to the attendace of the staff their 
      salary amount has been credited and make sure that no money has to be left with the 
      school is the target of the solution. Whatever the fees are paid has to be converted to salaries.