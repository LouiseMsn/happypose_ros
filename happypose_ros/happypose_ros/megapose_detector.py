from ultralytics import YOLO
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

from happypose.toolbox.inference.types import ObservationTensor, DetectionsType
from happypose.toolbox.datasets.scene_dataset import ObjectData
from happypose.toolbox.inference.utils import (
    make_detections_from_object_data,
)

from rclpy.impl import rcutils_logger

DEBUG = False


class Detector:
    def __init__(self, params) -> None:
        """Setup of Detector object.

        :param params: Parameters used to initialize the HappyPose pipeline.
        :type params: dict
        """

        super().__init__()
        self.logger = rcutils_logger.RcutilsLogger(name="Megapose detector")

        super().__init__()
        self._params = params
        self._device = self._params["device"]

        self.detector_path = self._params["megapose"]["detector"]["detector_path"]
        self.label = self._params["megapose"]["detector"]["obj_label"]

        self.yolo_model = YOLO(self.detector_path)

    def run(self, observation: ObservationTensor) -> DetectionsType:
        """Performs detections using a YOLOv11 model trained to detect only the wanted object.

        :param observation: Tensor containing camera information and incoming images.
        :type observation: happypose.toolbox.inference.types.ObservationTensor
        :return: Dictionary with final detections. If pipeline failed or nothing
            was detected None is returned
        :rtype: Union[None, dict]
        """
        image = self.convert_obstensor_to_image(observation)
        results = self.yolo_model(image, stream=True)

        classNames = ["bar-holder-stripped-bi-v3","pannel"]
        object_data = [None] * len(classNames)
        object_confidence = [0] * len(classNames)

        for r in results:
            boxes = r.boxes

            if len(boxes) > 0:
                for box in boxes:
                    confidence = math.ceil((box.conf[0] * 100)) / 100
                    label=classNames[int(box.cls[0])]

                    if DEBUG:
                        self.logger.info("LABEL: "+ label)
                        self.logger.info("CONFIDENCE: "+ str(confidence))

                    if confidence >= object_confidence[int(box.cls[0])] and confidence >= 0.1: # 
                        self.logger.info(str(int(box.cls[0])))
                        object_confidence[int(box.cls[0])]
                        x1, y1, x2, y2 = box.xyxy[0]
                        x1, y1, x2, y2 = (
                                            int(x1),
                                            int(y1),
                                            int(x2),
                                            int(y2),
                                        )
                        object_to_add = ObjectData(label=label, bbox_modal=np.array([x1, y1, x2, y2]))
                        object_data[int(box.cls[0])] = object_to_add

                        if DEBUG:
                            self.logger.info(str(object_data))
            else:
                return None

        object_data = [x for x in object_data if x is not None] # remove None

        detections = make_detections_from_object_data(object_data).to(self._device)
        self.logger.info(str(type(detections)))

        return detections

    def convert_obstensor_to_image(self, observation: ObservationTensor) -> np.array:
        """Converts an ObservationTensor into a numpy array image legible by a YOLO model.

        :param observation: Tensor containing camera information and incoming images.
        :type observation: happypose.toolbox.inference.types.ObservationTensor
        :return: Numpy array of the converted image.
        :rtype: numpy.ndarray
        """
        rgb_tensor = observation.images[:, 0:3].cpu()
        rgb_image = rgb_tensor.numpy()

        # Remove extra dimension
        rgb_image = rgb_image[0, :, :, :]

        # Rearrange axis to have RGB image
        rgb_image = np.moveaxis(rgb_image, [0, 1], [2, 0])

        # Conversion from float32 to unit8 required for YOLO
        rgb_image *= 255
        rgb_image = rgb_image.astype(np.uint8)

        return rgb_image
