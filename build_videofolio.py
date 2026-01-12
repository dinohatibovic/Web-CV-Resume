import os
from datetime import datetime

# --- CONFIGURATION ---
VIDEO_FOLDER = 'videos'      # Place your .mp4 files here
OUTPUT_FILE = 'video_index.html'
AUTHOR_NAME = "Dino Hatibovic"
SIGNATURE = "Visual Narrative & Tech"
# ---------------------

def get_videos():
    """Scans the folder for video files."""
    valid_extensions = ('.mp4', '.webm', '.mov')
    videos = []
    
    if not os.path.exists(VIDEO_FOLDER):
        os.makedirs(VIDEO_FOLDER)
        print(f"[INFO] Created folder '{VIDEO_FOLDER}'. Add your short videos inside!")
        return []

    for filename in os.listdir(VIDEO_FOLDER):
        if filename.lower().endswith(valid_extensions):
            # Formats filename into a readable title
            title = filename.split('.')[0].replace('_', ' ').replace('-', ' ').title()
            videos.append({
                'src': f"./{VIDEO_FOLDER}/{filename}",
                'title': title
            })
    return videos

def generate_html(videos):
    """Generates HTML with a responsive video grid."""
    
    video_grid_html = ""
    for vid in videos:
        # Using HTML5 video tag with modern attributes
        video_grid_html += f"""
            <div class="group relative rounded-xl overflow-hidden bg-gray-900 border border-gray-800 hover:border-brand-accent transition-all duration-300">
                <div class="aspect-video w-full">
                    <video 
                        src="{vid['src']}" 
                        controls 
                        class="w-full h-full object-cover opacity-90 group-hover:opacity-100 transition-opacity"
                        preload="metadata">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="p-4 bg-black/80 absolute bottom-0 w-full transform translate-y-full group-hover:translate-y-0 transition-transform duration-300">
                    <h3 class="text-white font-bold text-lg">{vid['title']}</h3>
                    <p class="text-brand-accent text-xs uppercase tracking-widest">Video Log</p>
                </div>
            </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{AUTHOR_NAME} | Video Log</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Space Grotesk', 'sans-serif'] }},
                    colors: {{ 'brand-black': '#0a0a0a', 'brand-accent': '#00ff9d' }} 
                }}
            }}
        }}
    </script>
    <style>
        body {{ background-color: #050505; color: #e5e5e5; }}
        /* Cyberpunk scrollbar */
        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: #000; }}
        ::-webkit-scrollbar-thumb {{ background: #00ff9d; }}
    </style>
</head>
<body class="antialiased font-sans">

    <header class="py-12 px-6 text-center border-b border-gray-800">
        <h1 class="text-4xl md:text-6xl font-bold mb-2 tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-500">
            {AUTHOR_NAME}
        </h1>
        <p class="text-brand-accent uppercase tracking-[0.3em] text-sm md:text-base mb-6">
            // {SIGNATURE} //
        </p>
        <div class="flex justify-center gap-4 text-sm text-gray-500">
            <span>Python</span> &bull; <span>Cloud</span> &bull; <span>Visuals</span>
        </div>
    </header>

    <main class="max-w-7xl mx-auto py-16 px-4">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {video_grid_html}
        </div>
        
        {"" if videos else "<p class='text-center text-gray-600 mt-10'>No videos found. Run this script after adding .mp4 files to the 'videos' folder.</p>"}
    </main>

    <footer class="text-center py-12 text-gray-600 text-xs border-t border-gray-800 mt-12">
        <p>&copy; {datetime.now().year} {AUTHOR_NAME}. Generated via Python Automation.</p>
    </footer>

</body>
</html>"""

    return html_content

def main():
    print("--- Video Portfolio Builder v1.0 ---")
    videos = get_videos()
    
    if videos:
        html = generate_html(videos)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[SUCCESS] Generated '{OUTPUT_FILE}' with {len(videos)} videos.")
    else:
        print("[INFO] No videos found to process.")

if __name__ == "__main__":
    main()
