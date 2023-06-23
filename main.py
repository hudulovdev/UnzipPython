import zipfile

def unzip_file(zip_file_path, extract_directory):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_directory)

# Example usage
zip_file_path = input("Zip file path: ")
extract_directory = input("Extract path: ")
unzip_file(zip_file_path, extract_directory)