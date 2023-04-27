import os
import sys

import pykakasi
from bs4 import BeautifulSoup

import models


def furiganise(input_path: str):
    """
    Go through every file in the given path and furiganise each of them.
    """
    print(f"Furiganising files in {input_path}")
    for file_path in os.listdir(input_path):
        _furiganise_file(os.path.join(input_path, file_path))


def _furiganise_file(file_path: str):
    print(f"Furiganising {file_path}")
    furiganised_results = []
    with open(file_path, "r") as f:
        furiganised_results = [_furiganise_line(line) for line in f]

    # Write the furiganised file in the right directory.
    with open(file_path.replace("original", "text"), "w") as f:
        f.writelines(furiganised_results)


def _furiganise_line(line: str) -> str:
    soup = BeautifulSoup(line, "html.parser")
    if tag := soup.find("p"):
        contents = tag.get_text()
        result = models.KakasiResult(
            text=contents,
            result=pykakasi.kakasi().convert(contents),
        )

        # FIXME - this is super hacky, but I can't be bothered with BeautifulSoup right now
        if "id" in tag.attrs:
            id_value = tag.attrs["id"]
            id_attr = f'id="{id_value}" '
        else:
            id_attr = ""
        if "class" in tag.attrs:
            class_value = " ".join(tag.attrs["class"])
            class_attr = f'class="{class_value}" '
        else:
            class_attr = ""

        line = f"<p {id_attr}{class_attr}>{result.get_html()}</p>\n"
    return line


if __name__ == "__main__":
    furiganise(sys.argv[1])
