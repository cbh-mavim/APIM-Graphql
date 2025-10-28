import strawberry
from datetime import datetime
from .query import Query
from ..utils.datetime import DateTimeISO

schema = strawberry.Schema(
    query=Query,
    scalar_overrides={
        datetime: DateTimeISO
    }
)

__all__ = ["schema"]