# ========================
# Core Function Words
# ========================
core_function_words = [
    'a', 'an', 'the', 'and', 'or', 'but', 'of', 'in', 'on', 'at', 
    'to', 'for', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 
    'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 
    'does', 'did', 'this', 'that', 'these', 'those', 'it', 'its', 
    'they', 'them', 'their', 'we', 'our', 'us'
]

# ========================
# Academic Verbs
# ========================
academic_verbs = [
    'propose', 'demonstrate', 'leverage', 'preserve', 'enable',
    'verify', 'capture', 'employ', 'exceed', 'transform', 'integrate',
    'outperform', 'enhance', 'exhibit', 'disrupt', 'bridge', 'utilize',
    'craft', 'pose', 'elicit', 'calibrate', 'align', 'convert', 
    'address', 'implement', 'analyze', 'investigate', 'explore'
]

academic_verbs = academic_verbs + [v + 's' for v in academic_verbs]  + [v[:-1] + v[-1].replace('e', '') + 'ed' for v in academic_verbs] + [v + 'ing' for v in academic_verbs]

# ========================
# Technical Nouns
# ========================


# ========================
# Academic Adjectives/Adverbs
# ========================
academic_modifiers = [
    'novel',
    'critical', 'persistent', 'sophisticated', 'concretely', 'crucially',
    'fundamentally', 'primarily', 'strategically', 'effectively', 'efficiently',
]

# ========================
# Connective Phrases
# ========================
connective_phrases = [
    'in contrast', 'based on', 'fall short', 'lead to', 'result in',
    'give rise to', 'stem from', 'pave the way for', 'bridge the gap',
    'open the door to', 'set the stage for', 'hold the key to'
]


# ========================
# Redundant Quantifiers 
# ========================
redundant_quantifiers = [
    'various', 'extensive', 'significant', 'substantial', 'critical',
    'persistent', 'sophisticated', 'multiple', 'diverse', 'numerous'
]

# ========================
# Full Combined List
# ========================
academic_stopwords = (
    core_function_words +
    academic_verbs +
    academic_modifiers +
    connective_phrases +
    redundant_quantifiers
)

# Remove duplicates while preserving order
academic_stopwords = set(academic_stopwords)