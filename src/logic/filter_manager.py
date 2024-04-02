import src.domain.filter_generator as fg
from typing import Dict, List, Set, overload


class FilterManager:
    """
    The `FilterManager` class manages filters for different sources.

    Attributes:
        _filter_generators (Dict[str, fg.FilterGenerator]): A dictionary that maps source names to `FilterGenerator` objects.
        _filters (Dict[str, List[str]]): A dictionary that stores filters for each source.
        _params_log (Set[fg.FilterData]): A set that keeps track of filter parameters.

    Methods:
        __init__(): Initializes the `FilterManager` object.
        add_filter_generator(data: List[Dict[str, str]]): Adds a new filter generator object to the collection.
        add_filter(source: str, element: str, phrase: str): Adds a filter to the filter manager.
        __str__(): Returns a string representation of the filter manager.

    Note:
        The filters are stored in a dictionary where the keys are the sources and the values are lists of filters.
    """

    _filter_generators: Dict[str, fg.FilterGenerator]
    _filters: Dict[str, Set[str]]
    _params_log: Set[fg.FilterData]

    def __init__(self):
        self._filter_generators = {}
        self._filters = {}
        self._params_log = set()

    def add_filter_generator(self, data: List[Dict[str, str]]):
        """add new filter object to the collection"""
        self._filter_generators.update({data["source"]: fg.FilterGenerator(data["source"], data["filter"], data["selectors"])})
        self._filters.update({data["source"]: set()})

    def add_filter(self, source: str, element: str, phrase: str):
        """
        Adds a filter to the filter manager.

        :param source: The source of the filter.
        :type source: str
        :param element: The element to filter (optional).
        :type element: str, None
        :param phrase: The phrase to filter (optional).
        :type phrase: str, None
        :return: The result of adding the filter.
        :rtype: str

        If the source is "all" or an empty string, the method will add the filter to all available sources.
        Otherwise, it will add the filter to the specified source.

        If the source or element is not found, an appropriate error message will be printed.

        Note: The filters are stored in a dictionary where the keys are the sources and the values are lists of filters.
        """
        if source == "all" or source == "":
            for source in self._filter_generators.keys():
                self.add_filter(source, element, phrase)
            return
        
        self._params_log.add(fg.FilterData(source, element, phrase))

        filter_generator = self._filter_generators.get(source)
        
        if filter_generator is None:
            print(f"Element not found for {source}")
            return
        
        filters_src = self._filters[source]
        new_filter = filter_generator.create_filter(element, phrase)

        if new_filter is None:
            print(f"Element {element} not found for {source}")
            return
        
        filters_src.add(new_filter)

    
    def __str__(self) -> str:
        """filters to sorted string representation, sources separated by extra newlines"""
        return "\n\n".join([f"! {source}:\n" + "\n".join(sorted(filters)) for source, filters in self._filters.items()])
        