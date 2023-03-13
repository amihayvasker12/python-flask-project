FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
#RUN pip uninstall jinja2
#RUN pip install jinja2
#RUN pip install --upgrade jinja2
RUN pip install Flask==2.0.3
RUN pip install Jinja2==3.1.1
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

