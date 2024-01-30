from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page


def test_basic_duckduckgo_search(page: Page) -> None:
    result_page = DuckDuckGoResultPage(page)
    search_page = DuckDuckGoSearchPage(page)

    # Given the DuckDuckGo homepage displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search('panda')

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value('panda')

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase('panda')

    # And the search result title page contains the phrase
    expect(page).to_have_title('panda at DuckDuckGo')
