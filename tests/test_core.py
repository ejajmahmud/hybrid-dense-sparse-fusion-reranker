"""Tests for RRFFusionEngine."""
import unittest
from hybrid_dense_sparse_fusion_reranker.core import RRFFusionEngine

class TestRRFFusionEngine(unittest.TestCase):
    def test_rrf_scoring(self):
        dense = ["A", "B", "C"]
        sparse = ["B", "A", "D"]

        fused = RRFFusionEngine.fuse(dense, sparse)
        # B and A appear in both, so should beat C and D
        top_two = [doc for doc, _ in fused[:2]]
        self.assertIn("A", top_two)
        self.assertIn("B", top_two)
