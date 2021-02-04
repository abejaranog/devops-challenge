FROM python:3.7-slim
RUN python3 -m venv /opt/.venv
WORKDIR /opt/myapp
RUN /opt/.venv/bin/pip install --upgrade pip
COPY ./src/requirements.txt ./requirements/requirements.txt
COPY ./src/app.py ./app.py
RUN /opt/.venv/bin/pip install -r /opt/myapp/requirements/requirements.txt
CMD ["/opt/.venv/bin/python3", "/opt/myapp/app.py"]