# 학생관리 프로그램
DIRPATH='C:\\Users\\재필\\Desktop\\학생명부\\'
filename=DIRPATH+"student_list_final.txt"

class SamePerson(Exception):pass
data_list={}

# 학생 명부 클래스
class Student_list:
    def __init__(self, new_student_list):
        self.name=new_student_list[0]
        self.num=new_student_list[1]
        self.loc=new_student_list[2]
        self.etc=",".join(new_student_list[3:])

    def register(self):
        try:
            if (self.name in data_list.keys()) and (self.num == data_list[self.name][0]):
                raise SamePerson("********** 이미 저장된 학생입니다! **********")

            else:
                data_list[self.name]=(self.num, self.loc, self.etc)
                print(f"{self.name}학생이 명부에 저장되었습니다.")

        except SamePerson as s:
            print(s)

    def erase(self):
        if self.name in data_list.keys():
            del data_list[self.name]
        print(f"{self.name}학생이 명부에 삭제되었습니다.")

# 학교생활 클래스
class Student_info:
    def __init__(self, new_student_info):
        self.absent = int(new_student_info[0])
        self.health = new_student_info[1]
        self.score = int(new_student_info[2])

    def attendance(self):
        if self.absent >=5:
            print("출결 관련하여 주의 요함!")   
        elif self.absent >=10:
            print("유급대상입니다.")
        elif self.absent==0:
            print("개근입니다.")
        else:
            print("출결사항 이상 없습니다.")

    def grade(self):
        if self.score//10>=9:
            return 'A' 
        elif self.score//10>=8:
            return 'B'  
        elif self.score//10>=7:
            return 'C'
        elif self.score//10>=6 :
            return 'D' 
        else:
            return 'D' 

    def condition(self):
        return '건강상태가 '+self.health+' 상태'

# 상담 클래스
class Counsel:
    def __init__(self, new_student_counsel):
        self.__dream=new_student_counsel[0]
        self.__worry=new_student_counsel[1]

    @property
    def course(self):
        return "학생의 꿈은 "+self.__dream+" 입니다."
    @course.setter
    def course(self, new_dream):
        self.__dream=new_dream
        return "학생의 꿈은 "+self.__dream+" 입니다."

    @property
    def depression(self):
        return "학생의 고민이나 애로사항 정도가 "+self.__worry+" 입니다."
    @depression.setter
    def depression(self, new):
        self.__worry=new
        return "학생의 고민이나 애로사항 정도가 "+self.__worry+" 입니다."

# 학생관리 클래스
class Student_Manage(Student_list, Student_info, Counsel):

    def __init__(self, _appraise, new_student_counsel, new_student_info, new_student_list):
        Student_list.__init__(self, new_student_list)
        Student_info.__init__(self, new_student_info)
        Counsel.__init__(self, new_student_counsel)

        self.appraise=_appraise       

    def assessment(self, teacher):
        PassWord="스승의 은혜"
        print()
        print('-'*50)
        print(f'{self.name}학생의 종합평가 입니다.')
        print(f'출결상태 => 결석횟수 {self.absent}회로 ',end='')
        self.attendance()
        print(f'성적은 {self.grade()}학점으로, ', end='')
        if self.grade() == 'A':
            print("훌륭합니다.")
        elif self.grade() == 'B':
            print("준수합니다.")
        elif self.grade() == 'C':
            print("노력이 필요합니다.")
        elif self.grade() == 'D':
            print("분발해야 합니다.")
        else:
            print("보호자의 주의가 필요합니다.")
        print(f'건강상태는 {self.condition()}로 ',end="")
        if self.health in ['아주 좋음', '좋음', '준수']:
            print("훌륭합니다.")
        elif self.health in ['나쁨', '아주 나쁨']:
            print("보호자와 병원동행 요망")
        else:
            print("상담 필요합니다.")
        print()
        cnt=0
        while 1:
            pw=input("개인상담 정보이므로 비밀번호입력하세요\n나가시려면 q / Q 입력: ")
            if pw in ['q','Q']:
                break
            elif pw==PassWord:
                print(f'{self.name}{self.course}')
                print(f'{self.name}{self.depression}')
                break
            else:
                cnt+=1
                if cnt==5:
                    print("*****비밀번호가 5회이상 틀렸습니다. 행정실로 문의부탁드립니다.*****")
                    break
                else:
                    print(f"비밀번호가 {cnt}회 틀렸습니다.")
        print()
        print(f'기타사항 : {self.etc}')
        print(f'{teacher} 선생님의 종합평가 : [{self.appraise}]')
        print(f"이상 평가서 작성 끝 - 검토자 : {teacher}")
        print('-'*50)

    # 저장된 학생 명부 보기 함수
    def showlist():
        print('*'*150)
        for k, v in data_list.items():
            print(f'{k}:{v}',end='\n')
        print('*'*150)

    # 학생명부 파일로 쓰기 함수
    def writeAsfile():
        stu_list=''
        for k, v in data_list.items():
            stu_list+=str(k)+' : '+str(v)+'\n'
        stu_list=stu_list[0:-1]
        while 1:
            answer=input("학생 명부를 파일로 만드시겠습니까? (Y/N) : ")
            if answer=='N':
                break
            elif answer=='Y':
                with open(filename, mode='w', encoding='utf-8') as fp:
                    fp.write(stu_list)
                break
            else:
                print("잘못된 입력 Y 또는 N 키로 입력해주세요!")

    # 학생명부 파일 읽기 함수
    def readAsfile():
        try:
            print('*'*150)
            with open(filename, mode='r', encoding='utf-8') as fp:        
                    print(fp.read())
                    print('*'*150)
        except FileNotFoundError: 
            print("파일을 찾을 수 없습니다.")

# 파일경로
filename1=DIRPATH+"student_list.txt"
filename2=DIRPATH+"student_info.txt"
filename3=DIRPATH+"student_counsel.txt"

# 학생 명부 파일 불러오기 함수
def read_file_list():
    try:
        with open(filename1, mode='r', encoding='utf-8') as fp:        
                return fp.read()
    except FileNotFoundError: 
        print("파일을 찾을 수 없습니다.")

student_info_list1=read_file_list().split('\n')
cnt=0
new_student_list=[]

for stu in student_info_list1:
    stu=stu.split(',')
    stu.insert(1, cnt)
    new_student_list.append(stu)
    cnt+=1
print(new_student_list[0])
new_student_list[0][0] = new_student_list[0][0].replace("/ufeff", "")

# 학생 기본정보 파일 불러오기 함수
def read_file_info():
    try:
        with open(filename2, mode='r', encoding='utf-8') as fp:        
                return fp.read()
    except FileNotFoundError: 
        print("파일을 찾을 수 없습니다.")

student_info_list2=read_file_info().split('\n')
new_student_info=[]

for stu in student_info_list2:
    stu=stu.split(',')
    new_student_info.append(stu)
new_student_info[0][0] = new_student_info[0][0].replace("/ufeff", "")

# 학생 상담정보 파일 불러오기 함수
def read_file_counsel():
    try:
        with open(filename3, mode='r', encoding='utf-8') as fp:        
                return fp.read()
    except FileNotFoundError: 
        print("파일을 찾을 수 없습니다.")

student_info_list3=read_file_counsel().split('\n')
new_student_counsel=[]

for stu in student_info_list3:
    stu=stu.split(',')
    new_student_counsel.append(stu)

new_student_counsel[0][0] = new_student_counsel[0][0].replace("/ufeff", "")












# 프로그램 코드
print('#################################################################')
print("     학  생  관  리  프  로  그  램  을  실  행  합  니  다  .")
print('#################################################################')
print(f'총 {cnt-1}명의 학생입니다.')
print()
while 1:
    try:
        appraisal=input("선생님께서는 각 학생에 대한 평가를 순서대로 입력해주세요\n단, ','로 구분합니다. : ").split(',')
        print()
        all_stu=[]
        for i in list(range(0,cnt-1)):
            all_stu.append(Student_Manage(appraisal[i], new_student_counsel[i+1], new_student_info[i+1], new_student_list[i+1]))
        break
    except IndexError:
        print("선생님의 평가가지 수를 정확히 입력하세요!")
        print()

print(f'학생들을 명부에 저장하고 순서대로 번호를 부여하겠습니다.')
for i in list(range(0,cnt-1)):
    all_stu[i].register()
print()

while 1:
    print(f'학생을 명부에서 삭제하겠습니다.')
    inform=input("끝내시려면 q / Q 입력\n계속 진행하시려면 아무키나 입력하세요!")
    print()
    if inform not in ['q','Q']:
        try:
            stu_number_erase=int(input("지울 학생 번호: "))-1
            all_stu[stu_number_erase].erase()
            print()
        except Exception:
            print("숫자만 입력하세요!")
            print()
    else:
        break

while 1:
    print(f'학생을 명부에 저장하겠습니다.')
    inform=input("끝내시려면 q / Q 입력\n계속 진행하시려면 아무키나 입력하세요!")
    print()
    if inform not in ['q','Q']:
        try:
            stu_number_regi=int(input("저장할 학생 번호 : "))-1
            all_stu[stu_number_regi].register()
            print()
        except Exception:
            print("숫자만 입력하세요!")
            print()
    else:
        break
    print()

while 1:
    try:
        teacher=input("각 학생에 대한 담임선생님들을 순서대로 입력해주세요\n단, ','로 구분합니다. : ").split(',')
        if len(teacher) == cnt-1:
            print("각 담임선생님의 학생에 대한 평가입니다.")
            for i in list(range(0,cnt-1)):
                all_stu[i].assessment(teacher[i])
                print()
            break
        else:raise IndexError
    except IndexError:
        print("선생님의 평가가지 수를 정확히 입력하세요!")
        print()

while 1:
    q1=input("전체 명부를 보시겠습니까?(Y/N) : ")
    if q1 == 'Y':
        Student_Manage.showlist()
        break
    elif q1 == 'N':
        break
    else:
        print("잘못된 입력!!")
print()

Student_Manage.writeAsfile()
print()

while 1:
    q1=input("전체 명부 파일을 읽으시겠습니까?(Y/N) : ")
    if q1 == 'Y':
        Student_Manage.readAsfile()
        break
    elif q1 == 'N':
        break
    else:
        print("잘못된 입력!!")
print()

print('#################################################################')
print("     학  생  관  리  프  로  그  램  을  종  료  합  니  다  .")
print('#################################################################')

