import pandas as pd

from content_changer.services.dataset_pipeline.dataset_modifier_pipeline import DatasetTransformerPipeline


def test_table_modifier(mock_data_path):
    columns = ['Makler', 'Verwalter', 'Projektentwickler']
    names_column = "Ansprechpartner"

    table_modifier = DatasetTransformerPipeline(mock_data_path, names_column, columns)
    assert type(table_modifier.dataset) == pd.DataFrame

    tags_columns = table_modifier.stack_tags_columns()
    assert type(tags_columns) == pd.DataFrame
    assert tags_columns.columns.array == ['name', 'Tags']
    assert tags_columns.columns.array[1] == 'Tags'
    assert len(tags_columns['Tags']) == 3
    assert tags_columns['Tags'][0] == ['Makler']
    assert tags_columns['Tags'][1] == ['Makler', 'Projektentwickler']
    assert tags_columns['Tags'][2] == ['Makler', 'Verwalter', 'Projektentwickler']

    split_names = table_modifier.split_names()
    assert type(split_names) == pd.DataFrame
    assert split_names.columns.array == \
           ['Ansprechpartner', 'Tags', 'first_name', 'last_name']
    print(split_names['Ansprechpartner'])
    assert split_names['Ansprechpartner'][0] == 'Thomas Clotten'
    assert split_names['Ansprechpartner'][1] == 'Walter Brune'
    assert split_names['Ansprechpartner'][2] == 'Tatjana Bähr'
    assert split_names['first_name'][0] == 'Thomas'
    assert split_names['first_name'][1] == 'Walter'
    assert split_names['first_name'][2] == 'Tatjana'
    assert split_names['last_name'][0] == 'Clotten'
    assert split_names['last_name'][1] == 'Brune'
    assert split_names['last_name'][2] == 'Bähr'
