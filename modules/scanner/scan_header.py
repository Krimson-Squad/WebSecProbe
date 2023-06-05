def scan_header(url):
    """
    Scans the security headers of a given URL and performs vulnerability checks.

    Args:
        url (str): The URL of the web application to scan.

    Returns:
        None

    Raises:
        ValueError: If the provided URL is invalid or inaccessible.

    Example:
        scan_header("https://example.com")
    [Contributor: Dev. Gautam Kumar]
    """
    import requests
    print("++++++++++++ Scanning header ++++++++++++")

    response = requests.get(url)
    headers = response.headers

    # Content Security Policy (CSP) Scanner
    if 'Content-Security-Policy' in headers:
        print("[+] Content-Security-Policy header found.")
        # Perform further checks or actions related to CSP
    else:
        print("\033[91m[-] Content-Security-Policy header not found.\033[0m")
        print("Reference: [OWASP Content Security Policy](https://owasp.org/www-project-secure-headers/#content-security-policy)")

    # X-XSS-Protection Scanner
    if 'X-XSS-Protection' in headers:
        print("[+] X-XSS-Protection header found.")
        # Perform further checks or actions related to XSS protection
    else:
        print("\033[91m[-] X-XSS-Protection header not found.\033[0m")
        print("Reference: [OWASP XSS (Cross Site Scripting) Prevention Cheat Sheet](https://owasp.org/www-community/xss-filter-evasion-cheatsheet)")

    # X-Frame-Options Scanner
    if 'X-Frame-Options' in headers:
        print("[+] X-Frame-Options header found.")
        # Perform further checks or actions related to clickjacking protection
    else:
        print("\033[91m[-] X-Frame-Options header not found.\033[0m")
        print("Reference: [OWASP Clickjacking Defense Cheat Sheet](https://owasp.org/www-community/attacks/Clickjacking)")

    # HSTS (Strict-Transport-Security) Scanner
    if 'Strict-Transport-Security' in headers:
        print("[+] Strict-Transport-Security header found.")
        # Perform further checks or actions related to HSTS
    else:
        print("\033[91m[-] Strict-Transport-Security header not found.\033[0m")
        print("Reference: [OWASP Transport Layer Protection Cheat Sheet](https://owasp.org/www-project-secure-headers/#http-strict-transport-security-hsts)")

    # CORS (Cross-Origin Resource Sharing) Scanner
    if 'Access-Control-Allow-Origin' in headers:
        print("[+] CORS headers found.")
        # Perform further checks or actions related to CORS configuration
    else:
        print("\033[91m[-] CORS headers not found.\033[0m")
        print("Reference: [OWASP Cross-Origin Resource Sharing (CORS) Cheat Sheet](https://owasp.org/www-community/attacks/CORS_OriginHeaderScrutiny)")

    # Members may add other headers scanners...
    # Add more scanners for additional security headers as needed

    # Access specific header values
    content_type = headers.get('Content-Type')
    server = headers.get('Server')
    # ... Perform actions based on specific header values
    
    # Perform additional tasks or analysis based on the headers
    
# Usage
# scan_header("https://example.com")
