import pandas as pd

def dataframe_to_xml(dataframe, file_path, root_name="data", row_name="row"):
    """
    Write a DataFrame to an XML file.
    
    Parameters:
    dataframe (DataFrame): The DataFrame to be written to XML.
    file_path (str): The path where the XML file will be saved.
    root_name (str, optional): The name of the root element in the XML file. Default is "data".
    row_name (str, optional): The name of the element for each row in the XML file. Default is "row".
    
    Returns:
    str: A message indicating success or any errors that occurred.
    """
    try:
        # Checking if the input is a DataFrame
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("The input must be a pandas DataFrame.")
        
        # Writing the DataFrame to an XML file
        dataframe.to_xml(file_path, root_name=root_name, row_name=row_name)
        
        return f"DataFrame has been successfully written to {file_path}"
        
    except Exception as e:
        return f"An error occurred while writing the DataFrame to XML: {e}"