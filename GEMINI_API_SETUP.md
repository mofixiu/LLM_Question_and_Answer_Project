# How to Get Your FREE Google Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
   (or https://aistudio.google.com/app/apikey)

2. Sign in with your Google account

3. Click "Create API Key"

4. Copy the key (starts with "AIza...")

5. Set it as an environment variable:

   ```bash
   export GEMINI_API_KEY="AIza..."
   ```

6. For Vercel deployment:
   - Go to your project Settings → Environment Variables
   - Add: GEMINI_API_KEY = your-key-here

