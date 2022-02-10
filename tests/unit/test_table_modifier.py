import pandas as pd

from content_changer.services.dataset_pipeline.dataset_transformer_pipeline import DatasetTransformerPipeline


def test_table_modifier(mock_dataset):

    columns = ['tag1', 'tag2']
    tags_column_name = 'Tags'
    names_column = "name"

    table_modifier = DatasetTransformerPipeline(mock_dataset)
    assert type(table_modifier.dataset) == pd.DataFrame

    tags_columns = table_modifier.stack_tags_columns(columns, tags_column_name)
    assert type(tags_columns) == pd.DataFrame
    assert tags_columns.columns.array == ['name', 'Tags']
    assert tags_columns.columns.array[1] == 'Tags'
    assert len(tags_columns['Tags']) == 3
    assert tags_columns['Tags'][0] == ['good', 'cringe']
    assert tags_columns['Tags'][1] == ['bad', 'based']
    assert tags_columns['Tags'][2] == ['evil']

    split_names = table_modifier.split_names(names_column)
    print(split_names)
    assert type(split_names) == pd.DataFrame
    assert split_names.columns.array == \
           ['name', 'Tags', 'full_name_split_length', 'first_name', 'last_name']
