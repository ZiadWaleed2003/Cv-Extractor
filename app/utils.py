import json
import os



def read_cv_json(file_path : str) -> json:
    """
        Reads the CV data stored in Json file
    """

    try:

        with open(file_path , "r") as f:

            data = json.load(f)
            print("Json data got loaded")

            return data
    
    except Exception as e:

        print("Failed to load the json file")

        raise ValueError(f"Error in read_cs_json : {e}")
    


def read_requirements_file(file_path):
    """
    Read requirements from a text file
    """
    try:
        # Validate file exists
        if not os.path.exists(file_path):
            raise ValueError(f"Requirements file not found: {file_path}")
        
        # Check file extension
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension not in ['.txt', '.md']:
            raise ValueError(f"Only .txt and .md files are supported. Got: {file_extension}")
        
        # Read file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            
        if not content:
            raise ValueError("Requirements file is empty")
            
        return content
        
    except UnicodeDecodeError:
        # Fallback to latin-1 encoding
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read().strip()
            return content
        except Exception as e:
            raise ValueError(f"Error reading file with different encodings: {e}")
    except Exception as e:
        raise ValueError(f"Failed to read requirements file: {e}")
