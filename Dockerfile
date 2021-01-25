FROM python:3.7-slim

COPY requirements.txt /app/
WORKDIR /app

RUN pip install --upgrade pip \
    &&  pip install --trusted-host pypi.python.org --requirement requirements.txt

COPY . /app

RUN python -m nltk.downloader vader_lexicon

CMD ["python", "Wallstreetbets.py"]