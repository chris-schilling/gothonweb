from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():

    rv = web.get('/test', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

def test_game():
    #check that we get a 200 on /game
    rv = web.get('/game', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    #check that we have response data on a form sumbit
    rv = web.post("/game", follow_redirects=True)
    assert_in(b"Central Corridor", rv.data)
