#!/usr/bin/env bash

# Stop immediately if anything goes wrong.
set -euo pipefail

# Switch to the tool chain's venv.
source .venv-convert/bin/activate

python -m tf2onnx.convert \
    --saved-model models/trained_model_tf \
    --output models/trained_model.onnx
