# Features Implemented

## Core Functionality
- Markdown file previewer using FastAPI
- Web interface to view all .md files in the current directory
- Preview individual markdown files with proper formatting

## Technical Features
- FastAPI backend framework
- Jinja2 templating for HTML rendering
- markdown-it-py for markdown to HTML conversion
- Static file serving for CSS/JS assets
- Automatic header ID generation for anchor links
- YouTube video embedding from links

## UI/UX Features
- Homepage listing all available .md files
- Clean, responsive preview of markdown content
- Error handling for missing files
- Table of contents generation from headers (H1-H3)
- YouTube video thumbnails with play button overlay (supports both youtube.com and youtu.be links)
- Responsive design that works on different screen sizes
- Theme switching with 6 dark themes (including one totally dark theme)
- Theme preference saved in localStorage
- Theme selector positioned above file list for better accessibility
- Current file visually marked in the sidebar
- Table of contents with fixed positioning for easy navigation

## File Structure
- `main.py` - Main application logic
- `templates/` - HTML templates (index.html, preview.html)
- `static/` - CSS, JS, and other static assets
- `.md files` - All markdown files in the root directory are accessible

## Routes
- `/` - Homepage with list of all .md files
- `/preview/{file_name}` - Preview page for individual markdown files

## Dependencies
- FastAPI
- Uvicorn
- markdown-it-py
- python-multipart