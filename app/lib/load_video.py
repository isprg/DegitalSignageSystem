from pathlib import Path


def load_videos():
    """
    Load videos from the 'videos' directory.

    Returns:
        list: A list of video file paths.
    """
    video_dir = Path(__file__).parents[1] / "static" / "videos"
    if not video_dir.exists():
        raise FileNotFoundError(f"The directory {video_dir} does not exist.")

    video_files = list(video_dir.glob("*.mp4"))  # Assuming videos are in .mp4 format
    return video_files
