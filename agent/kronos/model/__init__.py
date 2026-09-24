# Vendored from https://github.com/shiyu-coder/Kronos (commit 67b630e, model/__init__.py).
# Copyright (c) 2025 ShiYu. MIT License; see agent/kronos/LICENSE.
# Code unchanged (imports already package-relative).

from .kronos import KronosTokenizer, Kronos, KronosPredictor

model_dict = {
    'kronos_tokenizer': KronosTokenizer,
    'kronos': Kronos,
    'kronos_predictor': KronosPredictor
}


def get_model_class(model_name):
    if model_name in model_dict:
        return model_dict[model_name]
    else:
        print(f"Model {model_name} not found in model_dict")
        raise NotImplementedError


