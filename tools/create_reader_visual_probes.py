"""Create bounded visual QA views from the exact complete reader DOM."""

import copy
import hashlib
import json
import pathlib

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parents[1]
BUILD = ROOT / "build/full-edition"
SOURCE = BUILD / "openlogic-bn-Beng-IN-complete.html"
UNITS = ["OLP-0008", "OLP-0066", "OLP-0163", "OLP-0207", "OLP-0349", "OLP-0409", "OLP-0425", "OLP-0462",
         "OLP-0488", "OLP-0517", "OLP-0523", "OLP-0634", "OLP-0660", "OLP-0702"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    data = SOURCE.read_bytes()
    qa = json.loads((BUILD / "SEMANTIC_READER_QA.json").read_text(encoding="utf-8"))
    assert digest(data) == qa["html"]["html_sha256"]
    soup = BeautifulSoup(data, "html.parser")
    destination = BUILD / "visual-probes"
    destination.mkdir(exist_ok=True)
    main_content = soup.find(id="reader-content")
    receipts = []
    for uid in UNITS:
        marker = soup.find(attrs={"data-source-unit": uid})
        assert marker is not None
        start = marker
        while start.parent is not main_content:
            start = start.parent
            assert start is not None
        nodes = [start]
        for node in start.next_siblings:
            if getattr(node, "name", None) is not None and node.find(attrs={"data-source-unit": True}):
                break
            nodes.append(node)
        view = BeautifulSoup('<!doctype html><html lang="bn-Beng-IN"><head></head><body></body></html>', "html.parser")
        view.head.replace_with(copy.deepcopy(soup.head))
        view.title.string = "দৃশ্য-পরীক্ষা: " + uid
        content = view.new_tag("main", id="reader-content")
        for node in nodes:
            content.append(copy.deepcopy(node))
        view.body.append(content)
        path = destination / ("probe-" + uid + ".html")
        payload = (str(view) + "\n").encode("utf-8")
        path.write_bytes(payload)
        receipts.append({"unit_id": uid, "file": path.relative_to(BUILD).as_posix(),
                         "bytes": len(payload), "sha256": digest(payload)})
    result = {"schema": "openlogic-bn-reader-visual-probes/1", "reader_sha256": digest(data),
              "method": "সম্পূর্ণ HTML-এর অপরিবর্তিত DOM অংশ ও একই এম্বেড-করা ফন্ট/CSS থেকে সীমিত দৃশ্য-পরীক্ষা; কোনো সূত্র বা অনুবাদ বদলানো হয়নি।",
              "probes": receipts, "status": "generated; browser inspection pending"}
    (BUILD / "VISUAL_PROBES.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"probes": len(receipts), "reader_sha256": digest(data)}))


if __name__ == "__main__":
    main()
