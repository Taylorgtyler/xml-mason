from xmlReader import load_xml
import xml.etree.ElementTree as ET

class TagSearch:

    def __init__(self, path=None, xml_string=None):

        self.root = load_xml(path=path, xml_string=xml_string)

    def tag_exists(self, tag_name):

        """
        Check if a tag exists in the XML data.
        
        Parameters:
        tag_name (str): The name of the tag to be searched within the XML data.
                        The tag name should be provided as a non-empty string.
        
        Returns:
        Element or str: Returns the Element found with the tag_name if it exists,
                        or a message string in case the tag is not found, or
                        if there's an error like ValueError or any unexpected error.
        
        Raises:
        ValueError: If the tag_name is not a string or is empty.
        Exception: For unexpected errors, like issues with XML data structure.
        """

        try:
            # Checking if tag_name is a string and not empty
            if not isinstance(tag_name, str) or not tag_name.strip():
                raise ValueError("Tag name must be a non-empty string.")
            
            element = self.root.find(tag_name)
            
            if element is not None:
                return element
            else:
                return print("Tag not found")

        except ValueError as ve:
            return f"ValueError: {ve}"
        
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    
    def tags_exist(self, tag_names):
        """
        Check if multiple tags exist in the XML data.
        
        Parameters:
        tag_names (list or tuple of str): A list or tuple containing the names of the tags to be checked.
                                         Each tag name should be a non-empty string.
        
        Returns:
        bool or str: Returns True if all specified tags exist in the XML data, otherwise False.
                     In case of an error (e.g., invalid input), returns a string with an error message.
                     
        Raises:
        ValueError: Raised if a tag_name is not a string, is empty, or if tag_names is not a list or tuple.
        """
        try:
            # Check if tag_names is a list or tuple
            if not isinstance(tag_names, (list, tuple)):
                raise ValueError("Input must be a list or tuple of tag names.")
            
            # Check if each tag_name is a valid string
            for tag_name in tag_names:
                if not isinstance(tag_name, str) or not tag_name.strip():
                    raise ValueError("Each tag name must be a non-empty string.")
            
            # Check the existence of each tag and return True if all exist, otherwise False
            return all(self.tag_exists(tag_name) for tag_name in tag_names)
        
        except ValueError as ve:
            return f"ValueError: {ve}"
        
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    
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
    
    def find_values(self, tag_name):
        """
        Return the values of all instances of a tag
        
        Parameters:
        tag_name (str): The name of the tag whose values need to be found. 
                        It should be a non-empty string.
        
        Returns:
        list or str: Returns a list containing the text content of all occurrences 
                     of the specified tag. Returns an error message string in case 
                     of an error like ValueError or any unexpected error.
        """
        try:
            # Checking if tag_name is a string and not empty
            if not isinstance(tag_name, str) or not tag_name.strip():
                raise ValueError("Tag name must be a non-empty string.")
            
            elements = self.root.findall(tag_name)
            
            if elements:
                return [element.text for element in elements]
            else:
                return "Tag not found"
        
        except ValueError as ve:
            return f"ValueError: {ve}"
        
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def get_all_tags(self, output_format='tuple'):
        """
        Get all unique tags in the XML data along with optional occurrence counts.
        
        Parameters:
        output_format (str): Specify the output format. It can be 'tuple' for a list of unique tags,
                             or 'dict' for a dictionary with tags as keys and occurrences as values.
                             Default is 'tuple'.
        
        Returns:
        tuple or dict: A tuple containing all unique tag names in the XML data, or a dictionary
                       with tags as keys and their occurrences as values. In case of an error, 
                       returns a string with an error message.
        """
        try:
            tags = {}
            
            # Ensure there are elements in the XML data
            if self.root is None:
                raise ValueError("The XML data is empty or not properly loaded.")
            
            for element in self.root.iter():  # Iterating over all elements in the XML tree
                tags[element.tag] = tags.get(element.tag, 0) + 1
            
            if output_format == 'tuple':
                return tuple(tags.keys())
            elif output_format == 'dict':
                return tags
            else:
                raise ValueError("Invalid output_format. Use 'tuple' or 'dict'.")
            
        except ValueError as ve:
            return f"ValueError: {ve}"
        
        except Exception as e:
            return f"An unexpected error occurred: {e}"
