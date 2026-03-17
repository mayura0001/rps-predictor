# Rock Paper Scissors Predictor AI

An RPS predictor built entirely by Mayura Jayasinghe, as part of the
[freeCodeCamp Machine Learning with Python](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors) project.

---

## Overview

This project trains a machine learning model to predict opponent moves in
Rock Paper Scissors using historical play data.

---

## Tech Stack

| Library | Purpose |
|---|---|
| TensorFlow | Train the ML prediction model |
| Pandas | Data collection and preparation |

**`datacollector.py`** — Collects move data from opponent bots to build the training dataset.

---

## Docker Setup

Docker is used here to manage Python ML library dependencies in an isolated
environment — and as a learning exercise for containerized workflows.

> **Note:** The libraries also work fine without Docker, so the Docker setup
> is entirely optional.

### Commands
```bash
# Build the image from Dockerfile
docker build -t rps-ml-model .

# Force a clean rebuild from scratch (ignores cache)
docker build --no-cache -t rps-ml-model .

# Run the container, mounting your local project files
docker run -it -v "$(pwd)":/app rps-ml-model
```

> The `-v "$(pwd)":/app` flag mounts your current directory into the
> container, so any file changes you make locally are reflected immediately
> without needing to rebuild the image.