Feature: sort by ascending price  
  Scenario:  
    Given the user has gone into a garage sale menu, 
    When the user clicks on a sort by drop-down, 
    And the user chooses to sort by price, 
    And the user chooses to sort ascending, 
    Then the user should be shown the items with the cheapest items at the top and most expensive items at the bottom. 