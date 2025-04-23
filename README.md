# WebWeaver

This repo is currently under development with the end goal of being a code generation tool that will help with full stack development for the framework of your choice. Once the user fills out the form designed within our Tauri/Rust application they will then download the given files over the network, dynamically generate the source code they need given their overall config file, and have any of their specified set-up help run automatically.

## Overview

Look at backend_frameworks/quart/, code_builder.py, and *_config.json for a good idea of how the overall build process for WebWeaver is done. For now you must provide code_builder.py a path to the config file; eventually this config file will be generated for the user upon filling out our form through the Tauri application. The config file contains important information such as the resulting directory structure, information on how to build the files, and other necessary configurations such as the framework being used, whether or not to initialize a git repo, generate HTTPS keys, and the IP/port to host the webserver on by default.

Before developing familiarize yourself with Jinja (.j2) templates and their rendering process. Via the config file we are able to dynamically generate code at runtime so that the user only gets the exact source code that they requested and nothing more.

## Development

WebWeaver is beginning its development with Quart server statically rendering Jinja HTML + CSS templates to get the project started. Once this is finished, and before releasing 1.0 we will have support for Quart/Rust, Svelte/Jinja, PostgreSQL/MongoDB. If you would like to help with development please read the dev_manual and select a task from the TODO.md, or choose any of the not done tasks below which interest you.

## Plugins for each Framework
- [x] Initialize a Git Repo in the Directory Automatically
- [x] Generate PostgreSQL bash scripts such that the user can easily create/delete new DBs (these are auto connected to by Quart)
- [x] Generate HTTPS keys for self signed HTTPS sites
- [x] Hello World Example with Tabs / Sitemap Overview
- [x] Database hooked up with SQLAlchemy have working example of (add, get, edit, delete) with Base + User class (and API routes hooked up)
- [] Have a nav bar or side bar depending on web or mobile
- [] User Authentication + Profiles (login, logout, edit profile, edit password, sign up, forgot password, delete account, etc)
- [] Admin Dashboard + RBAC
- [] Websockets
- [] Payment + Subscription System
- [] Shopping Cart
- [] Email Notifications (notify, reset password, 2FA)
- [] File Uploading + Thumbail Generation
- [] Generate API Keys + Have API Throttling / Rate Limit
- [] Threadpools - for long running sync functions
- [] Scheduled Tasks with Cron Jobs
- [] Customized Logging
- [] Github Action; CI/CD pipeline auto generated
- [] Generate HTTPS keys given a website domain provided via LetsEncrypt

## Fullstack Website Templates (completely functional)
- [] Blogging
- [] Messaging + Video Chat + Voice Call
- [] End to End encryption with Web Crypto API + Indexed DB
- [] Shopping page with payment + cart
- [] Personal Resume Website
- [] Analytics Dashboard with Grafana
- [] Booking and Scheduling Events
- [] Social Media like with posts + comments