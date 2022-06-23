# Canopy Vision Docker Container

## Quick Start
1. Update the `uri` value in `config.txt` with your RTSP URL
2. Download the docker image:
    For CUDA 11.6:
    ```
    docker pull canopyvision/canopy-vision:dgpu-cuda11.6
    ```

3. Run a container, replacing the license key:
    ```
    docker run -d --mount type=bind,source=$PWD/config.txt,target=/root/config.txt --mount type=bind,source=$PWD/models,target=/var/lib/canopy/models --env LICENSE_KEY=YOUR_LICENSE_KEY --gpus all canopyvision/canopy-vision:dgpu-cuda11.6
    ```

## Modifying the post-processing script
The provided post-processing script, `models/hardhat/streaming_print.py`, is provided and will simply print out raw object detection data. You can update this script or create a new script with similar structure to implement your own post-processing business logic. Any post-processing script will need to have executable permissions:
```
sudo chmod +x models/hardhat/streaming_print.py
```

## Adding new models
New model bundles can be added by replicating the hardhat subfolder and enclosed files. In general, a .engine, .etlt, or .onnx file is needed to be able to run model inference.
