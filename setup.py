from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'telethon',
        'pandas',
        'sqlalchemy',
        'fastapi',
        'uvicorn',
        'opencv-python',
        'torch',
        'torchvision',
        'tensorflow',
        'dbt',
        'loguru'
    ],
    entry_points={
        'console_scripts': [
            'collect-data=src.data_collection:main',
            'clean-data=src.data_cleaning:main',
            'detect-objects=src.object_detection:main',
            'run-api=src.api:main'
        ],
    },
)
