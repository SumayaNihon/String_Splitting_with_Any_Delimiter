import re

def string_splitter_with_any_Delimiter(delimiter,input):
    fields = re.split(f'[{delimiter}\\s]+', input)
    non_empty_field = [field for field in fields if field]
    print(non_empty_field)
string_splitter_with_any_Delimiter('sdf','sdfkdjsadfsd diweiw;1231:foo')