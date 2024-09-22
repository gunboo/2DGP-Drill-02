import turtle

# 화면 설정
turtle.setup(600, 600)
turtle.bgcolor("white")
turtle.title("거북이 WASD 이동 및 선 그리기")

# 거북이 생성 및 설정
turtle.shape("turtle")  # 거북이 모양 설정
turtle.color("green")   # 거북이 색상 설정
turtle.pendown()        # 펜을 내린 상태로 시작 (이동 시 선을 그림)

# 이동 및 스탬프 함수
def move_up():
    turtle.setheading(90)  # 위쪽 방향
    y = turtle.ycor()
    turtle.sety(y + 50)
    turtle.stamp()  # 현재 위치에 스탬프 찍기

def move_down():
    turtle.setheading(270)  # 아래쪽 방향
    y = turtle.ycor()
    turtle.sety(y - 50)
    turtle.stamp()  # 현재 위치에 스탬프 찍기

def move_left():
    turtle.setheading(180)  # 왼쪽 방향
    x = turtle.xcor()
    turtle.setx(x - 50)
    turtle.stamp()  # 현재 위치에 스탬프 찍기

def move_right():
    turtle.setheading(0)  # 오른쪽 방향
    x = turtle.xcor()
    turtle.setx(x + 50)
    turtle.stamp()  # 현재 위치에 스탬프 찍기

def restart():
    turtle.clear()  # 모든 선 및 거북이의 경로 지우기
    turtle.penup()  # 거북이를 처음 위치로 이동할 때 선을 그리지 않음
    turtle.goto(0, 0)  # 거북이를 원래 위치로 이동
    turtle.pendown()  # 다시 펜을 내리고 이동

# 키보드 입력 연결
turtle.listen()
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(restart, "Escape")  # "Escape" 키로 다시 시작

# 메인 루프
turtle.mainloop()
