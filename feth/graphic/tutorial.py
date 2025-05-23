from feth.binary.gz import decompress_gz
from feth.utils.path import TUTORIALS_PATH, TUTORIALS_BIN_PATH
from feth.graphic.ba import BinaryArchiveModel
from iostuff.readers.binary import BinaryReader
from iostuff.writers.binary import BinaryWriter


def unpack_tutorials() -> None:
    if not TUTORIALS_BIN_PATH.exists():
        print("[Not found]:", TUTORIALS_BIN_PATH)
        exit(1)

    if not TUTORIALS_PATH.mkdir():
        TUTORIALS_PATH.mkdir()

    with BinaryReader(TUTORIALS_BIN_PATH) as reader:
        file = BinaryArchiveModel()
        file.number_of_entries = reader.read_uint()

        file.pointers = []
        for _ in range(file.number_of_entries):
            file.pointers.append([reader.read_uint(), reader.read_uint()])

        file.entries = []
        for pointer in file.pointers:
            reader.seek(pointer[0])
            file.entries.append(reader.read(pointer[1]))

        for entry_idx, entry in enumerate(file.entries):
            entry_path = TUTORIALS_PATH / f"{entry_idx}.g1t.gz"
            print("[Unpack tutorial]:", entry_path)
            with BinaryWriter(entry_path) as writer:
                writer.write(entry)


def decompress_tutorials() -> None:
    for input_file in TUTORIALS_PATH.glob("*.gz"):
        output_file = TUTORIALS_PATH / input_file.stem
        decompress_gz(input_file, output_file)
