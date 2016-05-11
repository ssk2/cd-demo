FROM python:2.7
RUN pip install yahoo-finance Flask requests
ADD project /var/site
CMD python /var/site/app.py