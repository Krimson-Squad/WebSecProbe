def scan_xss(url, timeout=30, payload_file="resources/xss.txt"):
    import argparse
    import random
    import re
    import string
    import requests
    from tqdm import tqdm
    from colorama import init, Fore, Style

    """
    Scans a web page for potential XSS vulnerabilities.

    Args:
        url (str): The URL of the web page to scan.
        timeout (int, optional): The request timeout in seconds (default is 30).
        payload_file (str, optional): The file path to the payload file (default is "resources/xss.txt").

    Returns:
        bool: True if potential XSS vulnerability found, False otherwise.
    """
    PAYLOADS_FILE = payload_file

    def _retrieve_content(url, data=None, method='GET'):
        try:
            if method == 'POST':
                response = requests.post(url, data=data)
            else:
                response = requests.get(url, params=data)
            retval = response.text
        except requests.RequestException as ex:
            retval = ex.response.text if ex.response else str(ex)
        return retval or ""

    def load_payloads(filename):
        try:
            with open(filename, 'r') as file:
                payloads = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"{Fore.YELLOW}[!] Payload file '{filename}' not found. No payloads loaded.{Style.RESET_ALL}")
            payloads = []
        return payloads

    def scan_page(url, payloads=None):
        retval, usable = False, False

        # Check if the URL has any query parameters
        if '?' in url:
            url, query = url.split('?', 1)
            params = dict(q.split('=') for q in query.split('&'))
        else:
            params = {}

        for payload in tqdm(payloads, desc="Scanning for XSS vulnerabilities"):
            modified_params = params.copy()

            # Modify each parameter with the XSS payload
            for key in modified_params:
                modified_params[key] = payload

            modified_url = url + '?' + '&'.join(f"{key}={modified_params[key]}" for key in modified_params)

            modified = _retrieve_content(modified_url, method='GET')

            if payload in modified:
                print(f"{Fore.RED}[+] Potential XSS vulnerability found with payload: {payload}{Style.RESET_ALL}")
                retval = True

        return retval

    print(Fore.GREEN+"++++++++++++ Scanning for XSS vuln. in URL ++++++++++++")
    payloads = load_payloads(PAYLOADS_FILE)
    scan_page(url, payloads=payloads)

