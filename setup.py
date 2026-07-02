#!/usr/bin/env python

# This is a shim to allow GitHub to detect the package, build is done with hatch
# Taken from https://github.com/Textualize/rich

from setuptools import setup

setup(
    name="sensirion-ble2",
    version="0.1.0",
    package_dir={"": "src"},
    packages=["sensirion_ble2"],
    install_requires=[
        "bluetooth-data-tools>=0.1",
        "bluetooth-sensor-state-data>=1.6",
        "home-assistant-bluetooth>=1.6",
        "sensor-state-data>=2.9",
    ],
)