# Re-exports resolve on first access (PEP 562), so importing a submodule (e.g. `prismatic.overwatch`) does not load
# `prismatic.models.load` and with it `prismatic.vla` / dlimp / TensorFlow.
import importlib

_EXPORTS = {
    "available_model_names": ".models",
    "available_models": ".models",
    "get_model_description": ".models",
    "load": ".models",
}


def __getattr__(name):
    if name not in _EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(_EXPORTS[name], __name__)
    for export, source in _EXPORTS.items():
        if source == _EXPORTS[name]:
            globals()[export] = getattr(module, export)
    return globals()[name]
