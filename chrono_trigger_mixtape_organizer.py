#!/usr/bin/env python3
# flake8: noqa: E501
# pylint: disable=line-too-long
"""
Chrono Trigger Mixtape Organizer

This script does everything in one step:
1. Cleans filenames by removing website URLs
2. Standardizes metadata tags
3. Organizes files into a proper music library structure

The final output will be in the "Music Library" directory with:
- Various Artists/Chrono Trigger Mixtape/ (DJ Mix)
- Various Artists/Chrono Trigger Mixtape (No DJ Version)/
- Compromised/Chrono Trigger Mixtape (Instrumentals)/
"""

import os
import re
import shutil
import subprocess
from pathlib import Path

# Base directories
SOURCE_DIR = Path("extracted music")
FINAL_DIR = Path("Music Library")

# Define the three versions and their metadata
VERSIONS = {
    "DJ Mix": {
        "source_dir": SOURCE_DIR / "Chrono Trigger Mixtape",
        "target_dir": FINAL_DIR / "Various Artists" / "Chrono Trigger Mixtape",
        "album": "Chrono Trigger Mixtape",
        "album_artist": "Various Artists",
        "year": "2005",
        "genre": "Hip-Hop/Rap (DJ Mix)",
        "disc_num": "1/3",
        "disc_prefix": "1-",
    },
    "No DJ Mix": {
        "source_dir": SOURCE_DIR / "Chrono Trigger Mixtape (No DJ Version)",
        "target_dir": (
            FINAL_DIR / "Various Artists" / "Chrono Trigger Mixtape (No DJ Version)"
        ),
        "album": "Chrono Trigger Mixtape (No DJ Version)",
        "album_artist": "Various Artists",
        "year": "2005",
        "genre": "Hip-Hop/Rap",
        "disc_num": "2/3",
        "disc_prefix": "2-",
    },
    "Instrumentals": {
        "source_dir": SOURCE_DIR / "Chrono Trigger Mixtape (Instrumentals)",
        "target_dir": (
            FINAL_DIR / "Compromised" / "Chrono Trigger Mixtape (Instrumentals)"
        ),
        "album": "Chrono Trigger Mixtape (Instrumentals)",
        "album_artist": "Compromised",
        "year": "2005",
        "genre": "Hip-Hop/Instrumental",
        "disc_num": "3/3",
        "disc_prefix": "3-",
    },
}

# Cover art file - will be copied from the Instrumentals directory if available
COVER_ART = Path("cover_art.jpg")


def clean_filename(filename):
    """Clean up filename by removing website URLs and standardizing format."""
    # Remove the website URL references
    clean_name = re.sub(r"\s*\[www\.chronotriggermixtape\.com\]", "", filename)
    clean_name = re.sub(r"\s*www\.chronotriggermixtape\.com", "", clean_name)

    # Clean up extra spaces and other inconsistencies
    clean_name = re.sub(r"\s+", " ", clean_name).strip()

    return clean_name


def extract_track_info(filename):
    """Extract track number, artist, and title from filename."""
    # Extract track number
    track_match = re.match(r"^(\d+)\s+(.+)\.mp3$", filename)
    if not track_match:
        return None, None, None

    track_num = track_match.group(1)
    rest = track_match.group(2)

    # Handle special cases for intros and outros
    if "Presentiment (Intro)" in rest and " - " not in rest:
        if "Chrono Trigger Mixtape -" in rest:
            # No DJ Mix version
            artist = "Chrono Trigger Mixtape"
            title = "Presentiment (Intro)"
        else:
            # DJ Mix version
            artist = "Various Artists"
            title = "Presentiment (Intro)"
    elif "Outro" in rest and " - " not in rest:
        artist = "Various Artists"
        title = "Outro"
    else:
        # Extract artist and title
        parts = rest.split(" - ", 1)
        if len(parts) != 2:
            return track_num, None, rest

        artist, title = parts

        # Remove website from title
        title = re.sub(r"\s*\[www\.chronotriggermixtape\.com\]", "", title)
        title = re.sub(r"\s*www\.chronotriggermixtape\.com", "", title)

    return track_num, artist, title


def update_metadata(file_path, **kwargs):
    """Update ID3 metadata tags using id3v2."""
    # Map kwargs to id3v2 tag options
    tag_map = {
        "title": "-t",
        "artist": "-a",
        "album": "-A",
        "album_artist": "--TPE2",
        "track_num": "-T",
        "year": "-y",
        "genre": "-g",
        "disc_num": "--TPOS",
    }

    # Prepare id3v2 command
    command = ["id3v2", "--delete-all", str(file_path)]
    subprocess.run(command, check=True)

    command = ["id3v2"]
    for key, value in kwargs.items():
        if key in tag_map and value:
            command.extend([tag_map[key], str(value)])

    command.append(str(file_path))
    subprocess.run(command, check=True)


def add_cover_art(file_path, cover_art_path):
    """Add cover art to the audio file using ffmpeg."""
    if cover_art_path.exists():
        temp_file = f"{file_path}.temp.mp3"
        command = [
            "ffmpeg",
            "-i",
            str(file_path),
            "-i",
            str(cover_art_path),
            "-map",
            "0:0",
            "-map",
            "1:0",
            "-c",
            "copy",
            "-id3v2_version",
            "3",
            "-metadata:s:v",
            'title="Album cover"',
            "-metadata:s:v",
            'comment="Cover (front)"',
            str(temp_file),
        ]

        try:
            subprocess.run(
                command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            os.replace(temp_file, file_path)
            print(f"Added cover art to {file_path}")
        except subprocess.CalledProcessError:
            print(f"Failed to add cover art to {file_path}")
            if os.path.exists(temp_file):
                os.remove(temp_file)


def process_files():
    """Process all files for all versions in one go."""
    # First, find and copy cover art
    found_cover = False

    # Try to copy the Creditz file (which we know exists) with proper quoting/escaping
    creditz_file = SOURCE_DIR / "Chrono Trigger Mixtape" / "Creditz+Contact info!.jpg"
    try:
        if creditz_file.exists():
            print(f"Using credits image as cover art: {creditz_file}")
            shutil.copy2(creditz_file, COVER_ART)
            found_cover = True
    except Exception as e:
        print(f"Error copying cover art: {e}")

    # Only if that fails, try the generic search
    if not found_cover:
        for version_key, version_info in VERSIONS.items():
            for file in version_info["source_dir"].glob("*.*"):
                if (
                    "cover" in file.name.lower()
                    or "art" in file.name.lower()
                    or "creditz" in file.name.lower()
                ):
                    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                        try:
                            print(f"Found cover art: {file}")
                            shutil.copy2(file, COVER_ART)
                            found_cover = True
                            break
                        except Exception as e:
                            print(f"Error copying file {file}: {e}")
            if found_cover:
                break

    # Process each version
    for version_key, version_info in VERSIONS.items():
        print(f"\nProcessing {version_key} version...")

        source_dir = version_info["source_dir"]
        target_dir = version_info["target_dir"]
        disc_prefix = version_info["disc_prefix"]

        # Ensure target directory exists
        target_dir.mkdir(exist_ok=True, parents=True)

        # Get all MP3 files in the source directory
        mp3_files = list(source_dir.glob("*.mp3"))
        total_tracks = len(mp3_files)

        # Process each file
        for source_file in mp3_files:
            # Get clean filename
            clean_name = clean_filename(source_file.name)
            print(f"Processing {clean_name}...")

            # Extract track info
            track_num, artist, title = extract_track_info(clean_name)

            if not track_num or not title:
                print(f"Couldn't extract info from {clean_name}, skipping...")
                continue

            # Create new filename with disc prefix
            if artist and not artist == version_info["album_artist"]:
                new_filename = f"{disc_prefix}{track_num} {artist} - {title}.mp3"
            else:
                new_filename = f"{disc_prefix}{track_num} {title}.mp3"

            target_file = target_dir / new_filename

            # Copy file with new name
            print(f"Copying {source_file} to {target_file}")
            shutil.copy2(source_file, target_file)

            # Update metadata
            update_metadata(
                target_file,
                title=title,
                artist=(
                    artist
                    if artist and version_key != "Instrumentals"
                    else version_info["album_artist"]
                ),
                album=version_info["album"],
                album_artist=version_info["album_artist"],
                track_num=f"{track_num}/{total_tracks}",
                year=version_info["year"],
                genre=version_info["genre"],
                disc_num=version_info["disc_num"],
            )

            # Add cover art
            if COVER_ART.exists():
                add_cover_art(target_file, COVER_ART)


def main():
    """Main function to run the entire process."""
    # Ensure final directory exists
    FINAL_DIR.mkdir(exist_ok=True, parents=True)

    # Process all files
    process_files()

    print(
        "\nAll done! Your organized Chrono Trigger Mixtape is in the 'Music Library' directory."
    )


if __name__ == "__main__":
    main()
