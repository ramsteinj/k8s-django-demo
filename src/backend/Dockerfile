# Create container
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/log/containers
RUN mkdir /backend
WORKDIR /backend
COPY ./backend /backend/

# DO NOT DECLARE environment variables here.
# All environment variables should be declared in kubernetes ConfigMap.
#RUN export DEBUG="True"

# Install python pakcages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install and manage system packages as below if needed
#RUN apt-get update
#RUN apt-get install -y fonts-noto-cjk

# Start this container
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
CMD ["/backend/docker-entrypoint.sh"]