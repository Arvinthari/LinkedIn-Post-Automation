# linkedin_auto_post.py
import requests
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Replace these with your LinkedIn app credentials
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:8000'
PERSON_URN = 'urn:li:person:YOUR_PERSON_URN'
POST_TEXT = "Hello from WinVinaya Foundation! This is an automated LinkedIn post using Python."

# Start local server to catch the authorization code
class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        auth_code = params.get('code', [None])[0]

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if auth_code:
            response_html = f"<h1>Authorization successful!</h1><p>Code: {auth_code}</p><p>Check your terminal.</p>"
            print("Authorization Code:", auth_code)
        else:
            response_html = "<h1>Authorization failed or cancelled.</h1>"

        self.wfile.write(response_html.encode('utf-8'))

def get_authorization_code():
    scope = 'w_member_social'
    auth_url = (
        f'https://www.linkedin.com/oauth/v2/authorization?response_type=code'
        f'&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={scope}'
    )
    print("Opening browser for LinkedIn login...")
    webbrowser.open(auth_url)

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, OAuthHandler)
    print("Server running at http://localhost:8000 to receive the auth code...")
    httpd.handle_request()

def get_access_token(auth_code):
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    response = requests.post(token_url, data=data)
    return response.json().get('access_token')

def post_to_linkedin(access_token):
    url = 'https://api.linkedin.com/v2/ugcPosts'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    post_data = {
        "author": PERSON_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": POST_TEXT
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, json=post_data)
    if response.status_code == 201:
        print("✅ Post successfully published on LinkedIn!")
    else:
        print("❌ Failed to post:", response.text)

if __name__ == "__main__":
    get_authorization_code()
    auth_code = input("Paste the authorization code here: ").strip()
    token = get_access_token(auth_code)
    print("Access Token:", token)
    post_to_linkedin(token)
