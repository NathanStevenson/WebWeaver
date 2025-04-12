from jinja2 import Template
import json
import os
import subprocess
import time

# function takes a Dict config (loaded from JSON) and builds a directory
# if the dict contains another dict then it is a folder; if it contains a list then it needs to generate a file
# first arg in the list is the file path it needs to copy/build. 2nd arg is if the file is a Jinja template; if so will need to build with generate_code fn
# builds the project structure located with its base starting at project directory
def build_directory(project_directory, project_structure, jinja_config):
    for name, data in project_structure.items():
        path = os.path.join(project_directory, name)
        # if dict then make dir; recursively build next directory 
        if isinstance(data, dict):
            os.makedirs(path, exist_ok=True)
            build_directory(path, data, jinja_config)
        # if not a dir; then see whether we just need to make the file with pure copy or build with gen_code()
        else:
            # Jinja template generate with generate_code()
            if (data[1] == True):
                path = os.path.dirname(path)
                generate_code(path, data[0], jinja_config)

            # if the code being copied is binary (images, etc)
            elif (data[1] == "binary"):
                with open(data[0], "rb") as template_file:
                    code = template_file.read()
                with open(path, "wb") as source_file:
                    source_file.write(code)
            
            # Normal code read from template source code into the new file 
            else:
                with open(data[0], "r") as template_file:
                    code = template_file.read()
                with open(path, "w") as source_file:
                    source_file.write(code)

# function takes a file path + config and renders a Jinja template
def generate_code(source_file_path, template_file_path, config):
    with open(template_file_path) as template_file:
        template = Template(template_file.read())
    
    # render the source code after passing in the needed config to build the code correctly
    rendered_code = template.render(config=config)

    # write the generated file to the correct file in the correct final directory
    file_name = template_file_path.split('/')[-1][:-3]
    file_path = os.path.join(source_file_path, file_name)
    with open(file_path, "w") as f:
        f.write(rendered_code)


if __name__ == "__main__":
    # read the config from the file and load it in as json
    with open("config.json", 'r') as config_file:
        config = json.load(config_file)

    # build the proper final directory by using pieces of the extracted config above
    build_directory(config['set_up']['project_directory'], config['dir_structure'], config)

    # if user wants automated setup for their system run the bash command from the dir (safest using subpr since user inputting dir name ensure used as dir)
    subprocess.run(["bash", "project_setup_help.sh"], cwd=config['set_up']["project_directory"] + "/" + config['set_up']["project_name"])