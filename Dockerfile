FROM python:3.9-bullseye

WORKDIR /project

COPY requirements.txt /project
COPY dev-requirements.txt /project

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r dev-requirements.txt

COPY pyproject.toml /project
COPY setup.py /project
COPY tests/ /project/tests
COPY inventory_report/ /project/inventory_report

RUN python3 -m pip install .
