import yaml
from jinja2 import Template, Environment, FileSystemLoader

def main(infile, outfile, tempfile='vcard.tmpl'):
    with open(infile, encoding='utf-8') as file:
        yml = yaml.safe_load(file) 
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(tempfile)
    result = template.render(yml)
    with open(outfile, 'w', encoding='utf-8') as out:
        print(result, file=out)

if __name__ == '__main__':
    import sys

    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile, outfile)
