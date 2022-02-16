'use strict';

const app = require('../../app.js');
const chai = require('chai');
const expect = chai.expect;
var event, context;

const sinon =  require('sinon');
const dd_lambda = require("datadog-lambda-js");

describe('Tests index', function () {
    it('verifies successful response', async () => {
        sinon.stub(dd_lambda, "sendDistributionMetric");
        
        const result = await app.lambdaHandler(event, context)

        expect(result).to.be.an('object');
        expect(result.statusCode).to.equal(200);
        expect(result.body).to.be.an('string');

        let response = JSON.parse(result.body);

        expect(response).to.be.an('object');
        expect(response.message).to.be.equal("Hello from serverless!");
    });
});
