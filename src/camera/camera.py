from typing import Optional

import cv2

from .exceptions import CameraAccessError, EmptyFrameError
from settings import load_settings


settings = load_settings()


if settings.type_checking:
    import numpy as np


class Camera:
    """Работа с камерой."""

    def __init__(
        self,
        camera_id: int,
        img_width: Optional[int],
        img_height: Optional[int],
    ):
        self.__camera_id: int = camera_id
        self.__img_width: Optional[int] = img_width
        self.__img_height: Optional[int] = img_height
        self.__capture: cv2.VideoCapture = self.init_capture()

    def init_capture(self) -> cv2.VideoCapture:
        """Инициализация работы камеры."""
        cap = cv2.VideoCapture(self.__camera_id)
        if not cap.isOpened():
            raise CameraAccessError(
                f"Cannot acces to camera with id: {self.__camera_id}"
            )
        return cap

    def get_frame(self) -> "np.ndarray":
        """Получение кадра"""
        ret, img = self.__capture.read()

        if not ret:
            raise EmptyFrameError

        original_height, original_width, _ = img.shape

        dst_width = self.__img_width or original_width
        dst_height = self.__img_height or original_height

        return cv2.resize(img, (dst_width, dst_height))

    def close(self):
        """Завершение работы камеры."""
        self.__capture.release()
