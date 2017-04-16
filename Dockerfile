# Dockerfile

# FROM directive instructing base image to build upon
FROM python:2-onbuild

# Set the file maintainer (your name - the file's author)
MAINTAINER Emeline Gaulard

# COPY startup script into known file location in container
COPY docker-entrypoint.sh /docker-entrypoint.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["/docker-entrypoint.sh"]
# done!
