import time
from behave import when, then
from selenium.webdriver.common.by import By

@when(u'clico em home')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'home').click()
    time.sleep(2)
@when(u'preencho "<email>" "<senha>" e clico no botão Login')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('claudio@iterasys.com.br')
    time.sleep(2)
    context.driver.find_element(By.ID, 'password').send_keys('123456')
    time.sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
    time.sleep(2)

@then(u'vejo a mensagem de confirmação')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
    time.sleep(2)
