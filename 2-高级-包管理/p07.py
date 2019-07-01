import pkg01

pkg01.inInit()

teacher = pkg01.Person("MR", 28)
teacher.teach()

student = pkg01.Student("aa", 29)   #报错，不能用
student.say()