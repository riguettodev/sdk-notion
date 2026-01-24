from .Block     import Block     as _Block
from .BlockList import BlockList as _BlockList
from .Toggle    import Toggle    as _Toggle

class Schemas:

    Block     = _Block
    BlockList = _BlockList
    Toggle    = _Toggle

__all__ = ["Schemas"]