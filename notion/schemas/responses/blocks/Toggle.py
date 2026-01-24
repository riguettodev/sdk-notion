from ...dto import BaseModelSdk
from pydantic import ConfigDict
from ..properties.RichText import RichText as _RichText

class Toggle(BaseModelSdk):
    model_config = ConfigDict(title = "Notion_Responses_Blocks_Toggle")
    rich_text : _RichText
    color : str
