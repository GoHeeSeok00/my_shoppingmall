# my_shoppingmall

## 😎 프로젝트 소개
my_shoppingmaill 프로젝트는 DRF를 이용해서 쇼핑몰을 만드는 프로젝트입니다. 

DRF를 공부하고 만든 첫 프로젝트이며 혼자서 모든것을 담당하는 개인 프로젝트입니다. 

백엔드 개발자를 지향하고 있기에 백엔드 API 설계를 중심으로 프로젝트가 진행되며 프론트적인 요소는 부트스트랩을 이용해서 간단히 구현할 예정입니다.

자세한 S.A(start Assignment)는 노션으로 작성되었으며 블로그에 매일 작업한 내용이 기록되어있습니다.
  - S.A : https://wool-cobalt-585.notion.site/DRF-dbc23bcd0c464415aba43f2a1e67df17
  - blog : https://a-littlecoding.tistory.com/category/Project/DRF_ShoppingMall

<br>

### 📎 기술스택
  - **✔**사용언어 및 프레임워크 :  Python, Django, Django rest framework

  - **✔**데이터베이스: AWS RDS(mysql)

  - **✔**API 관리 툴 : postman

  - **✔**개발툴: PyCharm
  
<br>

### 📎 브랜치 구조
  - main  
    - feature
      - user
      - product
      - order

<br>

### 📎 커밋 컨벤션
  - 규칙
    - 제목
    - 본문
    - 푸터

```
 ∙ 각 사항은 공백의 라인으로 구분한다.
 ∙ 제목 줄은 가급적 50자로 제한하고, 가능한 간결하게 작성한다.
 ∙ 제목의 시작은 대문자로 작성한다.
 ∙ 제목에 마침표를 사용하지 않는다.
 ∙ 제목은 동사로 시작하여 명령형으로 작성한다.
 ∙ 본문을 통해 무엇을, 왜 등을 설명한다.
 ∙ 본문은 72자가 넘어가는 경우 줄바꿈을 시행한다.
```

  - 자주 사용하는 단어
    - Add: 무언가 추가할 때 사용한다. 
    - Fix: 잘못된 동작을 고칠 때 주로 사용한다.
    - Remove: 삭제가 있을 때 사용한다.
    - Simplify: 코드를 단순화 했을 때 사용한다.
    - Update: Fix와 달리 원래 정상적으로 동작했지만 보완하는 개념이다.
    - Implement: 무언가 구현을 달성했을 때 사용한다. 큰 단위에 작성하면 좋다.
    - Prevent: 특정한 동작을 못하게 막을 때 사용한다.
    - Move: 코드나 파일의 이동에 사용한다.
    - Rename: 이름의 변경이 있을 때, Rename A to B의 형태로 많이 쓰인다.


<br>

### 📎 APP 별 구현 기능
  - user
      1. 회원가입
          1. 일반사용자
          2. 판매자
      2. 로그인
      3. 프로필 수정
      4. 회원 탈퇴
  - product
      1. 상품 CRUD

          카테고리, 리뷰, 옵션

  - order
      1. 장바구니
      2. 구매목록
          
<br>

### 📎 모델 설계 (ERD)
  - 사용 서비스 : ERDCloud
![ERD 1차 수정](https://user-images.githubusercontent.com/96563183/175559947-54e6b6d5-ed77-42ae-bcb7-ecf8201a848f.png)

<br>

### 📎 테이블 명세서
![SA 테이블 명세서3](https://user-images.githubusercontent.com/96563183/175560025-695c541d-3f1b-4275-9efd-938c09e105fe.png)

<br>

### 📎 API 명세서
![SA API 명세서6](https://user-images.githubusercontent.com/96563183/175560067-5e3dc916-30c6-4454-8c8c-069c4902be82.png)

