
def scan_csp(url):
  """
    Scans the security headers if it conatins csp implementation of a given URL and performs vulnerability checks.

    Args:
        url (str): The URL of the web application to scan.

    Returns:
        None

    Raises:
        ValueError: If the provided URL is invalid or inaccessible.

    Example:
        scan_header("https://example.com")
    [Contributor: TheNittam]
    """
  import sys
  from modules.config.chromedriver import driver
  driver.get(url)
  # Retrieve the page source code
  source_code = driver.page_source
  # Analyze the source code
  if 'Content-Security-Policy' in source_code:
    print('CSP is implemented.')
  else:
    print('CSP is not implemented.')
    # Close the driver
  driver.quit()
