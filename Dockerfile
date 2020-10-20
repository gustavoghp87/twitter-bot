FROM python:3.7

COPY exercise/config.py /bots/
COPY exercise/favretweet.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "favretweet.py"]
