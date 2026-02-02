# MathSketch

MathSketch is a lightweight, cloud‑deployed digit recognition service. It was originally built as a learning and exploration project around **ML‑assisted math tooling**, with an emphasis on *clean dependency boundaries*, *reproducibility*, and *fast iteration*.

The project deliberately separates **model development and conversion** from **runtime serving**, so the deployed system stays small, stable, and predictable.

---

## High‑level architecture

MathSketch is split into three distinct dependency environments:

1. **Runtime (API / serving)**
   What actually runs in production. No TensorFlow.

2. **Training / Conversion**
   Offline environment for training and converting models (TensorFlow → ONNX).

3. **Tooling**
   Developer tools used to manage dependencies (e.g. pip‑tools).

This separation is intentional and enforced.

---

## Dependency philosophy

The project follows a strict **intent vs artifact** model:

* `*.in` files express **human intent** (allowed version ranges).
* `*.txt` files are **machine‑generated lockfiles** (fully pinned, reproducible).

You install from `*.txt`. You edit `*.in`. You never hand‑edit lockfiles.

---

## Repository layout

```
mathsketch/
├─ requirements/
│  ├─ runtime.in        # Runtime dependency intent (no TensorFlow)
│  ├─ runtime.txt       # Runtime lockfile (used for dev + deploy)
│  ├─ train.in          # Model training/conversion intent (TensorFlow, tf2onnx)
│  ├─ train.txt         # Frozen training/conversion lockfile
│  └─ tools.txt         # Tooling dependencies (pip-tools, pip version)
│
├─ mathsketch/          # FastAPI application code
├─ models/              # Keras/TF models and ONNX models used at runtime
├─ static/              # HTML/CSS/JavaScript static files
├─ tools/               # Training/conversion scripts
├─ Dockerfile           # Deployment image-building process
├─ README.md
└─ ...
```

---

## Runtime environment (API)

`.venv-runtime`

The runtime environment is intentionally minimal:

* FastAPI
* ONNX Runtime
* Pillow
* psycopg2-binary
* SQLAlchemy
* Uvicorn

TensorFlow is **never** installed in this environment — not in dev, not in prod.

### Install runtime deps

```bash
pip install -r requirements/runtime.txt
```

This is the environment used for:

* Local API development
* CI
* Deployment (fly.io)

---

## Model training/conversion environment

`.venv-train`

TensorFlow is used **only** for model authoring and conversion.

### Install training/conversion deps

**CPU Only:**

```bash
pip install -r requirements/train_CPU.txt
```

**GPU:**

```bash
pip install -r requirements/train_GPU.txt
```

This environment is:

* Offline / local
* Rarely changed
* Treated as a known‑good artifact

The resulting ONNX models are what get checked in and served.

---

## Tools environment

`.venv-tools`

Dependencies are locked using **pip‑tools**.

### Tooling setup

1. Downgrade pip

```bash
pip install "pip<26"
```

2. Install tools

```bash
pip install -r requirements/tools.txt
```

> Note: `pip` is soft‑pinned here to avoid known incompatibilities with pip‑tools.

### Compile lockfiles

```bash
pip-compile requirements/runtime.in
pip-compile requirements/train_CPU.in
pip-compile requirements/train_GPU.in
```

### Update dependencies (intentional)

```bash
pip-compile --upgrade requirements/runtime.in
```

Lockfiles should only change via `pip-compile`.

---

## Development workflow

1. Install runtime deps
2. Run the FastAPI app locally
3. (Optional) Switch to conversion env to update models
4. Commit ONNX artifacts, not TensorFlow models

This keeps dev and prod behavior aligned.

---

## Deployment

Deployment uses the **runtime lockfile only**.

* No TensorFlow wheels
* Small image size
* Fast cold starts

The deployed system is deterministic and reproducible.

---

## Design principles

* Separation of concerns
* Deterministic builds
* Explicit dependency boundaries
* Minimal production surface area
* Reproducibility over novelty

---

## Status

This project is stable and primarily maintained as:

* A reference architecture
* A portfolio artifact
* A testbed for clean ML‑adjacent workflows

---

## License

All Rights Reserved
