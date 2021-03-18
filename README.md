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
