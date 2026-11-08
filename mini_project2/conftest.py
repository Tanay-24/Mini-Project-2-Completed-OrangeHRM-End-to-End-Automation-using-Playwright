import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=700)
        yield browser
        browser.close()

@pytest.fixture
def page(browser_instance):
    context = browser_instance.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()