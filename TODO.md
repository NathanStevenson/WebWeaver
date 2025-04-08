# To Do List

## Overall Project Set-Up
* The build structure is done that is good
* When building the stuff maybe have a settings/infrastructure config that can be used to set-up needed things for that project
* For now have the infrastructre config (initialize a VENV if python based; init a git repo; pip install all the reqs into the venv)
* Include generating the certificates for HTTPS inside this setup too if specified
* Later on we can have this also set up other shit like Docker, testing scripts, custom CI/CD pipelines etc

## Quart
* Get the ORM v No ORM code into the project with correct Jinja templates
* Incorporate Threadpool into the base quart set-up

## SvelteKit
* Get a nice set up of svelte kit 
* Nice Hello World template with the frameworks being used + photos for all the front end (API returns same in JSON)
* Have HTTP v HTTPS and Desktop v Mobile templates set-up
* Figure out the rendering types later on once the project is coming together

## Jinja HTML Templates
* Get a nice set-up of Jinja HTML templates within the /frontend folder which we can use if needing to render HTML/JS statically from the backend

## Plugins
* Start with a blog plugin for Quart (Svelte/Static HTML)
* Move onto a login (Google/Apple/Custom) with Quart (Svelte/Static HTML)

## Future
* Once everything above has been finished then replicate the Quart code above with a Rust/tokio webserver
* Once we have (Quart/Rust) (SvelteKit/HTML+JS+CSS) then add plugins for websockets; RBAC; Admin Dashboard; Payment; Emailing

* Add React functionality where we have SvelteKit + HTML/JS
* Long term plugins (sending sms - twilio/custom modem; messaging + VOIP site; multi factor auth)