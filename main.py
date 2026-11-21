import os
import shutil
from pathlib import Path

def main():
    script_dir = Path(__file__).parent.resolve()
    src_file = script_dir / "art.jpg"
    out_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = Path(out_dir_str)
    out_dir.mkdir(parents=True, exist_ok=True)
    dst_file = out_dir / "entry.png"

    shutil.copyfile(src_file, dst_file)


if __name__ == "__main__":
    main()
