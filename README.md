# antony_server
Antony WEB-Server

## samples:

### no parameters
http://localhost:5000/move_forward
### single parameters
http://localhost:5000/move?dir=right
### multible parameters
http://localhost:5000/motors?m1=-1500&m2=-1500&m3=1000&m4=1000

Linux
    $ export FLASK_APP=app.py
    $ export FLASK_ENV=development
    $ flask run
Windows
    C:\> set FLASK_APP=app.py
    C:\> set FLASK_ENV=development
    C:\> flask run
    