# Redaction example using Tesseract

## To build

```shell
docker build -t redact -f Containerfile .
```

## To run

```shell
docker run --rm -d -v $(pwd):/data redact -i input.tiff -o output.tiff
```

The redacted image will appear in the mounted folder with the input image.

The script can also be run indepentantly, required packages can be installed via 

```shell
pip3 install -r requirements.txt
```

to run

```shell
python3 redact.py -i input.tiff -o output.tiff
```
