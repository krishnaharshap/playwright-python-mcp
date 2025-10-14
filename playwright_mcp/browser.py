from playwright.sync_api import sync_playwright

def launch_and_get_title(url: str = "https://example.com") -> str:
    """Launch Chromium headless, navigate to URL, return title."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        browser.close()
        return title

if __name__ == "__main__":
    print("Title:", launch_and_get_title())
