# Created by vishnu.vardhan at 03/02/21
Feature: Verify if todo get API is displaying the results
  # Enter feature description here
  @smoke
  Scenario Outline: Verify Todolist for a fake API
    Given The <userid> of todo in path param
    When  todo GET contract is executed
    Then Todo list is successfully displayed
    And check contract is returning 200
    Examples:
    |userid|
    |1     |
    |2     |
    |3     |

