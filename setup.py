from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'traffic_light_simulator_demo',
  packages = find_packages(),
  version = '0.3',
  license='MIT',
  description = 'traffic light simulator', 
  author = 'Yan', 
  author_email = 'yzhao1990@gmail.com',
  url = 'https://github.com/ydotzh/Traffic_Light_Simulator',
  download_url = 'https://github.com/ydotzh/Traffic_Light_Simulator/archive/refs/tags/v_02.tar.gz',
  keywords = ['Data Challenge'],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers', 
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
