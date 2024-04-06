## Install Python

Django is a Python web framework, thus requiring Python to be installed on your machine. At the time of writing, Python 3.12 is the latest version.

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
py -m venv healthpass
```
This will create a folder called ‘healthpass’ if it does not already exist and set up the virtual environment.
To activate the environment, run:
```
healthpass\Scripts\activate.bat
```
The virtual environment will be activated and you’ll see “(healthpass)” next to the command prompt to designate that.
Each time you start a new command prompt, you’ll need to activate the environment again.
using this
```
healthpass\Scripts\activate.bat
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
1. [healthpass](http://127.0.0.1:8000/healthpass/)
2. [accounts](http://127.0.0.1:8000/accounts/)
3. [admin](http://127.0.0.1:8000/admin/)
 
There you would see a page showing the path you could add
after the link these paths are the first argument of the
path function e.g user_signup

## Open vscode
1. click on new terminal
2. you would see the powershell terminal by default
3. then click on a '+' icon with down arrow
4. then click on command prompt to create a new terminal with
5. now you have powershell terminal and then command prompt terminal
6. use powershell to do linux commands and vscode
7. then use command prompt to do python manage.py check and python manage.py server

Abiodun put images for this step please

For healtpass/ application
all paths with this <type:parameter> can not be accessed directly from
the web browser but the html files beside it are connected to them
check the files and just style them here it this path
```
cd SE_FOUNDATIONS_PROJECT\BSE-FOUNDATIONS-PROJECT-HEALTH-PASS\easy_healthcare\healthpass\templates\healthpass
```

1. user_signup - django_user.html
2. user_home - user_home.html
3. custom_signup - custom_user.html
4. custom_login - custom_login.html
5. custom_home - custom_home.html
6. custom_logout - no html
7. custom_ban - custom_ban.html
8. custom_password_reset - custom_password_reset_form.html 
9. custom_password_reset_done - custom_password_reset_done.html 
10. custom_reset/<str:uidb64>/<str:token> - custom_reset_confirm_form.html
11. custom_reset_done - custom_reset_done.html
12. custom_password_reset_warning - custom_password_reset_warning.html
13. blood_work_create - bloodwork_form.html
14. blood_work_read - bloodwork_list.html
15. blood_work_read_update - bloodwork_updatelist.html
16. blood_work_update/<int:pk> - bloodwork_form.html
17. blood_work_read_delete - bloodwork_deletelist.html
18. blood_work_delete/<int:pk> - bloodwork_confirm_delete.html
19. general_info_create - generalinfo_form.html
20. general_info_read - generalinfo_list.html
21. general_info_read_update - generalinfo_updatelist.html
22. general_info_update/<int:pk> - generalinfo_form.html
23. general_info_read_delete - generalinfo_deletelist.html
24. general_info_delete/<int:pk> - generalinfo_confirm_delete.html
25. urinalysis_create - urinalysis_form.html
26. urinalysis_read - urinalysis_list.html
27. urinalysis_read_update - urinalysis_updatelist.html
28. urinalysis_update/<int:pk> - urinalysis_form.html
29. urinalysis_read_delete - urinalysis_deletelist.html
30. urinalysis_delete/<int:pk> - urinalysis_confirm_delete.html
31. custom_blood_work_read - custom_bloodwork_list.html
32. custom_general_info_read - custom_generalinfo_list.html 
33. custom_urinalysis_read - custom_urinalysis_list.html

For accounts/ application
all paths with this <type:parameter> can not be accessed directly from
the web browser but the html files beside it are connected to them
check the files and just style them
this is the path:
```
cd SE_FOUNDATIONS_PROJECT\BSE-FOUNDATIONS-PROJECT-HEALTH-PASS\easy_healthcare\healthpass\templates\registration
```
1. login - login.html
2. logout - no html
3. password_reset - password_reset_form.html
4. password_reset/done - password_reset_done.html
5. reset/<str:uidb64>/<str:token> - password_reset_confirm.html
6. reset/done - password_reset_complete.html

# Working with the html file, css file and js file
navigate to this directory
```
cd SE_FOUNDATIONS_PROJECT\BSE-FOUNDATIONS-PROJECT-HEALTH-PASS\easy_healthcare\healthpass
```
list directories and you would see files and folders
```
ls
```
then would see static folder, then change directory to it
```
cd static
```
then inside of static list directories
```
ls
```
then you would see styles, scripts, and images folder
put css file in styles folder
```
cd styles
```
put javascript files in scripts folder
```
cd scripts
```
put images files in images folder
```
cd images
```
then move to the folder of the html files you are working on
```
cd SE_FOUNDATIONS_PROJECT\BSE-FOUNDATIONS-PROJECT-HEALTH-PASS\easy_healthcare\healthpass\templates\healthpass
```
or
```
cd SE_FOUNDATIONS_PROJECT\BSE-FOUNDATIONS-PROJECT-HEALTH-PASS\easy_healthcare\healthpass\templates\registration
```
In your file put this in the head tag of your html as the first thing before title, meta tags
```
{% load static %}
```
before calling the style sheet in the link tag, the js in the script tag, and images in the image tag
```
<link rel="stylesheet" href="{% static './styles/yourcssscript.css' %}">
```
```
<script src="{% static './scripts/yourjsscript.js' %}"></script>
```
```
<img src="{% static './images/yourimagefile.[jpeg,jpg,png]' %}">
```
**then go back to this on cmd not powershell, use cmd on vscode to be running this commands below**
```
cd SE_FOUNDATIONS_PROJECT\BSE-FOUNDATIONS-PROJECT-HEALTH-PASS\easy_healthcare
```
the run this commands
```
python manage.py check
```
```
python manage.py runserver
```
then go back to the top of the readme to see what i said you should do after running this commands
**Use vscode powershell to actually edit the scripts i.e css, js, and html**
