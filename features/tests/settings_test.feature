Feature: Test settings screen

  Scenario: Change training time option
    Given Open settings screen

    When Tap right button training option
    Then Training time increase 10

    When Tap left button training option
    Then Training time decrease 10

  Scenario: Change sound value
    Given Open settings screen

    When Change slider sound settings

    Then Slider state should be changed