import unittest
from unittest.mock import MagicMock
from git_gud.Fzf import Fzf
from git_gud.GitDataGetter import GitDataGetter
from git_gud.CommandRunner import CommandRunner
from git_gud.TrackRemote import TrackRemote

class TestTrackRemote(unittest.TestCase):

    def test_run(self):
        branch = 'bar'
        remote = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_current_branch_name = MagicMock(return_value=branch)
        git_data_getter.get_remote_name = MagicMock(return_value=remote)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        fetch = TrackRemote(command_runner, git_data_getter)
        fetch.run()

        command_runner.run.assert_called_once_with(['git', 'branch', branch, '-u', remote + '/' + branch])

if __name__ == '__main__':
    unittest.main()
