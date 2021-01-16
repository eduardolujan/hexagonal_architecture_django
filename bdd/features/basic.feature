# file: features/basic.py

Feature: Basic first test


Scenario: Run a basic test
  Given we have health check to test if the application is running
  When the app is running
  Then with requests get the status
