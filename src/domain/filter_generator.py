from dataclasses import dataclass
from typing import List
from enum import Enum


# domain

class ElementType(Enum):
    COMPANY = "company"
    TITLE = "title"


class FilterGenerator:
    def __init__(self, source: str, filter: str, selectors: dict):
        self._source = source
        self._selectors = selectors
        self._filter = f'www.{source}.com##' + filter

    def create_filter(self, element, phrase) -> str:
        element = self._selectors[element]
        return self._filter.format(element=element, phrase=phrase)
    

@dataclass
class FilterData:
    source: str
    element_type: str
    phrase: str
