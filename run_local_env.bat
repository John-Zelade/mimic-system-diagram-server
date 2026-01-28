@echo off
rem Activate the virtual environment
@REM call .\rtap_admin_env\Scripts\activate
call .\himo_be_bsp_env\Scripts\activate

rem Run the Python script
@REM python manage.py runserver
python manage.py runserver 
@REM 192.168.16.254:8000
