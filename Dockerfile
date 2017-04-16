############################################################
# Dockerfile to run a Django-based web application
# Based on an Ubuntu Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:14.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Emeline Gaulard

# Set env variables used in this Dockerfile (add a unique prefix, such as DJANGOAPP)
# Local directory with project source
ENV DJANGOAPP_SRC=~/eps/psychic-waffle
# Directory in container for all project files
ENV DJANGOAPP_SRVHOME=/srv
# Directory in container for project source files
ENV DJANGOAPP_SRVPROJ=/srv/psychic-waffle

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip

# Create application subdirectories
WORKDIR $DJANGOAPP_SRVHOME
RUN mkdir media static logs
VOLUME ["$DJANGOAPP_SRVHOME/media/", "$DJANGOAPP_SRVHOME/logs/"]

# Copy application source code to SRCDIR
COPY $DJANGOAPP_SRC $DJANGOAPP_SRVPROJ

# Install Python dependencies
RUN pip install -r $DJANGOAPP_SRVPROJ/requirements.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DJANGOAPP_SRVPROJ
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]