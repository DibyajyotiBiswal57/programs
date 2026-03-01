from pathlib import Path

from update_markdown_timestamps import apply_timestamp_to_content, update_file


def test_appends_timestamp_when_missing(tmp_path: Path) -> None:
    markdown_file = tmp_path / "sample.md"
    markdown_file.write_text("# Title\n\nBody text\n", encoding="utf-8")

    timestamp = "2024-01-01 00:00:00 UTC"
    changed = update_file(markdown_file, timestamp)

    assert changed is True
    content = markdown_file.read_text(encoding="utf-8")
    assert content.endswith(f"Last updated: {timestamp}\n")


def test_replaces_existing_timestamp(tmp_path: Path) -> None:
    markdown_file = tmp_path / "sample.md"
    markdown_file.write_text(
        "# Title\n\nBody text\nLast updated: 2023-12-31 12:00:00 UTC\n",
        encoding="utf-8",
    )

    timestamp = "2024-01-01 00:00:00 UTC"
    changed = update_file(markdown_file, timestamp)

    assert changed is True
    content = markdown_file.read_text(encoding="utf-8").strip().splitlines()
    assert content[-1] == f"Last updated: {timestamp}"
    assert len([line for line in content if line.startswith("Last updated: ")]) == 1


def test_apply_timestamp_to_content_is_idempotent() -> None:
    timestamp = "2024-01-01 00:00:00 UTC"
    content = "# Title\n\nBody\nLast updated: 2024-01-01 00:00:00 UTC\n"

    updated = apply_timestamp_to_content(content, timestamp)

    assert updated == content
