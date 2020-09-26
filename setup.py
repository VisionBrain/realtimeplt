from setuptools import setup, find_packages
from os import path
import re


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='realtimeplt',
    version='0.0.1',
    python_requires=">3.5",
    install_requires=[
        'ipython', 'matplotlib;python_version>="3.6"', 'matplotlib<3.1;python_version<"3.6"',
        'numpy<1.18;python_version<"3.6"', 'bokeh;python_version>="3.6"', 'bokeh<=1.4.0;python_version<"3.6"'
    ],
    description='Realtime plot of loss plot in Jupyter Notebook for Keras, PyTorch and others.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    
    author='Aryan Karn',
    author_email='aryankarnin@gmail.com',
    
    keywords=['keras', 'pytorch', 'plot', 'chart', 'deep-learning'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Jupyter',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    zip_safe=False
)
