import os

def find_files_with_null_bytes(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                    if b'\0' in content:
                        print(f"Null byte found in: {file_path}")
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")

find_files_with_null_bytes('.')
