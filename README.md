# AI-Based LinkedIn Auto-Posting Tool

This repository contains a Python-based automation tool developed as part of my internship at **WinVinaya Foundation**, aimed at simplifying and automating the process of posting content to LinkedIn using the LinkedIn Developer API.

---

## 🔍 Project Description

The **LinkedIn Auto-Posting Tool** is designed to reduce manual effort and ensure timely social media engagement for organizations. The tool handles OAuth 2.0 authentication with LinkedIn and prepares the setup for posting content automatically to a user's LinkedIn feed.

Currently, the project successfully completes the LinkedIn authentication process and obtains the access token required for making authorized API requests.

---

## ✅ Features Completed

- LinkedIn Developer App registration and setup
- OAuth 2.0 flow with `http.server` to receive authorization code
- Secure token exchange for access token retrieval
- Ready for extension to automated post publishing

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `requests` (HTTP API calls)
  - `http.server` (local redirect handler)
  - `webbrowser` (open LinkedIn login page)
- **API Used:** LinkedIn REST API

---

## 🚀 How It Works

1. User runs the script.
2. Browser opens the LinkedIn login/authorization page.
3. After login, LinkedIn redirects to `http://localhost:8000` with an authorization code.
4. The script captures this code and exchanges it for an access token.

---

## 📌 Prerequisites

- A registered LinkedIn Developer App with permissions (`r_liteprofile`, `w_member_social`).
- Python 3.8+
- Internet connection

---

## 📝 Future Work

- Add functionality to generate and post messages using the LinkedIn `ugcPosts` endpoint.
- Extend to include other social platforms like Instagram and Twitter.
- Enable automatic content generation using OpenAI.
- Schedule recurring posts using `schedule` or cron jobs.

---

## 📂 Folder Structure (if applicable)
```bash
linkedin_auto_post/
├── linkedin_auth.py # Handles LinkedIn OAuth & token access
├── README.md # Project documentation

```
## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is for educational and internship use only.

---

## 🙋‍♂️ About Me
**A G Sriee Arvinth Raajhen**  
Intern at WinVinaya Foundation  
Passionate about using automation and AI for good.
