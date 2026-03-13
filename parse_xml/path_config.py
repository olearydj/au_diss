import os
from pathlib import Path

ENV_DATA_ROOT = "DISS_DATA_ROOT"
ENV_XML_ROOT = "DISS_XML_ROOT"
ENV_BOX_ROOT = "DISS_BOX_ROOT"

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_ROOT = REPO_ROOT / "data"
DEFAULT_UNAS_XML_ROOT = Path("/Volumes/tbm_archive/research_master/data")
DEFAULT_THUNDERBAY_XML_ROOT = Path("/Volumes/ThunderBay mini/Research Master/data")
DEFAULT_BOX_ROOT = "/Users/djo/Box%20Sync/Tiger%20Motors%20Research%20Team%20Collaboration%20Files/Investigation%201%20Data%20Files/trial-data/"


def _first_existing_path(*candidates: Path) -> Path:
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def resolve_data_root(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()

    env_raw = os.environ.get(ENV_DATA_ROOT)
    if env_raw:
        return Path(env_raw).expanduser()

    return DEFAULT_DATA_ROOT


def resolve_xml_root(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()

    env_raw = os.environ.get(ENV_XML_ROOT)
    if env_raw:
        return Path(env_raw).expanduser()

    return _first_existing_path(DEFAULT_UNAS_XML_ROOT, DEFAULT_THUNDERBAY_XML_ROOT)


def resolve_box_root(value: str | None = None) -> str:
    box_root = value or os.environ.get(ENV_BOX_ROOT) or DEFAULT_BOX_ROOT
    return box_root if box_root.endswith("/") else f"{box_root}/"
