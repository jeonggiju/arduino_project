from tkinter import *
from tkinter import messagebox
import os
import tkinter.messagebox
from Make_label import Get_label
from db import *
import pyglet


img_path = os.path.join(os.getcwd())


class Gui:
    def __init__(self):
        self.screen = Tk() # GUI 창 생성
        self.screen.iconbitmap("./images/logo.ico")
        self.screen.title("방문록 자동 입력 프로그램")
        self.screen.geometry("804x804")
        self.screen.resizable(width=False, height=False)
        self.center_window(804, 804)
        pyglet.font.add_file("./fonts/GodoM.otf")
        pyglet.font.add_file("./fonts/HoonDdukbokki.ttf")
        self.main_screen()
        self.screen.mainloop()
        # main loop를 실행하여 GUI 이벤트 처리 및 프로그램 실행

    def no_action(self):
        pass

    # 윈도우에 속한 모든 자식 위젯을 파괴
    def destroy(self):
        list1 = self.screen.place_slaves()
        #현재 Tkinter 윈도우에 속한 모든 자식 위젯을 반환하여 list1에 할당,
        # place_slaves 메서드는 배치 매니저에 의해 배치된 자식 위젯을 반환
        for l in list1: #반환된 자식 위젯 목록을 반복
            l.destroy() #각 자식 위젯에 대해 destroy 메서드를 호출하여 해당 위젯을 파괴

    # 주어진 너비와 높이의 윈도우를 화면 중앙에 정확하게 배치하는 데 사용
    def center_window(self, width, height):
        screen_width = self.screen.winfo_screenwidth() #현재 화면의 너비
        screen_height = self.screen.winfo_screenheight() # 높이
        x = (screen_width / 2) - (width / 2) #화면 중앙에 위치할 x 좌표를 계산
        y = (screen_height / 2) - (height / 2) - 25 #(-25)윈도우가 상단에 위치하도록 하기 위함
        self.screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
        #계산한 x, y 좌표를 이용하여 윈도우의 geometry를 설정

    # 첫 화면(메인 스크린)을 구성
    def main_screen(self):
        #현재 화면에 있는 모든 자식 위젯들을 파괴하여 화면을 초기화
        self.destroy()
        self.screen_num = 0
        self.sort_num = 0
        self.sort_color = 0

        # 배경이미지 표시
        Main_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "./images/main_bg.png"), 0, 0
        )

        # 회원가입 버튼 생성 -> apply_screan 함수 호출
        User_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/btn1.png"),
            20,
            290,
            self.apply_screen,
        )

        # 방명록보기 버튼 생성 -> reload 함수 호출
        List_button = Get_label.image_button(
            self, os.path.join(img_path, "./images/btn2.png"), 280, 290, self.reload
        )

        # 종료 버튼 생성 -> quit 함수 호출
        Exit_button = Get_label.image_button(
            self, os.path.join(img_path, "./images/btn3.png"), 540, 290, self._quit
        )

        # 마지막 유저 정보 가져옴
        self.user_data = get_last_user()

        # Date, Time, Name, Content(소속)의 리스트를 가져옴
        self.list_data = get_last_list() #

        # 사용자 정보를 표시하는 라벨 생성
        Data_1 = Get_label.image_label_text(
            self,
            os.path.join(img_path, "./images/Data.png"),
            32,
            390,
            f"{self.user_data[1]} 소속 \n\n {self.user_data[0]}님 \n\n 회원가입 되셨습니다. ", # 텍스트
            "#472f91", # 색
            ("고도 M", 24), # 폰트
        )

        # 방문 목록을 표시하는 라벨 생성
        Data_2 = Get_label.image_label_text(
            self,
            os.path.join(img_path, "./images/Data.png"),
            422,
            390,
            f"{self.list_data[2]} 님 \n\n {self.list_data[0]} \n\n {self.list_data[1]} \n\n 방문하셨습니다.",
            "#472f91",
            ("고도 M", 24),
        )

    # 회원가입 화면 구성
    def apply_screen(self):
        self.screen_num = 1 #변수를 1로 설정
        self.destroy() #화면 초기화

        # 회원가입의 배경화면 설정
        Apply_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "./images/apply_bg.png"), 0, 0
        )

        # '회원가입'의 '돌아가기' 버튼 구성 -> main_screan 함수 호출
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/return.png"),
            580,
            30,
            self.main_screen,
        )
        # 이름 입력하는 텍스트 박스
        self.name_entry = tkinter.Text(self.screen, width=10, height=1)
        self.name_entry.place(x=200, y=450)
        self.name_entry.config(font=("고도 M", 45))

        # 이름 입력을 확정하는 버튼 -> commit1 함수 설정
        self.name_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/commit.png"),
            560,
            450,
            self.commit1,
        )

        # 소속 입력 텍스트박스 생성
        self.content_entry = tkinter.Text(self.screen, width=10, height=1)
        self.content_entry.place(x=200, y=570)
        self.content_entry.config(font=("고도 M", 45))

        # 소속 입력 버튼 생성 -> commit2 함수 설정
        self.content_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/commit.png"),
            560,
            570,
            self.commit2,
        )

        # '다시 입력하기' 버튼 생성 -> apply_screen 함수 설정
        recommit_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/recommit.png"),
            250,
            700,
            self.apply_screen,
        )

    #name 버튼 함수
    def commit1(self):
        #name_entry 텍스트 박스 비활성화
        self.name_entry.config(state="disabled")
        #name_button 버튼 비활성화
        self.name_button.config(state="disabled")

        # 변수를 1증가->다음 단계의 화면으로 진행
        self.screen_num += 1

        # name_entry 텍스트박스의 값 가져오기 (1.0 : 시작 지점, end : 끝 지점)
        self.name = self.name_entry.get("1.0", "end")
        # 가져온 텍스트에서 양쪽 공백을 제거
        self.name = self.name.strip()

    # content 함수 설정
    def commit2(self):
        self.content_entry.config(state="disabled")
        self.content_button.config(state="disabled")
        self.screen_num += 1
        self.content = self.content_entry.get("1.0", "end")
        self.content = self.content.strip()

    # 방명록 보기 버튼의 함수
    def reload(self): #db에서 새로운 방문 목록을 가져와 화면에 표시(갱신)
        self.list = get_list("Date", self.sort_num) #date를 기준으로 정렬한 방문 목록 반환
        self.list_screen1() #방문목록을 표시하는 화면 생성

    # 방명록 목록 화면 구성
    def list_screen1(self):
        self.destroy() #초기화
        self.screen_num = 5
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "./images/list_bg.png"), 0, 0
        )

        # '돌아가기' 버튼 구성
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/return.png"),
            580,
            30,
            self.main_screen,
        )

        #방문 목록 페이지 변경하기 위한 좌우 화살표 버튼 생성
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/left.png"),
            300,
            40,
            self.no_action,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/right.png"),
            400,
            40,
            self.list_screen2,
        )

        #초기에는 좌우 화살표 비활성화
        left_button.config(state="disabled")
        right_button.config(state="disabled")

        # 버튼 구성
        # 차례 번호 구성 -> no_action 함수 설정
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li1.png"),
            12,
            133,
            self.no_action,
            f"",
            "#ffffff",
            ("고도 M", 13,"bold"),
        )

        # 날짜 구성 -> sort1 함수 설정
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li2.png"),
            62,
            133,
            self.sort1,
            f"날짜",
            "#ffffff",
            ("고도 M", 13,"bold"),
        )

        # 시간 설정 -> sort2 함수 설정
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li3.png"),
            272,
            133,
            self.sort2,
            f"시간",
            "#ffffff",
            ("고도 M", 13,"bold"),
        )

        # 이름 설정 -> sort3 함수 설정
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li4.png"),
            482,
            133,
            self.sort3,
            f"이름",
            "#ffffff",
            ("고도 M", 13,"bold"),
        )

        # 소속 구성 -> sort4 구성
        self.Intro5 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li5.png"),
            612,
            133,
            self.sort4,
            f"소속",
            "#ffffff",
            ("고도 M", 13,"bold"),
        )
        
        #정렬 방식에 따라 버튼의 색 변경
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")

        length = int(check_seq_list()) #현재 방문 목록의 총 개수 확인
        
        if length > 15: #방문 목록이 15보다 크면 우측 화살표 버튼을 활성화
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length

        # 방문 목록의 길이에 따라 반복문 실행, 각 항목의 라벨 생성
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li1-1.png"),
                12,
                173 + (40 * i),
                f"{i+1}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li2-1.png"),
                62,
                173 + (40 * i),
                f"{self.list[i][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li3-1.png"),
                272,
                173 + (40 * i),
                f"{self.list[i][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li4-1.png"),
                482,
                173 + (40 * i),
                f"{self.list[i][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            li5 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li5-1.png"),
                612,
                173 + (40 * i),
                f"{self.list[i][3]}",
                "#472f91",
                ("고도 M", 12),
            )

    # 두 번째 방명록
    def list_screen2(self):
        self.destroy() #화면 초기화
        List_Screen_background = Get_label.image_label( #배경이미지 표시
            self, os.path.join(img_path, "./images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button( #메인화면으로 돌아가는 버튼 생성
            self,
            os.path.join(img_path, "./images/return.png"),
            580,
            30,
            self.main_screen,
        )
        #좌우 화살표 버튼 생성
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/left.png"),
            300,
            40,
            self.list_screen1,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/right.png"),
            400,
            40,
            self.list_screen3,
        )
        right_button.config(state="disabled") #초기에 우측 화살표 비활성화
        #정렬방식 나타내는 버튼 생성
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li1.png"),
            12,
            133,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li2.png"),
            62,
            133,
            self.sort1,
            f"날짜",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li3.png"),
            272,
            133,
            self.sort2,
            f"시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li4.png"),
            482,
            133,
            self.sort3,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li5.png"),
            612,
            133,
            self.sort4,
            f"소속",
            "#472f91",
            ("고도 M", 12),
        )
        #정렬방식에 따라 버튼 색 변경
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 30: #30개 보다 많으면 우측 화살표 버튼 활성화
            length1 = 15
            right_button.config(state="normal")
        else: #그렇지 않으면 length1을 length - 15로 설정하여 나머지 항목을 표시
            length1 = length - 15
        for i in range(length1): #방문 목록의 길이에 따라 반복문을 실행하고, 각 항목에 대한 라벨을 생성하여 화면에 표시
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li1-1.png"),
                12,
                173 + (40 * i),
                f"{i+16}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li2-1.png"),
                62,
                173 + (40 * i),
                f"{self.list[i+15][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li3-1.png"),
                272,
                173 + (40 * i),
                f"{self.list[i+15][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li4-1.png"),
                482,
                173 + (40 * i),
                f"{self.list[i+15][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            li5 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li5-1.png"),
                612,
                173 + (40 * i),
                f"{self.list[i+15][3]}",
                "#472f91",
                ("고도 M", 12),
            )

    # 세 번째 방명록
    def list_screen3(self): #현재 페이지에서 다음 페이지로 이동하여 방문 목록을 표시하는 화면을 갱신
        self.destroy()
        List_Screen_background = Get_label.image_label(
            self, os.path.join(img_path, "./images/list_bg.png"), 0, 0
        )
        return_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/return.png"),
            580,
            30,
            self.main_screen,
        )
        left_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/left.png"),
            300,
            40,
            self.list_screen2,
        )
        right_button = Get_label.image_button(
            self,
            os.path.join(img_path, "./images/right.png"),
            400,
            40,
            self.no_action,
        )
        right_button.config(state="disabled")
        self.Intro1 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li1.png"),
            12,
            133,
            self.no_action,
            f"",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro2 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li2.png"),
            62,
            133,
            self.sort1,
            f"날짜",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro3 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li3.png"),
            272,
            133,
            self.sort2,
            f"시간",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro4 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li4.png"),
            482,
            133,
            self.sort3,
            f"이름",
            "#472f91",
            ("고도 M", 12),
        )
        self.Intro5 = Get_label.image_button_text(
            self,
            os.path.join(img_path, "./images/li5.png"),
            612,
            133,
            self.sort4,
            f"소속",
            "#472f91",
            ("고도 M", 12),
        )
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        length = int(check_seq_list())
        if length > 45:
            length1 = 15
            right_button.config(state="normal")
        else:
            length1 = length - 30
        for i in range(length1):
            li1 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li1-1.png"),
                12,
                173 + (40 * i),
                f"{i+31}",
                "#472f91",
                ("고도 M", 12),
            )
            li2 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li2-1.png"),
                62,
                173 + (40 * i),
                f"{self.list[i+30][0]}",
                "#472f91",
                ("고도 M", 12),
            )
            li3 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li3-1.png"),
                272,
                173 + (40 * i),
                f"{self.list[i+30][1]}",
                "#472f91",
                ("고도 M", 12),
            )
            li4 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li4-1.png"),
                482,
                173 + (40 * i),
                f"{self.list[i+30][2]}",
                "#472f91",
                ("고도 M", 12),
            )
            li5 = Get_label.image_label_text(
                self,
                os.path.join(img_path, "./images/li5-1.png"),
                612,
                173 + (40 * i),
                f"{self.list[i+30][3]}",
                "#472f91",
                ("고도 M", 12),
            )

    # 날짜 기준 정렬
    def sort1(self):
        self.sort = "Date"
        self.list = get_list("Date", self.sort_num)
        self.sort_color = 1
        fir = self.list_screen1()

    # 시간 기준 정렬
    def sort2(self):
        self.sort = "Time"
        self.list = get_list("Time", self.sort_num)
        self.sort_color = 2
        fir = self.list_screen1()

    # 이름 기준 정렬
    def sort3(self):
        self.sort = "Name"
        self.list = get_list("Name", self.sort_num)
        self.sort_color = 3
        fir = self.list_screen1()

    # 소속 기준 정렬
    def sort4(self):
        self.sort = "Content"
        self.list = get_list("Content", self.sort_num)
        self.sort_color = 4
        fir = self.list_screen1()

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.screen.quit()
            self.screen.destroy()
            exit()

    def change_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")

if __name__ == "__main__":
    a = Gui()
