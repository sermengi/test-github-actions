FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir streamlit numpy joblib pathlib scikit-learn

COPY app/* .
RUN mkdir -p model/ && cd model/ && mv ../model.joblib .

EXPOSE 8501

CMD ["streamlit", "run", "wine_quality_UI.py"]
