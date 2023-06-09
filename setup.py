from setuptools import find_packages, setup

setup(name='grid_plot',
      description='A python packaging for making figures for computational astrophysics algorithms',
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/zingale/grid_plot',
      license='BSD',
      version="0.1",
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'],
      zip_safe=False)
