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

When cloning this repo you will receive this `README.md` as well as `startup.py` file. You can run the startup file via `python startup.py --flag1 --flag2 --etc.` This list of flags currently supported is documented in this README.

When first running the startup script the only flag which will be required is `--add_backend` for now your options well be Quart / Rust. This will download the source code needed for that backend and create a very simple API which handles GET, POST, DELETE arguments as well as serving a simple `Hello World {backend_type}` webpage at `https:<ip>:<port>`.

The flag `--directory` to provide the script with a full path of the directory which you would like the incoming source code to be directed too.

While this is the only required flag you can also include flags such as `--add_database, --add_frontend, --add_plugin_x, etc.`. Each flag will download the templated source code specified and install any requirements. Each source code will come with comments to easily decipher what is going on and how the end user can expand on top of the functional template. Each argument will also update the provided config.py file with an accurate representation of a current web project given the directory it is located within. This will allow a unified list of all the WebWeaver products on your system, and it will also allow you to easily add or remove any new frameworks or plugins to a given directory and have them work as intended out of the box with no additional code required from your end.

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