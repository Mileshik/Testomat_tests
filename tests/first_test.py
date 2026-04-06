from playwright.sync_api import sync_playwright, Page
from playwright.sync_api import Page, expect

def test_login_with_invalid_creds(page: Page):
    open_home_page(page)
    page.wait_for_load_state("networkidle")

    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    page.locator("a[href*='sign_in']").first.click()
    # page.get_by_role("textbox", name="name@email.com")
    page.locator("#content-desktop #user_email").fill("consuertelm@gmail.com")
    page.locator("#content-desktop #user_password").fill("ktkckyl")

    page.get_by_role("button", name="Sign In").click()
    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()


def open_home_page(page: Page):
    page.goto("https://testomat.io")


def test_search_project_in_company(page: Page):
    page.goto("http://app.testomat.io/users/sign_in")


    login_user(page, email="consuertelm@gmail.com", password="*****")

    target_project = "MyProjectTaras"
    expect(page.get_by_role(role="searchbox", name="Search")).to_be_visible()
    search_for_project(page, target_project)

    expect(page.get_by_role(role="heading", name=target_project)).to_be_visible()

   # expect(page.locator("ul li h3", has_text=target_project)).to_be_visible()
    #expect(page.locator("ul li h3").filter(has_text=target_project)).to_be_visible()

def test_should_be_possible_to_open_free_project(page: Page):
    #arrange
    page.goto("http://app.testomat.io/users/sign_in")
    login_user(page, email="consuertelm@gmail.com", password="*****")
    #act
    page.locator("#company_id").click()
    page.locator("#company_id").select_option("Free Projects")
    # assert
    target_project = "MyProjectTaras"
    search_for_project(page, target_project)
    expect(page.get_by_role(role="heading", name=target_project)).to_be_hidden()

    expect(page.get_by_text("You have not crested any projects yet")).to_be_visible(timeout=10000)

def search_for_project(page: Page, target_project: str):
    page.locator("#content-desktop #search").fill(target_project)


def open_home_page(page: Page):
    page.goto("https://testomat.io")


def login_user(page:Page, email:str, password:str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role(role="button", name="Sign In").click(no_wait_after=True)

def test_search_case_insensitive(page: Page):
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page, "consuertelm@gmail.com", "Reyna2017milenko")

    search_for_project(page, "myprojecttaras")

    expect(page.get_by_text("MyProjectTaras")).to_be_visible()