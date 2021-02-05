# Created by vishnu.vardhan at 03/02/21
Feature: Github API validation
  # Enter feature description here

  Scenario: Session management in Github
    Given I have github auth credentials
    When github repo get contract is hit
    Then check contract is returning 200
  Scenario: Login in github
    Given I have login and auth credentials
    When user get contract is hit
    Then check contract is returning 200