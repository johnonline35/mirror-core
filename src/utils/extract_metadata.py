from tika import parser

def extract_metadata(file_path):
    parsed_file = parser.from_file(file_path)
    metadata = parsed_file.get("metadata", {})
    return metadata