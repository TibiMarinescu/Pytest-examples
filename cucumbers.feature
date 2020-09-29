# Created by tibi at 9/24/2020
Feature: Cucumber Basket
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.
  # Enter feature description here

  Scenario Outline: Add cucumbers to a basket
    Given the basket has "2" cucumbers
    When they are added "4" cucumbers to the basket
    Then the basket has "6" cucumbers.

  Scenario:  Remove cucumbers from a basket
    Given the basket has "8" cucumbers
    When they are removed "3" cucumbers from the basket
    Then the basket has "5" cucumbers