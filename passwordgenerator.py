def collect_words():
    """Collect words from user input until 'done' is entered."""
    words = []
    print("Enter words one at a time. Type 'done' when finished.")
    while True:
        word = input("Enter a word (or 'done' to finish): ").strip()
        if word.lower() == "done":
            break
        if word:  # Only add non-empty words
            words.append(word)
    return words

def generate_wordlist(words, filename="wordlist.txt"):
    """Generate password combinations and write them directly to file."""
    with open(filename, "w") as f:
        count = 0
        
        # Store base combinations to use later
        base_combinations = set()
        
        # Write original words
        for word in words:
            f.write(word + "\n")
            base_combinations.add(word)
            count += 1
        
        # Write capitalized words
        for word in words:
            capitalized = word.capitalize()
            if capitalized != word:  # Avoid duplicates
                f.write(capitalized + "\n")
                base_combinations.add(capitalized)
                count += 1
        
        # Write two-word combinations
        print("Generating two-word combinations...")
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:  # Avoid combining a word with itself
                    combo1 = words[i] + words[j]
                    combo2 = words[i].capitalize() + words[j]
                    combo3 = words[i] + words[j].capitalize()
                    combo4 = words[i].capitalize() + words[j].capitalize()
                    
                    f.write(combo1 + "\n")
                    f.write(combo2 + "\n")
                    f.write(combo3 + "\n")
                    f.write(combo4 + "\n")
                    base_combinations.add(combo1)
                    base_combinations.add(combo2)
                    base_combinations.add(combo3)
                    base_combinations.add(combo4)
                    count += 4
        
        print(f"Generated {count} basic word combinations. Adding variations...")
        
        # Generate additional related words
        common_prefixes = ["super", "ultra", "mega", "cyber", "my", "the", "best", "top"]
        common_suffixes = ["123", "xyz", "man", "girl", "fan", "master", "king", "queen"]
        common_symbols = ["!", "@", "#", "$", "%", "*"]
        
        # Add variations with prefixes, suffixes and symbols
        for word in words:
            # Add prefix variations
            for prefix in common_prefixes:
                variation1 = prefix + word
                variation2 = prefix + word.capitalize()
                f.write(variation1 + "\n")
                f.write(variation2 + "\n")
                base_combinations.add(variation1)
                base_combinations.add(variation2)
                count += 2
            
            # Add suffix variations
            for suffix in common_suffixes:
                variation1 = word + suffix
                variation2 = word.capitalize() + suffix
                f.write(variation1 + "\n")
                f.write(variation2 + "\n")
                base_combinations.add(variation1)
                base_combinations.add(variation2)
                count += 2
            
            # Add symbol variations
            for symbol in common_symbols:
                variation1 = word + symbol
                variation2 = word.capitalize() + symbol
                f.write(variation1 + "\n")
                f.write(variation2 + "\n")
                base_combinations.add(variation1)
                base_combinations.add(variation2)
                count += 2
        
        print(f"Generated {count} word variations. Adding numbers...")
        
        # Convert to list for easier iteration
        base_combinations = list(base_combinations)
        
        # Add years after 1900
        print("Adding years 1900-2025...")
        for combo in base_combinations:
            for year in range(1900, 2026):
                f.write(f"{combo}{year}\n")
                count += 1
        
        # Add numbers 0-9999
        print("Adding numbers 0-9999 to all combinations...")
        for combo in base_combinations:
            # Single digits (0-9)
            for num in range(10):
                f.write(f"{combo}{num}\n")
                count += 1
            
            # Double digits (10-99)
            for num in range(10, 100):
                f.write(f"{combo}{num:02d}\n")  # Zero-padded
                count += 1
            
            # Triple digits (100-999)
            for num in range(100, 1000):
                f.write(f"{combo}{num:03d}\n")
                count += 1

def main():
    words = collect_words()
    if not words:
        print("No words provided. Exiting.")
        return
    
    print(f"Collected {len(words)} words. Generating wordlist...")
    generate_wordlist(words)

if __name__ == "__main__":
    import os
    main()