from transformers import pipeline
from difflib import SequenceMatcher, ndiff

# Grammar correction model
grammar_corrector = pipeline(
    "text2text-generation",
    model="vennify/t5-base-grammar-correction"
)

def calculate_score(original: str, corrected: str) -> float:
    """Improved scoring based on similarity and error density."""
    similarity = SequenceMatcher(None, original, corrected).ratio()
    
    original_words = original.split()
    corrected_words = corrected.split()
    
    changes = sum(1 for o, c in zip(original_words, corrected_words) if o != c)
    error_density = changes / max(len(original_words), 1)
    
    # Combine similarity and error impact
    base_score = similarity * 10
    penalty = error_density * 3  # Tweak this value as needed
    final_score = max(0, base_score - penalty)
    
    return round(final_score, 1)

def score_grammar(text: str):
    """Scores grammar correctness and returns score, corrected sentence, and highlights."""
    if not text.strip():
        return 0.0, "", {}
    
    corrected = grammar_corrector(f"grammar: {text}", max_length=128)[0]["generated_text"]
    score = calculate_score(text, corrected)
    highlights = highlight_errors(text, corrected)
    
    return score, corrected, highlights

def highlight_errors(original: str, corrected: str) -> str:
    """Highlight differences between original and corrected text."""
    diff = ndiff(original.split(), corrected.split())
    result = []
    for word in diff:
        if word.startswith('- '):
            result.append(f'<span style="color:red">{word[2:]}</span>')
        elif word.startswith('+ '):
            result.append(f'<span style="color:green">{word[2:]}</span>')
        else:
            result.append(word[2:])
    return ' '.join(result)
