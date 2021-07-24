# Covid19VaccineRegister

### 공통 사항
1. 본 프로그램은 카카오톡 잔여백신 예약 시스템을 통해 예약을 진행합니다. 따라서 본 프로그램 이용 시 활용하는 카카오계정은 반드시 이용자 명의의 카카오톡에 로그인된 카카오계정이어야 하며, 해당 계정의 카카오톡에서 카카오톡 인증서 발급과 임의 의료기관에 대한 알림 신청을 통한 개인정보 수집, 이용, 제공 동의가 선행되어야 합니다.
2. 본 프로그램은 접종기관 검색 기능과 키워드 검색 등의 기능을 제공하지 않고, 접종기관의 의료기관코드(국민건강보험공단이 부여하는 요양기관기호) 만으로 접종기관을 선택하도록 되어 있으므로, 접종을 신청하고자 하는 의료기관의 의료기관코드을 사전에 확인하셔야 합니다.
3. 질병관리청 지침에 따라 만 18세 미만인 자, 접종대상/연령대 별 신청 기간에 사전예약을 이미 완료한 자, 이미 1차 접종을 완료한 자 및 잔여백신 신청을 성공하고 이를 취소하지 않고 접종하지 않은 자는 잔여백신 신청 대상에서 제외됩니다. 잔여백신 신청은 1차 접종에 한하며 잔여백신 신청에 성공하여 1차 접종을 받을 경우 2차 접종은 접종 주기에 따라 질병관리청에서 자동으로 예약하여 개별 통보됩니다.

### JSON Version
JSON 버전은 3가지 동작 방법에 대해 일반 버전과 Slient 버전 2가지, 총 6개 중 하나를 선택하여 이용할 수 있습니다.

1. Covid19VaccineRegisterSelectable(Slient).py - 이용자가 백신 종류를 한 가지 선택하여 해당 백신으로 접종예약을 지속적으로 전송합니다.
2. Covid19VaccineRegistermRNA(Slient).py - mRNA 백신(화이자, 모더나)을 번갈아가며 접종신청을 지속적으로 전송합니다.
3. Covid19VaccineRegisterAll(Slient).py - 모든 백신(아스트라제네카, 얀센, 화이자, 모더나)을 번갈아가며 접종신청을 지속적으로 전송합니다. 단, 만 30세 미만의 경우 바이러스벡터 백신(아스트라제네카, 얀센)의 접종이 정부 지침 상 불가능하므로 이 버전의 이용은 부적절합니다.

각 파일명 뒤에 Slient가 붙은 파일은 Slient 버전으로 접종 예약 시도 시 매회 결과를 표시하지 않고, 1,000회 마다 한 번 씩 출력하여, 출력을 위해 발생하는 지연을 줄여줍니다.

이용 전 사전에 KakaoCookies.txt 파일을 생성 후, 이 파일에 카카오계정 이용 시 발생하는 쿠키를 저장해야 합니다.

### WebDriver Version
WebDriver 버전은 MS Edge를 이용하여 브라우저를 자동으로 동작하여 지속적으로 잔여백신 접종신청을 전송합니다.
이를 위해 MS Edge 버전 92 이상이 필요합니다. 버전이 낮을 경우 오류가 발생합니다. 업데이트는 edge://settings/help를 통해 하실 수 있습니다.
또한 MS Edge Webdriver를 다운로드하여 COVID19VaccineBooking.py와 동일한 위치에 위치해야 합니다. 이는 https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ 에서 내려받을 수 있습니다.

### 이용 시 유의 사항
1. 본 프로그램 이용으로 인해 발생하는 문제는 이용자 본인에게 있습니다. 이용 시 이를 감안하여 사용해주십시오.
2. 이 프로그램이 잔여백신 성공을 보장하지 않습니다. 실패할 가능성이 있음을 감안하여 사용해주십시오.
