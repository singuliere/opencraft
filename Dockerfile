FROM python:3.5
EXPOSE 2001 2001
EXPOSE 5000 5000
EXPOSE 8888 8888
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&  \
    apt-get install -y postgresql-client libffi-dev   \
    libmysqlclient-dev libpq-dev subversion
RUN mkdir /opencraft
WORKDIR /opencraft
RUN python3 -m venv /venv
ADD requirements.txt .
RUN bash -c "source /venv/bin/activate && pip install -r requirements.txt"
