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
![ERD](https://user-images.githubusercontent.com/96563183/175491843-8208cebf-d26c-44ea-b0bc-d9288472318e.png)


<br>

### 📎 테이블 명세서
![SA 테이블 명세서](https://user-images.githubusercontent.com/96563183/175493018-9b8b064a-c1d4-4812-9049-d59c90f435e0.png)

<br>

### 📎 API 명세서
![SA API 명세서2](https://user-images.githubusercontent.com/96563183/175494370-68fd474f-0848-4c3b-ac24-9f6037a4ebdd.png)
