"""Core RRF Fusion implementation."""
from typing import Dict, List, Tuple

class ScoredDocument:
    def __init__(self, doc_id: str, content: str, score: float):
        self.doc_id = doc_id
        self.content = content
        self.score = score

class RRFFusionEngine:
    @staticmethod
    def fuse(dense_ranks: List[str], sparse_ranks: List[str], k: int = 60) -> List[Tuple[str, float]]:
        rrf_scores: Dict[str, float] = {}

        for rank, doc_id in enumerate(dense_ranks, 1):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (k + rank))

        for rank, doc_id in enumerate(sparse_ranks, 1):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + (1.0 / (k + rank))

        sorted_docs = sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True)
        return [(doc_id, round(score, 6)) for doc_id, score in sorted_docs]
