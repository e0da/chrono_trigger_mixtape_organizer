# Chrono Trigger Mixtape Organizer

Clean up and organize the Chrono Trigger Mixtape collection with standardized metadata for optimal music library integration.

## About

The Chrono Trigger Mixtape (2005) features artists rapping over beats sampled from the SNES game "Chrono Trigger." This project organizes three versions:

- **DJ Mix** - Original mixtape with DJ drops
- **No DJ Mix** - Clean versions without DJ drops
- **Instrumentals** - Original Chrono Trigger sample beats by Compromised

## Download

Get the mixtape archives from:
https://static.chronocompendium.com/Black/Music%20(Chrono%20Trigger)/CT%20Mixtape/

Required files:

- `Chrono Trigger Mixtape.rar`
- `Chrono Trigger Mixtape (No DJ Version).rar`
- `Chrono Trigger Mixtape (Instrumentals).rar`

## Installation

### Dependencies (macOS)

Install required tools with Homebrew:

```bash
brew bundle
```

The included Brewfile installs:

- ffmpeg (media processing and cover art)
- id3v2 (MP3 metadata tagging)
- unar (archive extraction)

### Manual Installation

If not using Homebrew, install these dependencies:

- Python 3.6+
- ffmpeg
- id3v2
- Archive extraction tool (unar recommended)

## Usage

### Setup Options

**Option 1: Pre-extracted files**

1. Extract the downloaded archives
2. Place files in `extracted music/` with respective folders:
   - `extracted music/Chrono Trigger Mixtape/`
   - `extracted music/Chrono Trigger Mixtape (No DJ Version)/`
   - `extracted music/Chrono Trigger Mixtape (Instrumentals)/`
3. Optionally store original archives in `original archives/`

**Option 2: Extract in place**

1. Place RAR archives in `extracted music/`
2. Extract them there to create necessary subdirectories

### Run

```bash
python3 chrono_trigger_mixtape_organizer.py
```

### Output Structure

```
Music Library/
├── Compromised/
│   └── Chrono Trigger Mixtape (Instrumentals)/
│       ├── 3-01 Compro - Gato's Theme (Instrumental).mp3
│       ├── ...
├── Various Artists/
    ├── Chrono Trigger Mixtape/
    │   ├── 1-01 Presentiment (Intro).mp3
    │   ├── ...
    └── Chrono Trigger Mixtape (No DJ Version)/
        ├── 2-01 Chrono Trigger Mixtape - Presentiment (Intro).mp3
        ├── ...
```

### Clean Up

Reset the project directory:

```bash
./cleanup.sh
```

## Metadata Standards

### DJ Mix

- Album: "Chrono Trigger Mixtape"
- Album Artist: "Various Artists"
- Disc: 1/3
- Genre: "Hip-Hop/Rap (DJ Mix)"

### No DJ Mix

- Album: "Chrono Trigger Mixtape (No DJ Version)"
- Album Artist: "Various Artists"
- Disc: 2/3
- Genre: "Hip-Hop/Rap"

### Instrumentals

- Album: "Chrono Trigger Mixtape (Instrumentals)"
- Album Artist: "Compromised"
- Disc: 3/3
- Genre: "Hip-Hop/Instrumental"

## Credits

- Original mixtape by Compromised (Ali Haeri), 2005
- Samples from Chrono Trigger soundtrack by Yasunori Mitsuda
- Organization tools created in 2025

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Justin Force <justin.force@gmail.com>
