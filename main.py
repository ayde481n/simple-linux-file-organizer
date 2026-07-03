import shutil
from pathlib import Path

extensions = {
    #documents
    ".txt": "Documents",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".md": "Documents",
    ".tex": "Documents",
    ".pages": "Documents",
    ".wpd": "Documents",
    ".xps": "Documents",
    ".djvu": "Documents",
    #spreadsheets
    ".csv": "Spreadsheets",
    ".tsv": "Spreadsheets",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".xlsm": "Spreadsheets",
    ".ods": "Spreadsheets",
    ".numbers": "Spreadsheets",
    #presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",
    ".odp": "Presentations",
    ".key": "Presentations",
    #images
    ".jpg": "Pictures",
    ".jpeg": "Pictures",
    ".png": "Pictures",
    ".gif": "Pictures",
    ".webp": "Pictures",
    ".svg": "Pictures",
    ".bmp": "Pictures",
    ".tiff": "Pictures",
    ".tif": "Pictures",
    ".ico": "Pictures",
    ".heic": "Pictures",
    ".heif": "Pictures",
    ".avif": "Pictures",
    ".raw": "Pictures",
    ".cr2": "Pictures",
    ".nef": "Pictures",
    ".arw": "Pictures",
    ".dng": "Pictures",
    ".psd": "Pictures",
    ".xcf": "Pictures",
    ".ai": "Pictures",
    ".eps": "Pictures",
    #videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".webm": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".m4v": "Videos",
    ".mpg": "Videos",
    ".mpeg": "Videos",
    ".3gp": "Videos",
    ".ts": "Videos",
    ".ogv": "Videos",
    #music/audio
    ".mp3": "Music",
    ".wav": "Music",
    ".flac": "Music",
    ".ogg": "Music",
    ".oga": "Music",
    ".m4a": "Music",
    ".aac": "Music",
    ".wma": "Music",
    ".opus": "Music",
    ".aiff": "Music",
    ".alac": "Music",
    ".mid": "Music",
    ".midi": "Music",
    #archives
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".tgz": "Archives",
    ".bz2": "Archives",
    ".7z": "Archives",
    ".rar": "Archives",
    ".xz": "Archives",
    ".zst": "Archives",
    ".lz": "Archives",
    ".lzma": "Archives",
    ".cab": "Archives",
    ".arj": "Archives",
    #scripts
    ".py": "Scripts",
    ".sh": "Scripts",
    ".bash": "Scripts",
    ".zsh": "Scripts",
    ".fish": "Scripts",
    ".pl": "Scripts",
    ".rb": "Scripts",
    ".lua": "Scripts",
    ".ps1": "Scripts",
    ".bat": "Scripts",
    #installers
    ".appimage": "Installers",
    ".deb": "Installers",
    ".rpm": "Installers",
    ".flatpakref": "Installers",
    ".snap": "Installers",
    ".exe": "Installers",
    ".msi": "Installers",
    ".dmg": "Installers",
    ".pkg": "Installers",
    ".apk": "Installers",
    #disk images
    ".iso": "DiskImages",
    ".img": "DiskImages",
    ".ova": "DiskImages",
    ".ovf": "DiskImages",
    ".vmdk": "DiskImages",
    ".vdi": "DiskImages",
    ".qcow2": "DiskImages",
    ".vhd": "DiskImages",
    ".bin": "DiskImages",
    ".cue": "DiskImages",
    #ebooks
    ".epub": "Ebooks",
    ".mobi": "Ebooks",
    ".azw": "Ebooks",
    ".azw3": "Ebooks",
    ".fb2": "Ebooks",
    ".cbz": "Ebooks",
    ".cbr": "Ebooks",
    #torrents
    ".torrent": "Torrents",
    #data
    ".db": "Data",
    ".sqlite": "Data",
    ".sql": "Data",
    ".log": "Data",
    ".yaml": "Data",
    ".yml": "Data",
    ".toml": "Data",
}


protected = [
    Path("/"), Path("/etc"), Path("/usr"), Path("/bin"), Path("/sbin"),
    Path("/boot"), Path("/var"), Path("/lib"), Path("/lib64"),
    Path("/sys"), Path("/proc"), Path("/dev"), Path("/root"),
]

location = Path(input("Path of the directory you'd like to clean: ")).expanduser()

if not location.is_dir():
    raise SystemExit("That is not a valid directory.")

if location.resolve() in protected:
    raise SystemExit("Refusing to organize a protected system directory.")

print('')
print("WARNING: Do not run on system directories or anything where files "
      "depend on staying together (websites, codebases, app bundles).")
confirm = input(f"Organize all files in {location}? (y/n): ")

if confirm.lower() not in ("yes", "y"):
    raise SystemExit("Cancelled.")

for item in list(location.iterdir()):
    if item.name.startswith("."):
        continue
    elif item.is_file():
        if item.suffix.lower() in extensions:
            directory = extensions[item.suffix.lower()]
            destination = location / directory
            destination.mkdir(exist_ok=True)
            target = destination / item.name

            if target.exists():
                print(f"Skipped {item.name}: already exists in {directory}")
                continue

            try:
                shutil.move(item, target)
                print(f"{item.name} moved to {directory}")
            except Exception as e:
                print(f"Skipped {item.name}: {e}")