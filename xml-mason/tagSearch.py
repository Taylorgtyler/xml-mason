from xmlReader import load_xml
import xml.etree.ElementTree as ET

class TagSearch:

    def __init__(self, path=None, xml_string=None):

        self.root = load_xml(path=path, xml_string=xml_string)

    def tag_exists(self, tag_name):

        """Check if a tag exists in the XML data"""
        element = self.root.find(tag_name)
        return element is not None
    
    def tags_exist(self, tag_names):
        
        """Check if multiple tags exist in the XML data"""
        return all(self.tag_exists(tag_name) for tag_name in tag_names)
    
    def find_value(self, tag_name):

        return None
    
    def find_values(self, tag_name):

        return None
    
