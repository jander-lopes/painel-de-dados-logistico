from typing import Generic, TypeVar

from attr import dataclass

T = TypeVar('T')

@dataclass
class RespostaEstagios(Generic[T]):
    sucesso: T
    erro: T
