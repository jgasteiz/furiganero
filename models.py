import pydantic


class KakasiResult(pydantic.BaseModel):
    text: str
    result: list[dict[str, str]]

    def get_html(self) -> str:
        html = ""
        for item in self.result:
            # If the original matches the hiragana
            if self._original(item) == self._hiragana(item) or self._original(
                item
            ) == self._katakana(item):
                html = f"{html}{self._original(item)}"
            else:
                html = f"{html}<ruby>{self._original(item)}<rt>{self._hiragana(item)}</rt></ruby>"
        return html

    def _original(self, item: dict[str, str]) -> str:
        return item["orig"]

    def _hiragana(self, item: dict[str, str]) -> str:
        return item["hira"]

    def _katakana(self, item: dict[str, str]) -> str:
        return item["kana"]
