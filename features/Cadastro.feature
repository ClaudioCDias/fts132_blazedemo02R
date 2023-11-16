@Cadastro
Feature: Cadastro de Usuário
  Scenario: Cadastro com Sucesso
    Given que acesso o site Blazedemo
    When clico em Home
    And clico em Register
    Then vejo o formulário de cadastro
    When preencho "<nome>" "<empresa>" "<email>" "<senha>"
    And clico no botão Register
    Then exibe a confirmação do cadastro