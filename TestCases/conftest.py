import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Ie

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--application", action="store", default="Orange_HRM"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        path = "./Driver/geckodriver.exe"
        firefox_opt = webdriver.FirefoxOptions()
        firefox_opt.add_argument('--disable-gpu')
        driver = Firefox(executable_path=path, options=firefox_opt)
    elif browser_name == "chrome":
        path = "./Driver/chromedriver.exe"
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        driver = Chrome(executable_path=path, options=chrome_opt)
    elif browser_name == "Ie":
        path = "./Driver/IEDriverServer.exe"
        driver = Ie(executable_path=path)
    else:
        print("No Browser path found")

    print("Driver Initiating Successfully")

    application = request.config.getoption("application")
    if application == "Git_Hub":
        driver.get("https://github.com/")
    elif application == "Orange_HRM":
        driver.get("https://opensource-demo.orangehrmlive.com/")
    else:
        print("URL path not found")

    print("Hit URL Successfully")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def startBrowser(request):
    global driver

    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        path = "./Driver/geckodriver.exe"
        firefox_opt = webdriver.FirefoxOptions()
        firefox_opt.add_argument('--disable-gpu')
        driver = Firefox(executable_path=path, options=firefox_opt)
    elif browser_name == "chrome":
        path = "./Driver/chromedriver.exe"
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        driver = Chrome(executable_path=path, options=chrome_opt)
    elif browser_name == "Ie":
        path = "./Driver/IEDriverServer.exe"
        driver = Ie(executable_path=path)
    else:
        print("No Browser path found")

    print("Driver Initiating Successfully")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    print("Url Hit Successfully")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
