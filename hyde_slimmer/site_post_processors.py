from __future__ import with_statement
import slimmer

class Compress(object):

    @staticmethod
    def process(folder, params):
        class Slimmer(object):
            def __init__(self, type):
                if type.lower() in ('css', 'html', 'xhtml'):
                    self.slimmer = getattr(slimmer, '%s_slimmer' % type.lower())
                else:
                    self.slimmer = None

            def visit_file(self, thefile):
                if self.slimmer:
                    file_content = thefile.read_all()
                    with open(thefile.path, 'w') as f:
                        f.write(self.slimmer(file_content))

        for key, value in params['slimmer'].iteritems():
            folder.walk(Slimmer(value), key)