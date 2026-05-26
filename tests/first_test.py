import os

import pytest
from playwright.sync_api import Page, expect

from tests.conftest import Config

@pytest.fixture(scope="function")
def login(page: Page, configs: Config):page.goto(configs.login_url, timeout=60000)
    login_user(page=page, mail=configs.email, password=configs.password)

    TARGET_PROJECT  = "MyProjectTaras"

def test_login_with_invalid_creds(page: Page, configs):
    #login_user(page=page, mail=EMAIL, password=PASSWORD)

    open_home_page(page)
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    page.get_by_text(text="Log in", exact=True).click()
    # page.get_by_role("textbox", name="name@email.com")

    from faker import Faker

    invalid_password = Faker().password(length=10)

    login_user(page=page, mail=configs.email, password=invalid_password)
    page.locator("#content-desktop #user_email").fill("consuertelm@gmail.com")
    page.locator("#content-desktop #user_password").fill("Reyna2017milenko")
    page.get_by_role(role="button", name="Sign in").click()

    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()

   # LOGIN_URL = os.getenv("LOGIN_URL")


def test_search_project_in_company(page: Page, configs: Config):
    page.goto(configs.login_url, timeout=60000)
    login_user(page=page, mail=configs.email, password=configs.password)

    # page.get_by_text("Log in", exact=True).click()

    # page.locator("#content-desktop #user_email").fill("consuertelm@gmail.com")
    # page.locator("#content-desktop #user_password").fill("ktkckyl")
    # page.get_by_role(role="button", name="Sign in").click()

    print(page.url)

    search_for_project(page=page, target_project=TARGET_PROJECT)
    # expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    # page.locator("#content-desktop #search").fill(target_project)

    expect(page.get_by_role("heading", name=TARGET_PROJECT)).to_be_visible()
    # expect(page.locator("ul li h3").filter(has_text=target_project)).to_have_text(target_project)


def search_for_project(page: Page, target_project: str):
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)


def test_should_be_possible_to_open_free_project(page: Page, configs: Config):
    # arrenge
    page.goto(configs.login_url, timeout=6000)
    login_user(page,configs.email , configs.password)
    # act
    page.locator("#company_id").click()
    page.locator("#company_id").select_option("Free Projects")

    # assert

    search_for_project(page=page, target_project=TARGET_PROJECT)
    expect(page.get_by_role("heading", name=TARGET_PROJECT)).to_be_hidden()

    expect(page.get_by_text("You have not created any projects yet")).to_be_visible(timeout=10000)


def open_home_page(page: Page):
    page.goto(os.getenv("BASE_URL"))


def login_user(page, mail, password):
    email_input = page.locator("input[name='user[email]']:visible")
    password_input = page.locator("input[name='user[password]']:visible")
    sign_in_button = page.locator("input[value='Sign In']:visible")

    email_input.fill(mail)
    password_input.fill(password)

    expect(sign_in_button).to_be_enabled()

    sign_in_button.click()

    # email.fill(mail)
    # password_input.fill(password)

    # password_input.press("Tab")

    # expect(button).to_be_visible()
    # expect(button).to_be_enabled()

    # button.click()
