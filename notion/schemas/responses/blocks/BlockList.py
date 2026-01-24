from ...dto import BaseModelSdk
from typing import Optional, List, Any, Union
from pydantic import ConfigDict, Field
from .Block import Block as _Block

class BlockList(BaseModelSdk):
    model_config = ConfigDict(title = "Notion_Responses_Blocks_BlockList")
    results: List[Union[_Block, Any]]
    next_cursor: Optional[str] = None
    has_more: bool
    type: str = "block"
    block: dict
