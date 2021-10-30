#use fixtures and tags on the feature/scenario level
Feature: showing off behave

  @nightly @staging @production
  Scenario: run a simple test
      Given we have behave installed
      When we implement a test
      Then behave will test it for us!


  @demo
  Scenario Outline: Explore Cuke py features
    Given Navigate to URL "<urls>"
    Examples: tutorials
    |urls                                                 |
    |https://behave.readthedocs.io/en/stable/gherkin.html |
    |https://behave.readthedocs.io/en/stable/tutorial.html|
    |https://behave.readthedocs.io/en/stable/fixtures.html|