from playwright_mcp.browser import launch_and_get_title

def test_example_title():
    title = launch_and_get_title("https://example.com")
    assert "Example Domain" in title
