project = 'TicketsCloud'
copyright = '2014-2016, TicketsCloud'
version = 'v1'
release = 'v1-beta'

extensions = [
    'sphinxcontrib.httpdomain',
    'cloud_sptheme',
    'cloud_sptheme.ext.index_styling',
]

source_suffix = '.rst'
source_encoding = 'utf8'
master_doc = 'index'
exclude_trees = ['_build']

pygments_style = 'sphinx'
html_theme = 'cloud'
# html_theme = 'ticketscloud'
# html_theme_options = {}
# html_theme_path = ['_templates']
html_static_path = ['_static']

primary_domain = 'http'
http_index_shortname = 'API Reference'
http_index_localname = 'TicketsCloud HTTP API'
http_index_grouping = False
