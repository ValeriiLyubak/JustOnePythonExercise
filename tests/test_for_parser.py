import pytest
import os
import csv
from my_parser import AdressParser

@pytest.fixture
def setup_parser():
    output_file = 'test_offices.csv'
    parser = AdressParser(output_file)
    yield parser
    parser.close()
    if os.path.exists(output_file):
        os.remove(output_file)

def test_parse_offices(setup_parser):
    parser = setup_parser
    parser.parse()

    assert os.path.exists(parser.output_file)
    print("файл был создан")

    with open(parser.output_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        headers = next(reader)
        assert headers == ['Country', 'CompanyName', 'FullAddress']
        print("заголовки корректны")

        rows = list(reader)
        assert len(rows) > 0
        print("файл не пуст")

        country, company_name, full_address = rows[0]
        assert isinstance(country, str)
        assert isinstance(company_name, str)
        assert isinstance(full_address, str)
        print("формат в первой записи верен")