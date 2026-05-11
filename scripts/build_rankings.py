from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
STATUS_WEIGHT = {
    "تأیید TA": 3,
    "بررسی شده": 2,
    "بررسی نشده": 1,
}


def parse_topic_ranking(path: Path) -> list[dict[str, str | int]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[dict[str, str | int]] = []
    in_table = False

    for line in lines:
        if line.startswith("| رتبه "):
            in_table = True
            continue
        if in_table and re.match(r"^\|\s*---", line):
            continue
        if in_table:
            if not line.startswith("|"):
                break

            columns = [part.strip() for part in line.strip().strip("|").split("|")]
            if len(columns) < 7:
                continue

            try:
                score = int(columns[3])
            except ValueError:
                score = 0

            rows.append(
                {
                    "rank": columns[0],
                    "id": columns[1],
                    "title": columns[2],
                    "score": score,
                    "status": columns[4],
                    "relevance": columns[5],
                    "link": columns[6],
                }
            )

    rows.sort(
        key=lambda row: (
            -int(row["score"]),
            -STATUS_WEIGHT.get(str(row["status"]), 0),
            str(row["id"]),
        )
    )
    return rows


def normalize_link(link: str, topic_name: str) -> str:
    return link.replace("(./", f"(./{topic_name}/")


def build() -> str:
    sections: list[str] = []
    topic_dirs = sorted(
        p for p in ROOT.iterdir() if p.is_dir() and (p / "ranking.md").exists()
    )

    for topic_dir in topic_dirs:
        rows = parse_topic_ranking(topic_dir / "ranking.md")
        if not rows:
            continue

        sections.append(f"## {topic_dir.name}")
        sections.append("")
        sections.append("| رتبه | شناسه | عنوان | امتیاز | وضعیت | ارتباط با تمرین | لینک |")
        sections.append("|---|---|---|---|---|---|---|")

        for index, row in enumerate(rows, start=1):
            sections.append(
                f"| {index} | {row['id']} | {row['title']} | {row['score']} | "
                f"{row['status']} | {row['relevance']} | "
                f"{normalize_link(str(row['link']), topic_dir.name)} |"
            )

        sections.append("")

    return "\n".join(
        [
            "# رتبه‌بندی منابع",
            "",
            "این فایل به‌صورت مرکزی از روی فایل‌های `ranking.md` داخل هر topic ساخته می‌شود.",
            "",
            "## منطق رتبه‌بندی",
            "",
            "- منابع `تأیید TA` در اولویت بالاتر دیده می‌شوند.",
            "- منابعی که رأی، استفاده یا بازخورد بیشتری گرفته‌اند امتیاز بالاتری می‌گیرند.",
            "- منبعی که `مطالعه اضافه` است با همان برچسب نمایش داده می‌شود.",
            "",
            "## جمع‌بندی topicها",
            "",
            *sections,
        ]
    ).rstrip() + "\n"


if __name__ == "__main__":
    (ROOT / "ranking.md").write_text(build(), encoding="utf-8")
