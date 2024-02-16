# bryn-mawr-eats

Thinking of things to cook is hard. Writing grocery lists is boring.

This is a simple Django/Nuxt app to handle both of those problems. It is meant to be run locally and has zero aspirations.

Front-end: http://localhost:3000/
Back-end: http://localhost:8000/admin/

![Homepage](documentation_images/bryn_mawr.png?raw=true)

## Spin-up instructions

### Build
Make sure Docker Desktop is running on your system.

Navigate to the project directory and run `docker-compose build`.

After the build is complete, run `docker-compose up`.

### Setup Django

Once the project is running, open up an interactive terminal in the `web` container.

Run migrations:

`python manage.py migrate`

![Run migrations](documentation_images/migrate.png?raw=true)

Create a superuser for Django using the `createsuperuser` prompt:

`python manage.py createsuperuser`

![Create superuser](documentation_images/createsuperuser.png?raw=true)

Login to the Django admin: `http://localhost:8000/admin/`

![Django admin](documentation_images/login.png?raw=true)

### Manage recipes

You can manage recipes in the Django admin. Once you add them, they will be visible on the front-end.

Ingredients can be added on the front-end or back-end.

![Recipes admin](documentation_images/recipes_admin.png?raw=true)

### It should just work 🪄
