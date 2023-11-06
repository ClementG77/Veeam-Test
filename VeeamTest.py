import os
import sys
import shutil
import time
from datetime import datetime

def sync_folders(source_folder, replica_folder, log_file):
    
    start = datetime.now()
    start_string = start.strftime("%d/%m/%Y %H:%M:%S")
    log(f" Synchronization started : {start_string}" , log_file)

    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        replica_path = os.path.join(replica_folder, relative_path)

        # Remove files or folders in the replica folder that don't exist in the source folder
        for replica_root, replica_dirs, replica_files in os.walk(replica_path):
            for replica_dir in replica_dirs:
                source_dir = os.path.join(root, replica_dir)
                if not os.path.exists(source_dir):
                    shutil.rmtree(os.path.join(replica_root, replica_dir))
                    log(f"Removed {os.path.join(replica_root, replica_dir)}", log_file)
            for replica_file in replica_files:
                source_file = os.path.join(root, replica_file)
                if not os.path.exists(source_file):
                    os.remove(os.path.join(replica_root, replica_file))
                    log(f"Removed {os.path.join(replica_root, replica_file)}", log_file)
            

        # Create the folder if it doesn't exist
        if not os.path.exists(replica_path):
            os.makedirs(replica_path)

        
        # Synchronize the files in the current directory
        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_path, file)

            # Copy the file if it doesn't exist in the replica folder 
            if not os.path.exists(replica_file) :
                shutil.copy2(source_file, replica_file)
                log(f"Copied {source_file} to {replica_file}", log_file)
                
            # Copy the file if it's different in the replica folder
            if  os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                shutil.copy2(source_file, replica_file)
                log(f"Updated {source_file} to {replica_file}", log_file)
    end = datetime.now()
    end_string = end.strftime("%d/%m/%Y %H:%M:%S")
    log(f" Synchronization finished : {end_string}", log_file)

def log(message, log_file):
    print(message)

    # Log the message to the log file
    with open(log_file, 'a') as file:
        file.write(f"{message}\n")

if __name__ == "__main__":
    # Get the command line arguments
    source_folder = sys.argv[1]
    replica_folder = sys.argv[2]
    sync_interval = int(sys.argv[3])
    log_file = sys.argv[4]

    sync_folders(source_folder, replica_folder, log_file)

    # Synchronize folders automatically
    while True:
        time.sleep(sync_interval)
        sync_folders(source_folder, replica_folder, log_file)
