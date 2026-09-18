SELECT * FROM mysql.user;

# 주석
-- 주석(대표주석)

# database 확인 - 테이블을 모아놓은 저장소
SHOW databases;

# CREATE 로 만든 녀석은 대부분 DROP 으로 삭제되고 ALTER 로 수정된다.
-- CREATE DATABASE [이름];	<- 만들기
-- DROP DATABASE [이름];		<- 삭제
-- USE [데이터베이스 이름];		<- 사용(들어가기)

-- mydb 라는 database 만들어보기, 그리고 사용하기
CREATE DATABASE mydb;
USE mydb;