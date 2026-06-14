# Chars74K_Style Dataset

This folder contains a style-conditioned character image dataset derived from Chars74K-style alphanumeric character samples. It is organized for character image generation, style transfer, and conditional synthesis tasks where a model learns to render a target character in a given visual style.

## Dataset Summary

- **Task type:** character style transfer / conditional character image generation
- **Characters:** 36 alphanumeric classes
  - digits: `0-9`
  - uppercase letters: `A-Z`
- **Number of styles:** 1,015 style folders
- **Target images:** 36,540 PNG images
- **Image size:**
  - `ContentImage`: 128 x 128
  - `ContentImage64`: 64 x 64
  - `TargetImage`: 64 x 64
- **Split included:** `train`

## Directory Structure

```text
Chars74K_Style/
├── README.md
├── 128_2_64.py
└── train/
    ├── ContentImage/
    │   ├── 0.png
    │   ├── 1.png
    │   └── ...
    ├── ContentImage64/
    │   ├── 0.png
    │   ├── 1.png
    │   └── ...
    └── TargetImage/
        ├── 00001/
        │   ├── 0_W_00001.png
        │   ├── 1_M_00001.png
        │   └── ...
        ├── 00002/
        └── ...
```

## Folder Description

### `train/ContentImage/`

Contains one reference content image for each character class. These images are 128 x 128 PNG files and represent the canonical character content used as input references.

Example:

```text
train/ContentImage/0.png
train/ContentImage/A.png
train/ContentImage/Z.png
```

### `train/ContentImage64/`

Contains resized 64 x 64 versions of the images in `ContentImage/`. These files are useful when the model input resolution is 64 x 64.

The script `128_2_64.py` can be used to resize images from `ContentImage/` into `ContentImage64/`.

### `train/TargetImage/`

Contains the target styled character images. Each subfolder corresponds to one style ID. Every style folder contains 36 character images, one for each alphanumeric class.

Example:

```text
train/TargetImage/00001/0_W_00001.png
train/TargetImage/00001/A_W_00001.png
train/TargetImage/00001/Z_M_00001.png
```

The target filename follows this pattern:

```text
<character>_<source_tag>_<style_id>.png
```

where:

- `<character>` is the character class, such as `0`, `A`, or `Z`.
- `<source_tag>` is an auxiliary tag retained from the source data.
- `<style_id>` matches the parent style folder name.

For most training pipelines, the class label can be read from the first field of the filename, and the style label can be read from the parent folder name.

## Pairing Rule

A typical training sample can be constructed as:

```text
content image: train/ContentImage64/<character>.png
target image:  train/TargetImage/<style_id>/<character>_<source_tag>_<style_id>.png
```

For example:

```text
content image: train/ContentImage64/A.png
target image:  train/TargetImage/00001/A_W_00001.png
```

This pair asks the model to preserve the content of character `A` while generating it in style `00001`.


## Notes

- Style IDs should be treated as folder names rather than assumed to be continuous integers.
- All target style folders currently contain 36 images.
- The dataset currently provides the training split only. If validation or test splits are required, they should be created explicitly according to the intended experimental protocol.
- File names on different operating systems may handle letter case differently. When using this dataset, keep character labels and paths consistent with the actual filenames on disk.

## Preprocessing Script

`128_2_64.py` resizes images from 128 x 128 to 64 x 64 using PIL:

```python
img_resized = img.resize((64, 64), Image.LANCZOS)
```

Before running the script, update the input and output paths to match your local dataset location.
