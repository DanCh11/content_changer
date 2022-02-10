import pytest
import pandas as pd

from content_changer.services.dataset_pipeline.dataset_transformer_pipeline import DatasetTransformerPipeline


def test_table_modifier(mock_dataset):

    dataset = pd.DataFrame()
    columns = ['tag1', 'tag2']
    tags_column_name = 'new_tag_column'
    names_column = "names"

    table_modifier = DatasetTransformerPipeline(mock_dataset)
    assert type(table_modifier.dataset) == pd.DataFrame

    tags_columns = table_modifier.stack_tags_columns(columns, tags_column_name)
    assert type(tags_columns) == pd.DataFrame
    assert tags_columns.columns.array == ['tag1', 'tag2', 'Tags']
    assert tags_columns.columns.array[2] == 'Tags'
    assert len(tags_columns['Tags']) == 3
    assert tags_columns['Tags'][0] == 'good, cringe'
    assert tags_columns['Tags'][1] == 'bad, based'
    assert tags_columns['Tags'][2] == 'evil, '

    # splited_names = table_modifier.split_names(names_column)


