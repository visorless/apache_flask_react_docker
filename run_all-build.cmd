docker-compose up -d --build
:: start frontend, fire up the logs in a new window
start cmd /k "docker-compose logs -f frontend"

:: start backend, fire up the logs in a new window
start cmd /k "docker-compose logs -f backend"
