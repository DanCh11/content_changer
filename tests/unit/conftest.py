import pytest


@pytest.fixture(scope="session")
def mock_data_path() -> str:
    return '../test_data/mock_data.xlsx'
