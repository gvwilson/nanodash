"""Processing hooks used by AMW theme."""

import ark
from pathlib import Path
from shutil import copyfile


@ark.events.register(ark.events.Event.EXIT_BUILD)
def exit_build():
    """Finalize build by copying files matching patterns in configuration."""
    for pat in ark.site.config.get("copy", []):
        src_dir = ark.site.src()
        out_dir = ark.site.out()
        for src_file in Path(src_dir).rglob(f"**/{pat}"):
            out_file = str(src_file).replace(src_dir, out_dir)
            Path(out_file).parent.mkdir(exist_ok=True, parents=True)
            copyfile(src_file, out_file)
