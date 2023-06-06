from ../../config/chromedriver import driver
def scan_csp(url):
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
