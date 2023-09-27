import time
import yaml
from module import Site
import pytest

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def site():
    site1 = Site(testdata['address'])
    yield site1
    site1.driver.quit()