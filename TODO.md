# To Do List

## Overall Project Set-Up
* sudo apt install all the packages we need -- will need sudo permissions for apt installing hopefully reasonable
* Later on we can have this also set up Docker, testing scripts, custom CI/CD pipelines etc

## Quart
* Next Tasks: Add Login / Sign Up / Unauthorized Pages / Private page display username/email; change tabs href to be lower case (90 min)
* Test new Custom Login to make sure it works; add the bearer mode Quart Auth (120 min)
* Update the README.md - new info link this file for more work to do + new ideas
* Implement Google OAuth, Apple OAuth, GitHub OAuth, (look into JWT token support - look into why JWT better than basic Quart Auth - seems like better for scale??) (120 min)
* Implement a few more useful routes: Forgot password, Change Password, Profile Routes, Editing Profile, Emailing user with 2FA code to verify account before adding users (120 min)

* Payment and cart
* Admin Dashboard + RBAC
* Websockets
* Emailing - include email verification before adding user to DB
* Incorporate Threadpool into the base quart set-up
* Posts with comments, likes, etc
* Personal Information Form

## Plugins with Fullstack web templates
* Have the templates be 'bundles' of plugins:
* blogging: posting, user login, dark mode
* message server: emailing, login, websockets
* shopping site: lists of items, admin dashboard, personal info form, payment and cart
* etc
* Users can then get individual plugins or they can bundle their plugins with a full blown working site out of the box which they can customize 


* generating configs for specific website types (blogs, hello world, api, user auth, messaging, shopping, payments, websockets/streaming)"

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