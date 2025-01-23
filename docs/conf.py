# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- General ABlog Options ----------------------------------------------------

# A path relative to the configuration directory for blog archive pages.
# blog_path = "blog"

# The "title" for the blog, used in active pages.  Default is ``"Blog"``.
blog_title = "misgnros.github.io"

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
# blog_baseurl = ""

# Choose to archive only post titles. Archiving only titles can speed
# up project building.
# blog_archive_titles = False

# -- Blog Authors, Languages, and Locations -----------------------------------

# A dictionary of author names mapping to author full display names and
# links. Dictionary keys are what should be used in ``post`` directive
# to refer to the author.  Default is ``{}``.
# blog_authors = {}


# A dictionary of language code names mapping to full display names and
# links of these languages. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
# blog_languages = {
#    "en": ("English", None),
# }


# A dictionary of location names mapping to full display names and
# links of these locations. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
# blog_locations = {
#    "Earth": ("The Blue Planet", 'https://en.wikipedia.org/wiki/Earth),
# }

# This will prevent ablog from injecting its own templates into the Sphinx
# build. This is only useful when you have a custom template bridge (rare).
# See https://github.com/sunpy/ablog/pull/144 for the full context.
# skip_injecting_base_ablog_templates = False

# -- Blog Post Related --------------------------------------------------------

# Format date for a post.
# post_date_format = "%%b %%d, %%Y"

# Number of paragraphs (default is ``1``) that will be displayed as an excerpt
# from the post. Setting thisi ``0`` will result in displaying no post excerpt
# in archive pages.  This option can be set on a per post basis using
# post_auto_excerpt = 1

# Index of the image that will be displayed in the excerpt of the post.
# Default is ``0``, meaning no image.  Setting this to ``1`` will include
# the first image, when available, to the excerpt.  This option can be set
# on a per post basis using :rst:dir:`post` directive option ``image``.
# post_auto_image = 0

# Number of seconds (default is ``5``) that a redirect page waits before
# refreshing the page to redirect to the post.
# post_redirect_refresh = 5

# When ``True``, post title and excerpt is always taken from the section that
# contains the :rst:dir:`post` directive, instead of the document. This is the
# behavior when :rst:dir:`post` is used multiple times in a document. Default
# is ``False``.
# post_always_section = False

# When ``True``, links to the previous and next posts will be rendered at the
# bottom of the page.
# Default is ``True``
# post_show_prev_next = True

# When ``False``, the :rst:dir:`orphan` directive is not automatically set
# for each post. Without this directive, Sphinx will warn about posts that
# are not explicitly referenced via another document. :rst:dir:`orphan` can
# be set on a per-post basis as well if this is false. Default is ``True``.
# post_auto_orphan = True

# -- ABlog Sidebars -------------------------------------------------------

# There are seven sidebars you can include in your HTML output.
# postcard.html provides information regarding the current post.
# recentposts.html lists most recent five posts. Others provide
# a link to a archive pages generated for each tag, category, and year.
# In addition, there are authors.html, languages.html, and locations.html
# sidebars that link to author and location archive pages.

# -- Blog Feed Options --------------------------------------------------------

# Turn feeds by setting :confval:`blog_baseurl` configuration variable.
# Choose to create feeds per author, location, tag, category, and year,
# default is ``False``.
# blog_feed_archives = False

# Choose to display full text in blog feeds, default is ``False``.
# blog_feed_fulltext = False

# Blog feed subtitle, default is ``None``.
# blog_feed_subtitle = None

# Choose to feed only post titles, default is ``False``.
# blog_feed_titles = False

# Specify custom Jinja2 templates for feed entry elements:
#     `title`, `summary`, or `content`
# For example, to add an additional feed for posting to social media:
# blog_feed_templates = {
#     # Use defaults, no templates
#     "atom": {},
#     # Create content text suitable posting to social media
#     "social": {
#         # Format tags as hashtags and append to the content
#         "content": "{ title }{% for tag in post.tags %}"
#         " #{ tag.name|trim()|replace(" ", "") }"
#         "{% endfor %}",
#     },
# }
# Default: Create one `atom.xml` feed without any templates
# blog_feed_templates = {"atom": {} }

# Specify number of recent posts to include in feeds, default is ``None``
# for all posts.
# blog_feed_length = None

# -- Font-Awesome Options -----------------------------------------------------

# ABlog templates will use of Font Awesome icons if one of the following
# is ``True``

# Link to `Font Awesome`_ at `Bootstrap CDN`_ and use icons in sidebars
# and post footers.  Default: ``None``
# fontawesome_link_cdn = None

# Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``
# fontawesome_included = False

# Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
# with the configuration option: fontawesome_css_file
# Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
# be linked to in HTML output by ABlog.
# fontawesome_css_file = None

# -- Disqus Integration -------------------------------------------------------

# You can enable Disqus_ by setting ``disqus_shortname`` variable.
# Disqus_ short name for the blog.
# disqus_shortname = None

# Choose to disqus pages that are not posts, default is ``False``.
# disqus_pages = False

# Choose to disqus posts that are drafts (without a published date),
# default is ``False``.
# disqus_drafts = False


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "misgnros.github.io"
copyright = "2025, misgnros"
author = "misgnros"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	"sphinx.ext.githubpages",
	"sphinx.ext.extlinks",
	"sphinx.ext.todo",
	"myst_parser",
	"ablog",
	"sphinx.ext.intersphinx",
	"sphinx_design",
	"sphinxcontrib.mermaid",
	"sphinx_copybutton",
	# "sphinxcontrib.googleanalytics",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

source_suffix = {
	".rst": "restructuredtext",
	".md": "markdown",
}

myst_enable_extensions = [
	"amsmath",
	"attrs_inline",
	"colon_fence",
	"deflist",
	"dollarmath",
	"fieldlist",
	"html_admonition",
	"html_image",
	"linkify",
	"replacements",
	"smartquotes",
	"strikethrough",
	"substitution",
	"tasklist",
]

myst_linkify_fuzzy_links=False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_sidebars = {"**": []}

html_theme_options = {
	"external_links": [
		{
			"url": "https://misgnros.github.io/blog/index.html",
			"name": "Posts",
		},
		{
			"url": "https://github.com/misgnros/misgnros.github.io/releases",
			"name": "Changelog",
		},
	],
	"icon_links": [
		{
			"name": "GitHub",
			"url": "https://github.com/misgnros/misgnros.github.io",
			"icon": "fa-brands fa-github",
			"type": "fontawesome",
		},
	],
	"secondary_sidebar_items": {
		"**": ["page-toc","ablog/tagcloud.html","ablog/categories.html","ablog/archives.html","sourcelink"],
		"index": ["page-toc","sourcelink"],
	},
	"show_prev_next": False,
	"logo": {
		"text": "misgnros.github.io",
	},
	"analytics": {"google_analytics_id": "G-06Z6FZYZYE"},
}

# Google analytics setting for all themes with sphinxcontrib-googleanalytics is loaded
# googleanalytics_enabled = True
# googleanalytics_id = "G-xxxxxxxx"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not "", a "Last updated on:" timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%%b %%d, %%Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ""

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   "da", "de", "en", "es", "fi", "fr", "hu", "it", "ja"
#   "nl", "no", "pt", "ro", "ru", "sv", "tr"
# html_search_language = "en"

# A dictionary with options for the search language support, empty by default.
# Now only "ja" uses this config value
# html_search_options = {"type": "default"}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = "scorer.js"

# Output file base name for HTML help builder.
# htmlhelp_basename = "doc"
