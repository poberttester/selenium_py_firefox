import time
import yaml
from module import Site
import pytest

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata['address'])


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


def test_create_post(site):
    """ Условие: Добавить в наш тестовый проект шаг добавления поста после входа.
        Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
        Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.
    """
    input_username = '//*[@id="login"]/div[1]'
    input_password = '//*[@id="login"]/div[2]'
    login_button = '//*[@id="login"]/div[3]'

    username = site.find_element(mode='xpath', path=input_username)
    username.send_keys(testdata['user'])
    password = site.find_element(mode='xpath', path=input_password)
    password.send_keys(testdata['password'])
    login = site.find_element(mode='xpath', path=login_button)
    login.click()
    time.sleep(testdata['sleep_time'])

    create_new_post = '//*[@id="app"]/main/div/div[2]/div[1]'
    input_title = '//*[@id="create-item"]/div/div/div[1]/div/label/input'
    input_description = '//*[@id="create-item"]/div/div/div[2]/div/label/input'
    input_content = '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'
    save_button = '//*[@id="create-item"]/div/div/div[7]/div/button/div'

    add_post = site.find_element(mode='xpath', path=create_new_post)
    add_post.click()
    title = site.find_element(mode='xpath', path=input_title)
    title.send_keys(testdata['name'])
    description = site.find_element(mode='xpath', path=input_description)
    description.send_keys(testdata['description'])
    content = site.find_element(mode='xpath', path=input_content)
    content.send_keys(testdata['сontent'])
    save = site.find_element(mode='xpath', path=save_button)
    save.click()
    time.sleep(testdata['sleep_time'])

    findly_text = '//*[@id="app"]/main/div/div[1]/h1'
    result = site.find_element(mode='xpath', path=findly_text)
    text_cat = result.text

    assert text_cat == testdata['name']



if __name__ == '__main__':
    pytest.main(['-v'])

# if __name__ == '__main__':
#     ceate_post(testdata['address'])
