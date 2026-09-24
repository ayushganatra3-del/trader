"""Optional Kronos forecasting (https://github.com/shiyu-coder/Kronos, MIT).

The model code is vendored in ``agent.kronos.model``; it needs the extra
packages in ``requirements-kronos.txt`` (torch, einops, huggingface_hub,
safetensors, tqdm). Importing this package does not import torch.
"""
from .forecaster import (
    KronosForecaster,
    KronosUnavailable,
    forecasts_as_series,
    kronos_available,
    update_forecasts,
)

__all__ = [
    "KronosForecaster",
    "KronosUnavailable",
    "forecasts_as_series",
    "kronos_available",
    "update_forecasts",
]
