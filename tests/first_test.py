from playwright.sync_api import sync_playwright, Page
from playwright.sync_api import Page, expect

def test_login_with_invalid_creds(page: Page):
    login_user(page=page, mail="consuertelm@gmail.com", password="Reyna2017milenko")

    page.goto("https://testomat.io")
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    page.get_by_text(text="Log in", exact=True).click()
    # page.get_by_role("textbox", name="name@email.com")

    login_user(page=page, mail="consuertelm@gmail.com", password="Reyna2017milenko")
    page.locator("#content-desktop #user_email").fill("consuertelm@gmail.com")
    page.locator("#content-desktop #user_password").fill("Reyna2017milenko")
    page.get_by_role(role="button", name="Sign in").click()

    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()

def test_search_project_in_company(page: Page):
    page.goto("https://app.testomat.io/users/sign_in")


   # page.get_by_text("Log in", exact=True).click()

   # page.locator("#content-desktop #user_email").fill("consuertelm@gmail.com")
   # page.locator("#content-desktop #user_password").fill("ktkckyl")
   # page.get_by_role(role="button", name="Sign in").click()

    login_user(page=page, mail="consuertelm@gmail.com", password="Reyna2017milenko")
    print(page.url)
    target_project="MyProjectTaras"
    search_for_project(page=page, target_project=target_project)
   # expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    # page.locator("#content-desktop #search").fill(target_project)

    expect(page.get_by_role("heading", name=target_project)).to_be_visible()
    #expect(page.locator("ul li h3").filter(has_text=target_project)).to_have_text(target_project)

def search_for_project(page: Page, target_project:str):
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)

def test_should_be_possible_to_open_free_project(page: Page):
    #arrenge
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page=page, mail="consuertelm@gmail.com", password="Reyna2017milenko")
    #act
    page.locator("#company_id").click()
    page.locator("#company_id").select_option("Free Projects")

    #assert
    target_project = "MyProjectTaras"
    search_for_project(page=page, target_project=target_project)
    expect(page.get_by_role("heading", name=target_project)).to_be_hidden()

    expect(page.get_by_text("You have not created any projects yet")).to_be_visible(timeout=10000)

def open_home_page(page: Page):
    page.goto("https://testomat.io")



def login_user(page, mail, password):
    page.goto("https://app.testomat.io/users/sign_in")

    page.set_viewport_size({"width": 1280, "height": 800})

    container = page.locator("#content-desktop:visible")

    email = container.locator("#user_email")
    password_input = container.locator("#user_password")
    button = container.locator("input[name='commit']")

    email.fill(mail)
    password_input.fill(password)

    password_input.press("Tab")

    expect(button).to_be_visible()
    expect(button).to_be_enabled()

    button.click()