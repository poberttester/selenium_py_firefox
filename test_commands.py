import time
import yaml
from module import Site
import pytest

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

#site = Site(testdata['address'])


def test_find(site):
    selectir = '//*[@id="APjFqb"]'
    button = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"
    findly_text = '/html/body/div[6]/div/div[12]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div'

    input1 = site.find_element(mode='xpath', path=selectir)
    input1.send_keys('Коты')
    button1 = site.find_element(mode='xpath', path=button)
    button1.click()
    time.sleep(testdata['sleep_time'])

    result = site.find_element(mode='xpath', path=findly_text)
    text_cat = result.text

    assert text_cat == 'Кошка'


if __name__ == '__main__':
    pytest.main(['-v'])