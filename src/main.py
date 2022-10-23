from time import monotonic

import cv2

from camera import Camera
from settings import load_settings


settings = load_settings()


def main():
    camera = Camera(
        camera_id=settings.camera_id,
        img_width=settings.image_width,
        img_height=settings.image_height,
    )

    dst_delay: float = 1. / settings.fps

    last_frame_getting: float = monotonic()

    while True:
        current_time: float = monotonic()
        current_delay: float = current_time - last_frame_getting
        if current_delay < dst_delay:
            continue

        last_frame_getting = current_time
        img = camera.get_frame()

        if settings.show_image:
            cv2.imshow("image", img)
            if cv2.waitKey(int(dst_delay * 1000)) == 27:
                break

    camera.close()


if __name__ == "__main__":
    main()
