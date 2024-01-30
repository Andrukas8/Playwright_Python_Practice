# Playwright_Python_Practice
Practicing Python Playwright for Test Automation

Tutorial: [https://github.com/AutomationPanda/playwright-python-tutorial](https://github.com/AutomationPanda/playwright-python-tutorial)

### Tips
```python -m venv venv``` - creates a new environment for the project

```pip install playwright``` - installs playwright

```pip install pytest``` - installs pytest

```pip install pytest-playwright``` - installs pytest plugin for playwright

```playwright install``` - this installs projects Chromium, FFMPEG, Firefox, and Webkit

```python -m pytest tests``` - runs the tests which are in tests directory

```--headed ``` - flag to show ih browser how test runs

```--slowmo 1000``` - makes test run slower in order to be able to see it

```--verbose``` - runs tests with explanations

```--browser chromium``` - select browser project (by default ```chromium```, other options: ```firefox```, ```webkit```)

```--browser chromium --browser firefox --browser webkit``` - runs tests in all 3 browser projects at the same time (not recommended in headed mode)

```--browser-channel chrome``` or ```--browser-channel msedge``` - runs tests in adcual browsers Chrome and Edge

```--device "iPad Mini"``` - emulates mobile devices

```--screenshot on``` - screenshot on every test (saves into a ```test-results``` folder that Playwright creates)

```--screenshot only-on-failure``` - makes screenshots only if test fails

```--video on``` - makes video on every test

```--video retain-on-failure``` - makes video if the test fails

##### For parallel testing:
```pip install pytest-xdist``` - installs pytest-xdist plugin, needed for parallel testing

```-n 2``` - launches tests using 2 workers

```-n 5 --browser --browser chromium --browser firefox --browser webkit``` - launches 5 workers and tests in 3 browsers
