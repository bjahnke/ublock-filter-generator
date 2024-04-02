import pytest
from src.logic.filter_manager import FilterManager

class TestFilterManager:
    @pytest.fixture
    def filter_manager(self):
        manager = FilterManager()
        data = [
            {"source": "example1", "filter": "example-filter1", "selectors": {"element1": "selector1"}},
            {"source": "example2", "filter": "example-filter2", "selectors": {"element2": "selector2"}}
        ]
        manager.add_filter_generator(*data)
        return manager

    def test_add_filter_generator(self, manager):
        """Test if the add_filter_generator method adds a new filter generator object to the collection"""

        assert len(manager._filter_generators) == 2
        assert len(manager._filters) == 2
        assert len(manager._params_log) == 0

    def test_add_filter(self, manager):
        """Test if the add_filter method adds a filter to the filter manager"""

        # Test adding filter to a specific source
        source = "example1"
        element = "element1"
        phrase = "example-phrase"
        manager.add_filter(source, element, phrase)
        assert len(manager._filters[source]) == 1
        assert len(manager._params_log) == 1

        # Test adding filter to all sources
        source = "all"
        element = "element2"
        phrase = "example-phrase"
        manager.add_filter(source, element, phrase)
        assert len(manager._filters["example1"]) == 1
        assert len(manager._filters["example2"]) == 1
        assert len(manager._params_log) == 3

    def test_str(self, manager):
        """Test if the __str__ method returns a string representation of the filter manager"""

        source = "example1"
        element = "element1"
        phrase = "example-phrase"
        manager.add_filter(source, element, phrase)

        source = "example2"
        element = "element2"
        phrase = "example-phrase"
        manager.add_filter(source, element, phrase)

        expected_output = "! example1:\nwww.example1.com##example-filter1\n\n! example2:\nwww.example2.com##example-filter2"
        assert str(manager) == expected_output