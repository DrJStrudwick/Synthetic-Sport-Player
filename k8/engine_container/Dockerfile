FROM python:3.8.0
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
WORKDIR code/
COPY requirements.txt .
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 2001
CMD ["python", "app.py"]
