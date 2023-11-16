import time

from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico em Register')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Register').click()
    time.sleep(1)
@then(u'vejo o formulário de cadastro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Register'
    time.sleep(1)
@when(u'preencho "<nome>" "<empresa>" "<email>" "<senha>"')
def step_impl(context):
    context.driver.find_element(By.ID, 'name').send_keys('Juca Pirama')
    time.sleep(1)
    context.driver.find_element(By.ID, 'company').send_keys('Iterasys')
    time.sleep(1)
    context.driver.find_element(By.ID, 'email').send_keys('juca@iterasys.com.br')
    time.sleep(1)
    context.driver.find_element(By.ID, 'password').send_keys('123456')
    time.sleep(1)
    context.driver.find_element(By.ID, 'password-confirm').send_keys('123456')
    time.sleep(1)

@when(u'clico no botão Register')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
    time.sleep(1)
@then(u'exibe a confirmação do cadastro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
    time.sleep(1)