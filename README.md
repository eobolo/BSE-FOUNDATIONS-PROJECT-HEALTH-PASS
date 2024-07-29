## Install Python

Django is a Python web framework, thus requiring Python to be installed on your machine. At the time of writing, Python 3.12 is the latest version.

## Checkout HealthPass
   - [Academic_Feedback_Sys](https://olugbeminiyi2000.pythonanywhere.com/academic_feedback_sys/dashboard/)

### Installation Steps:

1. **Download Python**: 
   - Go to [Python Downloads Page](https://www.python.org/downloads/).
   - Click on the download button for the latest Python version.
   - Download the executable installer.

2. **Run the Installer**:
   - Run the downloaded installer.
   - Check the box next to "Install launcher for all users (recommended)".
   - Click "Install Now" to begin the installation process.

3. **Verify Installation**:
   - After installation, open the command prompt.
   - Check that the Python version matches the version you installed by executing:
     ```
     py --version
     ```

   The command should display the installed Python version. If it does, Python has been successfully installed on your machine.

## About pip

pip is a package manager for Python and is included by default with the Python installer. It helps to install and uninstall Python packages (such as Django!). For the rest of the installation, we’ll use pip to install Python packages from the command line.

## Create a Folder called SE_FOUNDATIONS_PROJECT
```
mkdir SE_FOUNDATIONS_PROJECT
```
## Setting up a virtual environment

It is best practice to provide a dedicated environment for each Django project you create. There are many options to manage environments and packages within the Python ecosystem, some of which are recommended in the Python documentation. Python itself comes with venv for managing environments which we will use for this guide.

To create a virtual environment for your project, open a new command prompt, navigate to the folder where you want to create your project and then enter the following:

```
py -m venv django_apps
```
This will create a folder called ‘django_apps’ if it does not already exist and set up the virtual environment.
To activate the environment, run:
```
django_apps\Scripts\activate.bat
```
The virtual environment will be activated and you’ll see “(django_apps)” next to the command prompt to designate that.
Each time you start a new command prompt, you’ll need to activate the environment again.
using this
```
django_apps\Scripts\activate.bat
```

## Install Django

Django can be installed easily using pip within your virtual environment.

In the command prompt, ensure your virtual environment is active, and execute the following command:

```
py -m pip install Django
```
After the installation has completed, you can verify your Django installation by executing the following command in the command prompt:

```
django-admin --version
```
## change directory to SE_FOUNDATIONS_PROJECT
```
cd SE_FOUNDATIONS_PROJECT
```
## clone git hub repo
```
git clone https://github.com/eobolo/BSE-FOUNDATIONS-PROJECT-HEALTH-PASS.git
```
## change directory to cloned repo
```
cd BSE-FOUNDATIONS-PROJECT-HEALTH-PASS
```
## install the dependencies
```
pip install -r requirements.txt
```
## change directory to easy_healthcare
```
cd easy_healthcare
```
## check if errors are present in the app
```
python manage.py check
```
## run the django server
```
python manage.py runserver
```
## now copy this url to your browser
1. [Academic](http://127.0.0.1:8000/academic_feedback_sys/)
2. [admin](http://127.0.0.1:8000/admin/)
 
There you would see a page showing the path you could add
after the link these paths are the first argument of the
path function e.g dashboard/