import click
import json
import sys
from typing import TextIO

from .http import assault
from .stats import Results


@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output json file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    # print(f"requests: {requests}")
    # print(f"concurrency: {concurrency}")
    # print(f"json-file: {json_file}")
    # print(f"url: {url}")
    output_file = None
    if json_file:
        try:
            output_file = open(json_file, "w")
        except:
            print(f"Unable to open file {json_file}")
            sys.exit(1)
    total_time, request_dicts = assault(url, requests, concurrency)
    results = Results(total_time, request_dicts)
    display(results, output_file)


def display(results: Results, json_file: TextIO):
    if json_file:
        json.dump(
            {
                "successful_requests": results.successful_requests(),
                "slower": results.slowest(),
                "fastest": results.fastest(),
                "average": results.average_time(),
                "total_time": results.total_time,
                "requests_per_minute": results.requests_per_minute(),
                "requests_per_second": results.requests_per_second(),
            },
            json_file,
        )
        json_file.close()
        print(
            f"""
            Successful requests\t{results.successful_requests()}
            Slowest            \t{results.slowest()}
            Fastest            \t{results.fastest()}
            Average            \t{results.average_time()}
            Total time         \t{results.total_time}
            Requests Per Minute\t{results.requests_per_minute()}
            Requests Per Second\t{results.requests_per_second()}
            """
        )
        print(".... Done!")
    else:
        print("---Results---")
        print(
            f"""
            Successful requests\t{results.successful_requests()}
            Slowest            \t{results.slowest()}
            Fastest            \t{results.fastest()}
            Average            \t{results.average_time()}
            Total time         \t{results.total_time}
            Requests Per Minute\t{results.requests_per_minute()}
            Requests Per Second\t{results.requests_per_second()}
            """
        )
        print(".... Done!")


if __name__ == "__main__":
    cli()
