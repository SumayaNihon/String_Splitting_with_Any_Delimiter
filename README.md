# String_Splitting_with_Any_Delimiter

This is a Python function that splits a string using various delimiters provided by the user.

## Usage

You can use the `string_splitter_with_any_delimiters` function to split a string into fields based on a list of delimiters.

### Example

```python
import re

def string_splitter_with_any_delimiters(delimiters, input_string):
    fields = re.split('[' + re.escape(''.join(delimiters)) + '\\s]+', input_string)
    non_empty_fields = [field for field in fields if field]
    return non_empty_fields

# Usage example
delimiters = ['sdf', ' ', ';', ':']
input_string = 'sdfkdjsadfsd diweiw;1231:foo'
result = string_splitter_with_any_delimiters(delimiters, input_string)
print(result)
