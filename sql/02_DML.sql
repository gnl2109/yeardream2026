/* 문자열 캐릭터셋 변경 (latin1 -> utf8mb4)
sudo

[mysqld]
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
추가 후 :wq

sudo systemctl restart mariadb
systemctl status mariadb
*/

USE mydb;
DESC employees;
-- INSERT
-- INSERT INTO [테이블명]([컬럼명,...])VALUES([값들,...]);
INSERT INTO employees(
	emp_no, first_name, family_name, email, mobile, salary, depart_no, commission
)VALUES(
	111,'지훈','김','zerObox@naver.com','01020343054','90000000','dev001',90
);

-- UPDATE

-- DELETE

-- UPSERT(나중에 자세하게...)