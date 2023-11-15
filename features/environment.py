from selenium import webdriver

# Início
def before_all(context):      # Antes de tudo
    # Declarar o Selenium, instanciar como navegador e apontar o driver
    context.driver = webdriver.Chrome()

    # Maximizar a janela do navegador
    context.driver.maximize_window()

    print('Passo A - Antes de Tudo')

# Fim
def after_all(context):       # Depois de tudo

    # Desligar / Destruir o objeto do Selenium
    context.driver.quit()

    print('Passo Z - Depois de Tudo')