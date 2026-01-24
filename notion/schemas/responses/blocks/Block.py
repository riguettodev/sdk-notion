from ...dto import BaseModelSdk
from pydantic import ConfigDict
from typing   import Any, Union, Literal
from datetime import datetime
from ..users.User import User as _User
from ..misc.Parent import Parent  as _Parent
from .Toggle import Toggle as _Toggle

class Block(BaseModelSdk):
    model_config = ConfigDict(title = "Notion_Responses_Blocks_List")
    object: str
    id: str
    parent: _Parent
    created_time: datetime
    last_edited_time: datetime
    created_by: _User
    last_edited_by: _User
    has_children: bool
    archived: bool
    in_trash: bool
    type: Literal[
        "toggle"
    ]
    block : Union[Any,
        _Toggle
    ]
