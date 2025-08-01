# Fire Emblem: Three Houses - Translating tools

## Features

- Unpacking all binary files from DATA0/1.bin file
- Updating these files from patch(1-4) files
- Unpacking ENG_E game text and converting to json models
- Unpacking ENG_E DLC text and converting to json models
- Creating csv bundle from json models
- Patching json models from csv bundle
- Packing json models into binary
- Decompressing/compressing koei gz
- Unpacking game tutorials (graphic)
- Creating emu/nx version packages and creating zip bundles

## Requirements

- Python 3.12
- [DATA0.bin / DATA1.bin](https://github.com/bqio/feth-extractor)
- [Latest patches](https://github.com/bqio/feth-extractor)

## Usage

Create and activate environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create .env file

```bash
copy .env.example .env
```

Create a workdir folder in any location. Inside it, create two subfolders: `data` and `patches`.

Place `DATA0.bin` and `DATA1.bin` into the `data` folder, and all patches (folders patch1–patch4) into the `patches` folder.

Fill in the `.env` file by specifying the paths to your folders.

Then run

```bash
python -m feth init
```

This will create the `bundle.csv` and `dlc.csv` files, which contains the game's text.

**The `file_index`, `file_type` and `source_language` fields are for internal use—do not edit them.**

After editing the `bundle.csv` or `dlc.csv` files, run the command

```bash
python -m feth build
```

To view all available commands, run:

```bash
python -m feth
```
