__all__ = ["ConfigApp"]

from pydantic import BaseModel, Field, ConfigDict

from pgstudio.display import WinRes


class ConfigApp(BaseModel):
    app_name: str = Field(frozen=True)
    res: WinRes
    fps: int = 60

    model_config = ConfigDict(validate_assignment=True)

