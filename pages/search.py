from playwright.sync_api import Page


class DuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input = page.locator("id=searchbox_input")
        self.search_button = page.locator(
            "xpath=//button[@aria-label='Search']")

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()
