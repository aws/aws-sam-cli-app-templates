PWSH = pwsh
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
ARTIFACT_DIR:=$(shell pwsh -Command '"$$(Join-Path -Path '$(ROOT_DIR)' -ChildPath "../../" -Resolve).aws-sam/build/HelloWorldFunction"')

build-HelloWorldFunction: 
	$(PWSH) -Command 'Import-Module -Name AWSLambdaPSCore; New-AWSPowerShellLambdaPackage -ScriptPath '$(ROOT_DIR)/Function.ps1' -OutputPackage "$(ARTIFACT_DIR)/Function.zip"'
	unzip $(ARTIFACT_DIR)/Function.zip -d $(ARTIFACT_DIR)
	rm $(ARTIFACT_DIR)/Function.zip
	