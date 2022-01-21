from tests.integration.base import Base, LOG, run_command

import ipaddress
import json
import os

from pathlib import Path
from typing import Dict, Any, Optional

import pytest

# NOTE: Using `samdev` as against `sam` in cmdlist enables test with samcli in your dev environment.
SAM_CLI_EXECUTABLE = "samdev" if os.getenv("SAM_CLI_DEV") else "sam"

class BuildInvokeBase:
    class BuildInvokeBase(Base.IntegBase):
        """
        BuildInvokeBase will test the following sam commands:
        1. sam init
        2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
        3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
        """

        function_id_by_event: Optional[Dict[str, str]] = None
        invoke_output: Dict[str, Any]
        use_container: bool = True

        def _test_build(self):
            cmdlist = [SAM_CLI_EXECUTABLE, "build", "--debug"]
            if self.use_container:
                cmdlist.append("--use-container")
            LOG.info(cmdlist)
            result = run_command(cmdlist, self.cwd)
            self.assertIn("Build Succeeded", str(result.stdout))

        def _test_local_invoke(self):
            events_path = Path(self.cwd, "events")
            if not events_path.exists():
                LOG.info(f"Skip event testing, {events_path} does not exist")
                return
            event_files = os.listdir(events_path)
            for event_file in event_files:
                if self.function_id_by_event:
                    cmdlist = [
                        SAM_CLI_EXECUTABLE,
                        "local",
                        "invoke",
                        self.function_id_by_event[event_file],
                        "-e",
                        Path("events", event_file),
                        "--debug",
                    ]
                else:
                    cmdlist = [
                        SAM_CLI_EXECUTABLE,
                        "local",
                        "invoke",
                        "-e",
                        Path("events", event_file),
                        "--debug",
                    ]
                LOG.info(cmdlist)
                result = run_command(cmdlist, self.cwd)
                LOG.info(result)
                try:
                    self.invoke_output = json.loads(result.stdout)
                except json.decoder.JSONDecodeError:
                    self.fail(f"Response is not a valid JSON: {result.stdout}")

        @pytest.mark.flaky(reruns=3)
        def test_buld_and_invoke(self):
            self._test_init_template()
            self._test_build()
            self._test_local_invoke()

    class HelloWorldWithLocationBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, HelloWorldWithLocationBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's message is "hello world" and location is a valid IP address
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(
                self.invoke_output["headers"],
                {
                    "X-Custom-Header": "application/json",
                    "Content-Type": "application/json",
                },
            )
            body = json.loads(self.invoke_output["body"])
            self.assertEqual(body["message"], "hello world")
            # make sure it is an IP address
            try:
                ipaddress.ip_address(body["location"])
            except ValueError:
                self.fail(f'Invalid location: {body["location"]}')

    class EventBridgeHelloWorldBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, EventBridgeHelloWorldBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's detail, detail-type, resources, source, account and region
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(
                self.invoke_output["detail"],
                {"instance-id": "i-abcd1111", "state": "pending"},
            )
            self.assertEqual(
                self.invoke_output["detail-type"],
                "HelloWorldFunction updated event of EC2 Instance State-change Notification",
            )
            self.assertEqual(
                self.invoke_output["resources"],
                ["arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"],
            )
            self.assertEqual(self.invoke_output["source"], "aws.ec2")
            self.assertEqual(self.invoke_output["account"], "123456789012")
            self.assertEqual(self.invoke_output["region"], "us-east-1")

    class HelloWorldExclamationBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, HelloWorldExclamationBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's message is "Hello World!"
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(json.loads(self.invoke_output["body"]), {"message": "Hello World!"})

    class SimpleHelloWorldBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, SimpleHelloWorldBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's message is "hello world!"
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(json.loads(self.invoke_output["body"]), {"message": "hello world"})

    class QuickStartWebBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, quick start web templates have multiple events that call different lambda functions.
        """

        function_id_by_event = {
            "event-get-all-items.json": "getAllItemsFunction",
            "event-get-by-id.json": "getByIdFunction",
            "event-post-item.json": "putItemFunction",
        }

    class DotNetCoreExtraRerunBuildInvokeBase(BuildInvokeBase):
        """
        dotnet templates' building tends to fail arbitrarily, adding extra reruns here
        """

        @pytest.mark.flaky(reruns=5)
        def test_buld_and_invoke(self):
            super().test_buld_and_invoke()
