FROM python:slim-buster AS base

# Set environmental variable
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

RUN apt-get update
# Install pipenv to manage dependencies
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Assistant/Pipfile .
# Installation of packages useful to build pyAudio
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN apt-get -y install portaudio19-dev

# Install of the packages
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --skip-lock

FROM base AS runtime

# Install packages to run pyAudio
# --- 2nd install because with multi-stage the package is not shared
RUN apt-get update
RUN apt-get -y install portaudio19-dev

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

WORKDIR /home/dist

# Install application into container
COPY ./Assistant /home/dist

EXPOSE 8080

# Run the application
ENTRYPOINT ["python", "advanced.main.py"]