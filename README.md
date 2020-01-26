# Techweirdo
/* Python Backend Development */


This one is system solution to facilitate GlobalHR(one of the leading HR service providers) operations as described below :
      
      1. Design a database that will hold different clients of GlobalHR
      2. All clients will have some Users
      3. Users will be arranged in organizational hierarchy
      4. Api which will take an employee id to return (in JSON) all his superiors in the organizational hierarchy serially


Example : -
if the hierarchy is as follows

                  emp id (1)
            empid(2)      emp id(3)
      emp id (4, 5, 6)      empid(7, 8, 9)


if user inputs 8 - the api will return :

    {
        "hierarchy" : [1, 3, 8]
    }

=======================================================================================

important modules:
      
      pip install mysql-connector
      pip install flask
      
      
Source Code Editor to performed this specific task:
      
      python IDLE 3.8(32-bit)
