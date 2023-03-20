import pytest
from approvaltests.namer import NamerFactory
from pytest_mock import MockerFixture

from tests.utils.approvals import verify
from tests.utils.click_invoker import invoke


@pytest.mark.parametrize("command", ["", "localnet", "testnet", "mainnet"])
def test_explore(command: str, mocker: MockerFixture) -> None:
    launch_mock = mocker.patch("click.launch")
    result = invoke(f"explore {command}")

    assert result.exit_code == 0
    verify(launch_mock.call_args, options=NamerFactory.with_parameters(command or "localnet"))
