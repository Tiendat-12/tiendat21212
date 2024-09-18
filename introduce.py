class Person:
    def __init__(self, name, age, hobby, job):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.job = job

    def introduce(self):
        print(f"Xin chào! Tên tôi là {self.name}.")
        print(f"Tôi năm nay {self.age} tuổi.")
        print(f"Sở thích của tôi là {self.hobby}.")
        print(f"Tôi hiện đang làm công việc: {self.job}.")

# Tạo một đối tượng và gọi hàm giới thiệu
myself = Person(name="Mai Tien Dat", age=21, hobby="nghe nhac", job="kỹ sư phần mềm")
myself.introduce()
