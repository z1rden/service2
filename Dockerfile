FROM python:3.9

COPY ./requirements.txt .
COPY ./blueprint ./blueprint

RUN pip install --user -r requirements.txt
EXPOSE 8000

CMD ["python", "-m", "blueprint"]