import pytest


def test_add_two_numbers_fail():
    x = 5
    y = 6
    assert x == y, "test failed"


def test_add_two_numbers_pass():
    x = 6
    y = 6
    assert x == y, "test pass"

@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request):
    request.config._metadata = (
        {
            'Environment': 'QA',
            'Build Url': 'https://www.google.com'
        }
    )
