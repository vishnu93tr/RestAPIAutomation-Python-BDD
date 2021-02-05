# Created by vishnu.vardhan at 04/02/21
Feature: Github login API functionality
  # Enter feature description here

  Scenario: Login in github
    Given I have login and auth credentials
    When user get contract is hit
    Then check contract is returning 200