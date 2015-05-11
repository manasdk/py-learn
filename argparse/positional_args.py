#!/usr/bin/env python2.7

import argparse


def _single_positional_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int)
    args = parser.parse_args(['3'])
    parser.print_help()
    print args.square ** 2
    return parser


def _multiple_positional_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int)
    parser.add_argument("cube", type=int)
    args = parser.parse_args(['3', '2'])
    parser.print_help()
    print args.square ** 2
    print args.cube ** 3
    return parser


def _nargs_positional_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", nargs='+')
    parser.add_argument("arg2", nargs='?', default='1')
    args = parser.parse_args(['10', '20', '30'])
    parser.print_help()
    print 'arg1 : ', args.arg1
    print 'arg2 : ', args.arg2
    return parser


def _single_optional_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg1", nargs='+')
    args = parser.parse_args(['--arg1', '10', '20', '30'])
    parser.print_help()
    print 'arg1 : ', args.arg1
    return parser


def _multiple_optional_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg1", '-a', nargs='+')
    parser.add_argument("--arg2", '-b', nargs='?', default='1')
    parser.add_argument("arg3", type=int)
    parser.print_help()
    args = parser.parse_args(['-a', '10', '--arg2', '20', '30'])
    print 'arg1 : ', args.arg1
    print 'arg2 : ', args.arg2
    print 'arg3 : ', args.arg3
    return parser


def _arg_group():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg1", '-a', nargs='+')
    group = parser.add_argument_group('group')
    group.add_argument('--arg2', '-b')
    group.add_argument('--arg3', '-c', default='40')
    parser.print_help()
    args = parser.parse_args(['-b', '30', '-a', '20', '10'])
    print 'arg1 : ', args.arg1
    print 'arg2 : ', args.arg2
    print 'arg3 : ', args.arg3
    return parser


def _mex_arg_group():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg1", '-a', nargs='+')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--arg2', '-b')
    group.add_argument('--arg3', '-c')
    parser.print_help()
    args = parser.parse_args(['-b', '30', '-a', '20', '10'])
    print 'arg1 : ', args.arg1
    print 'arg2 : ', args.arg2
    print 'arg3 : ', args.arg3
    try:
        args = parser.parse_args(['-b', '30', '-c', '40', '-a', '20', '10'])
    except SystemExit:
        import traceback
        traceback.print_exc()
    return parser


def _mex_arg_group_positional_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--arg1", '-a', nargs='?', type=str)
    group = parser.add_argument_group('group')
    group.add_argument('arg2')
    group.add_argument('arg3')
    parser.print_help()
    args = parser.parse_args(['10', '20', '-a', '30'])
    print 'arg1 : ', args.arg1
    print 'arg2 : ', args.arg2
    print 'arg3 : ', args.arg3
    return parser


def _store_true_false_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', action='store_true')
    parser.add_argument('--arg2', action='store_false')
    args = parser.parse_args('--arg1 --arg2'.split())
    print args.arg1
    print args.arg2
    args = parser.parse_args([])
    print args.arg1
    print args.arg2
    return parser


def _inspect_parser(parser):
    print '\033[4mparam names\033[0m'
    for action in parser._actions:
        if action.dest is argparse.SUPPRESS or action.default is argparse.SUPPRESS:
            continue
        name = action.option_strings[0] if action.option_strings else action.dest
        print name, action.type, action


def run(fn):
    print '\n\033[92m\033[4m\033[1m%s\033[0m' % fn.func_name[1:]
    parser = fn()
    _inspect_parser(parser)


def main():
    run(_single_positional_arg)
    run(_multiple_positional_args)
    run(_nargs_positional_args)
    run(_single_optional_arg)
    run(_multiple_optional_args)
    run(_arg_group)
    run(_mex_arg_group)
    run(_mex_arg_group_positional_args)
    run(_store_true_false_args)


if __name__ == '__main__':
    main()
