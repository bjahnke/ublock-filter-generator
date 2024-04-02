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

    def create_filter(self, element, phrase) -> str | None:
        new_filter = None
        element = self._selectors.get(element)
        if element is not None:
            new_filter = self._filter.format(element=element, phrase=phrase)
        return new_filter
    

@dataclass
class FilterData:
    source: str
    element_type: str
    phrase: str

    def __str__(self):
        return f"{self.source}, {self.element_type}, {self.phrase}"
    
    def __eq__(self, other):
        return self.source == other.source and self.element_type == other.element_type and self.phrase == other.phrase
    
    def __hash__(self):
        return hash(str(self))