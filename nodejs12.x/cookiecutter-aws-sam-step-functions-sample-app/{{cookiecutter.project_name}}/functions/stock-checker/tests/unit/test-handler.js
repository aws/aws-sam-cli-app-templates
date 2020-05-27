'use strict';

const app = require('../../app.js');
const chai = require('chai');
const expect = chai.expect;
var event, context;

describe('Tests Stock Checker', function () {
    it('Verifies response', async () => {
        const result = await app.lambdaHandler(event, context)

        expect(result).to.be.an('object');
        expect(result.stock_price).to.be.an('number');
        expect(result.stock_price).to.be.at.least(0);
        expect(result.stock_price).to.be.at.most(100);
    });
});
