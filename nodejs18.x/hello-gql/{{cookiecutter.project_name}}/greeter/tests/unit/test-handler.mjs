"use strict";

import { lambdaHandler } from "../../app.mjs";
import { expect } from "chai";

import event from "../events/appsync.json" assert { type: "json" };

const context = {};

describe("Tests Lambda handler", function () {
  it("verifies successful response", async () => {
    const result = await lambdaHandler(event, context);

    expect(result).to.be.an("string");
    expect(result).to.be.equal("Hello, User");
  });
});
