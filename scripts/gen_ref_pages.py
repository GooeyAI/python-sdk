"""Generate the code reference pages."""

import importlib
from pathlib import Path

import mkdocs_gen_files


nav = mkdocs_gen_files.Nav()
mod_symbol = '<code class="doc-symbol doc-symbol-nav doc-symbol-module"></code>'

root = Path(__file__).parent.parent
src = root / "src"  

for path in sorted(src.rglob("*.py")):  
    module_path = path.relative_to(src).with_suffix("")  
    doc_path = path.relative_to(src).with_suffix(".md")  
    full_doc_path = Path("reference", doc_path)  

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":  
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    nav_parts = [f"{mod_symbol} {part}" for part in parts]
    nav[tuple(nav_parts)] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:  
        identifier = ".".join(parts)  
        print(f"---\ntitle: {identifier}\n---\n\n::: {identifier}", file=fd)

        if identifier.endswith("gooey"):
            print("    handler: python", file=fd)
            print("    options:", file=fd)
            print("      members:", file=fd)
            print("        - Gooey", file=fd)
            print("        - AsyncGooey", file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(root))

    with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())
