from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():

    rv = web.get('/test', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Central Corridor", rv.data)
