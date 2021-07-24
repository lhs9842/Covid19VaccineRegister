print("COVID-19 잔여백신 자동 신청 프로그램 - User Selectable Version")
print("======= 주 의 사 항 =======")
print("1. 사용 전 KakaoCookies.txt 파일에 카카오톡에 사용되는 카카오계정으로 로그인 후 https://vaccine.kakao.com/detail/ 접속 시 확인되는 쿠키 값을 저장해야 합니다.")
print("2. 접종 기관을 검색하는 기능은 제공되지 않으므로, 사전에 기관코드(해당 기관의 요양기관기호)를 숙지해야 합니다.")
print("3. 본 프로그램은 카카오톡의 잔여백신 신청 페이지를 이용하여 진행됩니다. 따라서 이용하는 카카오계정의 카카오톡 지갑 인증서 발급과 임의 기관 알림 신청(이후 즉시 해제해도 무관)을 통한 개인정보 관련 동의가 선행되어야 합니다.")
print("4. 본 프로그램은 requests, json 패키지를 사용합니다. 설치되지 않은 경우 pip를 통해 설치하셔야 합니다.")
print("5. 본 프로그램 이용으로 발생하는 문제는 본 프로그램 개발자는 지지 않습니다. 이용자가 이용 시 발생하는 문제에 대한 모든 책임을 가짐에 유념하십시오.")
input("계속 진행하려면 <Enter> 키를 누르세요.")
import json, requests, time, warnings
warnings.filterwarnings("ignore")
fp = open("KakaoCookies.txt", "r")
Kakaocookie = fp.readline()
head = {'Cookie': Kakaocookie, 'Host': 'vaccine.kakao.com'}
orgCode = int(input("접종을 희망하는 의료기관 요양기관기호를 입력하세요. : "))
res = requests.get("https://vaccine.kakao.com/api/v2/org/org_code/" + str(orgCode), headers = head, verify = False)
res.request
if res.status_code == 401:
    print("Cookie 값이 입력되었는지 확인하세요.")
    exit()
elif res.status_code == 404:
    print("접종기관 코드 오류입니다. \n입력한 요양기관기호가 코로나19 예방접종을 시행하는 기관이 맞는지 확인하세요.")
if res.status_code != 200:
    print("연결 오류입니다.\n인터넷 연결 상태를 확인하세요.")
    exit()
se = res.json()
print(se['organization']['orgName'] + "(" + se['organization']['address'] + ")으로 진행합니다.")
while True:
    select = input("접종을 희망하는 백신 종류를 선택하세요. \n1. 아스트라제네카 2. 얀센 3. 화이자 4. 모더나 5. 노바백스\n선택 : ")
    vacCode = {"1":"VEN00015", "2":"VEN00016", "3":"VEN00013", "4":"VEN00014", "5":"VEN00017"}.get(select, " ")
    if vacCode != " ":
        break
    print("잘못 입력했습니다.", end=" ")
count = 1
flag  = 0
while True:
    if count % 2 == 1:
        data = {"from":"TMS","vaccineCode":vacCode,"orgCode":orgCode,"distance":"null"}
        head = {'Cookie': Kakaocookie, 'Host': 'vaccine.kakao.com', 'Content-Type': 'application/json; charset=utf-8', 'Origin':'https://vaccine.kakao.com', 'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-G975N Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36;KAKAOTALK 2309420;KAKAOTALK', 'Cache-Control': 'no-cache', 'Referer': 'https://vaccine.kakao.com/reservation/' + str(orgCode) + "?from=TMS&code=" + vacCode, 'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate, br', 'DNT': '1', 'Connection': 'keep-alive', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin'}
    else:
        data = {"from":"Map","vaccineCode":vacCode,"orgCode":orgCode,"distance":"null"}
        head = {'Cookie': Kakaocookie, 'Host': 'vaccine.kakao.com', 'Content-Type': 'application/json; charset=utf-8', 'Origin':'https://vaccine.kakao.com', 'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-G975N Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36;KAKAOTALK 2309420;KAKAOTALK', 'Cache-Control': 'no-cache', 'Referer': 'https://vaccine.kakao.com/reservation/' + str(orgCode) + "?from=Map&code=" + vacCode, 'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate, br', 'DNT': '1', 'Connection': 'keep-alive', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin'}
    print(f"{count}회 째 시도 중...", end=" ")
    res = requests.post("https://vaccine.kakao.com/api/v1/reservation", json=data, headers=head, verify = False)
    res.request
    se = res.json()
    if se['code'] == "SUCCESS":
        print(f"예약 성공, {se['organization']['openHour']['openHour']['end']}까지 방문하여 접종하셔야 합니다.")
        print(f"예약한 접종 기관은 {se['organization']['orgName']}({se['organization']['address']})입니다.")
        break
    elif se['code'] == "ALREADY_REGISTERED":
        print("예약 기완료 계정, 카카오톡을 통해 예약 정보를 확인하세요.")
        break
    elif se['code'] == "NO_SUITABLE":
        print("접종 불가 연령, 화이자는 만 18세 이상, 아스트라제네카, 얀센은 만 30세 이상만 접종 가능합니다.")
        break
    elif se['code'] == "NOT_AVAILABLE":
        print("예약 불가 시간, 08:00 이후에 시도하세요.")
        break
    elif se['code'] == "TIMEOUT":
        print("시간 초과, 질병관리청 서버와 연결이 원활하지 않습니다.")
        continue
    res = requests.get("https://vaccine.kakao.com/api/v2/org/org_code/" + str(orgCode), headers = head, verify = False)
    res.request
    se = res.json()
    if se['status'] == "INPUT_YET":
        print("잔여백신 미입력")
    elif se['status'] == "EXHAUSTED":
        print("잔여백신 없음")
        if flag == 0:
            while True:
                resel = input("계속 시도하시겠습니까? (Y/n): ")
                if resel == 'Y' or resel == 'y':
                    flag = 1
                    break
                elif resel == 'N' or resel == 'n':
                    flag = -1
                    break
                print("잘못 입력하셨습니다.", end=" ")
            if flag == -1:
                break
    elif se['status'] == "CLOSED":
        if se['organization']['openHour']['dayOff']:
            print("접종 기관 미접종일, 해당 접종 기관은 금일 접종을 하지 않습니다.")
        else:
            print(f"접종 기관 접종 시간 마감, 해당 접종 기관의 접종 시간은 {se['organization']['openHour']['openHour']['end']}까지입니다.")
        break
    count += 1
    time.sleep(0.1)
