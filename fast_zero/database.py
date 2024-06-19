from sqlalchemy import create_engine

from fast_zero.settings import Settings

engine = create_engine(Settings().DATABASE_URL)

# pragma: no conver


def get_session():
    with Settings(engine) as session:
        yield session
