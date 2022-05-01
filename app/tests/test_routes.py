# Test Login
def test_login_success(client):
    # Page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_login_redirects(client):
    response = client.get('/anmeldung')
    assert response.status_code == 302

def test_login_content(client):
    # Returns login text
    response = client.get('/login')
    assert b'You can log in to save and look up your accounts' in response.data

# Test Sign Up
def test_signup_success(client):
    # Page loads
    response = client.get('/signup')
    assert response.status_code == 200

def test_sign_up_redirects(client):
    response = client.get('/sign-up')
    assert response.status_code == 302

def test_signup_content(client):
    # Returns sign up text
    response = client.get('/signup')
    assert b'You can sign up to save and look up your accounts' in response.data

