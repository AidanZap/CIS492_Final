# imports
from keybert import KeyBERT
import nltk
from nltk.stem import WordNetLemmatizer

# list of keywords to exclude
stopwords = set(['', 'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'])
removed_words = set(["episode", "episodes", "movie", "show", "TV", "film", "films"])

# KeyBERT keyword extraction model object
n_gram_range = (1, 1)
stop_words = stopwords # 'english'
top_n = 10
# MMR (Maximal Marginal Relevance)
# diversity of 0.8 may result in lower confidence but more diverse words
use_mmr = True
kb_diversity = 0.3
kw_model = KeyBERT()
nltk.download('wordnet')
nltk.download('omw-1.4')

def kw_cleanup(text):
    # Tokenize
    tokens = text.split(" ")
    # Remove Stopwords
    tokens = [tok for tok in tokens if tok not in stop_words]
    # Stem
    ls = WordNetLemmatizer()
    tokens = [ls.lemmatize(tok) for tok in tokens]
    return ' '.join(tokens)

def keybert_extraction(summary: str):

    summary_keywords = kw_model.extract_keywords(
        docs=summary, 
        keyphrase_ngram_range=n_gram_range, 
        stop_words=stop_words, 
        top_n=top_n,
        use_mmr=use_mmr,
        diversity=kb_diversity)

    # For keyBERT, we do 1 - x[1] in the sort method since highest confidence value is best
    keywords = summary_keywords
    keywords.sort(key = lambda x: 1 - x[1])
    return keywords


def derive_keywords(summary: str):
    summary = summary.lower()
    summary = kw_cleanup(summary)
    keybert_keywords = keybert_extraction(summary)
    return list(set(keybert_keywords))


def get_keywords(text: str):
    # use NLP to generate keywords
    generated_keywords = derive_keywords(text.replace('\n', ''))
    return [word[0] for word in generated_keywords if word[0] not in removed_words]