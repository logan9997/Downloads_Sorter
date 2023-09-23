import os

DOWNLOADS_DIR = r'C:\Users\logan\Downloads'
NO_EXTENSION_FOLDER = 'no_extension'

def get_file_extensions() -> list[str]:
    file_extensions = set([
        d.split('.')[-1].lower() for d in os.listdir(DOWNLOADS_DIR) 
        if not os.path.isdir(os.path.join(DOWNLOADS_DIR, d))
    ])  
    return file_extensions


def create_folders(file_extensions:list[str]) -> None:
    for extension in file_extensions:
        folder_location = os.path.join(DOWNLOADS_DIR, extension)
        if not os.path.exists(folder_location):
            os.mkdir(folder_location)

    no_extension_folder_path = os.path.join(DOWNLOADS_DIR, NO_EXTENSION_FOLDER)
    if not os.path.exists(no_extension_folder_path):
        os.mkdir(no_extension_folder_path)


def sort_files() -> None:
    for file in os.listdir(DOWNLOADS_DIR):
        if not os.path.isdir(os.path.join(DOWNLOADS_DIR, file)):
            print(f'SORTING - {file}')
            if '.' in file:
                file_extension = file.split('.')[-1].lower()
            else:
                file_extension = NO_EXTENSION_FOLDER
            os.rename(
                os.path.join(DOWNLOADS_DIR, file), 
                os.path.join(DOWNLOADS_DIR, file_extension, file)
            )

def main():
    file_extensions = get_file_extensions()
    create_folders(file_extensions)
    sort_files()


if __name__ == '__main__':
    main()