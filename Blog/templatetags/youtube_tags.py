import re
from django import template

register = template.Library()

@register.filter
def youtube_embed_id(youtube_url):
    """Extract YouTube video ID from various YouTube URL formats."""
    if not youtube_url:
        return None
    
    # Handle youtube.com/watch?v=ID format
    match = re.search(r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]+)', youtube_url)
    if match:
        return match.group(1)
    
    # Handle youtu.be/ID format
    match = re.search(r'(?:youtu\.be\/)([a-zA-Z0-9_-]+)', youtube_url)
    if match:
        return match.group(1)
    
    # Handle youtube.com/embed/ID format
    match = re.search(r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]+)', youtube_url)
    if match:
        return match.group(1)
    
    return None
