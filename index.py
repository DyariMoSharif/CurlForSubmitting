import requests

# Define the form data
form_data = {
    'Name': 'Dyari Ameen'
}

# Make the POST request with the form data
response = requests.post('https://ee.humanitarianresponse.info/x/vG9yQk80', data=form_data)

# Check the response
if response.status_code == 200:
    print('Form submitted successfully!')
else:
    print('Form submission failed.')
