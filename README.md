# Hack@Brown2018: The Retextualizationizer

### APIs used:
[Flask](http://flask.pocoo.org/docs/0.12/)

[jQuery](https://jquery.com/)

[Gensim](https://radimrehurek.com/gensim/)

[NLTK](http://www.nltk.org/)

[HTML5 Speech Recognition](https://dvcs.w3.org/hg/speech-api/raw-file/9a0075d25326/speechapi.html#dfn-resultIndex)

[PyPDF2](https://pythonhosted.org/PyPDF2/)

[Textract](https://textract.readthedocs.io/en/stable/)


We use Gensim and NLTK to implement natural language processing and machine learning in an easy-to-use tool. Specify your preferred summary target length and keyword count (in words), or use our default settings! Paste text directly, use the microphone for speech-to-text, or select a PDF. Note: Keywords may be stemmed.


##Backlog

1. Handle pdf formatting better: cleanly formatted pdfs are handled well, but more complex formatting can be a problem. Also, in scientific papers the program sometimes get sentences from the references section, so in future we would trim out the reference section.
2. One idea we started with but did not implement was to link sentences in summary back to text so that users can learn more about that topic quickly, making is easy to use quotes/pinpoint lines
3. For now, we return stemmed keywords. We need to stem them so that inflected/derived words are reduced to base meanings, but the resulting words are sometimes not actual words. We would eventually handle this so that we return actual words.