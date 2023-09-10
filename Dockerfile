FROM python:3.10.12-slim
WORKDIR fastapi-otel
COPY . .
RUN pip install -r requirements.txt
#RUN source venv/bin/activate
EXPOSE 8000
RUN ls
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]