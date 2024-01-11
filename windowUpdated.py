import subprocess

def get_last_update_state():
    try:
        # Run the 'wmic' command to get information about the last update
        result = subprocess.run(['wmic', 'qfe', 'get', 'Caption,Description,HotFixID,InstalledOn'], capture_output=True, text=True, check=True)

        # Find the line with the most recent update
        lines = result.stdout.split('\n')
        last_update_line = lines[2]  # Assuming the third line contains the most recent update information

        # Extract the relevant information
        update_info = last_update_line.split()
        caption = update_info[0]
        description = update_info[1]
        installed_on = update_info[3]

        return f"Last update: {caption} ({description}) installed on {installed_on}"

    except subprocess.CalledProcessError as e:
        return "Error running command: " + str(e)

def main():
    last_update_state = get_last_update_state()
    print(last_update_state)

if __name__ == "__main__":
    main()
