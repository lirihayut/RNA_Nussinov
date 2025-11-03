from src.rna_sequence import RNASequence
from src.nussinov_dp import NussinovDP

def main():
    print("==== RNA Folding with Nussinov-Jacobson Algorithm ====\n")

    # Get RNA sequence from user
    seq = input("Enter RNA sequence (A,U,G,C only): ").upper()
    rna_seq = RNASequence(seq)

    # Run Nussinov-Jacobson algorithm
    nussinov = NussinovDP(rna_seq)
    nussinov.fill_matrix()
    structure = nussinov.get_structure()
    max_pairs = nussinov.get_max_pairs()

    # Print results
    print("\n--- Results ---")
    print(f"RNA Sequence:        {seq}")
    print(f"Predicted Structure: {structure}")
    print(f"Max Base Pairs:      {max_pairs}")

if __name__ == "__main__":
    main()
