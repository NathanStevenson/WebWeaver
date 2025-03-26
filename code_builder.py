from jinja2 import Environment, FileSystemLoader

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

    print(f"Code generated successfully for {file_name}!")