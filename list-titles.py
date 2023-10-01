from savegame_banner import SavegameBanner
from pathlib import Path
import sys


def main(folder):
	pathlist = Path(folder).glob("*")
	for path in pathlist:
		banner = SavegameBanner.from_file(path / "banner.bin")

		print(f"{path.stem} - {banner.game_title} - {banner.game_subtitle}")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print(f"Usage: {sys.argv[0]} <path>")
	else:
		main(sys.argv[1])
