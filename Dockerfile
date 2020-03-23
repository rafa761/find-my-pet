FROM postgres:12.2-alpine as database

# Inform Docker that the container listens on the specified network ports at runtime (HOST:CONTAINER)
EXPOSE 5432
