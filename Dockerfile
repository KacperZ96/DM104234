FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_DEBUG=True
EXPOSE 5000
ENTRYPOINT ["flask"]
CMD ["run", "--host","0.0.0.0" ]
