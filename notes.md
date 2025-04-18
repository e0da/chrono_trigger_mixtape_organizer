# Chrono Trigger Mixtape Metadata Organization

## Problem

The Chrono Trigger Mixtape collection has inconsistent metadata across different versions:

- Main mixtape
- No DJ version
- Instrumentals

Issues identified:

1. Inconsistent file naming conventions
2. Metadata filled with website URLs instead of proper information
3. No consistent album art
4. No proper organization between the three versions
5. Tracks aren't properly numbered in metadata

## Goal

Standardize naming, organization, and ID3 metadata for better Apple Music integration.

## Current Structure

### Main Mixtape

- 12 tracks + intro/outro
- Artist names in filenames
- Metadata contains "The Chrono Trigger Mixtape, vol. #1" as album title
- All metadata fields contain website URLs

### No DJ Version

- Similar tracks to main version but without DJ drops
- Nearly identical metadata issues

### Instrumentals

- Original Chrono Trigger samples/beats
- Different naming convention
- Different metadata structure
- Listed as "Chrono Trigger Mixtape" as artist

## Standardization Plan

1. Create consistent album/compilation structure:

   - Album: "Chrono Trigger Mixtape"
   - Three versions as disc numbers or compilation parts

2. Metadata schema:

   - **Main Mixtape:**

     - Album: "Chrono Trigger Mixtape"
     - Album Artist: "Various Artists"
     - Disc/Compilation: "DJ Mix"
     - Year: 2005
     - Genre: Hip-Hop/Rap
     - Track numbers: Sequential (1-12)

   - **No DJ Version:**

     - Album: "Chrono Trigger Mixtape"
     - Album Artist: "Various Artists"
     - Disc/Compilation: "No DJ Mix"
     - Year: 2005
     - Genre: Hip-Hop/Rap
     - Track numbers: Sequential (1-11)

   - **Instrumentals:**
     - Album: "Chrono Trigger Mixtape"
     - Album Artist: "Compromised"
     - Disc/Compilation: "Instrumentals"
     - Year: 2005
     - Genre: Hip-Hop/Instrumental
     - Track numbers: Sequential (1-10)

3. Filename standardization:

   - Format: `[Track#] [Artist] - [Title].mp3`
   - Remove website URLs from filenames
   - Keep song title and artists consistent

4. Add consistent album artwork to all tracks

## Tools

- id3v2: Command-line ID3 tag editor
- ffmpeg: Audio processing
- Scripts for batch processing

## Progress

- ✅ Installed necessary tools
- ✅ Analyzed current file structure and metadata
- ✅ Created a comprehensive script (`chrono_trigger_mixtape_organizer.py`) that:
  - Cleans filenames by removing website URLs
  - Standardizes ID3 metadata tags for all three versions
  - Adds album artwork to all tracks
  - Organizes files into a proper music library structure
  - Implements disc numbering prefixes (1-xx, 2-xx, 3-xx)
- ✅ Successfully processed all tracks:
  - DJ Mix: 12 tracks under "Various Artists/Chrono Trigger Mixtape/"
  - No DJ Mix: 11 tracks under "Various Artists/Chrono Trigger Mixtape (No DJ Version)/"
  - Instrumentals: 10 tracks under "Compromised/Chrono Trigger Mixtape (Instrumentals)/"
- ⬜ Test in Apple Music app

## Final Structure

```
Music Library/
├── Compromised/
│   └── Chrono Trigger Mixtape (Instrumentals)/
│       ├── 3-01 Compro - Gato's Theme (Instrumental).mp3
│       ├── 3-02 Compro - Wind Scene (Instrumental).mp3
│       └── ...
├── Various Artists/
│   ├── Chrono Trigger Mixtape/
│   │   ├── 1-01 Presentiment (Intro).mp3
│   │   ├── 1-02 50 Cent - Disco Inferno.mp3
│   │   └── ...
│   └── Chrono Trigger Mixtape (No DJ Version)/
│       ├── 2-01 Chrono Trigger Mixtape - Presentiment (Intro).mp3
│       ├── 2-02 50 Cent - Disco Inferno.mp3
│       └── ...
```

The metadata for all tracks has been standardized according to the plan, with proper artist information, album names, track numbers, genre information, and embedded cover art.
