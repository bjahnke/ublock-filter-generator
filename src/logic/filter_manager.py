import src.domain.filter_generator as fg
from typing import Dict, List, overload


class FilterManager:
    """
    Build the Ublock origin filters from given data
    """

    _filter_generators: Dict[str, fg.FilterGenerator]
    _filters: Dict[str, List[str]]

    def __init__(self):
        self._filter_generators = {}
        self._filters = {}

    def add_filter_generator(self, data: List[Dict[str, str]]):
        """add new filter object to the collection"""
        self._filter_generators.update({data["source"]: fg.FilterGenerator(data["source"], data["filter"], data["selectors"])})
        self._filters.update({data["source"]: []})

    def add_filter(self, source: str, element: str | None = None, phrase: str | None = None) -> str:

        try:
            filter_generator = self._filter_generators[source]
        except KeyError:
            print(f"Element not found for {source}")
        else:
            filters_src = self._filters[source]
            try:
                filters_src.append(filter_generator.create_filter(element, phrase))
            except KeyError:
                print(f"Element {element} not found for {source}")
            else:
                self._filters[source] = list(set(filters_src))

    
    def __str__(self) -> str:
        string = ''
        for key, value in self._filters.items():
            string += "\n".join(value) + "\n\n"
        return string