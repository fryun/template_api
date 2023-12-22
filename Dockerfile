FROM python:3.10.12-alpine

ENV PYTHONUNBUFFERED=1
ENV GIT_PYTHON_REFRESH=warning
	
# Install all python library requirements
COPY . /home
WORKDIR /home

RUN python3 -m pip install --no-cache-dir -r /home/requirements.txt

RUN chmod +x /home/startup.sh
ENTRYPOINT /home/startup.sh