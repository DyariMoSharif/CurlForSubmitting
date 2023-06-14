import subprocess

# Define the form data as a dictionary
form_data = {
    'Name': 'John Doe'
}

# Convert the form data dictionary into a string of key-value pairs
form_data_str = '&'.join([f"{key}={value}" for key, value in form_data.items()])

# Prepare the curl command
curl_command = f"curl -X POST -d '{form_data_str}' https://ee.humanitarianresponse.info/x/vG9yQk80"

# Execute the curl command using subprocess
result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

# Check the result
if result.returncode == 0:
    print("Form submitted successfully!")
else:
    print("An error occurred while submitting the form.")
    print(result.stderr)
