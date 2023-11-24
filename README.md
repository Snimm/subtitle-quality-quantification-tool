# Project Name

Subtitle Analysis Tool

## Overview

This tool provides functionality for analyzing videos to identify subtitle obstruction. It includes two main commands: `main` for analyzing videos for subtitle obstruction and `get-video-details` for extracting video details such as FPS, frame count, width, and height.

## Installation

Make sure you have Python installed on your system. It is recommended to use a virtual environment. Here are the installation steps:

```bash
# Clone the repository
git clone https://github.com/Snimm/subtitle-quality-quantification-tool

# Navigate to the project directory
cd subtitle-quality-quantification-tool

# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# or
.\.venv\Scripts\activate  # For Windows

# Install the required dependencies
pip install -r requirements.txt

# Run the application
python main.py --help
```

## Usage

### `main` Command

The `main` command analyzes a video for subtitle obstruction.

```bash
python main.py main [OPTIONS] VIDEO_PATH SUB_PATH
```

#### Arguments:

- `VIDEO_PATH` [required]: Path to the video file.
- `SUB_PATH` [required]: Path to the subtitle file.

#### Options:

- `--percentage-width-covered-by-sub FLOAT`: Percentage of video width covered by subtitles (default: 85).
- `--percentage-height-covered-by-sub FLOAT`: Percentage of video height covered by subtitles (default: 15).
- `--display-images-with-issue / --no-display-images-with-issue`: Display images with subtitle obstruction (default: display-images-with-issue).
- `--save-images-with-issue / --no-save-images-with-issue`: Save images with subtitle obstruction (default: no-save-images-with-issue).
- `--number-of-frames-to-analyze INTEGER`: Number of frames to analyze (default: 10).
- `--help`: Show this message and exit.

### `get-video-details` Command

The `get-video-details` command extracts video details such as FPS, frame count, width, and height.

```bash
python main.py get-video-details [OPTIONS] VIDEO_PATH
```

#### Arguments:

- `VIDEO_PATH` [required]: Path to the video file.

#### Options:

- `--help`: Show this message and exit.

## Examples

### Analyze a video for subtitle obstruction:

```bash
python main.py main --percentage-width-covered-by-sub 80 --percentage-height-covered-by-sub 10 --save-images-with-issue --number-of-frames-to-analyze 5 video.mp4 subtitles.srt
```

### Extract video details:

```bash
python main.py get-video-details video.mp4
```

## Support and Contribution

Feel free to open an issue for any problems or suggestions. Contributions are welcome!
