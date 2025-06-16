@REM Generate docs for server code 
cd server
rmdir /s /q -r docs
doxygen

@REM Generate docs for python_controller code
cd ../python_controller
rmdir /s /q -r docs
doxygen

@REM Generate docs for bot code
cd ../bot
rmdir /s /q -r docs
doxygen