#   **Cleans up files that were last modified over 30 days ago at specified location**

#       **BACK UP IMPORTANT FILES BEFORE USE**

import os
import time

#30 days in seconds
cutoff_time = time.time() - 30 * 24 * 3600  

#Check if target file was last modified over a month ago
def is_old_file(file_path):
    try:
        file_stat = os.stat(file_path)
        return file_stat.st_atime < cutoff_time
    except Exception as e:
        return False      

#Grab target directory from user
def  grab_user_input():
    return input ("Enter Directory: ")

#Purge target directory of any files that were last modified over a month ago
def cleanup_directory():
    files_to_delete = []
    target= grab_user_input()

    desktop_path = os.path.expanduser("~/"+target)

    for root, _, files in os.walk(desktop_path):
        for file in files:
            file_path = os.path.join(root, file)
            if is_old_file(file_path):
                files_to_delete.append(file_path)

    if files_to_delete:

        print("Files to delete:")
        for file_path in files_to_delete:
            print("🧹"+file_path)
            os.remove(file_path)
        print("🧹 Cleanup completed at" +desktop_path+"🧹")
    else:
        print("No files to delete.")

if __name__ == "__main__":
    cleanup_directory()