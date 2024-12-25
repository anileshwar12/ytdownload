# YTDownload - YouTube Video Downloader

YTDownload is a simple and fast YouTube video downloader built with Python and the popular `yt-dl` library. This tool allows you to download YouTube videos effortlessly, without needing to open your browser.

## Features

- Download videos from YouTube.
- Simple, easy-to-use interface.
- Standalone executable (`.exe`) file for Windows, no need to install Python.

## Installation

1. Clone this repository or [download the ZIP file](https://github.com/anileshwar12/ytdownload/archive/main.zip).
2. Navigate to the project directory.
3. Download the compiled `.exe` file for Windows (if you don't want to run it through Python).
   You can download the latest release from the link below:

   [Download YTDownload.exe](./dist/YTDownload.exe)

### Requirements

- Python 3.x (if you want to run it directly through Python).
- `yt-dl` library for downloading the videos (already included in the `.exe`).

## Usage

1. **Using the .exe file:**
   - After downloading the `YTDownload.exe` file from the dist folder, simply double-click it to run the application.
   - Paste the YouTube video URL to download.

2. **Using Python (optional):**
   - Ensure Python 3.x is installed on your system.
   - Install the necessary libraries by running:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the script via:
     ```bash
     python ytdownload.py
     ```

## Contributing

We welcome contributions to improve the project! Feel free to fork the repository, make changes, and submit a pull request.


## Acknowledgments

- [yt-dl](https://github.com/yt-dl/yt-dl) - The core library for downloading YouTube videos.
