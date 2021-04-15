Feature: Test for round time stopwatch

  Scenario: run time stopwatch
     Given Round time is show

     When Tap start button
     Then Time should be started

     When Tap stop button
     Then Time should be stopped
