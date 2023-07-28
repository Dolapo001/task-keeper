# task-keeper
Task Keeper is a user-friendly to-do web app designed to help you manage your daily tasks and activities effectively. This app is built using Class-Based Views, making it easy to navigate and interact with your to-do list. With Task Keeper, you can stay organized, prioritize tasks, and achieve your goals efficiently.

## Technologies used

* Python
* Django (Class-Based Views)
* HTML
* JavaScript
* CSS
* SQlite3

## Users are able to:
1. Create an account or log in to Task Keeper to access your personalized to-do list.
2.  Easily add new tasks to your to-do list, providing a title, description, category and priority.
3.  You can modify task details or remove completed or unnecessary tasks.
4.  Organize your tasks into different categories for better management.
5. Mark tasks as high, medium, or low priority to focus on what matters most.
6. Move completed tasks to a separate section to maintain a clean and clutter-free task list.

## Installation
1. Clone the repository from GitHub:

`git clone https://github.com/https://github.com/LoneStarrD/task-keeper.git`

2. Navigate to the project directory:

`cd taskkeeper`

3. Create and Activate Virtual Environment:

`python -m venv env`

* On Windows, activate the virtual environment:

`env\Scripts\activate`

On macOS and Linux, activate the virtual environment:

`source env/bin/activate`

4. Install Dependencies:

`pip install -r requirements.txt`

5. Run Database Migrations:

`python manage.py migrate`

6. Create Superuser Account:

`python manage.py createsuperuser`

7. Start the Development Server:

`python manage.py runserver`

Use the superuser account credentials to log in to the admin interface at http://localhost:8000/admin/ and manage the platform content

## Preview

![](/task-keeper.png)

