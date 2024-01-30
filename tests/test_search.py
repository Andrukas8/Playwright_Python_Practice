from playwright.sync_api import expect, Page


def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo homepage displayed
    page.goto("https://duckduckgo.com")

    # When the user searches for a phrase
    page.locator("id=searchbox_input").fill("panda")
    page.locator("xpath=//button[@aria-label='Search']").click()
    
    # Then the search result query is the phrase
    expect(page.locator("//input[@id='search_form_input']")).to_have_value('panda')
    
    # And the search result links pertain to the phrase
    page.locator("xpath=//a[@data-testid='result-title-a']").nth(4).wait_for()
    titles = page.locator("xpath=//a[@data-testid='result-title-a']").all_text_contents()
    matches = [t for t in titles if 'panda' in t.lower()]
    assert len(matches) > 0
    
    # And the search result title page contains the phrase
    expect(page).to_have_title('panda at DuckDuckGo')