import json

def load_ground_truth(path='ground_truth.json'):
    with open(path) as f:
        return json.load(f)

def verify_claim(claim, ground_truth):
    # claim format: "key = value" or "key: value"
    for sep in ['=', ':']:
        if sep in claim:
            key, value = claim.split(sep, 1)
            key = key.strip().lower()
            value = value.strip()
            break
    else:
        return False, "No key-value separator found"
    
    if key in ground_truth:
        return ground_truth[key].lower() == value.lower(), f"Ground truth: {ground_truth[key]}"
    return False, f"Key '{key}' not found"

def main():
    gt = load_ground_truth()
    print("Fact Guard Demo — verify AI claims against ground truth")
    print("Ground truth:", gt)
    print()
    
    test_claims = [
        "capital = Paris",
        "population = 1400000",
        "language: French",
        "currency = Euro",
        "unknown_key = value"
    ]
    
    for claim in test_claims:
        is_correct, detail = verify_claim(claim, gt)
        status = "✓ CORRECT" if is_correct else "✗ WRONG / UNKNOWN"
        print(f"{claim:30} -> {status} | {detail}")

if __name__ == "__main__":
    main()
}

# Include a sample ground_truth.json creation if not exists
import os
if not os.path.exists('ground_truth.json'):
    sample = {
        "capital": "Paris",
        "population": "2100000",
        "language": "French",
        "currency": "Euro"
    }
    with open('ground_truth.json', 'w') as f:
        json.dump(sample, f, indent=2)
    print("Created sample ground_truth.json")