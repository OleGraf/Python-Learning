# Python-Learning

Setup and needed installs:
------------
Python 3.9.13 https://www.python.org/downloads/release/python-3913/<br>
vsCode https://code.visualstudio.com/<br>
    
    Extensions:
        Python Microsoft extension
        Rainbow CSV

Linter
------------
pip install flak8<br>

Settings File:

    preferences - settings - file view
    "editor.fontSize": 16,
     // Whether to lint Python files
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": false,
     "python.linting.flake8Enabled": true,
 
     // Path to flake8 executable
     //"python.linting.flake8Path": "/Library/Frameworks/Python.framework/Versions/3.9/bin/flake8",
 
     // Flake8 Arguments
     "python.linting.flake8Args": ["--ignore=E501, E128, W605", "--verbose", "--exclude=__init__.py"],
 
     // Formatting: Use AutoPep8
     "python.formatting.provider": "autopep8",
     "[python]" : {
         "editor.formatOnSave": true,
         "editor.codeActionsOnSave": {"source.organizeImports": true}
    },
    "workbench.colorTheme": "Default Dark+",
 
     // More settings goes here...

Other Pakages
------------
pip install pandas<br>
pip install seaborn<br>
pip install scikit-learn<br>

Following edX courses and learning
------------