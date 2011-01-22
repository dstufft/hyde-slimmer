Hyde Slimmer
------------

This module is a wrapper around Peter Bengtsson's slimmer. It can be used to
compress HTML, XHTML or CSS. It depends on the slimmer module from pypi.

Installation ::

    pip install hyde-slimmer

Install Post Processor::

    SITE_POST_PROCESSORS = {
        '/': {
            'hyde_slimmer.site_post_processors.Compress' : {
                'slimmer': {
                    '*.html': 'html',
                    #'*.html': 'xhtml',
                    #'*.css': 'css',
                }
            },
        }
    }