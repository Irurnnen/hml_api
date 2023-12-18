import environs

env = environs.Env()
env.read_env()


class Config:
    """Base configuration"""

    user = env.str("POSTGRES_USER", "postgres")
    password = env.str("POSTGRES_PASSWORD", "qwe123QWE")
    hostname = env.str("POSTGRES_HOSTNAME", "localhost")
    port = env.int("POSTGRES_PORT", 5432)
    database = env.str("POSTGRES_DB", "main")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production configuration"""

    pass


class DevelopmentConfig(Config):
    """Development configuration"""

    pass


class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
