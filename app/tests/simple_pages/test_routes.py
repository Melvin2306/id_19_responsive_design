### testing routes successfull ###
def test_index_success(client):
    response = client.get('/')
    assert response.status_code == 200

def test_imprint_success(client):
    response = client.get('/imprint')
    assert response.status_code == 200

def test_about_success(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_faq_success(client):
    response = client.get('/faq')
    assert response.status_code == 200

def test_signup_success(client):
    response = client.get('/signup')
    assert response.status_code == 200

### testing redirects ###
def test_home_redirects(client):
    response = client.get('/home')
    assert response.status_code == 302

def test_legal_redirects(client):
    response = client.get('/legal')
    assert response.status_code == 302

def test_about_me_redirects(client):
    response = client.get('/about-me')
    assert response.status_code == 302

def test_frequentlyaskedquestions_redirects(client):
    response = client.get('/frequentlyaskedquestions')
    assert response.status_code == 302

def test_sign_up_redirects(client):
    response = client.get('/sign-up')
    assert response.status_code == 302

