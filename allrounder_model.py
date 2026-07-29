def get_allrounder_list():
    return ["Nitish Kumar Reddy", "Hardik Pandya", "Ravindra Jadeja", "Axar Patel", "Abhishek Sharma"]

def get_player_stats(player):
    data = {
        "Nitish Kumar Reddy": {'batting_avg': 35.5, 'batting_sr': 145.2, 'wickets': 2, 'bowling_econ': 8.5, 'catches': 1, 'dots_balls': 12},
        "Hardik Pandya": {'batting_avg': 28.0, 'batting_sr': 150.0, 'wickets': 10, 'bowling_econ': 9.2, 'catches': 5, 'dots_balls': 25},
        "Ravindra Jadeja": {'batting_avg': 22.5, 'batting_sr': 125.0, 'wickets': 15, 'bowling_econ': 7.1, 'catches': 8, 'dots_balls': 40},
        "Axar Patel": {'batting_avg': 18.0, 'batting_sr': 135.0, 'wickets': 12, 'bowling_econ': 7.8, 'catches': 4, 'dots_balls': 35},
        "Abhishek Sharma": {'batting_avg': 40.2, 'batting_sr': 170.5, 'wickets': 2, 'bowling_econ': 9.0, 'catches': 3, 'dots_balls': 10}
    }
    return data.get(player)

def get_auction_value(player):
    values = {
        "Nitish Kumar Reddy": "₹8 Cr",
        "Hardik Pandya": "₹15 Cr",
        "Ravindra Jadeja": "₹16 Cr", 
        "Axar Patel": "₹9 Cr",
        "Abhishek Sharma": "₹14 Cr"
    }
    return values.get(player)

def predict_category(player):
    return "Batting All-Rounder" if player == "Abhishek Sharma" else "True All-Rounder"

def generate_swot(player_name):
    swot_data = {
        "Nitish Kumar Reddy": {
            "Strengths": ["Explosive batting strike rate", "Powerful lower order hitter"],
            "Weaknesses": ["Inconsistent bowling", "Lack of experience in pressure situations"],
            "Opportunities": ["Can become finisher for team", "Powerplay overs specialist"],
            "Threats": ["Injury risk due to workload", "Form dependent player"]
        },
        "Hardik Pandya": {
            "Strengths": ["Finishing ability", "Pace bowling in death"],
            "Weaknesses": ["Prone to injuries", "Expensive in death overs"],
            "Opportunities": ["Captaincy material", "Best finisher in India"],
            "Threats": ["Fitness issues", "Form fluctuations"]
        },
        "Ravindra Jadeja": {
            "Strengths": ["Best fielder in India", "Economical bowling"],
            "Weaknesses": ["Slow batting strike rate", "Not a power hitter"],
            "Opportunities": ["All-round anchor", "Mentor role"],
            "Threats": ["Age factor", "Batting position down the order"]
        },
        "Axar Patel": {
            "Strengths": ["Accurate left-arm spin", "Lower order batting"],
            "Weaknesses": ["Lack of big shots", "Batting inconsistency"],
            "Opportunities": ["Spin all-rounder", "PP overs specialist"],
            "Threats": ["Competition from other spinners"]
        },
        "Abhishek Sharma": {
            "Strengths": ["Explosive opening", "6 hitting ability"],
            "Weaknesses": ["Inconsistent against pace", "Limited bowling options"],
            "Opportunities": ["Future opener for India", "Powerplay specialist"],
            "Threats": ["Technique vs swing bowling"]
        }
    }
    return swot_data.get(player_name, {"Strengths":[],"Weaknesses":[],"Opportunities":[],"Threats":[]})