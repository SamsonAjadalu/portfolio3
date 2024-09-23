import os
import random

# Paths to the folders
static_projects_path = 'static/blog'
content_projects_path = 'content/blog'

# Get all folder names from 'static/projects', ignoring '.DS_Store'
static_folders = [folder for folder in os.listdir(static_projects_path) if folder != '.DS_Store']

# Get all .md file names from 'content/projects', removing the '.md' extension
content_folders = [os.path.splitext(file)[0] for file in os.listdir(content_projects_path) if file.endswith('.md')]

# Step 1: Rename all static folders to a temporary name (add '_temp' suffix)
print("Renaming all static folders to temporary names...")
for static_folder in static_folders:
    old_folder_path = os.path.join(static_projects_path, static_folder)
    temp_folder_path = os.path.join(static_projects_path, static_folder + "_temp")

    # Rename folder to temporary name
    os.rename(old_folder_path, temp_folder_path)
    print(f"Renamed '{static_folder}' to '{static_folder}_temp'")

# Shuffle the content folder names to ensure random assignment
random.shuffle(content_folders)

# Step 2: Rename from temporary names to randomly chosen content folder names
print("\nRenaming temporary folders to unique, randomly chosen content folder names...")
temp_folders = [folder for folder in os.listdir(static_projects_path) if folder.endswith('_temp')]

# Make sure we have enough content folder names for all static folders
if len(temp_folders) > len(content_folders):
    print("Warning: There are more folders in static/projects than in content/projects. Some folders will remain unrenamed.")
else:
    for temp_folder, content_folder in zip(temp_folders, content_folders):
        old_temp_folder_path = os.path.join(static_projects_path, temp_folder)
        new_folder_path = os.path.join(static_projects_path, content_folder)

        # Rename folder to match the randomly chosen content folder name
        os.rename(old_temp_folder_path, new_folder_path)
        print(f"Renamed '{temp_folder}' to '{content_folder}'")


git add static/blog
git add static/experience
git add static/projects
git add content/projects
git commit -m "Renamed folders in static/projects to match content/projects"
git push origin master