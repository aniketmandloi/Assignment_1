# importing module os for intracting with operating system.
# importing module time for timeStamps related operations.
import os
import time

# Defining the directory which we want to monitor.
#if unicode error occures just change the paths "\" ith "\\" that should work.
directory_to_monitor = "Replace_the_text_with_The_directory_you_want_to_monitor"

def get_new_files(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)
    
    # Filter out directories from the list of files.
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    return files

def monitor_directory(directory):
    # Initial list of files in the directory.
    current_files = get_new_files(directory)

    try:
        while True:
            # Get the updated list of files in the directory.
            updated_files = get_new_files(directory)

            # Find the difference between the current list and the updated list.
            new_files = [file for file in updated_files if file not in current_files]

            if new_files:
                # Print message with the current date-time stamp.
                for file in new_files:
                    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                    print(f"New file '{file}' created at {current_time}")

            # Update the current list of files.
            current_files = updated_files
            
            # Wait for a short interval before checking again to reduce excessive Checks for new files.
            time.sleep(4)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    monitor_directory(directory_to_monitor)