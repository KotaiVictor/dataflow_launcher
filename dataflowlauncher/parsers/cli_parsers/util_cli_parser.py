"""Utility cli arguments"""
from dataflowlauncher.parsers.cli_parsers.base_cli_parser import CliParser


class UtilCliParser(CliParser):
    def add_arguments_group(self, parser):
        util_parsers = parser.add_argument_group(
            "util",
            description="Pass in the utility parameters for the dataflow")
        util_parsers.add_argument(
            '--ignore_checks', action='store_true',
            help='Ignore production checks. Default: false')
        util_parsers.add_argument(
            '--unknown_arguments', action='store_true',
            help='Pass any unknown arguments to the underlying command'
                 'Default: false')
        util_parsers.add_argument(
            '-b', '--bypass_prompt', action='store_true',
            help='Skip enter key press required before launching. Default: false')

    def run_preprocessing(self, config_dict, cli_args):
        return None

    def get_updated_config_from_args(self, config_dict, cli_args):
        return None

    def get_updated_params_from_args(self, config_dict, cli_args):
        return None