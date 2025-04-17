# To Do List

## Overall Project Set-Up
* sudo apt install all the packages we need -- will need sudo permissions for apt installing hopefully reasonable
* Later on we can have this also set up other shit like Docker, testing scripts, custom CI/CD pipelines etc

## Quart
* SQLAlchemy for both ORM and no ORM. Use Session for ORM features and use connection.execute("raw SQL") for no ORM features
* Continue adding the User feature and some other ORM info; continue mix of ChatGPT and sql alchemy docs reading to learn more about how it works
* Restyle the home page (dark mode default; tabs array which differs based on plugins for nav bar; either top or side nav bar; webweaver image on left nav bar; tabs; (login / settings wheel / cart) right side)



* Google + Apple + Custom Auth (/login, logout, sign up, forgot password, User class with username/email/hashed password) in DB
* Admin Dashboard + RBAC
* Move the hello_world page to a /overview and link it to the home page of everything. For a simple hello_world site that will be the default home page so it is fine
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