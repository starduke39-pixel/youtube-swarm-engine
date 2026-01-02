import os
from moviepy.editor import *
import config

# --- CONFIGURATION ---
W, H = 1080, 1920
OUTPUT_DIR = os.path.join(config.BASE_DIR, "Rendered_Videos")

# In a live version, you would parse the script files from Step 1.
# For Phase 1 reliability, we use this structure for the demo render.
QUESTIONS = [
    {"q": "What is the capital of France?", "a": "Paris", "diff": "EASY"},
    {"q": "Which planet is red?", "a": "Mars", "diff": "MEDIUM"},
    {"q": "What year did Titanic sink?", "a": "1912", "diff": "HARD"},
]

def create_trivia_video(output_filename="trivia_output.mp4"):
    print("🎬 Rendering Trivia Video...")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    clips = []
    
    # 1. Background Layer (Safely handle missing assets)
    bg_path = os.path.join(config.ASSETS_DIR, "background.mp4")
    
    if os.path.exists(bg_path):
        try:
            bg = VideoFileClip(bg_path).resize(height=H)
            bg = bg.crop(x1=0, y1=0, width=W, height=H)
        except:
             print("⚠️ Error loading background. Using color.")
             bg = ColorClip(size=(W, H), color=(20, 20, 40))
    else:
        print("⚠️ No background.mp4 found. Using color.")
        bg = ColorClip(size=(W, H), color=(20, 20, 40))

    current_time = 0
    
    # 2. Add Questions
    for item in QUESTIONS:
        # Question Phase (4s)
        try:
            q_txt = (TextClip(item['q'], fontsize=80, color='white', font='Arial-Bold', method='caption', size=(900, None))
                     .set_position('center')
                     .set_start(current_time)
                     .set_duration(4))
            clips.append(q_txt)
            
            # Difficulty Label
            diff_txt = (TextClip(item['diff'], fontsize=50, color='yellow', font='Arial', method='caption')
                        .set_position(('center', 300))
                        .set_start(current_time)
                        .set_duration(4))
            clips.append(diff_txt)

            # Timer Bar (Visual only)
            timer = (ColorClip(size=(800, 20), color=(255,0,0))
                     .set_position(('center', 1500))
                     .set_start(current_time)
                     .set_duration(4))
            clips.append(timer)
        except Exception as e:
            print(f"ImageMagick Error (Text generation failed): {e}")

        current_time += 4
        
        # Answer Phase (2s)
        try:
            a_txt = (TextClip(item['a'], fontsize=100, color='green', font='Arial-Bold', method='caption', size=(900, None))
                     .set_position('center')
                     .set_start(current_time)
                     .set_duration(2))
            clips.append(a_txt)
        except: pass
        
        # Sound Effect (Safely handle missing audio)
        ding_path = os.path.join(config.ASSETS_DIR, "ding.mp3")
        if os.path.exists(ding_path):
            try:
                ding = AudioFileClip(ding_path).set_start(current_time)
            except: pass

        current_time += 2

    # 3. Composite
    final_video = CompositeVideoClip([bg.set_duration(current_time)] + clips)
    
    save_path = os.path.join(OUTPUT_DIR, output_filename)
    final_video.write_videofile(save_path, fps=24, codec="libx264", audio_codec="aac")
    print(f"✅ Saved: {save_path}")

if __name__ == "__main__":
    create_trivia_video()
