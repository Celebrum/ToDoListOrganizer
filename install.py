import json
import os
import shutil
import subprocess
import argparse

def install_module(path):
    # Load module configuration
    with open('module.json', 'r') as f:
        module_config = json.load(f)

    # Create necessary directories
    os.makedirs('models', exist_ok=True)
    os.makedirs('logs', exist_ok=True)

    # Install dependencies
    subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

    # Copy module files to CodeProject.AI Server modules directory
    ai_server_path = path
    os.makedirs(ai_server_path, exist_ok=True)
    
    files_to_copy = [
        'module.json',
        'modulesettings.json',
        'app.py',
        'src',
        'requirements.txt'
    ]

    for file in files_to_copy:
        if os.path.isdir(file):
            shutil.copytree(file, f"{ai_server_path}/{file}", dirs_exist_ok=True)
        else:
            shutil.copy2(file, ai_server_path)

    print(f"Module installed successfully at {ai_server_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Install ToDoListOrganizer module.')
    parser.add_argument('--path', type=str, required=True, help='Path to install the module')
    args = parser.parse_args()
    install_module(args.path)
