import pytest
from drivers.android_driver_factory import create_driver_android

@pytest.fixture(scope="function")
def driver(request):
    env = request.config.getoption("--env") or "android_app"
    driver = create_driver_android(env)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="android_app",
                     help="Choose environment: android or android_app")
