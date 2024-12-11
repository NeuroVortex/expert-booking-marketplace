from typing import NamedTuple
from fastapi import APIRouter


class Router(NamedTuple):
    prefix: str
    router: APIRouter
    tags: list[str]