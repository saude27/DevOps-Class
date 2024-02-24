FROM python:alpine

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY requirement.txt .

RUN pip install --no-cache-dir --trusted-host pypi.python.org --use-pep517 -r requirement.txt

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 5000

CMD [ "./entrypoint.sh" ]