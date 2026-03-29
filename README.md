# MintMind - AI Money Mentor 🚀

A fully functional, production-ready backend and frontend web application built during a hackathon to provide AI-powered financial advisory for Indian retail investors.

## ⚙️ Tech Stack

- **Backend:** FastAPI, Python 3.9+
- **Database:** MongoDB (using Motor async driver)
- **Auth:** JWT and `passlib` (bcrypt hashing)
- **AI Integration:** Anthropic API (Claude 3 Haiku)
- **Frontend:** HTML, CSS, Vanilla JS

## 📁 Project Structure

```text
├── main.py                  # FastAPI Application Entry
├── requirements.txt         # Dependencies
├── .env                     # Environment variables configuration
├── models/
│   ├── user.py              # Pydantic schemas for User Auth
│   └── report.py            # Pydantic schemas for AI Reports
├── auth/
│   └── jwt_handler.py       # JWT encoding/decoding, Auth dependencies
├── services/
│   └── db.py                # MongoDB async motor client setup
├── routes/
│   ├── auth.py              # Signup, Login, Me endpoints
│   ├── dashboard.py         # Fetch user dashboard reports
│   ├── wizard.py            # Tax Wizard PDF analysis via Anthropic
│   └── mfxray.py            # MF X-Ray CSV/PDF analysis via Anthropic
└── static/
    ├── index.html           # Marketing page with auth modal
    └── dashboard.html       # Protected dashboard to run reports
```

## 🚀 Running Locally

1. **Install Dependencies:**
   Ensure you have Python 3.8+ installed. Set up your virtual environment and install the requirements:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

2. **Setup MongoDB:**
   You must have MongoDB running locally at `mongodb://localhost:27017` or provide a cloud URI. Ensure your `.env` is updated:
   ```env
   MONGO_URI=mongodb://localhost:27017
   JWT_SECRET=your_super_secret_jwt_key
   ANTHROPIC_API_KEY=your_anthropic_api_key  # Optional: Will fallback to mock responses if blank
   ```

3. **Start the FastAPI Server:**
   ```bash
   uvicorn main:app --reload
   ```
   Or simply run the main script:
   ```bash
   python main.py
   ```

4. **Access the App:**
   - App URL: `http://localhost:8000`
   - API Docs: `http://localhost:8000/docs`

## ☁️ Deployment Instructions (Render / Railway / Heroku)

1. Provision a free MongoDB cluster on **MongoDB Atlas** and get the Connection string.
2. In your deployment dashboard (e.g., Render), create a new Web Service pointing to this GitHub Repo.
3. Add the Environment Variables: `MONGO_URI`, `JWT_SECRET`, and `ANTHROPIC_API_KEY`.
4. Set the Start Command to:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```


