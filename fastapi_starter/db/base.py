from sqlalchemy.orm import DeclarativeBase

from fastapi_starter.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
