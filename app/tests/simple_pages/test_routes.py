### testing routes ###
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

### testing content ###
def test_index_content(client):
    # Returns index text
    response = client.get('/')
    assert b'The Address Changer' in response.data

def test_imprint_content(client):
    # Returns imprint text
    response = client.get('/imprint')
    assert b'Melvin Rinkleff' in response.data

def test_about_content(client):
    # Returns about text
    response = client.get('/about')
    assert b'About this Project' in response.data

def test_faq_content(client):
    # Returns faq text
    response = client.get('/faq')
    assert b'FAQs' in response.data

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


