import os

def remove_null_bytes_from_file(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    
    new_content = content.replace(b'\x00', b' ')
    
    with open(file_path, 'wb') as f:
        f.write(new_content)

def remove_null_bytes_from_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                remove_null_bytes_from_file(file_path)
                print(f"Null bytes removed from: {file_path}")
            except Exception as e:
                print(f"Could not process file {file_path}: {e}")

if __name__ == "__main__":
    directory = "."  # Change this to the directory you want to process
    remove_null_bytes_from_directory(directory)
