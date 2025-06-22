import os



repo_folder_path = "F:\\apps\\Reposllm\\repofolder"


with os.scandir(repo_folder_path) as cloned_repo:
    for file in cloned_repo:
        print(file.name)