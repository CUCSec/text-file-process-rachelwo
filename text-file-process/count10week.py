with open('./log_files/201811123014.log',encoding='utf8')as lines:
    count=0
    for line in lines :
        student_id = line.split(',')[1]
        student_id = student_id.strip()
        if student_id=='学号：201811123014':
            count=count+1
print(count)
