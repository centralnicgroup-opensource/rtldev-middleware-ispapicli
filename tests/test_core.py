import pytest
import os
import argparse
from hexonet.apiconnector.response import Response
from hexonet.ispapicli.modules.core import Core


class TestCore():

    # Testing methods

    # 2 initParser
    def test_initParser(self):
        core_obj = Core()
        parser = core_obj.initParser()
        assert isinstance(parser, argparse.ArgumentParser) is True

    # 3 parseArgs
    def test_parseArgs(self):
        core_obj = Core()
        parser = core_obj.initParser()
        # example of login args
        login_args = "-u=test.user -p=test.passw0rd -e=ote"
        # split args in an array
        splitted_args = login_args.split()
        # get main commands such as "-c checkdomain"
        login_args = vars(parser.parse_args(splitted_args))
        result, data = core_obj.parseArgs(login_args)
        assert isinstance(result, str)
        assert isinstance(data, str)

    # 4 login
    def test_login(self):
        core_obj = Core()
        # login success case
        login_args = {'userid': 'test.user', 'password': 'test.passw0rd',
                      'entity': 'ote'}
        result, msg = core_obj.login(login_args)
        assert result is True

        # login failure case
        login_args = {'userid': 'NOUSER', 'password': 'test.passw0rd',
                      'entity': 'ote'}
        result, msg = core_obj.login(login_args)
        assert result is False

    # 5 checkSession
    def test_checkSession(self):
        """
        The login status could be: valid | init | expired depends on the time
        recorded in login session file.
        """
        core_obj = Core()
        result = core_obj.checkSession()
        assert (result in ('valid', 'init', 'expired')) is True

    # 6 logout
    def test_logout(self):
        '''
        The test of this function depends on the local session file which itself time dependent,
        thus here will check the return type only.
        '''
        core_obj = Core()
        result = core_obj.logout()
        assert isinstance(result, str) is True

    # 7 request
    def test_request(self):
        core_obj = Core()
        cmd_success = {'command': 'querydomainlist', 'limit': '2'}
        response = core_obj.request(cmd_success)
        assert isinstance(response, Response) is True

    # 8 getResponse
    def test_getResponse(self):
        core_obj = Core()
        cmd = {'command': 'querydomainlist', 'limit': '2'}
        response = core_obj.request(cmd)
        return_response = core_obj.getResponse(response, 'list')
        assert isinstance(return_response, dict) is True

    # 9 getCommandHelp
    def test_getCommandHelp(self):
        core_obj = Core()
        cmd_success = 'QueryDomainList'
        cmd_failure = 'WRONGCOMMAND'
        txt_failure = "Command 'WRONGCOMMAND' not found!"
        response_success = core_obj.getCommandHelp(cmd_success)
        reponse_failure = core_obj.getCommandHelp(cmd_failure)
        assert txt_failure == reponse_failure
        assert isinstance(response_success, str) is True

    # 10 __saveLocalSession -> private method
    # 11 parseParameters
    def test_parseParameters(self):
        core_obj = Core()
        reminderargs = ['limit', '5']
        reminderargs_with_equal = ['limit=5']
        params_list = core_obj.parseParameters(reminderargs)
        params_list_with_equal = core_obj.parseParameters(reminderargs_with_equal)
        assert isinstance(params_list, dict) is True
        assert isinstance(params_list_with_equal, dict) is True

    # 12 getCommandList
    def test_getCommandList(self):
        core_obj = Core()
        result = core_obj.getCommandList()
        assert isinstance(result, str) is True

    # 13 getMinParameters
    def test_getMinParameters(self):
        core_obj = Core()
        cmd = "CheckDomain"
        result = core_obj.getMinParameters(cmd)
        assert 'domain' == result[0]
