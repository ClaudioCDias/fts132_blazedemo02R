@Login
Feature: Login
  Scenario: Login com Sucesso
    Given que acesso o site Blazedemo
    When clico em Home
    And preencho "<email>" "<senha>" e clico no botão Login
    Then vejo a mensagem de confirmação