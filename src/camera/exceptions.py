class CameraError(ValueError):
    """Базовый класс ошибок работы с камерой."""


class CameraAccessError(CameraError):
    """Ошибка доступа к камере."""


class EmptyFrameError(CameraError):
    """Ошибка отсутствия кадра."""
