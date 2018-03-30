import nltk


class ExtractWord:

    def remove_stopwords(sentence):
        content_words = []
        STOPWORDS = nltk.corpus.stopwords.words('english')
        for word in sentence.split():
            if word not in STOPWORDS:
                content_words.append(word)
        return ' '.join(content_words)

    def extract_keywords(headline):
        headline = headline.lower()
        content_headline = ExtractWord.remove_stopwords(headline)
        words = content_headline.split()

        calamity = ['floods', 'flooding', 'flood', 'flooded', 'flood-hit',
                    'droughts', 'volcanic', 'volcano', 'drought', 'cyclone-hit', 'cyclonic',
                    'earthquake',  'quake', 'earthquakes', 'quake-hit', 'landslides','mudslides',
                    'storm', 'landslide', 'hurricane', 'avalanches', 'mudslide', 'flood-like',
                    'avalanche', 'typhoon', 'typhoon-hit', 'snowstorm', 'snowstorms',  'wildfire', 'wildfires',
                    'disaster-hit', 'thunderstorms', 'thunderstorm', 'tornadoes',  'tornado']

        for (word) in words:
            l = len(word)-1
            if word[l] == '?' or word[l] == ',' or word[l] == '!' or word[l] == ';' or word[l] == ':' :
                word = word[:(l-1)]
                if word in calamity:
                    return 1
            else:
                if word in calamity:
                    return 1

        return 0
