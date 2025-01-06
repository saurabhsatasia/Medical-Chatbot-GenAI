from dataclasses import dataclass
from typing import List

@dataclass
class ChatResponse:
    answer: str
    sources: List[str]