import re

def split_string_with_any_delimiters(delimiters, input_string):
    fields = re.split('[' + re.escape(''.join(delimiters)) + '\\s]+', input_string)
    non_empty_fields = [field for field in fields if field]
    print(non_empty_fields)

split_string_with_any_delimiters(['sdf', ' ', ';', ':'], 'sdfkdjsadfsd diweiw;1231:foo')