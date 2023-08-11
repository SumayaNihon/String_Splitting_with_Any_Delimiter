# String_Splitting_with_Any_Delimiter

This is a Python function that splits a string using various delimiters provided by the user.

## Usage

You can use the `string_splitter_with_any_delimiters` function to split a string into fields based on a list of delimiters.

### Example

```python

import re

##Method-1 (Single Delimiter)

def string_splitter_with_any_Delimiter(delimiter,input):
    fields = re.split(f'[{delimiter}\\s]+', input)
    non_empty_field = [field for field in fields if field]
    print(non_empty_field)
string_splitter_with_any_Delimiter('sdf','sdfkdjsadfsd diweiw;1231:foo')


##Method-2 (Multiple Delimiter)

def split_string_with_multiple_delimiters(delimiters, input_string):
    fields = re.split('[' + re.escape(''.join(delimiters)) + '\\s]+', input_string)
    non_empty_fields = [field for field in fields if field]
    print(non_empty_fields)


split_string_with_multiple_delimiters(['sdf', ' ', ';', ':'], 'sdfkdjsadfsd diweiw;1231:foo')


