import pytest
import pandas as pd


@pytest.fixture(scope="session")
def mock_dataset():
    data = {
        "name": ['bob dylan', 'dan chiriac', 'joachim K. pastor'],
        "tag1": ['good', 'bad', 'evil'],
        "tag2": ['cringe', 'based', '']
    }

    return pd.DataFrame(data)
