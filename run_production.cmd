@ECHO OFF

:: build images and up them
docker-compose --profile production -f docker-compose.yml -f docker-compose.production.yml up -d

:: find the id of the running frontend container
for /f %%i in ('docker-compose ps -q frontend') do set VAR=%%i

:: build the react application, then copy the files to backend
docker exec %VAR% yarn build
:: copy static, aka template, files
xcopy .\frontend\build .\backend\front  /y /i /s
:: copy public files, such as css
:: xcopy .\frontend\build\static .\backend\public /y /i /s

:: stop this docker container, otherwise it sits here re-building
docker stop %VAR%

:: open the logs, get rid of this eventually
start cmd /k "docker-compose logs -f backend"
