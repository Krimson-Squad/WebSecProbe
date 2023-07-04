import requests
from colorama import init, Fore
from tqdm import tqdm
# Initialize colorama
init(autoreset=True)
def test_sql_injection(url, parameters_file="resources/parameters.txt", payloads_file="resources/payloads.txt"):
    """
    Tests for SQL injection vulnerabilities by trying different payloads with parameters.

    Args:
        url (str): The URL of the web application to test.
        parameters_file (str): The file path to the text file containing the parameters.
        payloads_file (str): The file path to the text file containing the payloads.

    Returns:
        None

    Raises:
        ValueError: If the provided URL is invalid or inaccessible.

    Example:
        test_sql_injection("https://example.com", "parameters.txt", "payloads.txt")
    """

    print(Fore.GREEN+"++++++++++++ SQL Injection Testing ++++++++++++")

    with open(parameters_file, 'r') as f:
        parameters = [line.strip() for line in f.readlines()]
    total_tests = len(parameters)
    progress_bar = tqdm(total=total_tests, unit=" injection(s)")
    vulnerable_parameters = {}
    with open(payloads_file, 'r') as f:
        payloads = [line.strip() for line in f.readlines()]

    vulnerable_parameters = {}

    for parameter in parameters:
        progress_bar.set_description(f"Testing payload injection(s) with parameter name [{parameter}]")
        for payload in payloads:
           
            payload_data = {parameter: payload}
           
            try:
                response = requests.post(url, params=payload_data)
                # print('Trying ' + payload)
                
                error_strings = ["error", "syntax error", "unexpected", "query error", "server error"]
                if any(error_string in response.text.lower() for error_string in error_strings):
                    # print(f"\033[91m[-] Potential SQL injection vulnerability found with parameter '{parameter}' and payload '{payload}'")
                    vulnerable_parameters.setdefault(parameter, []).append(payload)
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"Error occurred while testing parameter '{parameter}' and payload '{payload}': {str(e)}")
            progress_bar.update(1)

    progress_bar.close()
    if len(vulnerable_parameters) != 0:
        print(Fore.RED + "\n[+] SQL Injection Vulnerabilities Found:")
        for parameter, payloads in vulnerable_parameters.items():
            print(Fore.BLUE+"Parameter:" + parameter)
            print("Payloads:")
            for payload in payloads:
                print(f"- {payload}")
            print("")
    else:
        print("\n[#] No SQL Injection vulnerabilities found.")

