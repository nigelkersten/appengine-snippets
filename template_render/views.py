from boilerplate.lib.basehandler import BaseHandler


class Index(BaseHandler):
    def get(self):
        return self.render_template('template/index.html')
