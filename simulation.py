from src.brackets import Region, Bracket
from src.stats import get_ratings, get_lehigh_method
from src.constants import (
    west_teams,
    west_playin,
    east_teams,
    east_playin,
    south_teams,
    south_playin,
    midwest_teams,
    midwest_playin,
)


def main(num_sims=1000, select_subset="Sports Reference"):
    if select_subset == "The Lehigh Method":
        ratings_df = get_lehigh_method()
        ratings = dict(zip(ratings_df["School"], ratings_df["TLM_NetRtg"]))
    else:
        ratings_df = get_ratings()
        ratings = dict(zip(ratings_df["School"], ratings_df["NRtg"]))

    west = Region("W", west_teams, west_playin)
    east = Region("W", east_teams, east_playin)
    south = Region("W", south_teams, south_playin)
    midwest = Region("W", midwest_teams, midwest_playin)
    bracket = Bracket(ratings, west, east, south, midwest)
    bracket.run_simulations(num_sims=num_sims)
    return bracket.output_df
    #bracket.output_df.to_csv("output.csv")


