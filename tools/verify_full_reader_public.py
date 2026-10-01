"""Anonymous byte readback of an explicitly selected complete-edition release."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen


REPO = Path(__file__).resolve().parents[1]
OWNER_REPO = "KokunoYumeto/OpenLogic-bn-Beng-IN"
PAGES_URL = "https://kokunoyumeto.github.io/OpenLogic-bn-Beng-IN/"
RAW_PATHS = (
    "bn-Beng-IN/content/first-order-logic/syntax-and-semantics/satisfaction.tex",
    "bn-Beng-IN/content/model-theory/lindstrom/ls-property.tex",
    "bn-Beng-IN/content/model-theory/lindstrom/lindstrom-proof.tex",
    "bn-Beng-IN/content/proof-theory/sequent-calculus/rules-mG3i.tex",
    "bn-Beng-IN/content/lambda-calculus/syntax/terms.tex",
    "bn-Beng-IN/content/proof-theory/proof-search/search-algorithm.tex",
    "evidence/GPT6_SOL_REDO_UNIT_REVIEWS.jsonl",
    "evidence/GPT6_SOL_REDO_PRODUCTION_SCRIPT_CHECK.json",
    "evidence/SOURCE_MODEL_PROVENANCE_722.json",
    "evidence/DRAFT_STATUS.json",
    "README.md",
)


def remote_hash(url: str) -> tuple[int, str]:
    request = Request(url, headers={"User-Agent": "openlogic-bengali-public-readback/1"})
    size = 0
    digest = hashlib.sha256()
    with urlopen(request, timeout=90) as response:
        assert response.status == 200, (url, response.status)
        while chunk := response.read(1024 * 1024):
            size += len(chunk)
            digest.update(chunk)
    return size, digest.hexdigest()


def local_hash(path: Path) -> tuple[int, str]:
    assert path.is_file(), path
    return path.stat().st_size, hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Anonymously verify a full-reader release and Pages bytes")
    parser.add_argument("--tag", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--expect-prerelease", action="store_true")
    parser.add_argument("--raw-path", action="append", dest="raw_paths")
    parser.add_argument("--asset", action="append", metavar="FILENAME=PATH",
                        help="Add an exact local file to the release asset readback")
    args = parser.parse_args()
    assert re.fullmatch(r"[0-9a-f]{40}", args.commit), "An exact release commit is required"
    assert args.receipt.resolve().is_relative_to(REPO.resolve()), "Receipt must stay in this repository"
    raw_paths = args.raw_paths if args.raw_paths is not None else RAW_PATHS
    asset_manifest = json.loads((REPO / "dist/FULL_RELEASE_ASSETS.json").read_text(encoding="utf-8"))
    assert asset_manifest["source_units"] == 722
    assert asset_manifest["pdf_included"] and asset_manifest["epub_included"], "Complete edition requires both PDF and EPUB"
    local_assets = {row["filename"]: REPO / "dist" / row["filename"] for row in asset_manifest["assets"]}
    assert len(local_assets) == len(asset_manifest["assets"])
    for name,path in local_assets.items():
        assert Path(name).name == name and path.resolve().is_relative_to((REPO / "dist").resolve())
    assert set(local_assets) == {
        "openlogic-bn-Beng-IN-complete." + suffix
        for suffix in ("pdf", "html", "epub", "tex")
    } | {"openlogic-bn-Beng-IN-complete-sources.zip"}, "Complete edition asset scope differs"
    for row in asset_manifest["assets"]:
        assert local_hash(local_assets[row["filename"]]) == (row["bytes"], row["sha256"]), row["filename"]
    expected_sums = "".join(row["sha256"] + "  " + row["filename"] + "\n"
                            for row in asset_manifest["assets"])
    assert (REPO / "dist/SHA256SUMS-complete.txt").read_text(encoding="ascii") == expected_sums
    for name in ("SHA256SUMS-complete.txt", "FULL_RELEASE_ASSETS.json"):
        local_assets[name] = REPO / "dist" / name
    for specification in args.asset or []:
        name, separator, filename = specification.partition("=")
        assert separator and name and filename, specification
        assert name not in local_assets, name
        path = Path(filename)
        assert path.is_file() and path.name == name, specification
        local_assets[name] = path
    api_url = f"https://api.github.com/repos/{OWNER_REPO}/releases/tags/{args.tag}"
    request = Request(api_url, headers={"User-Agent": "openlogic-bengali-public-readback/1"})
    with urlopen(request, timeout=30) as response:
        assert response.status == 200
        release = json.load(response)
    assert release["tag_name"] == args.tag and release["target_commitish"] == args.commit
    assert release["prerelease"] == args.expect_prerelease and not release["draft"]
    assert PAGES_URL in release["body"] and "PDF" in release["body"]
    published_assets = {asset["name"]: asset for asset in release["assets"]}
    assert set(published_assets) == set(local_assets)
    results = []
    for name, path in sorted(local_assets.items()):
        asset = published_assets[name]
        expected_size, expected_sha = local_hash(path)
        actual_size, actual_sha = remote_hash(asset["browser_download_url"])
        assert (actual_size, actual_sha) == (expected_size, expected_sha), name
        assert asset["size"] == expected_size, name
        if asset.get("digest") is not None:
            assert asset["digest"] == "sha256:" + expected_sha, name
        results.append({"filename": name, "url": asset["browser_download_url"],
                        "bytes": actual_size, "sha256": actual_sha})
    pages_size, pages_sha = remote_hash(PAGES_URL)
    assert (pages_size, pages_sha) == local_hash(REPO / "docs/index.html")
    assert pages_sha == local_hash(REPO / "dist/openlogic-bn-Beng-IN-complete.html")[1]
    raw = []
    for relative in raw_paths:
        url = f"https://raw.githubusercontent.com/{OWNER_REPO}/{args.commit}/{relative}"
        actual_size, actual_sha = remote_hash(url)
        assert (actual_size, actual_sha) == local_hash(REPO / relative), relative
        raw.append({"path": relative, "url": url, "bytes": actual_size, "sha256": actual_sha})
    receipt = {
        "schema": "openlogic-bn-reader-public-readback/1",
        "status": "passed",
        "anonymous": True,
        "credentials_used": False,
        "source_revision": "9620cc73f9c8e0ad003c514a5d3748f29611c4c0",
        "manifest_sha256": local_hash(REPO / "evidence/FULL_SOURCE_MANIFEST.jsonl")[1],
        "reader_units": 722,
        "git_commit": args.commit,
        "release_url": release["html_url"],
        "release_assets": results,
        "online_reader": {"url": PAGES_URL, "bytes": pages_size, "sha256": pages_sha},
        "raw_objects": raw,
        "pdf_claimed": True,
        "edition_identity": asset_manifest["edition_identity"],
    }
    args.receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "passed", "assets": len(results), "pages_bytes": pages_size,
                      "pages_sha256": pages_sha, "raw_objects": len(raw),
                      "receipt_sha256": local_hash(args.receipt)[1]}))


if __name__ == "__main__":
    main()
