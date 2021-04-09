# Getting Started with this app

To build a develop environment run run_all-build.cmd.
To up a develop environment that has already been built, run run_all.cmd.
To build a production environment run run_production-build.cmd.
To up a production environment that has already been built, run run_production.cmd

To down a develop or production build, use docker-compose down

This project utilizes docker-compose with override files to manage developent and production environments.
The development environment relies of Create-React-App and Flask development servers.
The production environment builds the production ready version of Create React App, then deploys it into an Apache container that runs the Flask application with mod_wsgi-express over port 8080. 

Port 8080 can be easily changed in the docker-compose file when you are ready to move these containers into your actual production environment.
