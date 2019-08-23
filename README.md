
- selenium_teplate
    - Elements
        - blocks      "Grouped locators in blocks"
        - locators    "Element locators (by class)"
    - Models  "Model in which the described pages are initialized"
    - Pages   "Page description and steps description"
    - Utils   "Some healpers utils "
    - Test


UI tests for the platform and games
Before launch:
```
pip install -r requirements.txt
```



Parallel test (default command in docker):
```
python3 -m pytest -n 2 --alluredir=./results -vv
```

See the report:
```
allure serve results/
```
