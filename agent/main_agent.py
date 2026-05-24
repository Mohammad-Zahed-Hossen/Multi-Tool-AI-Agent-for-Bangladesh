import argparse
from tools import institutions_tool, hospitals_tool, restaurants_tool


def main():
    parser = argparse.ArgumentParser(description='Simple multi-tool agent CLI')
    parser.add_argument('domain', choices=['institutions','hospitals','restaurants'], help='Domain to query')
    parser.add_argument('--q', '-q', help='Query string (name search)')
    args = parser.parse_args()

    q = args.q or ''
    if args.domain == 'institutions':
        results = institutions_tool.find_by_name(q) if q else institutions_tool.list_all()
    elif args.domain == 'hospitals':
        results = hospitals_tool.find_by_name(q) if q else hospitals_tool.list_all()
    else:
        results = restaurants_tool.find_by_name(q) if q else restaurants_tool.list_all()

    for r in results:
        print(r)


if __name__ == '__main__':
    main()
