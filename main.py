from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
import json
from markdown_it import MarkdownIt
import re
import uvicorn
import webbrowser
import threading
import time
import pystray
from PIL import Image
import sys

app = FastAPI()

# Mount static files directories
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/files", StaticFiles(directory="files"), name="files")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Initialize markdown parser
md = MarkdownIt()

# Load configuration
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Return default configuration if config.json doesn't exist
        return {
            "default_theme": "theme-default",
            "toc_visible": True
        }

def get_md_files():
    """Get all .md files in the 'files' directory"""
    files_dir = "files"
    if os.path.exists(files_dir):
        return [f for f in os.listdir(files_dir) if f.endswith(".md")]
    return []

def extract_headers(markdown_content):
    """Extract H1, H2, and H3 headers from markdown content"""
    headers = []
    lines = markdown_content.split('\n')
    
    for line in lines:
        # Match headers (## Header Text)
        header_match = re.match(r'^(#{1,3})\s+(.+)', line)
        if header_match:
            level = len(header_match.group(1))  # 1 for H1, 2 for H2, 3 for H3
            title = header_match.group(2).strip()
            # Create an ID for the header (slugify the title)
            header_id = re.sub(r'[^a-zA-Z0-9\-_]', '', re.sub(r'\s+', '-', title.lower()))
            headers.append({
                'level': level,
                'title': title,
                'id': header_id
            })
    
    return headers

def extract_youtube_id(url):
    """Extract YouTube video ID from various YouTube URL formats"""
    # Regularni izrazi za različite formate YouTube URL-ova
    patterns = [
        r'(?:https?://)?(?:www.)?youtube.com/watch?v=([^&\n\r\s]+)',
        r'(?:https?://)?(?:www.)?youtu.be/([^\n\r\s?&]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def add_header_ids_to_markdown(markdown_content):
    """Add IDs to headers in markdown content and add YouTube thumbnails"""
    lines = markdown_content.split('\n')
    processed_lines = []
    
    for line in lines:
        # Check for YouTube links first
        youtube_id = extract_youtube_id(line)
        if youtube_id:
            # Replace the line with a clickable YouTube thumbnail that looks like a video
            youtube_thumbnail = f'<div class="youtube-thumbnail-container"><a href="https://www.youtube.com/watch?v={youtube_id}" target="_blank"><img src="http://img.youtube.com/vi/{youtube_id}/maxresdefault.jpg" alt="YouTube Video" class="youtube-thumbnail"><div class="play-button-overlay"></div></a></div>'
            processed_lines.append(youtube_thumbnail)
            continue
            
        # Match headers (## Header Text)
        header_match = re.match(r'^(#{1,3})\s+(.+)', line)
        if header_match:
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            # Create an ID for the header (slugify the title)
            header_id = re.sub(r'[^a-zA-Z0-9\-_]', '', re.sub(r'\s+', '-', title.lower()))
            # Add ID to the header in markdown format
            processed_lines.append(f'<h{level} id="{header_id}">{title}</h{level}>')
        else:
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    md_files = get_md_files()
    config = load_config()
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "files": md_files,
        "default_theme": config["default_theme"],
        "toc_visible": config["toc_visible"]
    })

@app.get("/preview/{file_name}", response_class=HTMLResponse)
async def preview_file(request: Request, file_name: str):
    # Verify file exists and is a .md file
    file_path = os.path.join("files", file_name)
    if not file_name.endswith(".md") or not os.path.exists(file_path):
        md_files = get_md_files()
        config = load_config()
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "files": md_files, 
            "error": "File not found",
            "default_theme": config["default_theme"],
            "toc_visible": config["toc_visible"]
        }, status_code=404)
    
    # Read the markdown file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Extract headers for table of contents
    headers = extract_headers(content)
    
    # Add IDs to headers in content
    content_with_ids = add_header_ids_to_markdown(content)
    
    # Convert markdown to HTML
    html_content = md.render(content_with_ids)
    
    # Get all .md files in current directory
    md_files = get_md_files()
    
    # Load configuration
    config = load_config()
    
    return templates.TemplateResponse("preview.html", {
        "request": request, 
        "content": html_content, 
        "file_name": file_name, 
        "files": md_files,
        "headers": headers,
        "default_theme": config["default_theme"],
        "toc_visible": config["toc_visible"]
    })

def open_browser():
    """Open the browser after a short delay to ensure server is running"""
    time.sleep(2)  # Wait for server to start
    webbrowser.open("http://127.0.0.1:8000")

def create_image():
    # Create an image for the system tray icon
    # We'll use the icon.ico file if it exists, otherwise create a simple image
    try:
        # Try to load the icon file
        image = Image.open("icon.ico")
    except:
        # Create a simple image if icon file doesn't exist
        image = Image.new('RGB', (64, 64), color='blue')
    return image

def on_exit(icon, item):
    """Handle exit action from system tray"""
    icon.stop()
    os._exit(0)  # Force exit the application

def setup_system_tray():
    """Setup and run the system tray icon"""
    image = create_image()
    menu = pystray.Menu(
        pystray.MenuItem('Open Markdown+', lambda: webbrowser.open("http://127.0.0.1:8000")),
        pystray.MenuItem('Exit', on_exit)
    )
    icon = pystray.Icon("MD Profi", image, menu=menu)
    icon.run()

if __name__ == "__main__":
    # Start browser opening in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start system tray in a separate thread
    tray_thread = threading.Thread(target=setup_system_tray)
    tray_thread.daemon = True
    tray_thread.start()
    
    # Run the server with logging completely disabled
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8000,
        log_config=None,  # Disable uvicorn's default logging config
        log_level="critical",  # Set log level to critical to minimize output
        access_log=False       # Disable access log
    )
