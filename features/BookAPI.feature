# Created by vishnu.vardhan at 29/01/21
Feature: Verify if books are added and deleted using Library API
  # Enter feature description here
  @regression
  Scenario Outline:  Verify Add Book API functionality
    Given The book details which needed to be added to Library API with <title> and <body> and <userid>
    When The AddBook post contract is executed
    Then Book is successfully Added
    Examples:
      |title  | body| userid|
      |abcd   | loremipsum| 4|
      |efgh   | loremipsum1| 5|
      |ijkl   | loremipsum2| 6|

