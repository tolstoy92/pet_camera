from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    camera_id: int

    image_width: int = 640
    image_height: int = 480

    show_image: bool = False

    fps: int = 30

    type_checking: bool = False


@lru_cache
def load_settings():
    return Settings()
