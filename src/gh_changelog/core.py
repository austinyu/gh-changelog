
from typing import NamedTuple

class Version(NamedTuple):
    major: int
    minor: int
    patch: int
    pre_release: list[str]

