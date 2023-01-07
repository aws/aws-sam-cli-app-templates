'use strict';

import { lambdaHandler } from '../../app.mjs';
import { expect } from 'chai';
var event, context;

describe('Tests Stock Checker', function () {
    it('Verifies response', async () => {
        const result = await lambdaHandler(event, context)

        expect(result).to.be.an('object');
        expect(result.stock_price).to.be.an('number');
        expect(result.stock_price).to.be.at.least(0);
        expect(result.stock_price).to.be.at.most(100);
    });
});
