from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: MIT License',
    'Topic :: Utilities']

setup(name='split-images-with-annotations',
      version='0.1.5',
      description='Split training data images into training, validation and test (dataset) folders.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/saberd/annotated-images',
      author='zeppehpt1',
      author_email='richard@nieding.de',
      license='MIT',
      packages=['imageanno'],
      classifiers=classifiers)