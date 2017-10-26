FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip3 install -r /src/requirements.txt
ADD . /src/
CMD ["python3", "/src/manage.py", "migrate"]