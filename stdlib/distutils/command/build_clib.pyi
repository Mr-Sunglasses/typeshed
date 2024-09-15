from _typeshed import Unused
from collections.abc import Callable
from typing import Any, ClassVar

from ..cmd import Command

def show_compilers() -> None: ...

class build_clib(Command):
    description: str
    user_options: ClassVar[list[tuple[str, str, str]]]
    boolean_options: ClassVar[list[str]]
    help_options: ClassVar[list[tuple[str, str | None, str, Callable[[], Unused]]]]
    build_clib: Any
    build_temp: Any
    libraries: Any
    include_dirs: Any
    define: Any
    undef: Any
    debug: Any
    force: int
    compiler: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_library_list(self, libraries) -> None: ...
    def get_library_names(self): ...
    def get_source_files(self): ...
    def build_libraries(self, libraries) -> None: ...
