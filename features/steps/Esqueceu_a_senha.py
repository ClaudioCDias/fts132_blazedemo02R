import time
from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico no link Forgot Your Password?')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Forgot Your Password?').click()
    time.sleep(1)
@then(u'vejo a página de reiniciar a senha')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Reset Password'
    time.sleep(1)
@when(u'preencho meu "{email}" e clico no botão Send Password Reset Link')
def step_impl(context, email):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/button[1]').click()
    time.sleep(1)
@then(u'vejo a confirmação')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
    time.sleep(1)