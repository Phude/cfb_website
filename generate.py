import os
import shutil
import jinja2

template_path = 'templates'
output_path = 'docs/'
static_path = 'static/'

def render(filename, context):
	return jinja2.Environment(
		loader=jinja2.FileSystemLoader(template_path)
	).get_template(filename).render(context)

context = {
	'test': 't'
}

if os.path.exists(output_path):
	shutil.rmtree(output_path)

shutil.copytree(static_path, output_path)

render('about.html', context)

for entry in os.scandir(template_path):
	with open(output_path + entry.name, 'w+') as f:
		if entry.name.endswith('.html'):
			f.write(render(entry.name, context))