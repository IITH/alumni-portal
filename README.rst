IITH Alumni portal
==================

This project will host code for the IITH Alumni portal.

GitHub Issues will be used to track all the new features to be developed, and
also for bugs. More information will be added soon.


Installation
------------

Install `pip` and then install system-wide `virtualenv` PIP package.

    sudo apt-get install python-pip
    sudo pip install virtualenv

Create a virtual environment for our current `alumni-portal` project in a
folder named `.venv`, and "activate" it, so that all our subsequent PIP
packages are installed in this virtual environment only, and not globally. Note
that you don't require `sudo` access any more to install PIP packages in this
local virtual environment.

    cd alumni-portal
    virtualenv .venv
    source .venv/bin/activate


Install `Django` package

    pip install Django

Run this command to see if you have successfully installed `Django`. If your
installation was successful, you'll see a version number (e.g. `1.7.3`) as the
output.

    python -c "import django; print(django.get_version())"
