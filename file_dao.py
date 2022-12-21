import os
from typing import TextIO
from constants import DATA_DIR
# ---------------------------------------------------------------------------


class FileDao:

    def __init__(self) -> None:

        self._filename = None
        self._file: TextIO = None

    def add_filename(self, filename: str) -> None:

        self._filename = os.path.join(DATA_DIR, filename)

    def open(self) -> TextIO:

        if self._file is not None and not self._file.closed:
            self._close()

        fin = open(self._filename, encoding='utf-8')
        self._file = fin

        return fin

    def _close(self) -> None:

        self._file.close()

    def __repr__(self) -> str:

        return f"FileDao({self._filename})"

    def __del__(self) -> None:

        if self._file is not None:
            self._close()
