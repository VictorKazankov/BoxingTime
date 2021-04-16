Feature: Test for round time stopwatch

  Scenario: Run time stopwatch
    Given Round time is show

    When Tap start button
    Then Time should be started

    When Tap stop button
    Then Time should be stopped


  Scenario: Reset Favorites Settings icon are presented
    Given Round time is show
    Then Reset icon is displayed
    Then Favorites icon is displayed
    Then Settings icon is displayed


  Scenario: Time can be reset
    Given Round time is show

    When Tap start button
    And Tap stop button
    And Tab reset button

    Then Time is reset