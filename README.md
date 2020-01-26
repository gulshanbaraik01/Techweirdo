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

To perform this task:

      create a database on 'phpmyadmin' and import the given/uploaded database (if you haven't)
      go to file path (eg:- D:\Techweirdo)
      write 'cmd' + ENTER to open command prompt
      write python solution.py <-ENTER
      
      this will open=>
      
            * Serving Flask app "solution" (lazy loading)
            * Environment: production
            WARNING: This is a development server. Do not use it in a production deployment.
            Use a production WSGI server instead.
            * Debug mode: on
            * Restarting with stat
            * Debugger is active!
            * Debugger PIN: 338-800-808
            * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
            
      copy this link and paste it on browser(Chrome, Mozilla etc.) like=>
      
            http://127.0.0.1:5000/?id=8  ->ENTER
            
      You will get the solution...

important modules:
      
      pip install mysql-connector
      pip install flask
      
      
Source Code Editor to performed this specific task:
      
      python IDLE 3.8(32-bit)
