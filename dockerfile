FROM python:3

ADD displayCsv.py /
ADD test.csv /
ADD requirements.txt /
RUN pip install -r requirements.txt

CMD [ "python", "./displayCsv.py" ]