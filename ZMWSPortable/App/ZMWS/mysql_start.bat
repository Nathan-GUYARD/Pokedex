@QPROCESS "mysqld.exe">NUL
@if "%ERRORLEVEL%"=="0" goto :suite
@start /min "serveur_mySQL" mySQL\bin\mysqld --initialize-insecure  --default-character-set=utf8
@start /min "serveur mySQL" mySQL\bin\mysqld --console --explicit_defaults_for_timestamp 
@exit
@:suite