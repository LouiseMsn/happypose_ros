# flake8: noqa

# auto-generated DO NOT EDIT

from rcl_interfaces.msg import ParameterDescriptor
from rcl_interfaces.msg import SetParametersResult
from rcl_interfaces.msg import FloatingPointRange, IntegerRange
from rclpy.clock import Clock
from rclpy.exceptions import InvalidParameterValueException
from rclpy.time import Time
import copy
import rclpy
import rclpy.parameter
from generate_parameter_library_py.python_validators import ParameterValidators

import happypose_ros.custom_validation as custom_validators


class happypose_ros:

    class Params:
        # for detecting if the parameter struct has been updated
        stamp_ = Time()

        device = "cpu"
        verbose_info_logs = False
        time_stamp_strategy = "oldest"
        use_depth = False
        pose_estimator_type = "cosypose"
        camera_names = None
        class __Visualization:
            publish_markers = False
            class __Markers:
                dynamic_opacity = False
                lifetime = 10.0
            markers = __Markers()
        visualization = __Visualization()
        class __Cosypose:
            dataset_name = ""
            model_type = "pbr"
            depth_refiner_type = "icp"
            class __Renderer:
                renderer_type = "panda3d"
                n_workers = 8
                use_antialiasing = True
            renderer = __Renderer()
            class __Inference:
                labels_to_keep = [""]
                class __Detector:
                    detection_th = 0.7
                detector = __Detector()
                class __PoseEstimator:
                    n_refiner_iterations = 3
                    n_coarse_iterations = 1
                pose_estimator = __PoseEstimator()
                class __Icp:
                    n_min_points = 1000
                    min_measured_depth = 0.2
                    max_measured_depth = 5.0
                    iterations = 100
                    tolerance = 0.05
                    rejection_scale = 2.5
                    num_levels = 4
                icp = __Icp()
                class __Multiview:
                    ransac_n_iter = 2000
                    ransac_dist_threshold = 0.2
                    ba_n_iter = 100
                multiview = __Multiview()
            inference = __Inference()
        cosypose = __Cosypose()
        class __Megapose:
            model_name = "megapose-1.0-RGB-multi-hypothesis"
            subsample_scale = 8
            class __Mesh:
                directory_path = "/home/ros/share/hpose_ws/src/happypose_ros/happypose_examples/resources/meshes/"
                units = "mm"
                file_extension = "obj"
            mesh = __Mesh()
            class __Detector:
                detector_path = "/share/hpose_ws/src/happypose_ros/happypose_examples/resources/yolo-checkpoints/bar-holder-stripped-bi-v3.pt"
                obj_label = "bar-holder-stripped-bi-v3"
            detector = __Detector()
        megapose = __Megapose()
        class __Cameras:
            timeout = 0.0
            n_min_cameras = 1
            class __MapCameraNames:
                compressed = False
                leading = False
                publish_tf = False
                estimated_tf_frame_id = ""
                time_sync_slop = 0.04
            __map_type = __MapCameraNames
            def add_entry(self, name):
                if not hasattr(self, name):
                    setattr(self, name, self.__map_type())
                return getattr(self, name)
            def get_entry(self, name):
                return getattr(self, name)
        cameras = __Cameras()



    class ParamListener:
        def __init__(self, node, prefix=""):
            self.prefix_ = prefix
            self.params_ = happypose_ros.Params()
            self.node_ = node
            self.logger_ = rclpy.logging.get_logger("happypose_ros." + prefix)

            self.declare_params()

            self.node_.add_on_set_parameters_callback(self.update)
            self.user_callback = None
            self.clock_ = Clock()

        def get_params(self):
            tmp = self.params_.stamp_
            self.params_.stamp_ = None
            paramCopy = copy.deepcopy(self.params_)
            paramCopy.stamp_ = tmp
            self.params_.stamp_ = tmp
            return paramCopy

        def is_old(self, other_param):
            return self.params_.stamp_ != other_param.stamp_

        def unpack_parameter_dict(self, namespace: str, parameter_dict: dict):
            """
            Flatten a parameter dictionary recursively.

            :param namespace: The namespace to prepend to the parameter names.
            :param parameter_dict: A dictionary of parameters keyed by the parameter names
            :return: A list of rclpy Parameter objects
            """
            parameters = []
            for param_name, param_value in parameter_dict.items():
                full_param_name = namespace + param_name
                # Unroll nested parameters
                if isinstance(param_value, dict):
                    nested_params = self.unpack_parameter_dict(
                            namespace=full_param_name + rclpy.parameter.PARAMETER_SEPARATOR_STRING,
                            parameter_dict=param_value)
                    parameters.extend(nested_params)
                else:
                    parameters.append(rclpy.parameter.Parameter(full_param_name, value=param_value))
            return parameters

        def set_params_from_dict(self, param_dict):
            params_to_set = self.unpack_parameter_dict('', param_dict)
            self.update(params_to_set)

        def set_user_callback(self, callback):
            self.user_callback = callback

        def clear_user_callback(self):
            self.user_callback = None

        def refresh_dynamic_parameters(self):
            updated_params = self.get_params()
            # TODO remove any destroyed dynamic parameters

            # declare any new dynamic parameters

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.compressed"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Expect compressed image messages from given camera.", read_only = True)
                    parameter = entry.compressed
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                entry.compressed = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.leading"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Consider the camera to be leading. If a camera is leading, its frame_id is used as a reference. Only one camera can be leading, and it can't publish TF at the same time.", read_only = True)
                    parameter = entry.leading
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                entry.leading = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.publish_tf"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Publish TF of a given camera relative to the leading camera.", read_only = True)
                    parameter = entry.publish_tf
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                entry.publish_tf = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.estimated_tf_frame_id"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Name of frame_id published for estimated camera poses. If empty string, frame_id of camera is used. Leading camera can not have estimated frame_id.", read_only = False)
                    parameter = entry.estimated_tf_frame_id
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                validation_result = custom_validators.check_tf_valid_name(param)
                if validation_result:
                    raise InvalidParameterValueException('cameras.__map_camera_names.estimated_tf_frame_id',param.value, 'Invalid value set during initialization for parameter cameras.__map_camera_names.estimated_tf_frame_id: ' + validation_result)
                entry.estimated_tf_frame_id = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.time_sync_slop"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Delay [seconds] with which incoming messages can be synchronized.", read_only = False)
                    descriptor.floating_point_range.append(FloatingPointRange())
                    descriptor.floating_point_range[-1].from_value = 0.0
                    descriptor.floating_point_range[-1].to_value = float('inf')
                    parameter = entry.time_sync_slop
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                validation_result = ParameterValidators.gt(param, 0.0)
                if validation_result:
                    raise InvalidParameterValueException('cameras.__map_camera_names.time_sync_slop',param.value, 'Invalid value set during initialization for parameter cameras.__map_camera_names.time_sync_slop: ' + validation_result)
                entry.time_sync_slop = param.value

        def update(self, parameters):
            updated_params = self.get_params()

            for param in parameters:
                if param.name == self.prefix_ + "device":
                    validation_result = custom_validators.torch_check_device(param)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.device = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "verbose_info_logs":
                    updated_params.verbose_info_logs = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "time_stamp_strategy":
                    validation_result = ParameterValidators.one_of(param, ["average", "newest", "oldest"])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.time_stamp_strategy = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "visualization.publish_markers":
                    updated_params.visualization.publish_markers = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "visualization.markers.dynamic_opacity":
                    updated_params.visualization.markers.dynamic_opacity = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "visualization.markers.lifetime":
                    validation_result = ParameterValidators.gt(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.visualization.markers.lifetime = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "use_depth":
                    updated_params.use_depth = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "pose_estimator_type":
                    validation_result = ParameterValidators.one_of(param, ["cosypose", "megapose"])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.pose_estimator_type = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.dataset_name":
                    validation_result = ParameterValidators.one_of(param, ["hope", "tless", "ycbv", ""])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.dataset_name = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.model_type":
                    validation_result = ParameterValidators.one_of(param, ["pbr", "synth+real", ""])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.model_type = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.depth_refiner_type":
                    validation_result = ParameterValidators.one_of(param, ["icp"])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    validation_result = custom_validators.check_teaserpp_installed(param)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.depth_refiner_type = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.renderer.renderer_type":
                    validation_result = ParameterValidators.one_of(param, ["panda3d", "bullet"])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.renderer.renderer_type = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.renderer.n_workers":
                    validation_result = ParameterValidators.gt_eq(param, 1)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.renderer.n_workers = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.renderer.use_antialiasing":
                    updated_params.cosypose.renderer.use_antialiasing = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.detector.detection_th":
                    validation_result = ParameterValidators.bounds(param, 0.0, 1.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.detector.detection_th = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.pose_estimator.n_refiner_iterations":
                    validation_result = ParameterValidators.gt_eq(param, 1)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.pose_estimator.n_refiner_iterations = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.pose_estimator.n_coarse_iterations":
                    validation_result = ParameterValidators.gt_eq(param, 1)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.pose_estimator.n_coarse_iterations = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.icp.n_min_points":
                    validation_result = ParameterValidators.gt_eq(param, 1)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.icp.n_min_points = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.icp.min_measured_depth":
                    validation_result = ParameterValidators.gt_eq(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.icp.min_measured_depth = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.icp.max_measured_depth":
                    validation_result = ParameterValidators.gt_eq(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.icp.max_measured_depth = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.icp.iterations":
                    validation_result = ParameterValidators.gt_eq(param, 1)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.icp.iterations = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.icp.tolerance":
                    validation_result = ParameterValidators.gt_eq(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.icp.tolerance = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.icp.rejection_scale":
                    validation_result = ParameterValidators.gt_eq(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.icp.rejection_scale = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.icp.num_levels":
                    validation_result = ParameterValidators.gt_eq(param, 1)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.icp.num_levels = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.multiview.ransac_n_iter":
                    updated_params.cosypose.inference.multiview.ransac_n_iter = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.multiview.ransac_dist_threshold":
                    updated_params.cosypose.inference.multiview.ransac_dist_threshold = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.multiview.ba_n_iter":
                    updated_params.cosypose.inference.multiview.ba_n_iter = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cosypose.inference.labels_to_keep":
                    validation_result = ParameterValidators.unique(param)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cosypose.inference.labels_to_keep = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "megapose.model_name":
                    validation_result = ParameterValidators.one_of(param, ["megapose-1.0-RGB-multi-hypothesis", "megapose-1.0-RGB"])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.megapose.model_name = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "megapose.mesh.directory_path":
                    updated_params.megapose.mesh.directory_path = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "megapose.mesh.units":
                    validation_result = ParameterValidators.one_of(param, ["mm"])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.megapose.mesh.units = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "megapose.mesh.file_extension":
                    validation_result = ParameterValidators.one_of(param, ["ply", "obj"])
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.megapose.mesh.file_extension = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "megapose.subsample_scale":
                    updated_params.megapose.subsample_scale = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "megapose.detector.detector_path":
                    updated_params.megapose.detector.detector_path = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "megapose.detector.obj_label":
                    updated_params.megapose.detector.obj_label = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "camera_names":
                    validation_result = ParameterValidators.size_gt(param, 0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    validation_result = ParameterValidators.unique(param)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.camera_names = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cameras.timeout":
                    validation_result = ParameterValidators.gt_eq(param, 0.0)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cameras.timeout = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))

                if param.name == self.prefix_ + "cameras.n_min_cameras":
                    validation_result = ParameterValidators.gt_eq(param, 1)
                    if validation_result:
                        return SetParametersResult(successful=False, reason=validation_result)
                    updated_params.cameras.n_min_cameras = param.value
                    self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))


            # update dynamic parameters
            for param in parameters:

                    for value_1 in updated_params.camera_names:

                        param_name = f"{self.prefix_}cameras.{value_1}.compressed"
                        if param.name == param_name:

                            updated_params.cameras.get_entry(value_1).compressed = param.value
                            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))


                    for value_1 in updated_params.camera_names:

                        param_name = f"{self.prefix_}cameras.{value_1}.leading"
                        if param.name == param_name:

                            updated_params.cameras.get_entry(value_1).leading = param.value
                            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))


                    for value_1 in updated_params.camera_names:

                        param_name = f"{self.prefix_}cameras.{value_1}.publish_tf"
                        if param.name == param_name:

                            updated_params.cameras.get_entry(value_1).publish_tf = param.value
                            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))


                    for value_1 in updated_params.camera_names:

                        param_name = f"{self.prefix_}cameras.{value_1}.estimated_tf_frame_id"
                        if param.name == param_name:
                            validation_result = custom_validators.check_tf_valid_name(param)
                            if validation_result:
                                return SetParametersResult(successful=False, reason=validation_result)

                            updated_params.cameras.get_entry(value_1).estimated_tf_frame_id = param.value
                            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))


                    for value_1 in updated_params.camera_names:

                        param_name = f"{self.prefix_}cameras.{value_1}.time_sync_slop"
                        if param.name == param_name:
                            validation_result = ParameterValidators.gt(param, 0.0)
                            if validation_result:
                                return SetParametersResult(successful=False, reason=validation_result)

                            updated_params.cameras.get_entry(value_1).time_sync_slop = param.value
                            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))


            updated_params.stamp_ = self.clock_.now()
            self.update_internal_params(updated_params)
            if self.user_callback:
                self.user_callback(self.get_params())
            return SetParametersResult(successful=True)

        def update_internal_params(self, updated_params):
            self.params_ = updated_params

        def declare_params(self):
            updated_params = self.get_params()
            # declare all parameters and give default values to non-required ones
            if not self.node_.has_parameter(self.prefix_ + "device"):
                descriptor = ParameterDescriptor(description="Device to which the models will be loaded. Supported options are 'cpu' and 'cuda:x' where 'x' is the GPU number.", read_only = True)
                parameter = updated_params.device
                self.node_.declare_parameter(self.prefix_ + "device", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "verbose_info_logs"):
                descriptor = ParameterDescriptor(description="Extended verbosity on info logs. Show logs with number of detections and more.", read_only = False)
                parameter = updated_params.verbose_info_logs
                self.node_.declare_parameter(self.prefix_ + "verbose_info_logs", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "time_stamp_strategy"):
                descriptor = ParameterDescriptor(description="Which image time stamp to use in final detection message.", read_only = False)
                parameter = updated_params.time_stamp_strategy
                self.node_.declare_parameter(self.prefix_ + "time_stamp_strategy", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "visualization.publish_markers"):
                descriptor = ParameterDescriptor(description="Publish detected objects as markers to visualize detections in RViz.", read_only = True)
                parameter = updated_params.visualization.publish_markers
                self.node_.declare_parameter(self.prefix_ + "visualization.publish_markers", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "visualization.markers.dynamic_opacity"):
                descriptor = ParameterDescriptor(description="Change opacity of published markers based on their prediction score.", read_only = False)
                parameter = updated_params.visualization.markers.dynamic_opacity
                self.node_.declare_parameter(self.prefix_ + "visualization.markers.dynamic_opacity", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "visualization.markers.lifetime"):
                descriptor = ParameterDescriptor(description="Lifetime of a published marker.", read_only = False)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.visualization.markers.lifetime
                self.node_.declare_parameter(self.prefix_ + "visualization.markers.lifetime", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "use_depth"):
                descriptor = ParameterDescriptor(description="Specifies whether to use depth images for pose refinement. If set to `true` all cameras are expected to provide depth images.", read_only = True)
                parameter = updated_params.use_depth
                self.node_.declare_parameter(self.prefix_ + "use_depth", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "pose_estimator_type"):
                descriptor = ParameterDescriptor(description="Specifies which pose estimator to use in the pipeline.", read_only = True)
                parameter = updated_params.pose_estimator_type
                self.node_.declare_parameter(self.prefix_ + "pose_estimator_type", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.dataset_name"):
                descriptor = ParameterDescriptor(description="Name of BOP dataset, used to load specific weights and object models.", read_only = True)
                parameter = updated_params.cosypose.dataset_name
                self.node_.declare_parameter(self.prefix_ + "cosypose.dataset_name", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.model_type"):
                descriptor = ParameterDescriptor(description="Type of neural network model to use. Available: 'pbr'|'synth+real'", read_only = True)
                parameter = updated_params.cosypose.model_type
                self.node_.declare_parameter(self.prefix_ + "cosypose.model_type", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.depth_refiner_type"):
                descriptor = ParameterDescriptor(description="Type of happypose depth refinement. Available: 'icp'", read_only = True)
                parameter = updated_params.cosypose.depth_refiner_type
                self.node_.declare_parameter(self.prefix_ + "cosypose.depth_refiner_type", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.renderer.renderer_type"):
                descriptor = ParameterDescriptor(description="Specifies which renderer to use in the pipeline.", read_only = True)
                parameter = updated_params.cosypose.renderer.renderer_type
                self.node_.declare_parameter(self.prefix_ + "cosypose.renderer.renderer_type", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.renderer.n_workers"):
                descriptor = ParameterDescriptor(description="Number of CPU cores to use during rendering.", read_only = True)
                descriptor.integer_range.append(IntegerRange())
                descriptor.integer_range[-1].from_value = 1
                descriptor.integer_range[-1].to_value = 2**31-1
                parameter = updated_params.cosypose.renderer.n_workers
                self.node_.declare_parameter(self.prefix_ + "cosypose.renderer.n_workers", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.renderer.use_antialiasing"):
                descriptor = ParameterDescriptor(description="Use antialiasing in the rendering process. Slower and does not increase much performance. Only for panda3d. Enabled by default for backwards compatibility.", read_only = True)
                parameter = updated_params.cosypose.renderer.use_antialiasing
                self.node_.declare_parameter(self.prefix_ + "cosypose.renderer.use_antialiasing", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.detector.detection_th"):
                descriptor = ParameterDescriptor(description="Detection threshold of an object used by detector.", read_only = False)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = 1.0
                parameter = updated_params.cosypose.inference.detector.detection_th
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.detector.detection_th", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.pose_estimator.n_refiner_iterations"):
                descriptor = ParameterDescriptor(description="Number of iterations for the refiner.", read_only = False)
                descriptor.integer_range.append(IntegerRange())
                descriptor.integer_range[-1].from_value = 1
                descriptor.integer_range[-1].to_value = 2**31-1
                parameter = updated_params.cosypose.inference.pose_estimator.n_refiner_iterations
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.pose_estimator.n_refiner_iterations", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.pose_estimator.n_coarse_iterations"):
                descriptor = ParameterDescriptor(description="Number of iterations for the coarse estimate.", read_only = False)
                descriptor.integer_range.append(IntegerRange())
                descriptor.integer_range[-1].from_value = 1
                descriptor.integer_range[-1].to_value = 2**31-1
                parameter = updated_params.cosypose.inference.pose_estimator.n_coarse_iterations
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.pose_estimator.n_coarse_iterations", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.icp.n_min_points"):
                descriptor = ParameterDescriptor(description="Minimum number of matching depth points to consider detection valid.", read_only = False)
                descriptor.integer_range.append(IntegerRange())
                descriptor.integer_range[-1].from_value = 1
                descriptor.integer_range[-1].to_value = 2**31-1
                parameter = updated_params.cosypose.inference.icp.n_min_points
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.icp.n_min_points", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.icp.min_measured_depth"):
                descriptor = ParameterDescriptor(description="Minimum clipping distance of depth point from the camera to be considered valid.", read_only = False)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.cosypose.inference.icp.min_measured_depth
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.icp.min_measured_depth", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.icp.max_measured_depth"):
                descriptor = ParameterDescriptor(description="Maximum clipping distance of depth point from the camera to be considered valid.", read_only = False)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.cosypose.inference.icp.max_measured_depth
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.icp.max_measured_depth", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.icp.iterations"):
                descriptor = ParameterDescriptor(description="Number of iterations of ICP algorithm.", read_only = False)
                descriptor.integer_range.append(IntegerRange())
                descriptor.integer_range[-1].from_value = 1
                descriptor.integer_range[-1].to_value = 2**31-1
                parameter = updated_params.cosypose.inference.icp.iterations
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.icp.iterations", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.icp.tolerance"):
                descriptor = ParameterDescriptor(description="Tells the algorithm to stop when the norm of the error vector makes less improvement in percent, than tolerance value. The error function is the norm of the difference of the matched 3D points.", read_only = False)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.cosypose.inference.icp.tolerance
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.icp.tolerance", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.icp.rejection_scale"):
                descriptor = ParameterDescriptor(description="Robust outlier rejection is applied for robustness. This value actually corresponds to the standard deviation coefficient. Points with rejectionScale * &sigma are ignored during registration.", read_only = False)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.cosypose.inference.icp.rejection_scale
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.icp.rejection_scale", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.icp.num_levels"):
                descriptor = ParameterDescriptor(description="Corresponds to iterative ICP, where the original point cloud is subsampled. Note that if the output of CosyPose is considered good, ``num_levels`` does not have to be high.", read_only = False)
                descriptor.integer_range.append(IntegerRange())
                descriptor.integer_range[-1].from_value = 1
                descriptor.integer_range[-1].to_value = 2**31-1
                parameter = updated_params.cosypose.inference.icp.num_levels
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.icp.num_levels", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.multiview.ransac_n_iter"):
                descriptor = ParameterDescriptor(description="Number of ransac iterations when matching views.", read_only = False)
                parameter = updated_params.cosypose.inference.multiview.ransac_n_iter
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.multiview.ransac_n_iter", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.multiview.ransac_dist_threshold"):
                descriptor = ParameterDescriptor(description="Threshold (in metter) on the symmetric distance (Mean Symmetry-Aware Surface Distance) used consider a tentative match as an inlier during RANSAC iterations.", read_only = False)
                parameter = updated_params.cosypose.inference.multiview.ransac_dist_threshold
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.multiview.ransac_dist_threshold", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.multiview.ba_n_iter"):
                descriptor = ParameterDescriptor(description="Number of steps in the final bundle adjustment refinement.", read_only = False)
                parameter = updated_params.cosypose.inference.multiview.ba_n_iter
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.multiview.ba_n_iter", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cosypose.inference.labels_to_keep"):
                descriptor = ParameterDescriptor(description="Labels of detected objects to keep. If not specified, all objects are kept.", read_only = False)
                parameter = updated_params.cosypose.inference.labels_to_keep
                self.node_.declare_parameter(self.prefix_ + "cosypose.inference.labels_to_keep", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "megapose.model_name"):
                descriptor = ParameterDescriptor(description="Name of the megapose model to be used in inference, for now no model with depth is supported.", read_only = True)
                parameter = updated_params.megapose.model_name
                self.node_.declare_parameter(self.prefix_ + "megapose.model_name", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "megapose.mesh.directory_path"):
                descriptor = ParameterDescriptor(description="Path to the mesh directory.", read_only = False)
                parameter = updated_params.megapose.mesh.directory_path
                self.node_.declare_parameter(self.prefix_ + "megapose.mesh.directory_path", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "megapose.mesh.units"):
                descriptor = ParameterDescriptor(description="Unit of the mesh.", read_only = True)
                parameter = updated_params.megapose.mesh.units
                self.node_.declare_parameter(self.prefix_ + "megapose.mesh.units", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "megapose.mesh.file_extension"):
                descriptor = ParameterDescriptor(description="Filetype of the mesh.", read_only = True)
                parameter = updated_params.megapose.mesh.file_extension
                self.node_.declare_parameter(self.prefix_ + "megapose.mesh.file_extension", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "megapose.subsample_scale"):
                descriptor = ParameterDescriptor(description="Subsampling scale value", read_only = True)
                parameter = updated_params.megapose.subsample_scale
                self.node_.declare_parameter(self.prefix_ + "megapose.subsample_scale", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "megapose.detector.detector_path"):
                descriptor = ParameterDescriptor(description="Path to the .pt yolo model used as a detector for megapose", read_only = False)
                parameter = updated_params.megapose.detector.detector_path
                self.node_.declare_parameter(self.prefix_ + "megapose.detector.detector_path", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "megapose.detector.obj_label"):
                descriptor = ParameterDescriptor(description="Yolo label of the object to detect", read_only = False)
                parameter = updated_params.megapose.detector.obj_label
                self.node_.declare_parameter(self.prefix_ + "megapose.detector.obj_label", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "camera_names"):
                descriptor = ParameterDescriptor(description="List of names of cameras to subscribe.", read_only = True)
                parameter = rclpy.Parameter.Type.STRING_ARRAY
                self.node_.declare_parameter(self.prefix_ + "camera_names", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cameras.timeout"):
                descriptor = ParameterDescriptor(description="Timeout, after which a frame from a camera is considered too old. Value '0.0' disables timeout.", read_only = False)
                descriptor.floating_point_range.append(FloatingPointRange())
                descriptor.floating_point_range[-1].from_value = 0.0
                descriptor.floating_point_range[-1].to_value = float('inf')
                parameter = updated_params.cameras.timeout
                self.node_.declare_parameter(self.prefix_ + "cameras.timeout", parameter, descriptor)

            if not self.node_.has_parameter(self.prefix_ + "cameras.n_min_cameras"):
                descriptor = ParameterDescriptor(description="Minimum number of valid camera views to start pose estimation pipeline.", read_only = True)
                descriptor.integer_range.append(IntegerRange())
                descriptor.integer_range[-1].from_value = 1
                descriptor.integer_range[-1].to_value = 2**31-1
                parameter = updated_params.cameras.n_min_cameras
                self.node_.declare_parameter(self.prefix_ + "cameras.n_min_cameras", parameter, descriptor)

            # TODO: need validation
            # get parameters and fill struct fields
            param = self.node_.get_parameter(self.prefix_ + "device")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = custom_validators.torch_check_device(param)
            if validation_result:
                raise InvalidParameterValueException('device',param.value, 'Invalid value set during initialization for parameter device: ' + validation_result)
            updated_params.device = param.value
            param = self.node_.get_parameter(self.prefix_ + "verbose_info_logs")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.verbose_info_logs = param.value
            param = self.node_.get_parameter(self.prefix_ + "time_stamp_strategy")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["average", "newest", "oldest"])
            if validation_result:
                raise InvalidParameterValueException('time_stamp_strategy',param.value, 'Invalid value set during initialization for parameter time_stamp_strategy: ' + validation_result)
            updated_params.time_stamp_strategy = param.value
            param = self.node_.get_parameter(self.prefix_ + "visualization.publish_markers")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.visualization.publish_markers = param.value
            param = self.node_.get_parameter(self.prefix_ + "visualization.markers.dynamic_opacity")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.visualization.markers.dynamic_opacity = param.value
            param = self.node_.get_parameter(self.prefix_ + "visualization.markers.lifetime")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('visualization.markers.lifetime',param.value, 'Invalid value set during initialization for parameter visualization.markers.lifetime: ' + validation_result)
            updated_params.visualization.markers.lifetime = param.value
            param = self.node_.get_parameter(self.prefix_ + "use_depth")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.use_depth = param.value
            param = self.node_.get_parameter(self.prefix_ + "pose_estimator_type")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["cosypose", "megapose"])
            if validation_result:
                raise InvalidParameterValueException('pose_estimator_type',param.value, 'Invalid value set during initialization for parameter pose_estimator_type: ' + validation_result)
            updated_params.pose_estimator_type = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.dataset_name")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["hope", "tless", "ycbv", ""])
            if validation_result:
                raise InvalidParameterValueException('cosypose.dataset_name',param.value, 'Invalid value set during initialization for parameter cosypose.dataset_name: ' + validation_result)
            updated_params.cosypose.dataset_name = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.model_type")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["pbr", "synth+real", ""])
            if validation_result:
                raise InvalidParameterValueException('cosypose.model_type',param.value, 'Invalid value set during initialization for parameter cosypose.model_type: ' + validation_result)
            updated_params.cosypose.model_type = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.depth_refiner_type")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["icp"])
            if validation_result:
                raise InvalidParameterValueException('cosypose.depth_refiner_type',param.value, 'Invalid value set during initialization for parameter cosypose.depth_refiner_type: ' + validation_result)
            validation_result = custom_validators.check_teaserpp_installed(param)
            if validation_result:
                raise InvalidParameterValueException('cosypose.depth_refiner_type',param.value, 'Invalid value set during initialization for parameter cosypose.depth_refiner_type: ' + validation_result)
            updated_params.cosypose.depth_refiner_type = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.renderer.renderer_type")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["panda3d", "bullet"])
            if validation_result:
                raise InvalidParameterValueException('cosypose.renderer.renderer_type',param.value, 'Invalid value set during initialization for parameter cosypose.renderer.renderer_type: ' + validation_result)
            updated_params.cosypose.renderer.renderer_type = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.renderer.n_workers")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 1)
            if validation_result:
                raise InvalidParameterValueException('cosypose.renderer.n_workers',param.value, 'Invalid value set during initialization for parameter cosypose.renderer.n_workers: ' + validation_result)
            updated_params.cosypose.renderer.n_workers = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.renderer.use_antialiasing")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.cosypose.renderer.use_antialiasing = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.detector.detection_th")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.bounds(param, 0.0, 1.0)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.detector.detection_th',param.value, 'Invalid value set during initialization for parameter cosypose.inference.detector.detection_th: ' + validation_result)
            updated_params.cosypose.inference.detector.detection_th = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.pose_estimator.n_refiner_iterations")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 1)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.pose_estimator.n_refiner_iterations',param.value, 'Invalid value set during initialization for parameter cosypose.inference.pose_estimator.n_refiner_iterations: ' + validation_result)
            updated_params.cosypose.inference.pose_estimator.n_refiner_iterations = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.pose_estimator.n_coarse_iterations")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 1)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.pose_estimator.n_coarse_iterations',param.value, 'Invalid value set during initialization for parameter cosypose.inference.pose_estimator.n_coarse_iterations: ' + validation_result)
            updated_params.cosypose.inference.pose_estimator.n_coarse_iterations = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.icp.n_min_points")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 1)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.icp.n_min_points',param.value, 'Invalid value set during initialization for parameter cosypose.inference.icp.n_min_points: ' + validation_result)
            updated_params.cosypose.inference.icp.n_min_points = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.icp.min_measured_depth")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.icp.min_measured_depth',param.value, 'Invalid value set during initialization for parameter cosypose.inference.icp.min_measured_depth: ' + validation_result)
            updated_params.cosypose.inference.icp.min_measured_depth = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.icp.max_measured_depth")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.icp.max_measured_depth',param.value, 'Invalid value set during initialization for parameter cosypose.inference.icp.max_measured_depth: ' + validation_result)
            updated_params.cosypose.inference.icp.max_measured_depth = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.icp.iterations")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 1)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.icp.iterations',param.value, 'Invalid value set during initialization for parameter cosypose.inference.icp.iterations: ' + validation_result)
            updated_params.cosypose.inference.icp.iterations = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.icp.tolerance")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.icp.tolerance',param.value, 'Invalid value set during initialization for parameter cosypose.inference.icp.tolerance: ' + validation_result)
            updated_params.cosypose.inference.icp.tolerance = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.icp.rejection_scale")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.icp.rejection_scale',param.value, 'Invalid value set during initialization for parameter cosypose.inference.icp.rejection_scale: ' + validation_result)
            updated_params.cosypose.inference.icp.rejection_scale = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.icp.num_levels")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 1)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.icp.num_levels',param.value, 'Invalid value set during initialization for parameter cosypose.inference.icp.num_levels: ' + validation_result)
            updated_params.cosypose.inference.icp.num_levels = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.multiview.ransac_n_iter")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.cosypose.inference.multiview.ransac_n_iter = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.multiview.ransac_dist_threshold")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.cosypose.inference.multiview.ransac_dist_threshold = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.multiview.ba_n_iter")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.cosypose.inference.multiview.ba_n_iter = param.value
            param = self.node_.get_parameter(self.prefix_ + "cosypose.inference.labels_to_keep")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.unique(param)
            if validation_result:
                raise InvalidParameterValueException('cosypose.inference.labels_to_keep',param.value, 'Invalid value set during initialization for parameter cosypose.inference.labels_to_keep: ' + validation_result)
            updated_params.cosypose.inference.labels_to_keep = param.value
            param = self.node_.get_parameter(self.prefix_ + "megapose.model_name")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["megapose-1.0-RGB-multi-hypothesis", "megapose-1.0-RGB"])
            if validation_result:
                raise InvalidParameterValueException('megapose.model_name',param.value, 'Invalid value set during initialization for parameter megapose.model_name: ' + validation_result)
            updated_params.megapose.model_name = param.value
            param = self.node_.get_parameter(self.prefix_ + "megapose.mesh.directory_path")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.megapose.mesh.directory_path = param.value
            param = self.node_.get_parameter(self.prefix_ + "megapose.mesh.units")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["mm"])
            if validation_result:
                raise InvalidParameterValueException('megapose.mesh.units',param.value, 'Invalid value set during initialization for parameter megapose.mesh.units: ' + validation_result)
            updated_params.megapose.mesh.units = param.value
            param = self.node_.get_parameter(self.prefix_ + "megapose.mesh.file_extension")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.one_of(param, ["ply", "obj"])
            if validation_result:
                raise InvalidParameterValueException('megapose.mesh.file_extension',param.value, 'Invalid value set during initialization for parameter megapose.mesh.file_extension: ' + validation_result)
            updated_params.megapose.mesh.file_extension = param.value
            param = self.node_.get_parameter(self.prefix_ + "megapose.subsample_scale")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.megapose.subsample_scale = param.value
            param = self.node_.get_parameter(self.prefix_ + "megapose.detector.detector_path")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.megapose.detector.detector_path = param.value
            param = self.node_.get_parameter(self.prefix_ + "megapose.detector.obj_label")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            updated_params.megapose.detector.obj_label = param.value
            param = self.node_.get_parameter(self.prefix_ + "camera_names")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.size_gt(param, 0)
            if validation_result:
                raise InvalidParameterValueException('camera_names',param.value, 'Invalid value set during initialization for parameter camera_names: ' + validation_result)
            validation_result = ParameterValidators.unique(param)
            if validation_result:
                raise InvalidParameterValueException('camera_names',param.value, 'Invalid value set during initialization for parameter camera_names: ' + validation_result)
            updated_params.camera_names = param.value
            param = self.node_.get_parameter(self.prefix_ + "cameras.timeout")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 0.0)
            if validation_result:
                raise InvalidParameterValueException('cameras.timeout',param.value, 'Invalid value set during initialization for parameter cameras.timeout: ' + validation_result)
            updated_params.cameras.timeout = param.value
            param = self.node_.get_parameter(self.prefix_ + "cameras.n_min_cameras")
            self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
            validation_result = ParameterValidators.gt_eq(param, 1)
            if validation_result:
                raise InvalidParameterValueException('cameras.n_min_cameras',param.value, 'Invalid value set during initialization for parameter cameras.n_min_cameras: ' + validation_result)
            updated_params.cameras.n_min_cameras = param.value


            # declare and set all dynamic parameters

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.compressed"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Expect compressed image messages from given camera.", read_only = True)
                    parameter = entry.compressed
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                entry.compressed = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.leading"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Consider the camera to be leading. If a camera is leading, its frame_id is used as a reference. Only one camera can be leading, and it can't publish TF at the same time.", read_only = True)
                    parameter = entry.leading
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                entry.leading = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.publish_tf"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Publish TF of a given camera relative to the leading camera.", read_only = True)
                    parameter = entry.publish_tf
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                entry.publish_tf = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.estimated_tf_frame_id"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Name of frame_id published for estimated camera poses. If empty string, frame_id of camera is used. Leading camera can not have estimated frame_id.", read_only = False)
                    parameter = entry.estimated_tf_frame_id
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                validation_result = custom_validators.check_tf_valid_name(param)
                if validation_result:
                    raise InvalidParameterValueException('cameras.__map_camera_names.estimated_tf_frame_id',param.value, 'Invalid value set during initialization for parameter cameras.__map_camera_names.estimated_tf_frame_id: ' + validation_result)
                entry.estimated_tf_frame_id = param.value

            for value_1 in updated_params.camera_names:

                updated_params.cameras.add_entry(value_1)
                entry = updated_params.cameras.get_entry(value_1)
                param_name = f"{self.prefix_}cameras.{value_1}.time_sync_slop"
                if not self.node_.has_parameter(self.prefix_ + param_name):
                    descriptor = ParameterDescriptor(description="Delay [seconds] with which incoming messages can be synchronized.", read_only = False)
                    descriptor.floating_point_range.append(FloatingPointRange())
                    descriptor.floating_point_range[-1].from_value = 0.0
                    descriptor.floating_point_range[-1].to_value = float('inf')
                    parameter = entry.time_sync_slop
                    self.node_.declare_parameter(param_name, parameter, descriptor)
                param = self.node_.get_parameter(param_name)
                self.logger_.debug(param.name + ": " + param.type_.name + " = " + str(param.value))
                validation_result = ParameterValidators.gt(param, 0.0)
                if validation_result:
                    raise InvalidParameterValueException('cameras.__map_camera_names.time_sync_slop',param.value, 'Invalid value set during initialization for parameter cameras.__map_camera_names.time_sync_slop: ' + validation_result)
                entry.time_sync_slop = param.value

            self.update_internal_params(updated_params)
