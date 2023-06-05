import requests

def scan_header(url):
    print("++++++++++++ Scanning header ++++++++++++")

    response = requests.get(url)
    # Extract and print the headers
    headers = response.headers
    print("Response Headers:")
    for header, value in headers.items():
        print(f"{header}: {value}")
    
    # Perform further analysis or checks on the headers
    
    # Example: Check for specific headers
    if 'Content-Security-Policy' in headers:
        pass
    else:
        print("Content-Security-Policy header not found.")
    
    if 'X-XSS-Protection' in headers:
        print("X-XSS-Protection header found.")
    else:
        print("X-XSS-Protection header not found.")
    
    # ... Continue checking for other headers
    
    # Access specific header values
    content_type = headers.get('Content-Type')
    server = headers.get('Server')
    # ... Perform actions based on specific header values
    
    # Perform additional tasks or analysis based on the headers
    
 # Usage
# scan_header("https://example.com")
