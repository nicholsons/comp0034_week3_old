# COMP0034 week 3 code to support the activities on Moodle

The code in this repository supports the activities in Moodle. It is not intended to function as an exemplar or as a
standalone repository.

## Contents

This week there are 2 directories in the repository:

1. `activities`

   This contains 3 Jupyter notebooks for learning to use Plotly Express and creating choropleth maps.

   There is also an activity written in markdown that explains how to save the chart types created so far and add them
   to the template Flask app for coursework 1.

   You may use your IDE (if it supports Jupyter notebooks) or Binder for these activities.

   You can use a preconfigured Binder session
   here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nicholsons/comp0034_week3/HEAD)

   You can also create your own Binder session linked to your GitHub classroom repo. Go
   to [mybinder.org](https://mybinder.org) amd enter the URL to your GitHub repo. Binder will not keep your notebook
   changes once you close the session, however you can download a copy of your notebook before quitting binder and you
   can add that to your repo. There wasn't previously a facility to save back to GitHub though do check the Binder
   documentation as new features may have been added.

2. `flask_app`

   This contains a Flask web app that is similar to the template provided for courswork 1 in GitHub classroom.

   Ideally you should use an IDE such as PyCharm for this as it should provide better support for Flask. If you need an
   online IDE then [Pythonanywhere](https://help.pythonanywhere.com/pages/Flask/) allows Flask apps to be created and
   run online, however you will need to read their documentation as there are some minor differences in how you
   configure Flask to run online.

## Setting up your coding environment

### Jupyter notebooks

The plotly express activities are contained within jupyter notebooks. These can either be accessed in Binder or in your
preferred IDE (if it supports Jupyter).

### Flask app

To use the Flask app you will need to:

1. create a virtual environment ([PyCharm documentation]())
2. install the dependencies from requirements.txt ([PyCharm documentation](https://www.jetbrains.com/help/pycharm/managing-dependencies.html))
3. check your IDE configuration:  [Pycharm Flask documentation](https://www.jetbrains.com/help/pycharm/flask.html)
    - supports Flask
    - supports Jinja
    - recognises the template and static folders

You should by now know how to create a venv in your preferred development environment as this was covered several times
in COMP0035. Use the help for your IDE for instructions. For those familiar with a command
line [refer to the Python documentation](https://docs.python.org/3/library/venv.html).

Likewise you should be able to install the requirements from requirements.txt. If not then lookup in your IDE help or to
use a command
line [refer to the pip documentation here.](https://pip.pypa.io/en/stable/reference/pip_install/#example-requirements-file)

To check that your IDE config supports Flask then for PyCharm view the instructor video in Moodle, for all other IDEs
you will need to use their online documentation. Please attend the Monday or Friday tutorial sessions if you need help.
