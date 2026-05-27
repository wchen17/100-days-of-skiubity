# Day 70: Git & Deployment

## Skills Today
- Git: branches, merging, .gitignore
- Deploying a Flask app to the cloud

## Deployment Options (2025/2026)
Heroku removed its free tier, so use one of these instead:

### Option 1: Render (recommended, free tier)
1. Push your Flask app to GitHub
2. Go to render.com → New → Web Service
3. Connect your GitHub repo
4. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Add environment variables in the Render dashboard

### Option 2: Railway.app (free trial credits)
1. Push to GitHub
2. railway.app → New Project → Deploy from GitHub repo
3. Set start command: `gunicorn app:app`

### Option 3: PythonAnywhere (free forever for Flask)
1. Sign up at pythonanywhere.com
2. Upload files or clone from GitHub
3. Set up a WSGI config file

## TODO: Deploy Your Day 67 or 69 Blog

### Pre-deployment checklist
- [ ] `requirements.txt` exists (`pip freeze > requirements.txt`)
- [ ] `Procfile` exists: `web: gunicorn app:app`
- [ ] Debug mode is OFF in production: `app.run(debug=False)`
- [ ] SECRET_KEY is an environment variable (not hardcoded)
- [ ] Database URI works in production (use PostgreSQL not SQLite for Render)
- [ ] `.gitignore` excludes `.env`, `*.db`, `__pycache__`

### Sample `.gitignore`
```
.env
*.db
__pycache__/
*.pyc
.DS_Store
token.txt
```

### Sample `requirements.txt` (Flask app)
```
flask
flask-sqlalchemy
flask-login
flask-wtf
gunicorn
psycopg2-binary
python-dotenv
```

## Stretch Goals
1. Set up a custom domain for your deployed app
2. Add HTTPS (Render handles this automatically)
3. Set up continuous deployment: push to GitHub → auto-deploys
