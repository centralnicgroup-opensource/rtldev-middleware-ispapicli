import pytest
import argparse
from hexonet.ispapicli.modules.scrap import Scrap


@pytest.fixture
def scrap_obj():
    """Returns a Scrap instance"""
    scrap_obj = Scrap()
    return scrap_obj


@pytest.fixture
def command_example():
    """Returns a command example"""
    commandExample = {
        "command": "CheckTMCHMarkSMD",
        "description": "With this command you may decode the information from an SMD file and check a domain name against it.",
        "availability": "All users have access to this command.",
        "paramaters": [
            {
                "Parameter": "COMMAND",
                "Min": "1",
                "Definition": "`CheckTMCHMarkSMD`",
                "Type": "COMMAND",
            },
            {
                "Parameter": "SMD[0..N]",
                "Min": "1",
                "Definition": "SMD file strings",
                "Type": "TEXT",
            },
            {
                "Parameter": "DOMAIN",
                "Min": "0",
                "Definition": "Second level domain name",
                "Type": "DOMAIN",
            },
        ],
    }
    return commandExample


@pytest.fixture
def raw_params_data():
    data = [
        "## COMMAND",
        "",
        "Parameter | Min | Definition | Type",
        "---- | ---- | ---- | ----",
        "COMMAND | 1 | `CheckTMCHMarkSMD` | COMMAND",
        "SMD[0..N] | 1 | SMD file strings | TEXT",
        "DOMAIN | 0 | Second level domain name | DOMAIN",
        "",
        "----",
        "## RESPONSE",
        "",
        "Code | Description",
        "---- | ----",
        "200 | Command completed successfully",
        "420 | Command failed due to server error. Server closing connection",
        "421 | Command failed due to server error. Client should try again",
        "423 | Command failed due to server error. Client should try again (Could not get session)",
        "503 | Invalid attribute name",
        "505 | Invalid attribute value syntax",
        "530 | Authentication failed",
        "541 | Invalid attribute value",
        "549 | Command failed",
        "",
        "Property | Min | Max | Definition | Type",
        "---- | ---- | ---- | ---- | ----",
        "CREATEDDATE | 1 | 1 | The start of validity of the SMD file | DATETIME",
        "EXPIRATIONDATE | 1 | 1 | The end of validity of the SMD file | DATETIME",
        "ID | 1 | 1 | Trademark ID | TEXT",
        "LABEL[0..N] | 1 | N | Labels, which can be used to register domain names, converted to punycode | TEXT",
        "MARKNAME | 1 | 1 | The trademark this SMD FILE refers to | TEXT",
        "SMD-ID | 1 | 1 | A unique SMD file identifier | TEXT",
        "ULABEL[0..N] | 1 | N | Labels, which can be used to register domain names | TEXT",
        "",
        "----",
        "## Example",
        "",
        "### Command",
        "",
        "```",
        "[COMMAND]",
        "COMMAND = CheckTMCHMarkSMD",
        "DOMAIN = testvalidate.com",
        "SMD0 = PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHNtZDpzaWduZWRNYXJrIHh",
        "SMD1 = tbG5zOnNtZD0idXJuOmlldGY6cGFyYW1zOnhtbDpuczpzaWduZWRNYXJrLTEuMCIgaWQ9Il85MG",
        "...",
        "SMD94 = E9PC9kczpYNTA5Q2VydGlmaWNhdGU+PC9kczpYNTA5RGF0YT48L2RzOktleUluZm8+PC9kczpTa",
        "SMD95 = WDUYXR1CMU+PC9ZBWQ6C2LNBMVKTWFYAZ4 =",
        "EOF",
        "```",
        "### Response",
        "",
        "```",
        "[RESPONSE]",
        "CODE = 200",
        "DESCRIPTION = Command completed successfully",
        "PROPERTY[CREATEDDATE][0] = 2013-11-22 10:42:16",
        "PROPERTY[EXPIRATIONDATE][0] = 2017-07-23 22:00:00",
        "PROPERTY[ID][0] = 00052013734689731373468973-65535",
        "PROPERTY[LABEL][0] = testandvalidate",
        "PROPERTY[LABEL][1] = test---validate",
        "...",
        "PROPERTY[LABEL][8] = testvalidate",
        "PROPERTY[LABEL][9] = testet-validate",
        "PROPERTY[MARKNAME][0] = Test & Validate",
        "PROPERTY[SMD-ID][0] = 0000001751385116936920-65535",
        "PROPERTY[ULABEL][0] = testandvalidate",
        "PROPERTY[ULABEL][1] = test---validate",
        "...",
        "PROPERTY[ULABEL][9] = testet-validate",
        "EOF",
        "```",
        "",
        "----",
    ]
    return data


@pytest.fixture
def command_params():
    paramaters = [
        {
            "Parameter": "COMMAND",
            "Min": "1",
            "Definition": "`CheckTMCHMarkSMD`",
            "Type": "COMMAND",
        },
        {
            "Parameter": "SMD[0..N]",
            "Min": "1",
            "Definition": "SMD file strings",
            "Type": "TEXT",
        },
        {
            "Parameter": "DOMAIN",
            "Min": "0",
            "Definition": "Second level domain name",
            "Type": "DOMAIN",
        },
    ]
    return paramaters


def test_saveCommandToDB(scrap_obj, command_example):
    commandName = "CheckTMCHMarkSMD"
    result = scrap_obj._Scrap__saveCommandToDB(commandName, command_example)
    assert result is True


def test_getCommandData(scrap_obj, command_example, command_params):
    command = "CheckTMCHMarkSMD"
    description = "With this command you may decode the information from an SMD file and check a domain name against it."
    availability = "All users have access to this command."

    result = scrap_obj._Scrap__getCommandData(
        command, description, availability, command_params
    )
    assert (result == command_example) is True


def test_cloneRepo(scrap_obj):
    result = scrap_obj._Scrap__cloneRepo()
    assert result is True


def test_getCommandsParams(scrap_obj, raw_params_data, command_params):
    result = scrap_obj._Scrap__getCommandsParams(raw_params_data)
    assert (result == command_params) is True


def test_scrapCommands(scrap_obj):
    result = scrap_obj.scrapCommands()
    assert result is True