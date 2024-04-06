ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run:
	docker run -p 8083:8083 \
  	--mount type=bind,readonly,source=$(ROOT_DIR)/statemachine/test/MockConfigFile.json,destination=/home/StepFunctionsLocal/MockConfigFile.json \
  	-e SFN_MOCK_CONFIG="/home/StepFunctionsLocal/MockConfigFile.json" \
  	amazon/aws-stepfunctions-local

create:
	sed -E -e 's/\$$\{.+\}/arn:aws:lambda:us-east-1:123456789012:function:mock/' statemachine/stock_trader.asl.json > statemachine/test/mocked.test.asl.json
	aws stepfunctions create-state-machine \
		--endpoint-url http://localhost:8083 \
		--definition file://statemachine/test/mocked.test.asl.json \
		--name "StockTradingLocalTesting" \
		--role-arn "arn:aws:iam::123456789012:role/DummyRole" \
		--no-cli-pager
	rm statemachine/test/mocked.test.asl.json

happypathsellstocktest:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name HappyPathSellStockTest \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:StockTradingLocalTesting#HappyPathSellStockTest \
		--no-cli-pager

happypathbuystocktest:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name HappyPathBuyStockTest \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:StockTradingLocalTesting#HappyPathBuyStockTest \
		--no-cli-pager

checkstockerrorwithretry:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name checkStockErrorExecution \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:StockTradingLocalTesting#CheckStockRetryOnServiceExceptionTest \
		--no-cli-pager

sellstockerrorwithretry:
	aws stepfunctions start-execution \
		--endpoint http://localhost:8083 \
		--name sellStockErrorExecution \
		--state-machine arn:aws:states:us-east-1:123456789012:stateMachine:StockTradingLocalTesting#SellStockRetryOnServiceExceptionTest \
		--no-cli-pager


all: create happypathsellstocktest happypathbuystocktest checkstockerrorwithretry sellstockerrorwithretry 

happypathsellstocktest-h:
	aws stepfunctions get-execution-history \
		--endpoint http://localhost:8083 \
		--execution-arn arn:aws:states:us-east-1:123456789012:execution:StockTradingLocalTesting:HappyPathSellStockTest \
		--query 'events[?type==`TaskStateExited` && stateExitedEventDetails.name==`Record Transaction`]' \
		--no-cli-pager

checkstockerror:
	aws stepfunctions get-execution-history \
		--endpoint http://localhost:8083 \
		--execution-arn arn:aws:states:us-east-1:123456789012:execution:StockTradingLocalTesting:checkStockErrorExecution \
		--query 'events[?type==`TaskStateExited` && stateExitedEventDetails.name==`Record Transaction` ]' \
		--no-cli-pager

sellstockerror:
	aws stepfunctions get-execution-history \
		--endpoint http://localhost:8083 \
		--execution-arn arn:aws:states:us-east-1:123456789012:execution:StockTradingLocalTesting:sellStockErrorExecution \
		--query 'events[?type==`TaskStateExited` && stateExitedEventDetails.name==`Record Transaction` ]' \
		--no-cli-pager

history: happypathsellstocktest-h checkstockerror sellstockerror