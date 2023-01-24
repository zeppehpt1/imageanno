# Annotated images

Split folders with files (e.g. images) into train, validation and test folders. 

Keeps the annotation data (if there are any) together with their images.  
Given the input folder in the following format:

```
input/
        img1.jpg
        img1.xml
        img1.json
        img1.*
        img2.jpg
        img2.xml
        img2.json
        img2.*
        ...
    ...
```

Gives you this:

```
output/
    train/
        img1.jpg
        img1.xml
        img1.json
        img1.*
        ...
    val/
        img2.jpg
        img2.xml
        img2.json
        img2.*
        ...
    test/
        whatever.jpg
        whatever.xml
        whatever.json
        whatever.*
        ...
```
-   Works on any file types.
-   A [seed](https://docs.python.org/3/library/random.html#random.seed) lets you reproduce the splits.

## Counting occurrences of tags
This package includes functions to count the occurrences of a tag in JSON and XML files.  
They can go through all files in a folder and count the occurrence of each tag on every (annotated) image.

## Install

```bash
pip install git+https://github.com/zeppehpt1/imageanno.git
```

### Module

```python
import imageanno

# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
imageanno.split('input_folder', 'output_folder', seed=1337, ratio=(.7, .2, .1)) # train, test, valid
```

```python
import imageanno

# Returns total count of 'tag' found in all json files in 'path'
imageanno.findTagsJson('path', 'tag')

# Returns total count of 'tag' found in all xml files in 'path'
imageanno.findTagsXml('path', 'tag')
```

### Ref
this package was forked from https://github.com/SaberD/annotated-images to support different splits
