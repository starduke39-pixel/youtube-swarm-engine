import os
import requests
import config

VIDEOS_PER_SEARCH = 3 # Kept low to save bandwidth on GitHub Actions
ORIENTATION = "portrait"

def search_and_download(query, save_folder):
    print(f"\n🔍 Searching Pexels for: '{query}'...")
    
    headers = {'Authorization': config.PEXELS_API_KEY}
    url = f"https://api.pexels.com/videos/search?query={query}&per_page={VIDEOS_PER_SEARCH}&orientation={ORIENTATION}&size=medium"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error connecting to Pexels: {response.status_code}")
            return

        data = response.json()
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        for video in data.get('videos', []):
            # Pick the HD version (1280x720 or similar)
            video_files = video.get('video_files', [])
            target_file = next((v for v in video_files if v['height'] >= 1080), video_files[0])
            
            download_url = target_file['link']
            file_name = f"{video['id']}.mp4"
            full_path = os.path.join(save_folder, file_name)
            
            if not os.path.exists(full_path):
                print(f"   ⬇️ Downloading: {file_name}")
                with open(full_path, 'wb') as f:
                    f.write(requests.get(download_url).content)
            else:
                print(f"   ⏩ Skipping {file_name}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    asset_dir = os.path.join(config.BASE_DIR, "Stock_Footage")
    
    # Define what keywords to search for each channel
    search_map = {
        "Ancient_Echoes": ["Greek Statue", "Night Sky", "Storm"],
        "Abyss_Archives": ["Dark Ocean", "Fog", "Mystery"],
        "Apex_Lists": ["Luxury Car", "Money", "Mansion"],
        "Mind_Architect": ["Gym", "Library", "Statue"]
    }

    for channel, keywords in search_map.items():
        channel_asset_dir = os.path.join(asset_dir, channel)
        for keyword in keywords:
            search_and_download(keyword, channel_asset_dir)

if __name__ == "__main__":
    main()
