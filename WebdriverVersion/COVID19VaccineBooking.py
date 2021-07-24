print("COVID-19 백신 예약 자동화 프로그램")
print("본 프로그램은 Selenium 패키지가 사용합니다. 실행해본 적 없는 패키지라면 명령 프롬프트를 열어 \"pip install selenium\"을 실행하세요.")
print("MS Edge 버전 92 이상의 설치를 요구합니다. Legucy Edge나 버전 91 이하를 이용 중이라면 업데이트 후 이용해주세요.(Edge 브라우저로 edge://settings/help 접속 후 확인)")
input("준비가 완료되면 <Enter>키를 눌러주세요...")
import time
from selenium import webdriver
orgCode = int(input("접종기관 코드 : "))
vacCode = ["VEN00015", "VEN00016", "VEN00013", "VEN00014", "VEN00017"]
print("접종 신청하려는 백신을 선택하세요\n1. 아스트라제네카 2. 얀센 3. 화이자 4. 모더나 5. 노바백스")
while True:
    vacSel = int(input("선택 : ")) - 1
    if vacSel > 0 and vacSel < 6:
        break
    print("잘못 선택하셨습니다.", end=" ")
print("Microsoft Edge가 실행되면 카카오톡의 카카오계정으로 로그인해주세요. 열리는 Edge는 일반적으로 실행되는 Edge와 로그인 정보 등 브라우저 내 저장되는 정보가 공유되지 않습니다.")
print("\"Microsodt Edge가 자동화된 테스트 소프트웨어에 의해 제외되고 있습니다.\"라는 문구가 나타나는 Edge 창이 나타납니다.")
print("IDLE 등으로 실행한 경우 본 메시지 표출 직후 나타나는 명령 프롬프트 창을 절대 닫지 마십시오. 본 프로그램이 브라우저를 제어하기 위해 필요한 프로그램입니다. 프로그램이 정상 종료될 경우 Edge와 명령 프롬프트가 함께 종료됩니다.")
driver = webdriver.Edge(executable_path='msedgedriver.exe')
driver.get(url="https://accounts.kakao.com/login?continue=https%3A%2F%2Fvaccine.kakao.com%2Fdetail%2F" + str(orgCode))
while True:
    if driver.current_url.find("https://vaccine.kakao.com/detail") != -1:
        break
while True:
    sel = input("브라우저에 표출된 접종기관 정보가 예약하고자 하는 접종기관이 맞습니까? (Y/n) : ")
    sel = sel.upper()
    if sel == "Y" or sel == "N":
        break
    print("잘못 입력했습니다. ", end="")
if sel == "N":
    driver.close()
    exit()
print("예약 접수를 시작합니다.")
print("도중에 중단하려면 브라우저를 닫지 마시고 Ctrl+C를 이 창에서 누르세요.")
while True:
    driver.get(url="https://vaccine.kakao.com/reservation/" + str(orgCode) +"?from=TMS&code=" + vacCode[vacSel])
    while True:
        if driver.current_url.find("?from=TMS") == -1:
            break
    code = driver.current_url
    if code.find("complete") != -1:
        print("예약 성공. 예약 정보는 브라우저를 통해 확인하세요.")
        print("엣지 브라우저를 직접 종료하지 마시고 여기에 엔터를 치세요. Edge가 종료되고 쌓인 정보가 정상적으로 삭제됩니다.")
        input("엔터를 치시면 종료합니다.")
        break
    if code.find("ALREADY_REGISTERED") != -1 or code.find("NO_SUITABLE") != -1 or code.find("NOT_AVAILABLE") != -1:
        print("예약 불가 오류 발생. 오류 내용은 브라우저를 통해 확인하세요.")
        print("엣지 브라우저를 직접 종료하지 마시고 여기에 엔터를 치세요. Edge가 종료되고 쌓인 정보가 정상적으로 삭제됩니다.")
        input("엔터를 치시면 종료합니다.")
        break
driver.close()
