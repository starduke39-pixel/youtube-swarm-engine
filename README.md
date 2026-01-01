🐝 YouTube Swarm Engine

A headless, serverless production studio for high-volume YouTube automation.

This repository contains the automation suite designed to bootstrap 5 niche YouTube channels to monetization (1,000 Subscribers / 4,000 Watch Hours) within 30 days. It runs entirely on GitHub Actions, removing the need for a local high-end PC.

🚀 Capabilities

The engine is split into 4 modular workers:

🧠 Script Generator: Connects to OpenRouter/OpenAI to generate viral scripts for 5 distinct niches (Trivia, History, Mystery, Luxury, Stoicism).

🎙️ Audio Factory: Batch processes text files into high-quality AI narration using the ElevenLabs API.

🎞️ Visual Asset Manager: Automatically scrapes and downloads HD stock footage from Pexels based on script keywords.

🎬 Trivia Render Bot: A moviepy engine that programmatically assembles fully edited Trivia Shorts with timers, sound effects, and text overlays.

🛠️ Tech Stack

Core: Python 3.9

Infrastructure: GitHub Actions (Ubuntu Runners)

AI Logic: OpenAI GPT-4 / Google Gemini Flash (via OpenRouter)

Audio: ElevenLabs API (Turbo v2 Model)

Video Processing: MoviePy + ImageMagick + FFmpeg

Assets: Pexels API

⚡ Quick Start

Fork this repo.

Add Secrets: Go to Settings > Secrets > Actions and add:

OPENROUTER_API_KEY

ELEVENLABS_API_KEY

PEXELS_API_KEY

Run: Go to the Actions tab, select Daily Content Factory, and click Run Workflow.

Download: Collect your daily content pack from the Artifacts section.

📂 Channel Architecture

Trivia Core: High-speed quiz automation.

Ancient Echoes: Sleep stories & mythology.

Abyss Archives: Unsolved mysteries & noir history.

Apex Lists: Luxury lifestyle & top 10s.

Mind Architect: Stoicism & psychology.
