#!/usr/bin/env python3
"""
Build all FreeSTAR wikis and create a unified documentation site.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

# Wiki directories
WIKIS = [
    "everywhere",
    "multi-mode",
    "systemx",
    "modulex"
]

# Base directory
BASE_DIR = Path(__file__).parent
WIKIS_DIR = BASE_DIR / "wikis"
OUTPUT_DIR = BASE_DIR / "site"

def build_wiki(wiki_name):
    """Build a single wiki."""
    wiki_path = WIKIS_DIR / wiki_name
    if not wiki_path.exists():
        print(f"❌ Wiki directory not found: {wiki_name}")
        return False
    
    print(f"\n📚 Building {wiki_name} wiki...")
    
    try:
        # Change to wiki directory and build
        subprocess.run(
            ["mkdocs", "build", "-d", f"site"],
            cwd=wiki_path,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ Successfully built {wiki_name} wiki")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to build {wiki_name} wiki:")
        print(e.stderr)
        return False

def create_site_structure():
    """Create the output site structure."""
    print("\n📁 Creating site structure...")
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Copy main index.html
    index_source = BASE_DIR / "index.html"
    if index_source.exists():
        shutil.copy(index_source, OUTPUT_DIR / "index.html")
        print("✅ Copied main index.html")
    
    # Create wikis subdirectory in output
    wikis_output = OUTPUT_DIR / "wikis"
    wikis_output.mkdir(exist_ok=True)
    
    # Copy built wikis to site/wikis/ structure
    for wiki in WIKIS:
        wiki_site_dir = WIKIS_DIR / wiki / "site"
        if wiki_site_dir.exists():
            target_dir = wikis_output / wiki
            if target_dir.exists():
                shutil.rmtree(target_dir)
            shutil.copytree(wiki_site_dir, target_dir)
            print(f"✅ Copied {wiki} wiki to site/wikis/{wiki}")
    
    return True

def main():
    """Main build process."""
    print("🚀 FreeSTAR Wiki Builder")
    print("=" * 50)
    
    # Check if mkdocs is installed
    try:
        subprocess.run(["mkdocs", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ MkDocs is not installed. Please run: pip install -r requirements.txt")
        sys.exit(1)
    
    # Build all wikis
    success_count = 0
    for wiki in WIKIS:
        if build_wiki(wiki):
            success_count += 1
    
    # Create site structure
    create_site_structure()
    
    # Summary
    print("\n" + "=" * 50)
    print(f"📊 Build Summary: {success_count}/{len(WIKIS)} wikis built successfully")
    
    if success_count == len(WIKIS):
        print("✅ All wikis built successfully!")
        print(f"\n🌐 Open {OUTPUT_DIR / 'index.html'} to view the wiki hub")
        return 0
    else:
        print("⚠️  Some wikis failed to build")
        return 1

if __name__ == "__main__":
    sys.exit(main())
