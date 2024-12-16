import os

def list_folder_structure(root_folder, exclude_folder="node_modules"):
    for root, dirs, files in os.walk(root_folder):
        # Remove the excluded folder(s) from the directory list
        dirs[:] = [d for d in dirs if d != exclude_folder]
        
        level = root.replace(root_folder, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

# Replace 'your_folder_path' with the path of the folder you want to explore
list_folder_structure("/Users/shahanurmdsharif/development/learn/learnReact/my-app")