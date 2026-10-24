from pathlib
import Path 
import shutil
DOWNLOADS=Path.home() / "Downloads"
file_types={
  "Images":[.jpg,.jpeg,.png] 
  "Documents":[.pdf,.txt,.docx]
  "Videos":[.mp4,.mkv]
  "Music":[.mp3]
  "Code":[.py,.java,.html,.css,.c,.js]
}
def category(file):
    ext=suffix(file)
    for category,ext in file.items():
        if ext in ext:
            return cateogory