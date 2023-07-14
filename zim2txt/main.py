import os
import shutil
from bs4 import BeautifulSoup
def Export(zim_path, temp_path, files_path, encoding="utf8"):
    os.system(f"sudo zimdump dump --dir={temp_path} {zim_path}")
    for file in os.listdir(temp_path):
        newname = file + ".txt"
        current_file_path = os.path.join(temp_path, file)
        with open(current_file_path, 'r', encoding="utf8", errors='ignore') as current_file:
            content = current_file.read()
        soup = BeautifulSoup(content, 'html.parser')
        plain_text = soup.get_text()
        new_file_path = os.path.join(files_path, newname)
        with open(new_file_path, 'w', encoding=encoding, errors='ignore') as new_file:
            new_file.write(plain_text)
    shutil.rmtree(temp_path)