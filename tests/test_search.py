from playwright.sync_api import Page


def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo homepage displayed
    page.goto("https://duckduckgo.com")

    # When the user searches for a phrase
    page.locator("id=searchbox_input").fill("panda")
    page.locator("xpath=//button[@aria-label='Search']").click()
    
    # Then the search result query is the phrase
    # And the search result links pertain to the phrase
    # And the search result title contains the phrase
    pass
