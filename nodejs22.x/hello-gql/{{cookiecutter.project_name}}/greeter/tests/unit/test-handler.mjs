"use strict";

import { lambdaHandler } from "../../app.mjs";
import { expect } from "chai";
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const event = require('../events/appsync.json');

const context = {};

describe("Tests Lambda handler", function () {
  it("verifies successful response", async () => {
    const result = await lambdaHandler(event, context);

    expect(result).to.be.an("string");
    expect(result).to.be.equal("Hello, User");
  });
});
