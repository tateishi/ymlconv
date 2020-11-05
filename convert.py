import yaml
from jinja2 import Template, Environment, FileSystemLoader

def main(infile, outfile, tempfile='vcard.tmpl'):
    with open(infile) as file:
        yml = yaml.safe_load(file) 
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(tempfile)
    result = template.render(yml)
    with open(outfile, 'w') as out:
        print(result, file=out)

if __name__ == '__main__':
    main('family.yml', 'result.vcf')