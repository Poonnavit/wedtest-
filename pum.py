import random 
digits = list(range(10)) # เลข 0-9 
random.shuffle(digits) # สลับตำแหน่งแบบสุ่ม
student_id = ""
for i in range(6):
    student_id += str(digits[i])
print("รหัสนักเรียน:", student_id)