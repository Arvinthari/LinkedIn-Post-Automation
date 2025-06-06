import requests

# Replace with your details
access_token = "AQWWpL7vXM814SFNVMePf8lh7dfGO6re4WU-aq04LqfnZu-YHlZJWWYEhxLyxZMyDbvzMIkt_hqNQFtYe12TtWKwbASkOQ2GLm22xiS4WpDEjsAb7hDRBrCDR7KZgJdqMaI3Hzyc8P-E1EJ3wCFXBWeb6Hcp_uSZHXKfWx6NTjpkYLyCKJuCCIurV6V9WQILZK6ZyigIj6ZOh6uaAVGkFMduVAWEfVpXuMlX8G_EyTBC-8IKS-jj3BQUckSBRyJFOj8gyhqdt1Kd5NuyFhUPsWyc3bQD-9yfMB4x83EQDIgERxBx819psysIo6nUKEExPeB9nbi_XyIiXbnxNf_xOQnS1UIGlg"
headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
print(response.json())
