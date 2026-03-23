from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

def login_with_invalid_creds(page: Page):
    page.goto("https://testomat.io")

    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    page.get_by_text(text="Log in", exact=True).click()
    # page.get_by_role("textbox", name="name@email.com")
    page.locator("#content-desktop #user_email").fill("consuertelm@gmail.com")
    page.locator("#content-desktop #user_password").fill("ktkckyl")
    page.get_by_role(role="button", name="Sign in").click()

    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
