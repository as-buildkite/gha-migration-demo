/** @type {import('jest').Config} */
module.exports = {
  preset: "ts-jest",
  testEnvironment: "node",
  roots: ["<rootDir>/frontend/src"],
  testMatch: ["**/*.test.ts"],
};
