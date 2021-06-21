FROM python:3.8.3
WORKDIR code/
COPY requirements.txt .
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 2001
CMD ["python3", "app.py"]
