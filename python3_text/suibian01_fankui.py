import json
import os

class NoteApp:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.notes = json.load(f)
        else:
            self.notes = []

    def save_notes(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def add_note(self, content):
        self.notes.append(content)
        self.save_notes()
        print("✅ 笔记已添加！")

    def list_notes(self):
        if not self.notes:
            print("⚠️ 暂无笔记！")
            return
        print("\n=== 笔记列表 ===")
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            removed = self.notes.pop(index)
            self.save_notes()
            print(f"✅ 删除成功: {removed}")
        else:
            print("❌ 无效的序号！")


def main():
    app = NoteApp()

    while True:
        print("\n===== 记事本 =====")
        print("1. 添加笔记")
        print("2. 查看笔记")
        print("3. 删除笔记")
        print("0. 退出")
        choice = input("请选择操作: ")

        if choice == "1":
            content = input("输入笔记内容: ")
            app.add_note(content)
        elif choice == "2":
            app.list_notes()
        elif choice == "3":
            app.list_notes()
            idx = int(input("输入要删除的笔记序号: ")) - 1
            app.delete_note(idx)
        elif choice == "0":
            print("📕 程序已退出，再见！")
            break
        else:
            print("⚠️ 无效选项，请重新输入！")


if __name__ == "__main__":
    main()
