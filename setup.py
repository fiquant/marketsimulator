from setuptools import setup

setup(name='fiquant-marketsim',
      version='0.1',
      description='FiQuant Market Simulator',
      author='Anton Kolotaev',
      author_email='anton.kolotaev@gmail.com',
      url='https://github.com/fiquant/marketsimulator',
      install_requires=['Flask', 'blist', 'numpy', 'docutils', 'pandas', 'veusz'],
     )