import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    The function `read_yaml` reads a YAML file from a specified path and returns its content as a
    `ConfigBox` object.
    
    :param path_to_yaml: The `path_to_yaml` parameter is the file path to the YAML file that you want to
    read and load into a `ConfigBox` object
    :type path_to_yaml: Path
    :return: The function `read_yaml` is returning a `ConfigBox` object initialized with the content
    loaded from the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    The function `create_directories` creates directories based on the provided list of paths and logs
    the creation if verbose mode is enabled.
    
    :param path_to_directories: The `path_to_directories` parameter is a list containing the paths to
    the directories that you want to create. Each element in the list represents a directory path that
    you want to create using the `os.makedirs()` function
    :type path_to_directories: list
    :param verbose: The `verbose` parameter in the `create_directories` function is a boolean flag that
    determines whether additional information or logs should be displayed during the execution of the
    function. If `verbose` is set to `True`, the function will log a message indicating that a directory
    has been created. If `, defaults to True (optional)
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"{path} directory created")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    The `save_json` function saves a dictionary as JSON data to a specified file path and logs the
    action.
    
    :param path: The `path` parameter is expected to be of type `Path`, which represents a path-like
    object that can be used to interact with the file system. It is typically used to specify the
    location where the JSON data will be saved
    :type path: Path
    :param data: The `data` parameter in the `save_json` function is expected to be a dictionary
    containing the data that you want to save to a JSON file. This dictionary will be serialized and
    written to the file specified by the `path` parameter
    :type data: dict
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    The function `load_json` reads and loads a JSON file from a specified path and logs a success
    message.
    
    :param path: The `path` parameter in the `load_json` function is expected to be of type `Path`,
    which is likely a path-like object representing a file path. This parameter is used to specify the
    location of the JSON file that needs to be loaded by the function
    :type path: Path
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    The function `save_bin` saves binary data to a specified file path using joblib and logs the saved
    file path using a logger.
    
    :param data: The `data` parameter is the information or object that you want to save in binary
    format using the `save_bin` function. This data can be of any type, as indicated by the type hint
    `Any` in the function signature
    :type data: Any
    :param path: The `path` parameter in the `save_bin` function is the location where the binary file
    will be saved. It should be a `Path` object representing the file path where you want to save the
    binary data
    :type path: Path
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data