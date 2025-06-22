import os
from git import Repo


link = "https://github.com/Giorgiod91/Repo-Analyzer-Transformer-for-Large-Language-Models"
repo_link = input(link)
clone_target_folder = "F:\\apps\\Reposllm\\repofolder"


Repo.clone_from(link , clone_target_folder)




