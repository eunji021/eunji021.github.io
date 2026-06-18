import re

def remove_emojis_from_tabs(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Define target replacements for the tab buttons
    replacements = {
        "💻 시뮬레이터": "시뮬레이터",
        "📊 한눈에 보기": "한눈에 보기",
        "📄 소개": "소개",
        "🔢 코드": "코드"
    }

    updated_content = content
    for old, new in replacements.items():
        updated_content = updated_content.replace(old, new)

    # Let's also check if there are other occurrences in tab-nav
    # e.g., if there are spaces or variations:
    # <button class="tab-btn active" data-target="tab-simulator">💻 시뮬레이터</button>
    # We did direct string replacement, which is very safe.

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Removed emojis from tabs in {path}!")

remove_emojis_from_tabs("fire-evacuation-system.md")
remove_emojis_from_tabs("safety-equipment-system.md")
