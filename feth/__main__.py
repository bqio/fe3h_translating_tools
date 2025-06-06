from feth.binary.unpack import unpack_binary
from feth.binary.update import update_info0_binary, update_info1_binary
from feth.binary.gz import decompress_gz, compress_gz
from feth.text.unpack import unpack_text
from feth.text.pack import pack_text
from feth.csv.bundle import make_bundle, patch_bundle, make_dlc_bundle
from feth.utils.clear import clear_all, clear_bin, clear_json, clear_mods
from feth.utils.merge import merge_bundles
from feth.build.pack_info import build_distrib
from feth.build.arch import make_nx_arch
from feth.graphic.tutorial import unpack_tutorials, decompress_tutorials
from feth.graphic.ba import unpack_binary_archive
from feth.parser.support import parse_support_files
from feth.parser.map import parse_map_files
from feth.parser.msgdata import parse_msgdata_files
from feth.parser.subtitle import parse_subtitle_files

from time import perf_counter
from colorama import init as colorama_init, Fore, Style
from pathlib import Path


import click

colorama_init()


@click.group()
def cli():
    pass


@cli.command("unpack-bin")
def cli_unpack_binary():
    print(f"{Fore.YELLOW}Unpacking binary...{Style.RESET_ALL}")
    unpack_binary()


@cli.command("update-bin")
def cli_update_binary():
    print(f"{Fore.YELLOW}Updating binary...{Style.RESET_ALL}")
    update_info0_binary()
    update_info1_binary()


@cli.command("unpack-text")
def cli_unpack_text():
    print(f"{Fore.YELLOW}Unpacking text...{Style.RESET_ALL}")
    unpack_text()


@cli.command("pack-text")
def cli_pack_text():
    print(f"{Fore.YELLOW}Packing text...{Style.RESET_ALL}")
    pack_text()


@cli.command("make-arch")
@click.argument("version")
def cli_make_arch(version: str):
    print(f"{Fore.YELLOW}Making archives...{Style.RESET_ALL}")
    make_nx_arch(version)


@cli.command("make-bundle")
def cli_make_bundle():
    print(f"{Fore.YELLOW}Making bundle...{Style.RESET_ALL}")
    make_bundle()
    print(f"{Fore.YELLOW}Making dlc bundle...{Style.RESET_ALL}")
    make_dlc_bundle()


@cli.command("patch-bundle")
def cli_patch_bundle():
    print(f"{Fore.YELLOW}Patching bundle...{Style.RESET_ALL}")
    patch_bundle()


@cli.command("clear-all")
def cli_clear_all():
    print(f"{Fore.YELLOW}Clearing files...{Style.RESET_ALL}")
    clear_all()


@cli.command("clear-bin")
def cli_clear_bin():
    print(f"{Fore.YELLOW}Clearing binary...{Style.RESET_ALL}")
    clear_bin()


@cli.command("clear-json")
def cli_clear_json():
    print(f"{Fore.YELLOW}Clearing json...{Style.RESET_ALL}")
    clear_json()


@cli.command("clear-mods")
def cli_clear_mods():
    print(f"{Fore.YELLOW}Clearing mods...{Style.RESET_ALL}")
    clear_mods()


@cli.command("unpack-tutorials")
def cli_unpack_tutorials():
    print(f"{Fore.YELLOW}Unpacking tutorials...{Style.RESET_ALL}")
    unpack_tutorials()


@cli.command("build-distrib")
def cli_build_distrib():
    print(f"{Fore.YELLOW}Building distribution...{Style.RESET_ALL}")
    build_distrib()


@cli.command("decompress-tutorials")
def cli_decompress_tutorials():
    print(f"{Fore.YELLOW}Decompressing tutorials...{Style.RESET_ALL}")
    decompress_tutorials()


@cli.command("merge-bundles")
@click.argument("src-bundle-path")
@click.argument("dest-bundle-path")
@click.argument("out-bundle-path")
def cli_merge_bundles(
    src_bundle_path: Path, dest_bundle_path: Path, out_bundle_path: Path
):
    print(f"{Fore.YELLOW}Merging bundles... (!!LONG OPERATION!!){Style.RESET_ALL}")
    merge_bundles(src_bundle_path, dest_bundle_path, out_bundle_path)


@cli.command("decompress-gz")
@click.argument("input-file")
@click.argument("output-file")
def cli_decompress_gz(input_file: Path, output_file: Path):
    decompress_gz(input_file, output_file)


@cli.command("compress-gz")
@click.argument("input-file")
@click.argument("output-file")
def cli_compress_gz(input_file: Path, output_file: Path):
    compress_gz(input_file, output_file)


@cli.command("unpack-bin-arch")
@click.argument("archive-path")
@click.argument("output-path")
@click.argument("entry-ext")
def cli_unpack_binary_archive(archive_path: Path, output_path: Path, entry_ext: str):
    unpack_binary_archive(archive_path, output_path, entry_ext)


@cli.command("parse-support")
@click.argument("dirs-path")
def cli_parse_support(dirs_path: Path):
    parse_support_files(dirs_path)


@cli.command("parse-map")
@click.argument("dirs-path")
def cli_parse_map(dirs_path: Path):
    parse_map_files(dirs_path)


@cli.command("parse-msgdata")
@click.argument("dirs-path")
def cli_parse_msgdata(dirs_path: Path):
    parse_msgdata_files(dirs_path)


@cli.command("parse-subtitle")
@click.argument("dirs-path")
def cli_parse_subtitle(dirs_path: Path):
    parse_subtitle_files(dirs_path)


@cli.command("init")
@click.pass_context
def cli_hard_build(ctx: click.Context):
    print(f"{Fore.YELLOW}Initialize...{Style.RESET_ALL}")
    start_time = perf_counter()
    ctx.invoke(cli_clear_all)
    ctx.invoke(cli_unpack_binary)
    ctx.invoke(cli_update_binary)
    ctx.invoke(cli_unpack_text)
    ctx.invoke(cli_make_bundle)
    end_time = perf_counter()
    print(
        f"{Fore.CYAN}Initialize is done. Time: {end_time - start_time}s{Style.RESET_ALL}"
    )


@cli.command("build")
@click.pass_context
def cli_build(ctx: click.Context):
    print(f"{Fore.YELLOW}Building...{Style.RESET_ALL}")
    start_time = perf_counter()
    ctx.invoke(cli_clear_mods)
    ctx.invoke(cli_patch_bundle)
    ctx.invoke(cli_pack_text)
    ctx.invoke(cli_build_distrib)
    end_time = perf_counter()
    print(f"{Fore.CYAN}Build is done. Time: {end_time - start_time}{Style.RESET_ALL}")


if __name__ == "__main__":
    print(
        f"{Fore.YELLOW}=== Fire Emblem: Three Houses - Translating tools ==={Style.RESET_ALL}"
    )
    print(f"{Fore.YELLOW}=== by bqio ==={Style.RESET_ALL}")
    cli()
