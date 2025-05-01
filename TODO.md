# To Do List

## Overall Project Set-Up
* sudo apt install all the packages we need -- will need sudo permissions for apt installing hopefully reasonable
* Later on we can have this also set up Docker, testing scripts, custom CI/CD pipelines etc

## Quart
* Next Tasks: Add Login / Sign Up / Dark Mode buttons; Add Login / Sign Up / Unauthorized Pages (90 min)
* Make the header be an importable template to include it at the top of every other template (10 min) - base.html and then it has {% block content %} in it. The rest extend base.html and define block content
* Hook up the index HTML routes inside that folder properly and get the authentication_config.json to match accordingly (30 min)
* Test new Custom Login to make sure it works; add the bearer mode Quart Auth (120 min)
* Make the private page display personal information about the user (15 min)
* Implement Google OAuth, Apple OAuth, GitHub OAuth, (look into JWT token support - look into why JWT better than basic Quart Auth - seems like better for scale??) (120 min)
* Implement a few more useful routes: Forgot password, Change Password, Profile Routes, Editing Profile, Emailing user with 2FA code to verify account before adding users (120 min)


* Admin Dashboard + RBAC
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