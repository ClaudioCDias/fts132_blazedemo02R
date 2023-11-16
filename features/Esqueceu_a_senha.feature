@esqueceu_a_senha
Feature: Esqueceu a senha
  Scenario Outline: Usuários Cadastrados
    Given que acesso o site Blazedemo
    When clico em Home
    And clico no link Forgot Your Password?
    Then vejo a página de reiniciar a senha
    When preencho meu "<email>" e clico no botão Send Password Reset Link
    Then vejo a mensagem de confirmação
    Examples:
      | email                   |
      | juca@iterasys.com.br    |
      | correia@iterasys.com.br |

