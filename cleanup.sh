#!/bin/bash
# Cleanup script to organize the Chrono Trigger Mixtape project

echo "Cleaning up project directory..."

# 1. Remove unnecessary output directories
echo "Removing intermediate and output directories..."
rm -rf "clean_files" "final_files" "working_files" "Music Library - Fixed"

# 2. Remove old transformation scripts that are no longer needed
echo "Removing old/redundant scripts..."
rm -f "clean_filenames.py" "metadata_fixer.py" "organize_music_library.py" "organize_music_library_fixed.py" "clean_metadata.py"

# 3. Keep only the original source and the comprehensive script
echo "Keeping only source files and the comprehensive transformation script..."
mkdir -p "backup"
mv "Music Library" "backup/" 2>/dev/null

# 4. Clean up working copy of cover art if it exists
if [ -f "cover_art.jpg" ]; then
  rm -f "cover_art.jpg"
fi

echo ""
echo "Clean-up complete! The project now contains:"
echo "- 'extracted music/' directory (original source files)"
echo "- 'chrono_trigger_mixtape_organizer.py' (transformation script)"
echo "- 'backup/Music Library/' (previous transformation output, if you need it)"
echo ""
echo "You can now run the clean transformation by executing:"
echo "python3 chrono_trigger_mixtape_organizer.py"
echo ""
echo "This will produce a fresh 'Music Library' directory with the correctly organized files."
