# WebWeaver 1.0

With all the different backend/frontend frameworks and databasing surrounding web development choosing the proper set-up can be overwhelming. WebWeaver assists developers by providing templates that work out of the box for numerous different languages to allow devlopers to get a jumpstart on coding any of their websites. 

Backend Frameworks supported
- Quart / Flask
- Rust
- NodeJS/ExpressJS (future)
- Django (future)
- FastAPI (future)

Frontend Frameworks supported
- Svelte/SvelteKit
- React
- Angular (future)

Databases Supported + Language Based ORMs
- PostgreSQL
- MongoDB
- MySQL(future)

- Python - SQLAlchemy
- Rust - SeaORM

## Workflow

When cloning this repo you will receive `README.md, startup.py, and config.json`. The README contains instructions on how to use WebWeaver as well as upcoming features. `startup.py` is the python script which is used to install all frameworks, databases, plugins, and performing any other templating logic. `config.json` will store global configs based on directory for frameworks and database port/name for databases. This will track all things downloaded from WebWeaver.

Important startup.py flags:

`--add_backend`: this will prompt the user what framework they would like to use, what IP/port they would like to host it on, name of systemd service, and what directory they would like this web app to be downloaded to. This will then download the backend source code to that directory, update the config.json file, install all dependencies, and create/start a systemd service, all while logging what is happening in the terminal.

`--attach_backend_to_db`: this will prompt the user for the directory of the backend, the specific database (name/port) that they would like to connect to each other. This will then download the needed source code to the backend directory, install all dependencies, and update config.json file of the backend to show there is a database attached to it so that the create_app() function knows and can update its logic.

`--add_database`: this will prompt the user what type of database they want (async/not), database username/password/db_name. This will then install the database on their system and update the config.json file to show there is a new database on the system.

`--add_frontend`: this will prompt the user for the directory to install the front end, the directory (if any) of the backend they would like to link it too. They will also be prompted for what framework they would like to use, ip/port to host frontend on, and systemd service name. This will then download the frontend source code to the specified directory, update the config.json to show there is a frontend and potentially update it to show a linked frontend and backend. It will then install all the dependencies and log everything it is doing in the terminal.

`--add_plugin`: this will prompt the user what directory the backend is located which they would like to add the plugin too. It will also prompt the user for what type of plugin they would like to add. (auth/payment/messaging/logs/etc.) It will then download the needed source code, install all dependencies, and update the config.json file of the backend to show there is a new plugin attached to that backend so the create_app() function knows what to do.

## Plugins
- Databases with optional GUI interfaces
- Custom Login, Google/Apple Login
- Built in payment options (Venmo, Apple Pay, PayPal, General Credit Card)
- SMS Messaging / Emailing (Twilio API / GMAIL) - include link to my blog talking about setting up custom hardware to send/receive SMS messages
- Detailed Access Logs / Backend logic logs
- Backend Hosted Static files or separate backend / frontend applications
- Dynamic Hosting options + flags (IP/port/number of workers/hot reload/etc.)

## Future

As of a 1.0 release we support the frameworks listed above. Please feel free to fork the repo and submit a PR for any other plugin features you would like to see in WebWeaver as well as if you would like to create your own complete template for a language we do not yet support.