# Python의 GUI라이브러리
from tkinter import *
import tkinter
# os: 디렉터리에서 파일을 가져오기 위함
import os
# Python Imaging Library는 이미지 처리를 위한 라이브러리.
#   이미지를 열고 수정하는 다양한 기능을 제공
# ImageTk는 Tkinter와 함께 사용할 수 있도록 이미지를 Tkinter에서 사용가능한 형식으로 변환하는 역할
from PIL import ImageTk


class Get_label:
    def __init__(self):
        self.screen = None

    # 이미지 파일명과 위치(x, y)를 받아 이미지를 배치시키고 그 label을 반환
    def image_label(self, file_name, x, y):
        # os.getcwd() : 현재 작업 디렉터리의 경로를 반환하는 함수
        # os.path.join(): 파일 경로를 생성할 때 사용되는 함수, 여러 개의 경로 구성 요소를 결합하여 전체 경로를 생성
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        photo_image = ImageTk.PhotoImage(file = final_path)
        # 이미지 파일을 tkinter에서 사용할 수 있는 형식으로 변환
        # PhotoImage 객체를 반환

        # Label 클래스를 사용하여 새로운 라벨 위젯을 생성
        image_label = Label(self.screen)

        # configure(image): Label 위젯의 속성을 설정
        image_label.configure(image = photo_image)
        image_label.image = photo_image
        
        # Label 의 위치 조정
        image_label.place(x=x, y=y)
        return image_label

    # file_name(이미지파일)과 위치(x, y), 텍스트 내용(text), 텍스트 생상(color), font(텍스트 폰트)를 입력받아 label을 만든 후
    # return 한다.
    def image_label_text(self, file_name, x, y, text, color, font):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        
        # 이미지를 PhotoImage 객체로 변환
        image = ImageTk.PhotoImage(file=final_path)
        image_label = Label(
            # 부모 위젯  |텍스트 내용 |이미지와 텍스트의 배치 방법 |텍스트 색상 | 텍스트 폰트
            self.screen, text=text, compound=tkinter.CENTER, fg=color, font=font
        )
        image_label.configure(image=image)
        image_label.image = image

        image_label.configure(text=text)

        image_label.place(x=x, y=y)
        return image_label

    # 버튼을 생성한다. 버튼의 이미지와 위치를 설정 후 클릭 시 실행시킬 이벤트(함수)를 설정시킨다.
    def image_button(self, file_name, x, y, command):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)

        image = ImageTk.PhotoImage(file=final_path)

        # Button 위젯 생성 및 속성 설정( overrelief=SOLID는 마우스를 올렸을 때 실선 형태의 테두리 표시, command는 실행시킬 이벤트)
        image_button = Button(self.screen, overrelief=SOLID, command=command)

        image_button.configure(image=image)
        image_button.image = image

        image_button.place(x=x, y=y)
        return image_button


    def image_button_text(self, file_name, x, y, command, text, color, font):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_button = Button(
            self.screen,
            overrelief=SOLID,
            command=command,
            text=text,
            compound=tkinter.CENTER, # 이미지와 텍스트 정렬(중앙)
            fg=color,
            font=font,
            justify=LEFT,   # 텍스트 정렬(왼쪽)
        )
        image_button.configure(image=image)
        image_button.image = image

        image_button.configure(text=text)

        image_button.place(x=x, y=y)
        return image_button
