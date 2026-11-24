"""CLI for RRF Fusion Re-Ranker."""
import argparse
from .core import RRFFusionEngine

def main():
    parser = argparse.ArgumentParser(description="Hybrid Dense-Sparse Fusion Re-Ranker CLI")
    parser.add_argument("--demo", action="store_true", help="Run RRF demo")
    args = parser.parse_args()

    dense_results = ["doc-auth", "doc-database", "doc-ui"]
    sparse_results = ["doc-api-v2", "doc-auth", "doc-readme"]

    fused = RRFFusionEngine.fuse(dense_results, sparse_results)
    print("Fused Ranking (Top-K):")
    for doc_id, score in fused:
        print(f"  {doc_id}: RRF Score = {score}")

if __name__ == "__main__":
    main()
