# Re-exports resolve on first access (PEP 562), so importing a submodule (e.g. `prismatic.models.backbones.llm`) does
# not load `.load` and with it `prismatic.vla` / dlimp / TensorFlow.
import importlib

_EXPORTS = {
    "available_model_names": ".load",
    "available_models": ".load",
    "get_model_description": ".load",
    "load": ".load",
    "load_vla": ".load",
    "get_llm_backbone_and_tokenizer": ".materialize",
    "get_vision_backbone_and_transform": ".materialize",
    "get_vlm": ".materialize",
}


def __getattr__(name):
    if name not in _EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    # Importing `.load` binds the submodule to `load` here; the assignment below replaces it with the function.
    value = getattr(importlib.import_module(_EXPORTS[name], __name__), name)
    globals()[name] = value
    return value
