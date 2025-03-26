# Developer Manual 

This manual provides a general workflow for how to develop WebWeaver frameworks and plugins.

## Developing Frameworks

- Begin by placing your framework in the correct category; whether it is a backend framework, frontend framework, or a script which is used to initialize a database.
- Try to make the new framework as modular as possible. Split the code up into many smaller files that make logical sense. To get a good idea for this look at the initial Quart / Rust projects. These have been split up for API routes, API routes/sub-routes, routes which serve html, databasing logic, each model for ORMs has their own file, etc.
- In many cases it will be necessary to have some dynamic code generation (whether it is importing sub-files in the top level; or ORM v No-ORM databasing queries which is the only difference for that file). In these cases you can use our `code_builder.py` file and name your file: `<filename>.<ext>.j2`.
- You can then give `code_builder.generate_code(filepath, config)` at which point it will dynamically build your code and only include the needed parts so the end user only gets what they need.

## Developing Plugins
- Always looking for new creative plugins. When you develop a plugin make sure to update the documentation for the framework you develop it in.
- If possible it would be great if each plugin developed has at least one corresponding default front-end template that it goes with.
- When developing these plugins continue to make them as modular as possible
- Even if you are only familiar with the language you developed the plugin for, please update the other frameworks issues/documentation so we can support it across all WebWeaver supported frameworks.