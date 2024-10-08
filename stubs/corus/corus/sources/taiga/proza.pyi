from _typeshed import Incomplete

__all__ = ["load_taiga_proza_metas", "load_taiga_proza", "load_taiga_stihi_metas", "load_taiga_stihi"]

def load_taiga_proza_metas(path, offset: int = 0, count=13): ...
def load_taiga_stihi_metas(path, offset: int = 0, count=3): ...
def load_taiga_proza(path, metas: Incomplete | None = None, offset: int = ..., count: int = ...): ...
def load_taiga_stihi(path, metas: Incomplete | None = None, offset: int = ..., count: int = ...): ...
