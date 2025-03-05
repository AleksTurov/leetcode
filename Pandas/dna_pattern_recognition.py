import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = samples['dna_sequence'].apply(lambda x: 1 if x[:3] == 'ATG' else 0)
    samples['has_stop'] = samples['dna_sequence'].apply(lambda x: 1 if x[-3:] in ['TAA', 'TAG', 'TGA'] else 0)
    samples['has_atat'] = samples['dna_sequence'].apply(lambda x: 1 if 'ATAT' in x else 0)
    samples['has_ggg'] = samples['dna_sequence'].apply(lambda x: 1 if 'GGG' in x else 0)
    return samples


# Create a sample DataFrame
data = {
    'sample_id': [1, 2, 3, 4, 5, 6, 7],
    'dna_sequence': ['ATGCTAGCTAGCTAA', 'GGGTCAATCATC', 'ATATATCGTAGCTA', 'ATGGGGTCATCATAA', 'TCAGTCAGTCAG', 'ATATCGCGCTAG', 'CGTATGCGTCGTA'],
    'species': ['Human', 'Human', 'Human', 'Mouse', 'Mouse', 'Zebrafish', 'Zebrafish']
}

samples = pd.DataFrame(data)

print(analyze_dna_patterns(samples))
