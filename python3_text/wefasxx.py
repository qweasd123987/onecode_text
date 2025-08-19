class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"ID: {self.id} | 书名: {self.title} | 作者: {self.author}"


class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self):
        title = input("请输入书名: ")
        author = input("请输入作者: ")
        book = Book(self.next_id, title, author)
        self.books.append(book)
        self.next_id += 1
        print("添加成功！")

    def show_books(self):
        if not self.books:
            print("当前没有图书。")
            return
        print("\n--- 图书列表 ---")
        for b in self.books:
            print(b)

    def search_book(self):
        key = input("请输入要搜索的书名关键词: ")
        found = False
        for b in self.books:
            if key in b.title:
                print("找到:", b)
                found = True
        if not found:
            print("未找到相关图书。")

    def delete_book(self):
        try:
            book_id = int(input("请输入要删除的图书ID: "))
        except ValueError:
            print("输入无效，请输入数字 ID。")
            return
        for b in self.books:
            if b.id == book_id:
                self.books.remove(b)
                print("已删除:", b.title)
                return
        print("未找到ID对应的图书。")


def main():
    lib = Library()
    while True:
        print("\n===== 图书管理系统 =====")
        print("1. 添加图书")
        print("2. 显示所有图书")
        print("3. 搜索图书")
        print("4. 删除图书")
        print("5. 退出")

        choice = input("请输入选项: ")
        if choice == "1":
            lib.add_book()
        elif choice == "2":
            lib.show_books()
        elif choice == "3":
            lib.search_book()
        elif choice == "4":
            lib.delete_book()
        elif choice == "5":
            print("退出系统。")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()
