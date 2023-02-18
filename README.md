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
  
  - 날씨, 기분에 따른 새로운 데일리 룩을 입고 싶어 하는 욕구가 있다.
  - 키워드 검색시 추천받은 스타일링이 있더라도, 쉽게 연출하기란 쉽지 않다.
  - 고객의 정보(신체 수치)와 사용자가 입력한 본인 옷장에 있는 옷을 기반으로 가능한 유사 스타일링을 추천해준다.
  - 웹, 데이터베이스, 타 사용자의 스타일링 정보와 상품 정보를 추천하여 구매를 유도할 수 있도록 한다.

</div>

## Work Log
<div>
<table>
  <th> Date </th>
  <th> Contents </th>
  <th> Goal </th>
  <th> More </th>
  <tr>
    <td> 2023-02-06 </td>
    <td> 이미지 데이터 크롤링 </td>
    <td> 
        MUSINSA Webpage에서 스타일별 이미지 데이터 크롤링
    </td>
    <td>  </td>
  </tr>
  
  <tr>
    <td> 2023-02-08 </td>
    <td> 패션 이미지 특징 추출  VGG16 </td>
    <td> Query 이미지 배경 제거 전 </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/original_img.png"/> </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/original_ret.png"/> </td>
  </tr>
  <tr>
    <td> 2023-02-09 </td>
    <td> 패션 이미지 특징 추출  VGG16 </td>
    <td> Query 이미지 배경 제거 후 </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/removed_img.png"/> </td>
    <td> <img src="https://github.com/B-JayU/CJ-Internship_23Winter/blob/main/ReadMe_IMG/removed_ret.png"/> </td>
  </tr>
  <tr>
    <td> 2023-02-14 ~ 2023-02-17 </td>
    <td> 패션 이미지 메타 데이터셋 구축 </td>
    <td> 웹 페이지내 패션 착장 이미지에서 성별, 카테고리, 태그정보 등을 수집 ( 이미지 메타 데이터 셋 구축 하기 ) </td>
    <td> </td>
  </tr>
</div> 
