# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T08:15:48+00:00



import argparse
import json
import os
from datetime import datetime
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Path, Query
from pydantic import conint

from models import (
    Comparators,
    DataDivisionsSearchGetResponse,
    DivisionGroupByPartyViewModel,
    DivisionViewModel,
    MemberVotingRecordViewModel,
)

app = MCPProxy(
    contact={
        'email': 'softwareengineering@parliament.uk',
        'name': 'UK Parliament',
        'url': 'https://www.parliament.uk/',
    },
    description='An API that allows querying of Lords Votes data.',
    title='Lords Votes API',
    version='v1',
)


@app.get(
    '/data/Divisions/groupedbyparty',
    description=""" Get a list of Divisions which contain grouped by party """,
    tags=[
        'division_management',
        'member_voting_records',
        'division_summary_statistics',
    ],
)
def get_data__divisions_groupedbyparty(
    search_term: Optional[str] = Query(None, alias='SearchTerm'),
    member_id: Optional[int] = Query(None, alias='MemberId'),
    include_when_member_was_teller: Optional[bool] = Query(
        None, alias='IncludeWhenMemberWasTeller'
    ),
    start_date: Optional[datetime] = Query(None, alias='StartDate'),
    end_date: Optional[datetime] = Query(None, alias='EndDate'),
    division_number: Optional[int] = Query(None, alias='DivisionNumber'),
    total_votes_cast__comparator: Optional[Comparators] = Query(
        None, alias='TotalVotesCast.Comparator'
    ),
    total_votes_cast__value_to_compare: Optional[int] = Query(
        None, alias='TotalVotesCast.ValueToCompare'
    ),
    majority__comparator: Optional[Comparators] = Query(
        None, alias='Majority.Comparator'
    ),
    majority__value_to_compare: Optional[int] = Query(
        None, alias='Majority.ValueToCompare'
    ),
):
    """
    Return Divisions results grouped by party
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/data/Divisions/membervoting',
    description=""" Get a list of voting records for a Member. """,
    tags=['member_voting_records', 'division_summary_statistics'],
)
def get_data__divisions_membervoting(
    member_id: conint(ge=1, le=2147483647) = Query(..., alias='MemberId'),
    search_term: Optional[str] = Query(None, alias='SearchTerm'),
    include_when_member_was_teller: Optional[bool] = Query(
        None, alias='IncludeWhenMemberWasTeller'
    ),
    start_date: Optional[datetime] = Query(None, alias='StartDate'),
    end_date: Optional[datetime] = Query(None, alias='EndDate'),
    division_number: Optional[int] = Query(None, alias='DivisionNumber'),
    total_votes_cast__comparator: Optional[Comparators] = Query(
        None, alias='TotalVotesCast.Comparator'
    ),
    total_votes_cast__value_to_compare: Optional[int] = Query(
        None, alias='TotalVotesCast.ValueToCompare'
    ),
    majority__comparator: Optional[Comparators] = Query(
        None, alias='Majority.Comparator'
    ),
    majority__value_to_compare: Optional[int] = Query(
        None, alias='Majority.ValueToCompare'
    ),
    skip: Optional[int] = 0,
    take: Optional[int] = 25,
):
    """
    Return voting records for a Member
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/data/Divisions/search',
    description=""" Get a list of Divisions which meet the specified criteria. """,
    tags=[
        'division_management',
        'member_voting_records',
        'division_summary_statistics',
    ],
)
def get_data__divisions_search(
    search_term: Optional[str] = Query(None, alias='SearchTerm'),
    member_id: Optional[int] = Query(None, alias='MemberId'),
    include_when_member_was_teller: Optional[bool] = Query(
        None, alias='IncludeWhenMemberWasTeller'
    ),
    start_date: Optional[datetime] = Query(None, alias='StartDate'),
    end_date: Optional[datetime] = Query(None, alias='EndDate'),
    division_number: Optional[int] = Query(None, alias='DivisionNumber'),
    total_votes_cast__comparator: Optional[Comparators] = Query(
        None, alias='TotalVotesCast.Comparator'
    ),
    total_votes_cast__value_to_compare: Optional[int] = Query(
        None, alias='TotalVotesCast.ValueToCompare'
    ),
    majority__comparator: Optional[Comparators] = Query(
        None, alias='Majority.Comparator'
    ),
    majority__value_to_compare: Optional[int] = Query(
        None, alias='Majority.ValueToCompare'
    ),
    skip: Optional[int] = 0,
    take: Optional[int] = 25,
):
    """
    Return a list of Divisions
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/data/Divisions/searchTotalResults',
    description=""" Get total count of Divisions meeting the specified query, useful for paging lists etc... """,
    tags=['division_summary_statistics', 'member_voting_records'],
)
def get_data__divisions_search_total_results(
    search_term: Optional[str] = Query(None, alias='SearchTerm'),
    member_id: Optional[int] = Query(None, alias='MemberId'),
    include_when_member_was_teller: Optional[bool] = Query(
        None, alias='IncludeWhenMemberWasTeller'
    ),
    start_date: Optional[datetime] = Query(None, alias='StartDate'),
    end_date: Optional[datetime] = Query(None, alias='EndDate'),
    division_number: Optional[int] = Query(None, alias='DivisionNumber'),
    total_votes_cast__comparator: Optional[Comparators] = Query(
        None, alias='TotalVotesCast.Comparator'
    ),
    total_votes_cast__value_to_compare: Optional[int] = Query(
        None, alias='TotalVotesCast.ValueToCompare'
    ),
    majority__comparator: Optional[Comparators] = Query(
        None, alias='Majority.Comparator'
    ),
    majority__value_to_compare: Optional[int] = Query(
        None, alias='Majority.ValueToCompare'
    ),
):
    """
    Return total results count
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/data/Divisions/{divisionId}',
    description=""" Get a single Division which has the Id specified. """,
    tags=['division_management', 'division_summary_statistics'],
)
def get_data__divisions__division_id(division_id: int = Path(..., alias='divisionId')):
    """
    Return a Division
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
