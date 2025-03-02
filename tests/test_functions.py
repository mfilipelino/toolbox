import pytest
from toolbox.functions import listChunker, weirdCase
from datetime import datetime
import io
import sys
from contextlib import redirect_stdout
from toolbox import report


class TestListChunker:
    def test_empty_list(self):
        result = list(listChunker([], 3))
        assert result == []

    def test_chunk_size_equal_to_list_length(self):
        result = list(listChunker([1, 2, 3], 3))
        assert result == [[1, 2, 3]]

    def test_chunk_size_greater_than_list_length(self):
        result = list(listChunker([1, 2, 3], 5))
        assert result == [[1, 2, 3]]

    def test_even_chunks(self):
        result = list(listChunker([1, 2, 3, 4, 5, 6], 2))
        assert result == [[1, 2], [3, 4], [5, 6]]

    def test_uneven_chunks(self):
        result = list(listChunker([1, 2, 3, 4, 5, 6, 7], 3))
        assert result == [[1, 2, 3], [4, 5, 6], [7]]


class TestWeirdCase:
    def test_empty_string(self):
        result = weirdCase("")
        assert result == ""

    def test_single_character(self):
        result = weirdCase("a")
        assert result == "A"

    def test_even_length_string(self):
        result = weirdCase("abcd")
        assert result == "AbCd"

    def test_odd_length_string(self):
        result = weirdCase("abc")
        assert result == "AbC"

    def test_with_spaces(self):
        result = weirdCase("hello world")
        assert result == "HeLlO WoRlD"

    def test_with_special_characters(self):
        result = weirdCase("Hello, World!")
        assert result == "HeLlO, wOrLd!"


class TestReport:
    def test_report_format(self):
        message = "Test message"
        
        # Capture stdout
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            report(message)
        
        output = captured_output.getvalue().strip()
        
        # Check that the output contains the message
        assert message in output
        
        # Check that the output starts with a timestamp in the format YYYY-MM-DD HH:MM:SS.mmm
        timestamp_format = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}'
        import re
        assert re.match(f"{timestamp_format}: {message}", output)