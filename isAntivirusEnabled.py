import subprocess

antivirus_name = "WinDefend"

def is_antivirus_enabled():
    try:
        # Run the 'sc query' command to get information about the service
        result = subprocess.run(['sc', 'query', antivirus_name], capture_output=True, text=True, check=True)

        # Check if the service is in the output
        if "RUNNING" in result.stdout:
            return 0
        elif "STOPPED" in result.stdout:
            return 1
        else:
            print("Unexpected output:", result.stdout)
            return 1

    except subprocess.CalledProcessError as e:
        print("Error running command:", e)
        return 1

# Check if antivirus is enabled
antivirus_enabled = is_antivirus_enabled()
print(antivirus_enabled)

