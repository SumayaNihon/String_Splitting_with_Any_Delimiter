import re

def string_splitter_with_any_delimiters(delimiters, input):
    fields = re.split('[' + re.escape(''.join(delimiters)) + '\\s]+', input)
    non_empty_fields = [field for field in fields if field]
    print(non_empty_fields)

string_splitter_with_any_delimiters(['sdf', ' ', ';', ':'], 'sdfkdjsadfsd diweiw;1231:foo')