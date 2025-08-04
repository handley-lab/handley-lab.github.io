# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the Handley Research Group website, a Jekyll-based GitHub Pages site for the University of Cambridge research group. The site showcases research papers, group members, and academic activities with content automatically generated using Large Language Models.

## Essential Commands

### Development Server
```bash
# Start local Jekyll development server
script/server

# Alternative: bundle exec jekyll serve
bundle exec jekyll serve
```

### Build & Deploy
```bash
# Build the site
script/build

# CI build (includes validation)
script/cibuild

# Bootstrap dependencies
script/bootstrap
```

### Setup Dependencies
```bash
# Install Ruby gems
gem install bundler
bundle install
```

## Architecture & Structure

### Jekyll Configuration
- **Site Configuration**: `_config.yml` - Main Jekyll configuration with theme (minima), plugins, and site metadata
- **Dependencies**: `Gemfile` - Ruby gem dependencies including Jekyll 3.10.0 and minima theme
- **Custom Styling**: `_sass/minima/` - SCSS overrides for the minima theme

### Content Organization
- **Posts**: `_posts/` - Academic paper blog posts with standardized naming: `YYYY-MM-DD-ARXIV_ID.md`
- **Layouts**: `_layouts/` - Jekyll templates (base, home, post, page, group)
- **Includes**: `_includes/` - Reusable components (header, footer, social icons)
- **Static Assets**: `assets/` - Images, CSS, and group-related content

### Automated Content Generation

#### Paper Posts (`script/posts/arxiv.py`)
Generates blog posts from arXiv papers using Google's Gemini API:
- **Usage**: `python script/posts/arxiv.py <arxiv_id>`
- **Process**: Fetches paper metadata, LaTeX source, extracts author info from `group.yaml`, generates content and accompanying image
- **Dependencies**: Requires `GEMINI_API_KEY` environment variable
- **Output**: Creates post in `_posts/`, image in `assets/images/posts/`, and prompts in `prompts/`

#### Group Management
- **Data Source**: `assets/group/group.yaml` - Central YAML database of all group members with roles, dates, images, and links
- **HTML Generation**: `assets/group/html_table.py` - Generates responsive HTML grid layout for group page
- **Python Classes**: `assets/group/group.py` - Object model for managing academic roles (PI, PostDoc, PhD, etc.) with chronological sorting

### Academic Role Hierarchy
```python
# Seniority levels (lower number = higher seniority)
PI: -1
Co-I: -1  
PostDoc: 0
PhD: 1
MPhil: 2
PartIII: 3
Summer: 4
```

### Group Member Data Structure
```yaml
Person Name:
  role_type:                    # pi, coi, postdoc, phd, mphil, partiii, summer
    start: YYYY-MM-DD
    end: YYYY-MM-DD            # Optional, null for current
    supervisors: [list]        # Optional
    thesis: "Title"            # Optional
  image: path/to/image.jpg
  original_image: path/to/original.jpg  # Before processing
  links:
    Description: URL
  destination:                 # Post-group career tracking
    YYYY-MM-DD: Position
```

## Python Environment & Dependencies

### Required Python Packages
```python
# Core dependencies for group management
import yaml          # Group data parsing
import pandas        # Data manipulation
import datetime      # Date handling

# Web generation
from yattag import Doc  # HTML generation

# arXiv post generation
from google import genai     # Gemini API
import requests             # HTTP requests  
import feedparser          # RSS/Atom feeds
import tarfile, io         # arXiv source extraction
from PIL import Image      # Image processing
```

### Environment Variables
- `GEMINI_API_KEY` - Required for automated post generation via Gemini API

## Content Management Workflows

### Adding Group Members
1. Update `assets/group/group.yaml` with new member data
2. Add member photo to `assets/group/images/originals/`
3. Run `python assets/group/group.py` to process and sort data
4. Run `python assets/group/html_table.py` to regenerate group page HTML

### Creating Paper Posts
1. Get arXiv ID for the paper
2. Run: `python script/posts/arxiv.py <arxiv_id>`
3. Review generated content in `_posts/YYYY-MM-DD-<arxiv_id>.md`
4. Check generated image in `assets/images/posts/`

### Site Deployment
- **Automatic**: Pushes to `main` branch trigger GitHub Pages rebuild
- **Manual**: Run `script/build` locally to test before pushing

## File Organization Logic

### Generated Content Tracking
- `prompts/content/` - Text prompts used for post generation
- `prompts/images/` - Image prompts used for visual generation  
- `_site/` - Jekyll build output (auto-generated, not tracked)

### Image Management
- `assets/group/images/originals/` - Source images before processing
- `assets/group/images/` - Processed member photos (standardized size/format)
- `assets/images/posts/` - AI-generated paper post images
- `assets/images/` - General site images and backgrounds

### Academic Integration Features
- **ArXiv Integration**: Automatic paper metadata extraction and bibliography formatting
- **Author Linking**: Cross-references group members with paper authors
- **Citation Formatting**: Converts LaTeX citations to Markdown links (DOI/arXiv)
- **Timeline Management**: Tracks member academic progressions and career destinations