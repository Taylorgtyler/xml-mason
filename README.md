# XML Mason

## Description

XML Mason is a Python package that provides a versatile tool for XML data processing and analysis. With this package, you can load XML data, search for specific tags, retrieve values, check for the existence of tags, and more. It also allows users to export data to XML format from dataframes.

## Features

- Load XML data from a file or a string.
- Search and retrieve the value(s) of specific tags.
- Check the existence of specific tags.
- Retrieve all unique tags present in the XML data.
- Export dataframe data to XML format.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Taylorgtyler/xml-mason.git
   ```

2. **Navigate to the Directory:**
   ```bash
   cd xml-mason
   ```

3. **Install with pip:**
   ```bash
   pip install .
   ```

## Usage

Here are some examples of how to use the package:

### Loading XML Data

```python
from xmlMason import load_xml

root = load_xml(path="path/to/your/xml")
```

### Searching and Retrieving Tags

```python
from xmlMason import TagSearch

ts = TagSearch(path="path/to/your/xml")

# Find value
value = ts.find_value("your_tag")

# Check if tag exists
does_exist = ts.tag_exists("your_tag")
```

## Contributing

Contributions are welcome! For bug reports or enhancements, please open an issue.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
