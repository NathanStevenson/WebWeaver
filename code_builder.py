from jinja2 import Environment, FileSystemLoader
import json
import os

# dictionary of list of files for each framework which need to be generated via Jinja templates
templated_files = {
        "quart": ["app.py.pj2", "secrets.py.j2"],
        "rust": []
}

def generate_code(file_path, config):
    # load the templated Jinja source file
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(file_path)
    
    # render the source code after passing in the needed config to build the code correctly
    rendered_code = template.render(config=config)

    # write the generated file to the correct file
    file_name = file_path.split('/')[-1][:-3]
    with open(f"{file_name}", "w") as f:
        f.write(rendered_code)


if __name__ == "__main__":
    # read the config from the file and load it in as json
    with open("config.json", 'r') as config_file:
        config = json.load(config_file)

    # setup the overall project directory based on the config file
    if config['overview']['project_name']:
        os.makedirs(config['overview']['project_name'], exist_ok=True)
        # set up the database sub-directory within the project
        if config['overview']['database']:
            os.makedirs(f"{config['overview']['project_name']}/{config['overview']['database']}", exist_ok=True)
        
        # set up the backend sub-directory within the project
        if config['overview']['backend']:
            os.makedirs(f"{config['overview']['project_name']}/{config['overview']['backend']}", exist_ok=True)
        
        # set up the frontend sub-directory within the project
        if config['overview']['frontend']:
            os.makedirs(f"{config['overview']['project_name']}/{config['overview']['frontend']}", exist_ok=True)
