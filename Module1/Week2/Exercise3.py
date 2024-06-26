import os

file_path = './P1_data.txt'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        print(content)
else:
    print(f"File {file_path} không tồn tại.")


