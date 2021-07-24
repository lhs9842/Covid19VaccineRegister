def reg(vacCode, orgCode, Kakaocookie):
    data = {"from":"TMS","vaccineCode":vacCode,"orgCode":orgCode,"distance":"null"}
    head = {'Cookie': Kakaocookie, 'Host': 'vaccine.kakao.com', 'Content-Type': 'application/json; charset=utf-8', 'Origin':'https://vaccine.kakao.com', 'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-G975N Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36;KAKAOTALK 2309420;KAKAOTALK', 'Cache-Control': 'no-cache', 'Referer': 'https://vaccine.kakao.com/reservation/' + str(orgCode) + "?from=TMS&code=" + vacCode, 'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate, br', 'DNT': '1', 'Connection': 'keep-alive', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin'}
    req = requests.post("https://vaccine.kakao.com/api/v1/reservation", json=data, headers=head, verify = False)
    req.request
    se = req.json()
    if se['code'] == "SUCCESS":
        print(f"예약 성공, {se['organization']['openHour']['openHour']['end']}까지 방문하여 접종하셔야 합니다.")
        print(f"예약한 접종 기관은 {se['organization']['orgName']}({se['organization']['address']})입니다.")
        return True
    elif se['code'] == "ALREADY_REGISTERED":
        print("예약 기완료 계정, 카카오톡을 통해 예약 정보를 확인하세요.")
        return True
    elif se['code'] == "NOT_AVAILABLE":
        print("예약 불가 시간, 08:00 이후에 시도하세요.")
        return True
    elif se['code'] == "TIMEOUT":
        print("시간 초과, 질병관리청 서버와 연결이 원활하지 않습니다.", end="")
        return False
    else:
        print("예약 실패", end="")
        return False
print("COVID-19 잔여백신 자동 신청 프로그램 - mRNA Random Selection Version")
print("======= 주 의 사 항 =======")
print("1. 사용 전 KakaoCookies.txt 파일에 카카오톡에 사용되는 카카오계정으로 로그인 후 https://vaccine.kakao.com/detail/ 접속 시 확인되는 쿠키 값을 저장해야 합니다.")
print("2. 접종 기관을 검색하는 기능은 제공되지 않으므로, 사전에 기관코드(해당 기관의 요양기관기호)를 숙지해야 합니다.")
print("3. 본 프로그램은 카카오톡의 잔여백신 신청 페이지를 이용하여 진행됩니다. 따라서 이용하는 카카오계정의 카카오톡 지갑 인증서 발급과 임의 기관 알림 신청(이후 즉시 해제해도 무관)을 통한 개인정보 관련 동의가 선행되어야 합니다.")
print("4. 본 프로그램은 requests, json 패키지를 사용합니다. 설치되지 않은 경우 pip를 통해 설치하셔야 합니다.")
print("5. 본 프로그램은 화이자와 모더나 백신을 번갈아가며 지속적으로 신청합니다. 이를 선택하는 기능은 구현되지 않았음을 유념하시기 바랍니다.")
print("6. 본 프로그램 이용으로 발생하는 문제는 본 프로그램 개발자는 지지 않습니다. 이용자가 이용 시 발생하는 문제에 대한 모든 책임을 가짐에 유념하십시오.")
input("계속 진행하려면 <Enter> 키를 누르세요.")
import json, requests, time, warnings
warnings.filterwarnings("ignore")
fp = open("KakaoCookies.txt", "r")
Kakaocookie = fp.readline()
head = {'Cookie': Kakaocookie, 'Host': 'vaccine.kakao.com', 'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-G975N Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36;KAKAOTALK 2309420;KAKAOTALK'}
orgCode = int(input("접종을 희망하는 의료기관 요양기관기호를 입력하세요. : "))
res = requests.get("https://vaccine.kakao.com/api/v2/org/org_code/" + str(orgCode), headers = head, verify = False)
res.request
if res.status_code == 401:
    print("Cookie 값이 입력되었는지 확인하세요.")
    exit()
elif res.status_code == 404:
    print("접종기관 코드 오류입니다. \n입력한 요양기관기호가 코로나19 예방접종을 시행하는 기관이 맞는지 확인하세요.")
    exit()
elif res.status_code != 200:
    print("연결 오류입니다.\n인터넷 연결 상태를 확인하세요.")
    exit()
se = res.json()
print(se['organization']['orgName'] + "(" + se['organization']['address'] + ")으로 진행합니다.")
count = 1
while True:
    print(f"{count}회 째 시도", end=" ")
    print("화이자 : ", end="")
    if reg("VEN00013", orgCode, Kakaocookie):
        break
    print(", 모더나 : ", end="")
    if reg("VEN00014", orgCode, Kakaocookie):
        break
    print()
    count += 1
