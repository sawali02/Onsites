import requests

def check_website_status(urls):
    status_report = {}
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                status_report[url] = "Up"
            else:
                status_report[url] = f"Down (Status Code: {response.status_code})"
        except requests.RequestException as e:
            status_report[url] = f"Down (Error: {e})"
    
    return status_report

def display_status(status_report):
    print("Website Status Report:")
    for url, status in status_report.items():
        print(f"{url}: {status}")

if __name__ == "__main__":
    # List of websites to check
    websites = [
        "https://www.github.com",
        "https://www.google.com",
        "https://www.wikipedia.org",
       
        
        "https://spider.nitt.edu"
    ]
    
    report = check_website_status(websites)
    display_status(report)
