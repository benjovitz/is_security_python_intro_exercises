import hashlib
import itertools
import string

def sha1_cracker(target_hash):
    # Define the character set (lowercase letters only)
    chars = string.ascii_lowercase
    # Loop over all 4-letter combinations of the character set
    for combo in itertools.product(chars, repeat=4):
        # Join the combination into a string
        candidate = ''.join(combo)
        # Hash the candidate string using SHA-1
        hashed_candidate = hashlib.sha1(candidate.encode()).hexdigest()
        # Check if it matches the target hash
        if hashed_candidate == target_hash:
            return candidate
    return None

# Example usage
target_hash = 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'  # SHA-1 hash of "test"
cracked = sha1_cracker(target_hash)

if cracked:
    print(f"Hash cracked! The original string is: {cracked}")
else:
    print("Hash not found.")



