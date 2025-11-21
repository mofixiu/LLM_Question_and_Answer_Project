LLM_QA_Project_EboMofiyinfoluwa_22CG031849

Simple Q&A system using an LLM API (Google Gemini by default - FREE!).


Files:

- `LLM_QA_CLI.py` : Python CLI to ask a question and get an answer.
- `app.py` : Flask web GUI.
- `requirements.txt` : Python dependencies.
- `templates/index.html` : Web GUI template.
- `static/style.css` : Optional styles.
- `vercel.json` : Vercel deployment configuration.
- `LLM_QA_hosted_webGUI_link.txt` : Contains name, matric number, live URL, GitHub repo link.

## Quick Start (Local)

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Get a free Google Gemini API key at [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

3. Set `GEMINI_API_KEY` environment variable:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

4. Run the CLI:

```bash
python LLM_QA_CLI.py
```

5. Run the web GUI (Flask):

```bash
python app.py
# open http://127.0.0.1:5000
```

## Deployment to Vercel

1. **Install Vercel CLI** (optional):

```bash
npm install -g vercel
```

2. **Push to GitHub**:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/LLM_QA_Project_EboMofiyinfoluwa_22CG031849.git
git push -u origin main
```

3. **Deploy via Vercel Dashboard**:

   - Go to [vercel.com](https://vercel.com)
   - Click "New Project" and import your GitHub repo
   - Vercel will detect `vercel.json` automatically
   - Add environment variable: `GEMINI_API_KEY` = your Gemini API key (in Settings → Environment Variables)
   - Deploy

4. **Or deploy via CLI**:

```bash
vercel
# Follow prompts to link project
# Add env var: vercel env add GEMINI_API_KEY
```

5. **Update `LLM_QA_hosted_webGUI_link.txt`** with your live Vercel URL and GitHub repo link.

## Alternative Deployment Options

- **Render.com**: Connect the GitHub repo, set env var `GEMINI_API_KEY` in settings.
- **PythonAnywhere**: Upload files or push via Git, configure Flask app, set env vars.
- **Streamlit Cloud**: Port `app.py` to Streamlit easily.

Notes:

- This project uses Google Gemini (free tier available); you may modify `call_gemini` to integrate a different LLM provider if desired.
- If `GEMINI_API_KEY` is not set, a simulated message will be returned.
- Get your free Gemini API key at: https://makersuite.google.com/app/apikey
