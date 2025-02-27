import sys
from _typeshed import ReadOnlyBuffer, StrOrBytesPath
from types import TracebackType
from typing import TypeVar, overload
from typing_extensions import Self, TypeAlias

if sys.platform != "win32":
    _T = TypeVar("_T")
    _KeyType: TypeAlias = str | ReadOnlyBuffer
    _ValueType: TypeAlias = str | ReadOnlyBuffer

    open_flags: str

    class error(OSError): ...
    # Actual typename gdbm, not exposed by the implementation
    class _gdbm:
        def firstkey(self) -> bytes | None: ...
        def nextkey(self, key: _KeyType) -> bytes | None: ...
        def reorganize(self) -> None: ...
        def sync(self) -> None: ...
        def close(self) -> None: ...
        if sys.version_info >= (3, 13):
            def clear(self) -> None: ...

        def __getitem__(self, item: _KeyType) -> bytes: ...
        def __setitem__(self, key: _KeyType, value: _ValueType) -> None: ...
        def __delitem__(self, key: _KeyType) -> None: ...
        def __contains__(self, key: _KeyType) -> bool: ...
        def __len__(self) -> int: ...
        def __enter__(self) -> Self: ...
        def __exit__(
            self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
        ) -> None: ...
        @overload
        def get(self, k: _KeyType) -> bytes | None: ...
        @overload
        def get(self, k: _KeyType, default: _T) -> bytes | _T: ...
        def keys(self) -> list[bytes]: ...
        def setdefault(self, k: _KeyType, default: _ValueType = ...) -> bytes: ...
        # Don't exist at runtime
        __new__: None  # type: ignore[assignment]
        __init__: None  # type: ignore[assignment]

    if sys.version_info >= (3, 11):
        def open(filename: StrOrBytesPath, flags: str = "r", mode: int = 0o666, /) -> _gdbm: ...
    else:
        def open(filename: str, flags: str = "r", mode: int = 0o666, /) -> _gdbm: ...
