#C:\Users\olive\AppData\Local\Packages\Microsoft.YourPhone_8wekyb3d8bbwe\LocalCache\Indexed\4a932ba5-d3aa-43cc-bdd8-89db578e00ff\System\Database

import os

def find_your_phone_dir():
    packages = os.getenv('LOCALAPPDATA') + '\\Packages'
    subfolders = [f.path for f in os.scandir(packages) if f.is_dir()]

    for i in subfolders:
        if "YourPhone" in i:
            return i

    return None

def find_your_phone_database(your_phone_dir):
    if not os.path.exists(your_phone_dir):
        print(f"Your Phone dir does not exist! Make sure the application is installed")
        return None

    indexed = your_phone_dir + '\\LocalCache\\Indexed'
    subfolders = [a.path for a in os.scandir(indexed) if a.is_dir()]

    for i in subfolders:
        if i != 'FullTrust':
            return i + '\\System\\Database'

    return None

def extract_data(database_dir, target_dir):
    if not os.path.exists(database_dir):
        print(f"Database dir does not exist! Make sure the application is installed")
        return None
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for i in os.listdir(database_dir):
        source_path = os.path.join(database_dir, i)
        destination_path = os.path.join(target_dir, i)
        os.rename(source_path, destination_path)
        print(f"Moved: {i}")

if __name__=="__main__":
    extract_data(find_your_phone_database(find_your_phone_dir()), 'YourPhoneDatabase')