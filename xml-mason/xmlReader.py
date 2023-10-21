import xml.etree.ElementTree as ET

def load_xml(path=None, xml_string=None):
    if path:
        tree = ET.parse(path)
        root = tree.getroot()
    elif xml_string:
        root = ET.fromstring(xml_string)
    else:
        raise ValueError("Either path or xml_string should be provided.")
    return root