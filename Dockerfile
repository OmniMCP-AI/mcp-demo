FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Install uv
RUN pip install --upgrade pip \
    && pip install uv

# Create virtual environment with uv
RUN uv venv --python=python3.12

# Use uv to install dependencies (prefer requirements.txt if present, otherwise install fastmcp directly)
RUN if [ -f requirements.txt ]; then \
        uv pip install -r requirements.txt; \
    else \
        uv pip install fastmcp; \
    fi

EXPOSE 8000

CMD ["uv", "run", "server.py", "--transport", "stdio"] 