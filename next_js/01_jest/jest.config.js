// next 와 jest 를 연동
const nextJest = require("next/jest");

// 여기에 있는 설정 파일들을 읽어라(설정파일들은 이 공간에 다 있어)
const createJestConfig = nextJest({dir:'./'});

const jestConfig = {
    testEnvironment: 'test-environment-jsdom',
    moduleNameMapper:{
        '^@/(.*)$':'<rootDir>/src/$1' // 정규표현식 활용
    }
};

module.exports = createJestConfig(jestConfig);