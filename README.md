# CJ-Internship_23Winter_Fashion Retrieval
2023년 CJ Olive Networks 동계 인턴십_패션 조합 추천 시스템

![header](https://capsule-render.vercel.app/api?type=Rounded&color=gradient&height=100&section=footer&text=2023년%20CJ%20Olive%20Networks%20동계인턴십%20Image%20Retrieval%20&fontSize=30)

## Motivation
<div>
  <table>
    <tr>
      <td><img alt="아우터" src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/Outer.png" /></td>
      <td><img alt="상의" src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/Upper.png" /></td>
      <td><img alt="하의" src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/Pants.png" /></td>
      <td><img alt="신발" src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/Shoes.png" /></td>
      <td><img alt="악세사리" src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/Acc.png" /></td>
    <tr>
  </table>
  
  - 개인의 외적인 단점을 보완하거나 날씨, 기분에 따른 새로운 데일리 룩을 입고 싶어 하는 욕구가 있다.
  - 새로운 분위기를 연출해보고 싶은 사람들이 존재한다.
  - 키워드 검색시 추천받은 스타일링이 있더라도, 쉽게 연출하기란 쉽지 않다.
  - 고객의 정보(신체 수치)와 사용자가 입력한 본인 옷장에 있는 옷을 기반으로 가능한 유사 스타일링을 추천해준다.
  - 웹, 데이터베이스, 타 사용자의 스타일링 정보와 상품 정보를 추천하여 구매를 유도할 수 있도록 한다.
  - Goal : 사용자가 가지고 있는 옷 또는 질의하는 이미지와 잘 어울리는 스타일링을 추천해줄 수 있다

</div>

## TO DO LIST

- [x] 이미지 데이터 셋 확보
- [x] 이미지 메타 데이터 수집
- [x] 이미지 전처리 (배경제거)
- [x] 키워드 기반 유사 패션 이미지 검색 엔진 구현
- [x] 이미지 특징추출 모델 학습
- [x] 간단한 검색 웹 API 구현

- [ ] 패션 이미지 segmentation
- [ ] 패션 이미지 detection
- [ ] CNN 특징 추출 모델 개선
- [ ] Private Digital Closet system 구현



## Work Log
<div>
<table>
  <th> Date </th>
  <th> Contents </th>
  <th> Goal </th>
  <th> More </th>
  <tr>
    <td> 01-30 ~ 02-01 </td>
    <td> Fashion Recommedation System 기획 </td>
    <td> 
        AI 기반의 패션 스타일링 추천 시스템을 기획
    </td>
    <td colspan=2> </td>
  </tr>
  <tr>
    <td> 02-02 ~ 02-03 </td>
    <td> 이미지 데이터 셋 구축 </td>
    <td> 
        MUSINSA Webpage에서 스타일별 이미지 데이터 크롤링
    </td>
    <td colspan=2> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/crawling.png"/> </td>
  </tr>
  
  <tr>
    <td> 02-06 ~ 02-07 </td>
    <td> 패션 이미지 특징 추출  VGG16 </td>
    <td> Query 이미지 배경 제거 전 </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/original_img.png"/> </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/original_ret.png"/> </td>
  </tr>
  <tr>
    <td> 02-08 ~ 02-09 </td>
    <td> 이미지 배경 제거 </td>
    <td> 
        bgrem 배경 제거와 colorthief 통해 이미지 내 주요 색상 추출
    </td>
    <td colspan=2> </td>
  </tr>
  <tr>
    <td> 02-10 </td>
    <td> 패션 이미지 특징 추출  VGG16 </td>
    <td> Query 이미지 배경 제거 후 </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/removed_img.png"/> </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/removed_ret.png"/> </td>
  </tr>
  <tr>
    <td> 02-13 ~ 02-15 </td>
    <td> 패션 이미지 메타 데이터셋 구축 </td>
    <td> 웹 페이지내 패션 착장 이미지에서 성별, 카테고리, 태그정보 등을 수집 ( 이미지 메타 데이터 셋 구축 하기 ) </td>
    <td colspan=2> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/metadata.png"/></td>
  </tr>
  <tr>
    <td> 02-16 ~ 02-17 </td>
    <td> 키워드 기반 정보 검색 기능 구현 </td>
    <td> 웹 페이지내 패션 착장 이미지에서 성별, 카테고리, 태그정보 등을 수집 ( 이미지 메타 데이터 셋 구축 하기 ) </td>
    <td colspan=2> </td>
  </tr>
  <tr>
    <td> 02-20 ~ 02-22 </td>
    <td> 패션 추천 시스템 API 설계 및 구현 및 발표 준비</td>
    <td> 성별 및 계절 필터링 기능 제공, 쿼리 이미지 입력, 키워드 입력 UI 설계 </td>
    <td colspan=2> </td>
  </tr>
  <tr>
    <td> 02-23 </td>
    <td> CTO + AI 연구소 미디어 부서 발표 </td>
    <td> 
        CJ OliveNetworks Internship AI 연구소 Small Presentation (with CTO)
    </td>
    <td colspan=2>  </td>
  </tr>
  <tr>
    <td> 02-24 </td>
    <td> Internship 최종 발표 </td>
    <td> 
        CJ OliveNetworks Internship 4주간의 인턴 체험기 최종 발표
    </td>
    <td colspan=2>  </td>
  </tr>
</div> 
