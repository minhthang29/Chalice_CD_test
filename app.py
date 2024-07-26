from chalice import Chalice

app = Chalice(app_name='hello')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/blogs')
def index():
    return {'My blog': 'This is Stephen blog!'}
