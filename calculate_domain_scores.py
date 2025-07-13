import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('/Users/sienn/Desktop/1/Nepal-Grid view.csv')

# Define the domains and their corresponding question columns
domains = {
    'Satisfaction with Life & Affect': {
        'questions': ['(1) Score', '(2) Score', '(3) Score', '(4) Score', '(5) Score'],
        'name': 'Domain 1: Satisfaction with Life & Affect'
    },
    'Psychological Well-being': {
        'questions': ['(6) Score', '(7) Score', '(8) Score', '(9) Score', '(10) Score'],
        'name': 'Domain 2: Psychological Well-being'
    },
    'Health': {
        'questions': ['(11) Score', '(12) Score', '(13) Score', '(14) Score'],
        'name': 'Domain 3: Health'
    },
    'Time Balance': {
        'questions': ['(15) Score', '(16) Score', '(17) Score'],
        'name': 'Domain 4: Time Balance'
    },
    'Community': {
        'questions': ['(18) Score', '(19) Score', '(20) Score', '(21) Score', '(22) Score', '(23) Score', '(24) Score'],
        'name': 'Domain 5: Community'
    },
    'Social Support': {
        'questions': ['(25) Score', '(26) Score', '(27) Score', '(28) Score'],
        'name': 'Domain 6: Social Support'
    },
    'Lifelong Learning, Arts & Culture': {
        'questions': ['(29) Score', '(30) Score', '(31) Score', '(32) Score'],
        'name': 'Domain 7: Lifelong Learning, Arts & Culture'
    },
    'Environment': {
        'questions': ['(33) Score', '(34) Score', '(35) Score', '(36) Score'],
        'name': 'Domain 8: Environment'
    },
    'Government': {
        'questions': ['(37) Score', '(38) Score', '(39) Score', '(40) Score'],
        'name': 'Domain 9: Government'
    },
    'Standard of Living / Economy': {
        'questions': ['(41) Score', '(42) Score', '(43) Score', '(44) Score'],
        'name': 'Domain 10: Standard of Living / Economy'
    },
    'Work': {
        'questions': ['(45) Score', '(46) Score', '(47) Score', '(48) Score', '(49) Score', '(50) Score'],
        'name': 'Domain 11: Work'
    },
    'Tourism': {
        'questions': ['(51) Score', '(52) Score', '(53) Score', '(54) Score', '(55) Score', '(56) Score'],
        'name': 'Domain 12: Tourism'
    }
}

# Function to convert percentage strings to numeric values
def convert_to_numeric(value):
    if pd.isna(value):
        return np.nan
    if isinstance(value, str) and '%' in value:
        return float(value.strip('%'))
    try:
        return float(value)
    except:
        return np.nan

# Calculate domain scores
print("Nepal Dashboard - Domain Scores Calculation for 2025")
print("=" * 70)
print()

domain_results = {}

for domain_key, domain_info in domains.items():
    print(f"\n{domain_info['name']}")
    print("-" * 50)
    
    # Extract scores for this domain
    domain_scores = []
    
    for q in domain_info['questions']:
        if q in df.columns:
            # Convert column to numeric, handling percentage strings
            numeric_col = df[q].apply(convert_to_numeric)
            # Filter out NaN values
            valid_scores = numeric_col.dropna()
            if len(valid_scores) > 0:
                domain_scores.extend(valid_scores.tolist())
                print(f"  {q}: {len(valid_scores)} valid responses")
        else:
            print(f"  {q}: Column not found")
    
    if domain_scores:
        # Calculate average score
        avg_score = np.mean(domain_scores)
        domain_results[domain_info['name']] = avg_score
        print(f"\n  Average Score: {avg_score:.1f}%")
        print(f"  Number of responses used: {len(domain_scores)}")
    else:
        print(f"\n  No valid scores found for this domain")

# Summary of all domain scores
print("\n" + "=" * 70)
print("SUMMARY - All Domain Scores for 2025")
print("=" * 70)

for domain_name, score in domain_results.items():
    print(f"{domain_name}: {score:.1f}%")

# Calculate overall average
if domain_results:
    overall_avg = np.mean(list(domain_results.values()))
    print(f"\nOverall Average across all domains: {overall_avg:.1f}%")

# Check for existing domain average columns in the CSV
print("\n" + "=" * 70)
print("Comparison with Existing Domain Averages in CSV")
print("=" * 70)

existing_domain_cols = {
    'Satisfaction with Life & Affect (feelings) (1-5) - Total': 'Domain 1',
    'Psychological Well-being/Flourishing (6-10) - Average': 'Domain 2',
    'Health (11-14) - Total Average': 'Domain 3',
    'Time Balance (15-17) - Total Average': 'Domain 4',
    'Community (18-24) - Total Average': 'Domain 5',
    'Social Support (25-28) - Total Average': 'Domain 6',
    'Lifelong Learning, Arts & Culture (29-32) - Total Average': 'Domain 7',
    'Environment (33-36) - Total Average': 'Domain 8',
    'Government (37-40) - Total Average': 'Domain 9',
    'Standard of Living / Economy (41-44) - Total Average': 'Domain 10',
    'Work (45-50) - Total Average': 'Domain 11',
    'Tourism (51-56) - Total Average': 'Domain 12'
}

print("\nChecking for existing calculated averages in the CSV:")
for col_name, domain_label in existing_domain_cols.items():
    if col_name in df.columns:
        existing_vals = df[col_name].apply(convert_to_numeric).dropna()
        if len(existing_vals) > 0:
            avg_existing = np.mean(existing_vals)
            print(f"\n{domain_label} - {col_name}:")
            print(f"  Average of existing calculations: {avg_existing:.1f}%")