def test_sql_injection(url, parameters_file="", payloads_file=""):
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
    import requests
    from modules.config.default_config import parameters_file,payloads_file
    print("++++++++++++ SQL Injection Testing ++++++++++++")

    with open(parameters_file, 'r') as f:
        parameters = [line.strip() for line in f.readlines()]

    with open(payloads_file, 'r') as f:
        payloads = [line.strip() for line in f.readlines()]

    for parameter in parameters:
        for payload in payloads:
            # Build the payload with the parameter
            payload_data = {parameter: payload}

            try:
                response = requests.get(url, params=payload_data)
                # Check the response for indications of SQL injection
                if "error" in response.text.lower() or "syntax error" in response.text.lower():
                    print(f"[+] Potential SQL injection vulnerability found with parameter '{parameter}' and payload '{payload}'")
                    print('response: '+ response.text)
            except requests.exceptions.RequestException as e:
                print(f"Error occurred while testing parameter '{parameter}' and payload '{payload}': {str(e)}")

