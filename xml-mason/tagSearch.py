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

        """
        Return the value of the first instance of a tag
        
        Parameters:
        tag_name (str): The name of the tag whose value needs to be found. 
                        It should be a non-empty string.
        
        Returns:
        str or None: Returns the text content of the first occurrence of the specified tag.
                     Returns None if the tag is not found.
                     In case of an error, returns a string with an error message.
        """

        try:
            # Checking if tag_name is a string and not empty
            if not isinstance(tag_name, str) or not tag_name.strip():
                raise ValueError("Tag name must be a non-empty string.")
            
            element = self.root.find(tag_name)
            
            if element is not None:
                return element.text
            else:
                return print("Tag not found")

        except ValueError as ve:
            return f"ValueError: {ve}"
        
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    
    def find_values(self, tag_names):

        return None

    def get_all_tags(self):
        """
        Get all unique tags in the XML data.
        
        Returns:
        tuple: A tuple containing all unique tag names in the XML data.
        """

        tags = set()
        for element in self.root.iter():
            tags.add(element.tag)

        return tuple(tags)