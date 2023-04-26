import sys

import pykakasi
from bs4 import BeautifulSoup

import models


def furiganise(file_path: str):
    furiganised_results = []
    furiganised_file_path = file_path.replace(".html", "_furiganised.html")
    with open(file_path, "r") as f:
        for line in f:
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
            furiganised_results.append(line)
    with open(furiganised_file_path, "w") as f:
        f.writelines(furiganised_results)


if __name__ == "__main__":
    file_paths = [
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0003.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0004.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0005.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0006.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0007.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0008.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0009.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0010.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0011.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0012.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0013.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0014.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0015.html",
        "/Users/javi.manzano/Downloads/majo no takkyuubin/text/part0016.html",
    ]
    for file_path in file_paths:
        furiganise(file_path)
