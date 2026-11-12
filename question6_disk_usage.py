from pathlib import Path


def disk_usage(path):
    """Return the total size in bytes of a file or folder and its contents."""
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    if path.is_file():
        return path.stat().st_size

    if path.is_dir():
        total_size = 0
        for child in path.iterdir():
            total_size += disk_usage(child)
        return total_size

    raise ValueError(f"Path is neither a regular file nor a folder: {path}")


if __name__ == "__main__":
    folder_path = input("Enter a file or folder path: ").strip()
    try:
        print(f"Total size: {disk_usage(folder_path)} bytes")
    except (FileNotFoundError, ValueError, PermissionError) as error:
        print(f"Could not calculate disk usage: {error}")
