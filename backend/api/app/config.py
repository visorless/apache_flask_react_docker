import os
# more configuration options here http://flask.pocoo.org/docs/1.0/config/


class Config:
    """
    Base Configuration
    """

    # CHANGE SECRET_KEY!!
    # Exmaple to retrieve env variable `SECRET_KEY`: os.environ.get("SECRET_KEY")
    SECRET_KEY = "testkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development Configuration - default config
    This defaults the Database URL that can be created through the docker
    cmd in the setup instructions. You can change this to environment variable as well.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production Configuration
    Most deployment options will provide an option to set environment variables.
    Hence, why it defaults to retrieving the value of the env variable `DATABASE_URL`.
    You can update it to use a `creds.ini` file or anything you want.
    Requires the environment variable `FLASK_ENV=prod`
    """
    DEBUG = False


class DockerDevConfig(Config):
    """
    Docker Development Configuration
    The container will have the environment variable `FLASK_ENV=docker`
    to enable this configuration.
    """
    DEBUG = True


# way to map the value of `FLASK_ENV` to a configuration
config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "docker": DockerDevConfig
}
