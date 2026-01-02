import os

# --- API KEYS ---
# These pull directly from your GitHub Secrets
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")

# --- OPENROUTER SETTINGS ---
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# Free Model - robust for scripting
MODEL_NAME = "google/gemini-2.0-flash-exp:free"

# --- DIRECTORY SETUP ---
# In GitHub Actions, we write to the workspace
BASE_DIR = "Production_Factory"
ASSETS_DIR = "assets"

# --- VOICE MAPPING (ElevenLabs IDs) ---
VOICE_MAP = {
    "Trivia_Core": "nPczCjz8TkKk1be360ku",      # Suggestion: Fin (Hyper)
    "Ancient_Echoes": "CwhRBWXzGAHq8TQ4Fs17",   # Suggestion: Roger (Deep)
    "Abyss_Archives": "TxGEqnHWrfWFTfGW9XjX",   # Suggestion: Josh (Creepy)
    "Apex_Lists": "29vD33N1CtxCmqQRPOHJ",       # Suggestion: Callum (Pro)
    "Mind_Architect": "ODq5zmih8GrVes37Dizj"    # Suggestion: Patrick (Stoic)
}

# --- CHANNEL PROMPTS ---
CHANNEL_PROMPTS = {
    "Trivia_Core": "You are a fast-paced trivia host. Write a 60-second YouTube Short script with 3 questions (Easy, Medium, Impossible). Format: Question, Answer, Pause cues.",
    "Ancient_Echoes": "You are a soothing storyteller. Write a 60-second Sleep Story summary about a specific Myth or Historical event. Tone: Relaxing, dreamy.",
    "Abyss_Archives": "You are a mystery investigator. Write a 60-second script about a creepy unsolved mystery. Tone: Suspenseful, dark, noir.",
    "Apex_Lists": "You are a luxury lifestyle curator. Write a 60-second script ranking the top 3 most expensive items in a specific category. Tone: Hype, expensive.",
    "Mind_Architect": "You are a Stoic philosopher. Write a 60-second script giving advice based on Marcus Aurelius or Dark Psychology. Tone: Authoritative, deep."
}
