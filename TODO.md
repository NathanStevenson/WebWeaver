# To Do List

## Overall Project Set-Up
* sudo apt install all the packages we need -- will need sudo permissions for apt installing hopefully reasonable
* Later on we can have this also set up other shit like Docker, testing scripts, custom CI/CD pipelines etc

## Quart
* Finish getting the DB working; right now we run the command then they install their database and then run with run_server.py. Ensure this works properly with curls to get, edit, delete, the users in the DB
* Restyle the home page (dark mode default; tabs array which differs based on plugins for nav bar; either top or side nav bar; webweaver image on left nav bar; tabs; (login / settings wheel / cart) right side)
* Once organized get the project dir structure a little cleaner so it is more scalable. Begin designing the tabs for the Hello World and the User Auth sites



* Google + Apple + Custom Auth (/login, logout, sign up, forgot password, User class with username/email/hashed password) in DB
* Admin Dashboard + RBAC
* Restyle so modern --> can find the overview in the settings/user profile dropdown. Click Overview to be taken to that page. Include in main README how to find sitemap quickly
* generating configs for specific website types (blogs, hello world, api, user auth, messaging, shopping, payments, websockets/streaming)"
* Incorporate Threadpool into the base quart set-up

## SvelteKit
* Get a nice set up of svelte kit 
* Nice Hello World template with the frameworks being used + photos for all the front end (API returns same in JSON)
* Have HTTP v HTTPS and Desktop v Mobile templates set-up
* Figure out the rendering types later on once the project is coming together

## Plugins
* Start with a blog plugin for Quart (Svelte/Static HTML)
* Move onto a login (Google/Apple/Custom) with Quart (Svelte/Static HTML)

## Future
* Once everything above has been finished then replicate the Quart code above with a Rust/tokio webserver
* Once we have (Quart/Rust) (SvelteKit/HTML+JS+CSS) then add plugins for websockets; RBAC; Admin Dashboard; Payment; Emailing

* Add React functionality where we have SvelteKit + HTML/JS
* Long term plugins (sending sms - twilio/custom modem; messaging + VOIP site; multi factor auth)