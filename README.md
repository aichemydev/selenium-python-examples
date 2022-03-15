# selenium-python-examples

Selenium Python example tests

The Test Gold Product allows you to submit a python selenium test script.

It learns from an old selenium script run
Make code changes to the site
It heals your Selenium script to work on the new site
Example is now with pip.

cd reactbank
Have the virtualenv executable installed
export your TG_TOKEN, e.g. export TG_TOKEN='eyJ3YWxTZ..' , get an account from nocode.testgold.dev if you dont have an account. Note that for new users, you have to wait up to 24 hours before you are manually activated. This is a measure to guard against hackers.
Download the selenium-20.11.0-py2.py3-none-any.whl wheel from the nocode.testgold.dev site and place it in the reactbank folder

./test_original_app.sh to test the original site (this installs the package in a virtual env and runs the script)
./test_modified_app.sh to test the modified site, you will see testgold healing in action. 


## Running the examples on Windows

You will need [Python 3.x.x ](https://www.python.org/downloads/) and pip package.

- Download Python on your machine.
- Install pip package.
- Download Python wheel in [Test Gold Interceptor packages.](https://dev.k8s.testgold.dev/details/installation)

Install pip package

- If you have Python installed on your machine, check for pip package ~ from command line run `pip --version` or `py -m pip --version`
- If pip isn’t already installed, then first try to bootstrap it from the standard library: `py -m ensurepip --default-pip`

If that still doesn’t allow you to run `python -m pip` 

- Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
- Run python get-pip.py

After downloading Python on your machine, you have to create a virtual environments. We recommend you this to create [virtual environments](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments).

Download the Python wheel from [Test Gold Interceptor packages.](https://dev.k8s.testgold.dev/details/installation) and add it to the virtual environment you created for Python.
And now you're ready to run Python Selenium examples.

- Open a `Command line` terminal by clicking on the "Start" button and typing in: `cmd` and hitting Enter.
- Navigate to where you have stored these Python examples by using cd, for example: `cd ~/Github/selenium-python-examples`
- Copy the value of TG_TOKEN on the [TestGold Installations page]((https://dev.k8s.testgold.dev/details/installation) and save it as an environment variable by pasting: `SET TG_TOKEN='your token goes here'
- Set the following environment variable: `python name-of-test.py`





