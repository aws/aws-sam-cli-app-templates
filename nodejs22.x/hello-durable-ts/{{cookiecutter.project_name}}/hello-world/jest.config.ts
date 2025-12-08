export default {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testMatch: ['**/tests/unit/*.test.ts'],
  transform: {
    '^.+\\.ts$': 'ts-jest'
  },
};
