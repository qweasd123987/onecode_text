class Student:
    def __init__(self, sid, name, age, score):
        self.sid = sid
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"ID: {self.sid} | 姓名: {self.name} | 年龄: {self.age} | 成绩: {self.score}"


class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, sid, name, age, score):
        self.students.append(Student(sid, name, age, score))
        print("✅ 添加成功！")

    def list_students(self):
        if not self.students:
            print("⚠️ 没有学生信息！")
            return
        print("\n=== 学生信息列表 ===")
        for stu in self.students:
            print(stu)

    def find_student(self, sid):
        for stu in self.students:
            if stu.sid == sid:
                print("找到学生:")
                print(stu)
                return
        print("❌ 未找到该学生！")

    def update_score(self, sid, new_score):
        for stu in self.students:
            if stu.sid == sid:
                stu.score = new_score
                print("✅ 成绩更新成功！")
                return
        print("❌ 未找到该学生！")


def main():
    system = StudentSystem()

    while True:
        print("\n===== 学生管理系统 =====")
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 查找学生")
        print("4. 修改成绩")
        print("0. 退出")
        choice = input("请选择操作: ")

        if choice == "1":
            sid = input("输入学号: ")
            name = input("输入姓名: ")
            age = input("输入年龄: ")
            score = input("输入成绩: ")
            system.add_student(sid, name, age, float(score))
        elif choice == "2":
            system.list_students()
        elif choice == "3":
            sid = input("输入要查找的学号: ")
            system.find_student(sid)
        elif choice == "4":
            sid = input("输入要修改的学号: ")
            new_score = float(input("输入新成绩: "))
            system.update_score(sid, new_score)
        elif choice == "0":
            print("系统已退出，再见！")
            break
        else:
            print("⚠️ 无效选项，请重新输入！")


if __name__ == "__main__":
    main()
