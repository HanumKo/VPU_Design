import random

# 양수 BF16 데이터를 생성하는 함수 (상위 1비트는 부호 비트로, 이를 0으로 설정)
def generate_bf16_data():
    return random.randint(0x0000, 0x7FFF)  # 상위 비트가 0인 양수 범위 (0x0000 ~ 0x7FFF)

# BF16 데이터를 96개 생성하고 파일에 쓰는 함수
def create_bf16_file(filename, num_lines=100):
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            bf16_data = [f"{generate_bf16_data():04x}" for _ in range(96)]  # 96개의 BF16 데이터 생성
            file.write(" ".join(bf16_data) + "\n")  # 한 줄에 96개 데이터를 공백으로 구분하여 작성

# 파일 생성
create_bf16_file("bf16_numbers_for_sqrt.txt")
